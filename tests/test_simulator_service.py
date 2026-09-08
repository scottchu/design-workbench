"""Exercise lifecycle transitions against bounded launchctl/health fakes; no real services."""
import importlib.util
from pathlib import Path
import plistlib
import subprocess
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('sim_service',ROOT/'scripts/simulator_service.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class Fake:
    def __init__(self):self.path=None;self.config=None;self.calls=[];self.foreign=None
    def run(self,args,**kwargs):
        self.calls.append(args[1:]);cmd=args[1]
        if cmd=='print':
            if self.path:
                arguments=''.join(f'\t\t{a}\n' for a in self.config['ProgramArguments'])
                environment=''.join(f'\t\t{k} => {v}\n' for k,v in self.config['EnvironmentVariables'].items())
                text=(f'\tpath = {self.path}\n\tprogram = {self.config["ProgramArguments"][0]}\n'
                      f'\targuments = {{\n{arguments}\t}}\n'
                      f'\tworking directory = {self.config["WorkingDirectory"]}\n'
                      '\tinherited environment = {\n\t\tHOST => unrelated-inherited\n\t}\n'
                      '\tdefault environment = {\n\t\tPORT => unrelated-default\n\t}\n'
                      f'\tenvironment = {{\n{environment}\t\tXPC_SERVICE_NAME => {m.LABEL}\n\t}}\n')
                return subprocess.CompletedProcess(args,0,text,'')
            return subprocess.CompletedProcess(args,113,'','Could not find service')
        if cmd=='bootstrap':self.path=Path(args[3]);self.config=plistlib.loads(self.path.read_bytes())
        elif cmd=='bootout':self.path=None;self.config=None
        return subprocess.CompletedProcess(args,0,'','')
    def health(self):
        if self.foreign:return self.foreign
        if self.path:return {'service':'cad-workbench-simulator','instance':self.config['EnvironmentVariables']['WORKBENCH_INSTANCE_ID']}
        return None

class LifecycleTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        base=Path(self.tmp.name).resolve();self.root=base/'root';self.root.mkdir();self.home=base/'home'
        self.entry=self.root/'apps/simulator/build/index.js';self.entry.parent.mkdir(parents=True);self.entry.write_text('// fixture')
        self.node=base/'node';self.node.write_text('fixture');self.node.chmod(0o700)
        self.registry=self.root/'registry.json';self.registry.write_text('{}')
        self.fake=Fake();self.s=m.Service(self.root,home=self.home,uid=123,run=self.fake.run,read_health=self.fake.health,port_listening=lambda:bool(self.fake.path or self.fake.foreign),sleep=lambda _:None)
        self.data=self.s.desired(self.node,self.registry)
    def test_ensure_reuses_exact_job(self):
        self.assertTrue(self.s.ensure(self.data)['healthy']);self.s.ensure(self.data)
        self.assertEqual(sum(c[0]=='bootstrap' for c in self.fake.calls),1)
        self.assertEqual(self.data['EnvironmentVariables']['HOST'],'127.0.0.1')
        self.assertEqual(self.data['EnvironmentVariables']['WORKBENCH_SIMULATORS'],str(self.registry))
    def test_unmanaged_port_never_stopped(self):
        self.fake.foreign={'service':'someone-else','instance':'other'}
        with self.assertRaisesRegex(m.ServiceError,'another service'):self.s.ensure(self.data)
        self.assertFalse(any(c[0] in ('bootout','bootstrap') for c in self.fake.calls))
    def test_foreign_checkout_label_refused(self):
        self.fake.path=Path('/foreign/job.plist');self.fake.config=self.data
        with self.assertRaisesRegex(m.ServiceError,'another checkout'):self.s.stop()
        self.assertFalse(any(c[0]=='bootout' for c in self.fake.calls))
    def test_install_stop_and_uninstall(self):
        self.s.ensure(self.data);self.s.install(self.data)
        self.assertEqual(self.fake.path,self.s.installed)
        self.assertTrue(self.s.stop()['installed_for_login']);self.assertTrue(self.s.installed.exists())
        self.s.ensure(self.data);self.s.uninstall()
        self.assertIsNone(self.fake.path);self.assertFalse(self.s.installed.exists())
    def test_foreign_install_preserved(self):
        self.s.installed.parent.mkdir(parents=True);self.s.installed.write_bytes(plistlib.dumps({'Label':m.LABEL,'WorkingDirectory':'/other'}))
        before=self.s.installed.read_bytes()
        with self.assertRaisesRegex(m.ServiceError,'foreign plist'):self.s.install(self.data)
        self.assertEqual(before,self.s.installed.read_bytes());self.assertEqual(self.fake.calls,[])
    def test_owned_disk_foreign_loaded_job_never_mutated(self):
        import copy
        self.s.install(self.data)
        original=self.s.installed.read_bytes()
        changes=[('ProgramArguments',[str(self.node),'/other/apps/simulator/build/index.js']),
                 ('WorkingDirectory','/other')]
        for key,value in changes:
            with self.subTest(field=key):
                self.fake.config=copy.deepcopy(self.data);self.fake.config[key]=value
                before=len(self.fake.calls)
                for operation in (self.s.stop,self.s.uninstall,lambda:self.s.install(self.data)):
                    with self.assertRaisesRegex(m.ServiceError,'differ'):operation()
                self.assertFalse(any(c[0] in ('bootout','bootstrap') for c in self.fake.calls[before:]))
                self.assertEqual(original,self.s.installed.read_bytes())
        for key in ('WORKBENCH_INSTANCE_ID','WORKBENCH_SIMULATORS','HOST','PORT','ORIGIN','WORKBENCH_ALLOWED_ORIGIN'):
            with self.subTest(environment=key):
                self.fake.config=copy.deepcopy(self.data);self.fake.config['EnvironmentVariables'][key]='foreign'
                before=len(self.fake.calls)
                with self.assertRaisesRegex(m.ServiceError,'loaded environment differs'):self.s.stop()
                self.assertFalse(any(c[0]=='bootout' for c in self.fake.calls[before:]))
    def test_noncanonical_origin_rejected_before_mutation(self):
        for value in ('https://foo.ts.net:443','https://FOO.ts.net','HTTPS://foo.ts.net','https://foo.ts.net:08454'):
            with self.subTest(origin=value):
                before=list(self.fake.calls)
                with self.assertRaises(m.ServiceError):self.s.desired(self.node,self.registry,value)
                self.assertEqual(before,self.fake.calls)
        self.assertEqual(m.origin('https://foo.ts.net'),'https://foo.ts.net')
    def test_missing_build_does_not_bootstrap(self):
        self.entry.unlink()
        with self.assertRaisesRegex(m.ServiceError,'built server missing'):self.s.desired(self.node,self.registry)
        self.assertEqual(self.fake.calls,[])
    def test_origin_and_configuration_drift(self):
        for value in ('https://example.com','http://a.ts.net','https://u:p@a.ts.net','https://a.ts.net/','https://a.ts.net?q=x'):
            with self.assertRaises(m.ServiceError):m.origin(value)
        data=self.s.desired(self.node,self.registry,'https://mac-mini.duckbill-ionian.ts.net:8454')
        self.s.ensure(data)
        with self.assertRaisesRegex(m.ServiceError,'configuration differs'):self.s.ensure(self.data)
    def test_saved_private_origin_survives_lazy_reuse(self):
        data=self.s.desired(self.node,self.registry,'https://mac-mini.duckbill-ionian.ts.net:8454')
        self.s.install(data);saved=self.s.saved_environment()
        resolved=self.s.desired(self.node,saved['WORKBENCH_SIMULATORS'],saved.get('WORKBENCH_ALLOWED_ORIGIN'))
        self.assertEqual(resolved,data);self.s.ensure(resolved)
        self.assertEqual(sum(c[0]=='bootstrap' for c in self.fake.calls),1)
    def test_health_timeout_keeps_failure_explicit(self):
        self.s.read_health=lambda:None
        with self.assertRaisesRegex(m.ServiceError,'did not become healthy'):self.s.ensure(self.data)
        self.assertIsNotNone(self.fake.path)
    def test_bootstrap_failure_not_reported_ready(self):
        original=self.fake.run
        self.s.run=lambda args,**kw:subprocess.CompletedProcess(args,5,'','failure') if args[1]=='bootstrap' else original(args,**kw)
        with self.assertRaisesRegex(m.ServiceError,'bootstrap failed'):self.s.ensure(self.data)
if __name__=='__main__':unittest.main()
