# Roadmap validation

Date: 2026-09-08. Development root:
`/Users/scottchu/Projects/personal/CAD-workbench-next`.
Baseline commit: `6466d15`; branch: `codex/composable-skills`.

Documentation-only scope: roadmap, architecture and continuity. No executable,
skill, packaged policy, dependency or runtime configuration changed. Existing
package/geometry tests were not rerun because this change makes no new runtime or
CAD acceptance claim.

Run from the development root:

```sh
uv run python - <<'PY'
from pathlib import Path
import re, subprocess
old = subprocess.check_output(['git', 'show', '6466d15:docs/roadmap.md'], text=True)
original = old[old.index('## 0. Reproducible foundation'):]
paragraphs = [p for p in original.split('\n\n') if p.strip() and not p.startswith('## ')]
new = Path('docs/roadmap.md').read_text()
for p in paragraphs:
    assert p.strip() in new, p
headings = re.findall(r'^## .+$', original, re.M)
for h in headings:
    assert h in new, h
print(f'PASS: {len(paragraphs)} original paragraphs and {len(headings)} original headings retained verbatim')
files = [Path(p) for p in ('docs/roadmap.md', 'docs/architecture.md', 'PROJECT_STATE.md', 'NEXT_AGENT.md')]
files += list(Path('docs/iterations/2026-09-08-roadmap').glob('*.md'))
links = 0
for p in files:
    for target in re.findall(r'\]\(([^)]+)\)', p.read_text()):
        if '://' in target or target.startswith('#'):
            continue
        assert (p.parent / target.split('#')[0]).is_file(), (p, target)
        links += 1
print(f'PASS: {len(files)} documents, {links} local links resolve')
PY
git diff --check
```

Results: all 14 original requirement/gate paragraphs and all 7 original headings
retained verbatim; all local links resolved; `git diff --check` passed.
Preservation checks verify text/heading retention, not conceptual coherence;
independent review covers scope, status and dependencies separately and reports no
remaining blocker after the two clarifications.
