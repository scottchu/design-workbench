"""Own one macOS user launchd simulator; never build, install dependencies or proxy controls."""
from __future__ import annotations
import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import plistlib
import re
import shutil
import socket
import subprocess
import sys
import time
from urllib.error import URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, build_opener

LABEL = 'com.scottchu.cad-workbench.simulator'
URL = 'http://127.0.0.1:4179'
ROOT = Path(__file__).resolve().parents[1]
BUILD_ENTRY = 'apps/playground/build/index.js'
LEGACY_BUILD_ENTRY = 'apps/simulator/build/index.js'

class ServiceError(RuntimeError): pass
class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs): return None

def health():
    try:
        with build_opener(NoRedirect).open(URL+'/health', timeout=1) as response:
            return json.load(response)
    except (URLError, OSError, ValueError): return None

def listening():
    try:
        with socket.create_connection(('127.0.0.1',4179),timeout=0.3): return True
    except OSError: return False

def origin(value):
    if not value: return None
    p=urlsplit(value)
    try: port=p.port
    except ValueError as exc: raise ServiceError('invalid allowed origin port') from exc
    if (p.scheme!='https' or not p.hostname or not p.hostname.endswith('.ts.net')
            or p.username or p.password or p.path or p.query or p.fragment
            or (port is not None and not 1<=port<=65535)):
        raise ServiceError('allowed origin must be an exact HTTPS *.ts.net origin without credentials/path/query/fragment')
    canonical='https://'+p.hostname+(f':{port}' if port is not None and port!=443 else '')
    if value!=canonical or not re.fullmatch(r'[a-z0-9._-]+\.ts\.net',p.hostname):
        raise ServiceError('allowed origin must already be canonical: lowercase host/scheme, no explicit default port')
    return value

def loaded_configuration(text):
    # launchctl has separate inherited/default environment blocks. Match only
    # exact field names, rejecting missing/duplicate or ambiguous ownership data.
    def scalar(name):
        values=re.findall(r'^\s*'+re.escape(name)+r' = (.+)$',text,re.M)
        if len(values)!=1:raise ServiceError(f'cannot verify loaded {name}')
        return values[0].strip()
    def block(name):
        values=re.findall(r'^\s*'+re.escape(name)+r' = \{\n(.*?)^\s*\}',text,re.M|re.S)
        if len(values)!=1:raise ServiceError(f'cannot verify loaded {name}')
        return [line.strip() for line in values[0].splitlines() if line.strip()]
    environment={}
    for line in block('environment'):
        key,separator,value=line.partition(' => ')
        if not separator or key in environment:raise ServiceError('ambiguous loaded environment')
        environment[key]=value
    return {'program':scalar('program'),'arguments':block('arguments'),
            'working_directory':scalar('working directory'),'environment':environment}

class Service:
    def __init__(self, root=ROOT, *, home=None, uid=None, run=subprocess.run,
                 read_health=health, port_listening=listening, sleep=time.sleep):
        self.root=Path(root).resolve();self.state=self.root/'.workbench/service'
        self.local=self.state/(LABEL+'.plist')
        self.installed=Path(home or Path.home())/'Library/LaunchAgents'/(LABEL+'.plist')
        self.instance=hashlib.sha256(str(self.root).encode()).hexdigest()[:24]
        self.domain=f'gui/{os.getuid() if uid is None else uid}';self.target=f'{self.domain}/{LABEL}'
        self.run=run;self.read_health=read_health;self.port_listening=port_listening;self.sleep=sleep
    def command(self,*args,check=True):
        result=self.run(['/bin/launchctl',*args],capture_output=True,text=True,timeout=10)
        if check and result.returncode:raise ServiceError(f'launchctl {args[0]} failed: {result.stderr.strip()}')
        return result
    def loaded(self):
        result=self.command('print',self.target,check=False)
        if result.returncode:
            if result.returncode==113 or 'Could not find service' in result.stderr:return None
            raise ServiceError(f'cannot inspect launchd ownership: {result.stderr.strip()}')
        match=re.search(r'^\s*path = (.+)$',result.stdout,re.M)
        if not match:raise ServiceError('loaded launchd job does not expose its plist path')
        path=Path(match.group(1).strip())
        if path not in (self.local,self.installed):raise ServiceError(f'launchd label belongs to another checkout: {path}')
        saved=self.owned_plist(path)
        actual=loaded_configuration(result.stdout)
        if (actual['program']!=saved['ProgramArguments'][0]
                or actual['arguments']!=saved['ProgramArguments']
                or actual['working_directory']!=saved['WorkingDirectory']):
            raise ServiceError('loaded program/arguments/working directory differ from owned plist')
        expected=saved['EnvironmentVariables']
        keys=set(expected)|{'WORKBENCH_ALLOWED_ORIGIN'}
        if any(actual['environment'].get(key)!=expected.get(key) for key in keys):
            raise ServiceError('loaded environment differs from owned plist')
        return path,saved
    def owned_plist(self,path):
        if path.is_symlink():raise ServiceError(f'refusing symlink plist: {path}')
        try:data=plistlib.loads(path.read_bytes())
        except (OSError,ValueError,plistlib.InvalidFileException) as exc:raise ServiceError(f'cannot read owned plist: {path}') from exc
        env=data.get('EnvironmentVariables',{})
        if (data.get('Label')!=LABEL or data.get('WorkingDirectory')!=str(self.root)
                or env.get('WORKBENCH_INSTANCE_ID')!=self.instance
                or data.get('ProgramArguments',[None,None])[1:] not in
                   ([str(self.root/BUILD_ENTRY)], [str(self.root/LEGACY_BUILD_ENTRY)])):
            raise ServiceError(f'foreign plist ownership: {path}')
        return data
    def desired(self,node,registry,allowed_origin=None,*,reuse=False):
        # ensure/open preserve the verified saved entrypoint, including an old
        # same-root simulator build. Explicit install selects the new build.
        saved=self.saved_configuration() if reuse else None
        entry=Path(saved['ProgramArguments'][1]) if saved else self.root/BUILD_ENTRY
        if not entry.is_file():
            raise ServiceError(f'built server missing: {entry}; build with npm run build:playground and use explicit install to change a saved entrypoint')
        node=Path(node)
        if not node.is_absolute() or not node.is_file() or not os.access(node,os.X_OK):raise ServiceError('node must be an absolute executable resolved by asdf')
        registry=Path(registry)
        if not registry.is_absolute() or not registry.is_file():raise ServiceError('WORKBENCH_SIMULATORS must name an existing absolute registry file')
        allowed_origin=origin(allowed_origin)
        env={'HOST':'127.0.0.1','PORT':'4179','ORIGIN':allowed_origin or URL,
             'WORKBENCH_INSTANCE_ID':self.instance,'WORKBENCH_SIMULATORS':str(registry)}
        if allowed_origin:env['WORKBENCH_ALLOWED_ORIGIN']=allowed_origin
        return {'Label':LABEL,'ProgramArguments':[str(node),str(entry)],'WorkingDirectory':str(self.root),
                'EnvironmentVariables':env,'RunAtLoad':True,'KeepAlive':True,'ThrottleInterval':5,
                'StandardOutPath':str(self.state/'stdout.log'),'StandardErrorPath':str(self.state/'stderr.log')}
    def write(self,path,data):
        existed=path.exists() or path.is_symlink()
        if existed:self.owned_plist(path)
        for parent in path.parents:
            if parent.is_symlink():raise ServiceError(f'refusing symlink directory: {parent}')
        path.parent.mkdir(parents=True,exist_ok=True)
        temp=path.with_suffix('.plist.tmp')
        if temp.exists() or temp.is_symlink():raise ServiceError(f'temporary path already exists: {temp}')
        with temp.open('xb') as f:plistlib.dump(data,f)
        temp.chmod(0o600)
        if existed:
            self.owned_plist(path);temp.replace(path)
        else:
            try:os.link(temp,path)
            except FileExistsError as exc:raise ServiceError('plist appeared concurrently; refusing overwrite') from exc
            finally:temp.unlink()
    def healthy(self):
        value=self.read_health()
        if value is None:return False
        if not isinstance(value,dict) or value.get('service')!='cad-workbench-simulator' or value.get('instance')!=self.instance:
            raise ServiceError('port 4179 responds as another service or checkout')
        return True
    def wait_ready(self):
        for _ in range(40):
            if self.healthy():return
            self.sleep(0.25)
        raise ServiceError('owned job did not become healthy within 10 seconds; inspect ignored service logs')
    def status(self):
        loaded=self.loaded();ready=self.healthy()
        installed=False
        if self.installed.exists() or self.installed.is_symlink():self.owned_plist(self.installed);installed=True
        return {'service':LABEL,'instance':self.instance,'loaded':bool(loaded),'healthy':ready,
                'managed':bool(loaded) and ready,'installed_for_login':installed,'url':URL,
                'plist':str(loaded[0]) if loaded else None}
    def ensure(self,data):
        installed=self.installed.exists() or self.installed.is_symlink()
        if installed and self.owned_plist(self.installed)!=data:raise ServiceError('installed configuration differs; use explicit install to update it')
        loaded=self.loaded()
        if loaded:
            if loaded[1]!=data:raise ServiceError('loaded configuration differs; stop then ensure, or install explicitly')
            self.wait_ready();return self.status()
        if self.healthy() or self.port_listening():raise ServiceError('port 4179 is occupied without an owned launchd job; refusing to reuse or stop it')
        target=self.installed if installed else self.local
        self.write(target,data)
        self.command('bootstrap',self.domain,str(target));self.wait_ready();return self.status()
    def saved_configuration(self):
        loaded=self.loaded()
        if loaded:return loaded[1]
        for path in (self.installed,self.local):
            if path.exists() or path.is_symlink():return self.owned_plist(path)
        return None
    def saved_environment(self):
        saved=self.saved_configuration()
        return saved['EnvironmentVariables'] if saved else {}
    def bootout(self):
        self.command('bootout',self.target)
        for _ in range(40):
            if self.loaded() is None and not self.port_listening():return
            self.sleep(0.25)
        raise ServiceError('owned job was removed but port 4179 did not clear; no process was killed')
    def stop(self):
        loaded=self.loaded()
        if loaded:self.bootout()
        return {'stopped':bool(loaded),'installed_for_login':self.installed.exists(),'url':URL}
    def install(self,data):
        # Check foreign global state before stopping or changing anything.
        if self.installed.exists() or self.installed.is_symlink():self.owned_plist(self.installed)
        loaded=self.loaded()
        if loaded and loaded[0]==self.installed and loaded[1]==data:
            self.wait_ready();return self.status()
        if not loaded and (self.healthy() or self.port_listening()):raise ServiceError('port 4179 is occupied by an unmanaged service')
        if loaded:self.bootout()
        self.write(self.installed,data)
        return self.ensure(data)
    def uninstall(self):
        if self.installed.exists() or self.installed.is_symlink():self.owned_plist(self.installed)
        result=self.stop()
        if self.installed.exists():self.installed.unlink()
        result['installed_for_login']=False
        return result

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=['ensure','start','status','stop','open','install','uninstall'])
    args=parser.parse_args()
    try:
        if sys.platform!='darwin':raise ServiceError('this lifecycle supports macOS user launchd only')
        service=Service()
        for path in (service.state,*service.state.parents):
            if path.is_symlink():raise ServiceError(f'refusing symlink state directory: {path}')
        service.state.mkdir(parents=True,exist_ok=True)
        lock=service.state/'lifecycle.lock'
        if lock.is_symlink():raise ServiceError('refusing symlink lock')
        with lock.open('a') as handle:
            fcntl.flock(handle,fcntl.LOCK_EX)
            if args.action in ('status','stop','uninstall'):result=getattr(service,args.action)()
            else:
                asdf=shutil.which('asdf')
                if not asdf:raise ServiceError('asdf is unavailable; no system Node fallback')
                found=subprocess.run([asdf,'which','node'],cwd=service.root,capture_output=True,text=True,timeout=10)
                if found.returncode:raise ServiceError('asdf could not resolve the pinned Node executable')
                saved=service.saved_environment()
                registry=os.environ.get('WORKBENCH_SIMULATORS',saved.get('WORKBENCH_SIMULATORS',str(service.root/'.workbench/simulators.json')))
                allowed=os.environ.get('WORKBENCH_ALLOWED_ORIGIN',saved.get('WORKBENCH_ALLOWED_ORIGIN'))
                data=service.desired(found.stdout.strip(),registry,allowed,reuse=args.action!='install')
                result=service.install(data) if args.action=='install' else service.ensure(data)
                if args.action=='open':subprocess.run(['/usr/bin/open',URL],check=True,timeout=10)
            print(json.dumps(result,indent=2));return 0
    except (ServiceError,OSError,subprocess.SubprocessError) as exc:
        print(json.dumps({'error':str(exc)}));return 1
if __name__=='__main__':raise SystemExit(main())
