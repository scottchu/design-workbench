"""Build a contained Workbench workflow and local simulator package without installing it."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
DIRECTORIES = ('skills', 'catalog', 'contracts', 'workflows', 'templates')
SUPPORT = ('scripts/check_registry.py', 'scripts/doctor.py', 'scripts/cad_smoke.py',
           'fixtures/smoke/plate.py', '.tool-versions', '.python-version',
           'pyproject.toml', 'uv.lock', 'package.json', 'package-lock.json',
           'scripts/simulator_service.py', 'apps/simulator/SERVICE.md',
           'docs/iterations/2026-09-06-foundation/VALIDATION.md')
SIMULATOR_SUPPORT = ('package.json', 'svelte.config.js', 'vite.config.js', 'jsconfig.json',
                     'config.example.json', 'README.md', '.gitignore', 'scripts/register.mjs')
SIMULATOR_SOURCE_SUFFIXES = {'.js', '.mjs', '.ts', '.svelte', '.html', '.css'}
SCOPE = 'docs/iterations/2026-09-07-workflow-ownership/PLUGIN_ADDENDUM.md'
SERVICE_SCOPE = 'docs/iterations/2026-09-07-simulator-service/BRIEF.md'

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def safe_file(root: Path, relative: str) -> Path:
    rel = Path(relative)
    if rel.is_absolute() or '..' in rel.parts:
        raise ValueError(f'escaping path: {relative}')
    path = root
    for part in rel.parts:
        path = path / part
        if path.is_symlink():
            raise ValueError(f'symlink is not a package input: {relative}')
    if not path.is_file() or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f'missing or escaping input: {relative}')
    return path

def source_map(root: Path) -> dict[str, str]:
    mapping = {'.codex-plugin/plugin.json': 'packaging/cad-workbench/.codex-plugin/plugin.json',
               'README.md': 'packaging/README.md'}
    for folder in DIRECTORIES:
        base = root / folder
        if base.is_symlink():
            raise ValueError(f'symlink input directory: {folder}')
        for path in sorted(base.rglob('*')):
            if path.is_symlink():
                raise ValueError(f'symlink input: {path.relative_to(root)}')
            if path.is_file():
                name = str(path.relative_to(root))
                mapping[name] = name
    # Only intentional source/config paths: never walk the app root, build cache,
    # node_modules, runtime registry, service state or external project assets.
    app = root / 'apps/simulator'
    for name in SIMULATOR_SUPPORT:
        relative = f'apps/simulator/{name}'
        mapping[relative] = relative
    source = app / 'src'
    if source.is_symlink():
        raise ValueError('symlink simulator source directory')
    for path in sorted(source.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'symlink simulator source: {path.relative_to(root)}')
        if path.is_file() and path.suffix in SIMULATOR_SOURCE_SUFFIXES and not any(part.startswith('.') for part in path.relative_to(source).parts):
            name = str(path.relative_to(root))
            mapping[name] = name
    mapping.update({path: path for path in SUPPORT})
    for path in mapping.values():
        safe_file(root, path)
    return mapping

def validate_package(output: Path) -> None:
    receipt = json.loads(safe_file(output, 'PACKAGE_RECEIPT.json').read_text())
    expected = set(receipt['files']) | {'PACKAGE_RECEIPT.json', 'PACKAGE_INPUTS.sha256'}
    actual = set()
    for p in output.rglob('*'):
        if p.is_symlink():
            raise ValueError(f'package symlink: {p}')
        if p.is_file(): actual.add(str(p.relative_to(output)))
    if actual != expected:
        raise ValueError('package file inventory differs from receipt')
    for target, row in receipt['files'].items():
        if digest(safe_file(output,target)) != row['sha256']:
            raise ValueError(f'package hash mismatch: {target}')
    for name in SUPPORT:
        safe_file(output, name)
    for name in SIMULATOR_SUPPORT:
        safe_file(output, f'apps/simulator/{name}')
    safe_file(output, 'apps/simulator/src/app.html')
    safe_file(output, 'apps/simulator/src/routes/+page.svelte')
    inputs = safe_file(output,'PACKAGE_INPUTS.sha256')
    if digest(inputs) != receipt['input_manifest_sha256']:
        raise ValueError('input manifest hash mismatch')
    for line in safe_file(output, 'catalog/POLICY.sha256').read_text().splitlines():
        sha, name = line.split('  ',1)
        if digest(safe_file(output,name)) != sha:
            raise ValueError(f'policy hash mismatch: {name}')
    for folder in ('skills','catalog','contracts','workflows'):
        for p in (output/folder).rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
                if '://' in target or target.startswith('#'): continue
                link = (p.parent/target.split('#',1)[0]).resolve()
                if not link.is_relative_to(output.resolve()) or not link.is_file():
                    raise ValueError(f'broken or escaping reference: {p}: {target}')
    registry = json.loads(safe_file(output,'catalog/registry.json').read_text())
    for cap in registry['capabilities']:
        for path in (cap['provider'].get('path'),cap['evidence'].get('reference')):
            if path: safe_file(output,path)
    manifest = json.loads(safe_file(output,'.codex-plugin/plugin.json').read_text())
    if manifest['name'] != output.name or manifest.get('skills') != './skills/':
        raise ValueError('plugin name/skills path mismatch')
    if any(key in manifest for key in ('apps','mcpServers','hooks')):
        raise ValueError('unexpected plugin runtime registration')

def build(root: Path, output: Path, revision: str | None = None) -> Path:
    root = root.absolute(); output = output.absolute()
    # Refuse symlink output ancestors as well as preexisting output.
    for p in (output,*output.parents):
        if p.is_symlink(): raise ValueError(f'symlink output path: {p}')
    if output.exists(): raise ValueError(f'output already exists: {output}')
    if output.name != 'cad-workbench': raise ValueError('output folder must be cad-workbench')
    mapping = source_map(root)
    scope = safe_file(root,SCOPE)
    service_scope = safe_file(root,SERVICE_SCOPE)
    if revision is None:
        revision = subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()
    if not re.fullmatch('[0-9a-f]{40}',revision): raise ValueError('invalid source revision')
    inputs = {source:digest(safe_file(root,source)) for source in mapping.values()}
    inputs[SCOPE] = digest(scope)
    inputs[SERVICE_SCOPE] = digest(service_scope)
    inputs['scripts/package_plugin.py'] = digest(safe_file(root,'scripts/package_plugin.py'))
    manifest_text=''.join(f'{sha}  {name}\n' for name,sha in sorted(inputs.items()))
    output.mkdir(parents=True)
    rows={}
    for target,source in sorted(mapping.items()):
        src=safe_file(root,source); data=src.read_bytes()
        if hashlib.sha256(data).hexdigest()!=inputs[source]:raise ValueError(f'input changed during packaging: {source}')
        dst=output/target;dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(data)
        rows[target]={'source':source,'sha256':inputs[source]}
    (output/'PACKAGE_INPUTS.sha256').write_text(manifest_text)
    receipt={'format_version':1,'source_revision':revision,'source_identity':'Git revision plus input manifest; includes uncommitted declared inputs when present','base_policy_revision':'36f41715ee2257c0f2e41e40329216e3d2b2747f','scope_sources':[SCOPE,SERVICE_SCOPE],'input_manifest_sha256':digest(output/'PACKAGE_INPUTS.sha256'),'files':rows,'components':{'simulator':{'setup_required':True,'source_files':[name for name in sorted(rows) if name.startswith('apps/simulator/') or name in ('package.json','package-lock.json','scripts/simulator_service.py')],'private_runtime_state_included':False}},'runtime_status':'not installed; local simulator source included but not built or started; no providers executed'}
    (output/'PACKAGE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    # Recheck all decision-bearing inputs after copying, including scope and builder.
    for source,sha in inputs.items():
        if digest(safe_file(root,source))!=sha:raise ValueError(f'input changed during packaging: {source}')
    validate_package(output)
    return output

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'.workbench/plugin/cad-workbench')
    parser.add_argument('--check',type=Path,help='read back an existing package only')
    args=parser.parse_args()
    try:
        if args.check:
            validate_package(args.check);print(f'PASS: package readback {args.check}')
        else:
            out=build(ROOT,args.output);print(f'PASS: built and read back {out}');print(f'receipt SHA-256 {digest(out/"PACKAGE_RECEIPT.json")}')
        return 0
    except (OSError,ValueError,KeyError,TypeError) as exc:
        print(f'ERROR: {exc}');return 1
if __name__=='__main__':raise SystemExit(main())
