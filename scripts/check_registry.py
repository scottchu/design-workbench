"""Check discovery references and pinned policy bytes; does not execute recipes."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

def check(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    def local(value: str) -> Path:
        path = root / value
        if not path.resolve().is_relative_to(root.resolve()) or not path.is_file():
            errors.append(f'missing or escaping local path: {value}')
        return path
    registry = json.loads((root / 'catalog/registry.json').read_text())
    caps, workflows = registry['capabilities'], registry['workflows']
    ids = [x['id'] for x in caps]
    if len(ids) != 12 or len(set(ids)) != len(ids):
        errors.append('expected twelve unique capabilities')
    workflow_ids = [x['id'] for x in workflows]
    if len(workflow_ids) != 2 or len(set(workflow_ids)) != len(workflow_ids):
        errors.append('expected two unique workflows')
    for cap in caps:
        for key in ('id','category','maturity','provider','evidence','completion_gate'):
            if not cap.get(key): errors.append(f'missing capability field {key}')
        p = cap['provider']; e = cap['evidence']
        if not p.get('version') or not cap['completion_gate']: errors.append('missing version or completion gate')
        if cap['maturity'] == 'reported-unknown':
            if p.get('path') or e.get('quality') != 'reported': errors.append('reported capability promoted without evidence')
        else:
            if not p.get('command') or not e.get('reference'): errors.append('missing provider command or evidence')
            if p.get('path'): local(p['path'])
            if e.get('reference'): local(e['reference'])
    for workflow in workflows:
        local(workflow['recipe']);local(workflow['binding_contract'])
        if set(workflow['capabilities']) - set(ids): errors.append('unknown capability reference')
        if not workflow.get('version') or not workflow.get('completion_gate'): errors.append('missing recipe version/gate')
    manifest = local(registry['policy_manifest'])
    covered = set()
    if manifest.is_file():
        for line in manifest.read_text().splitlines():
            digest, path = line.split('  ',1);covered.add(path);target=local(path)
            if not re.fullmatch('[0-9a-f]{64}',digest):errors.append(f'invalid digest: {path}')
            if target.is_file() and hashlib.sha256(target.read_bytes()).hexdigest()!=digest:errors.append(f'policy hash mismatch: {path}')
    required={str(p.relative_to(root)) for folder in ('catalog','contracts','workflows','skills','templates') for p in (root/folder).rglob('*') if p.is_file() and p.name!='POLICY.sha256'}
    if required-covered:errors.append(f'unpinned policy files: {sorted(required-covered)}')
    # Check maintained reference links; templates intentionally contain project placeholders.
    for folder in ('catalog','contracts','workflows','skills'):
        for p in (root/folder).rglob('*.md'):
            for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
                if '://' in link or link.startswith('#'):continue
                target=(p.parent/link.split('#')[0]).resolve()
                if not target.is_relative_to(root.resolve()) or not target.is_file():errors.append(f'broken link in {p.relative_to(root)}: {link}')
    json.loads((root/'contracts/receipt.schema.json').read_text())
    return errors

def main() -> int:
    try: errors=check()
    except (KeyError,ValueError,TypeError,OSError) as exc: errors=[str(exc)]
    for error in errors:print(f'ERROR: {error}')
    if not errors:print('PASS: 12 capabilities, 2 mapped recipes, local references and policy hashes; no recipe executed')
    return int(bool(errors))
if __name__=='__main__':raise SystemExit(main())
