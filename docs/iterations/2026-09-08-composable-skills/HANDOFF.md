# Composable skills: step 1 handoff

Base: `d92816a`; local development branch: `codex/composable-skills` in
`/Users/scottchu/Projects/personal/CAD-workbench-next`. Canonical main remains
unchanged and owns the installed simulator. Subsequent authorized delivery is
[PR4](https://github.com/scottchu/design-workbench/pull/4), open and not merged.

Step 1 recorded decision 0003's project/workflow/skill/tool responsibilities,
Markdown composition, and two-skill playground pilot. Step 2 implements that
source extraction as described below, without changing runtime behavior.

## Step 2 local source delivery

The user authorized the next step with "ok". Added simulator-server and
simulator-page, moved server instructions to the server skill, retained the old
local-server path as a compatibility pointer, and routed workbench-flow and the
CAD recipe to the new tasks. Corrected the stale simulator provider description.
Policy manifest includes both skills and all maintained policy inputs. No tool
implementation changed. The package has five skills; the installed plugin still
has three. See [VALIDATION.md](VALIDATION.md) and [REVIEW.md](REVIEW.md).

Independent generic forward testing covers registration, stale source/assets,
update and removal with sibling preservation. Review identified two refinements:
registry metadata availability is not full asset readback, and status uses the
existing absolute interpreter without environment sync while allowing the
controller's local lifecycle lock. Both are reflected in the final skill source.

Next bounded delivery: review/merge the now-open PR4.
No installed-plugin update, live server reuse, browser behavior or measured-build
acceptance is claimed. A future installation needs a distinct release identity;
the current package retains the existing manifest version as an unreleased source
candidate identified by its input manifest and receipt. Do not repin consumers to
this unmerged candidate. Scope live invocation separately before expanding the
pilot or splitting sticker tasks.

## Historical step 1 checks

Validation from the development root: `git diff --check` passed. The following
`uv run python` check passed: 6 documents, 11 local links resolve.

```sh
uv run python - <<'PY'
from pathlib import Path
import re
files = [Path(p) for p in ['NEXT_AGENT.md', 'PROJECT_STATE.md', 'docs/architecture.md', 'docs/decisions/0003-composable-skills.md', 'docs/iterations/2026-09-08-composable-skills/BRIEF.md', 'docs/iterations/2026-09-08-composable-skills/HANDOFF.md']]
count = 0
for p in files:
    for target in re.findall(r'\]\(([^)]+)\)', p.read_text()):
        if '://' in target or target.startswith('#'):
            continue
        assert (p.parent / target.split('#')[0]).exists(), (p, target)
        count += 1
print(f'PASS: {len(files)} documents, {count} local links resolve')
PY
```

No service, browser, CAD, export, printer or installed
plugin acceptance is claimed. Historical runtime relocation evidence remains in
the main-handoff iteration. The old fresh-session invocation check remains pending.
