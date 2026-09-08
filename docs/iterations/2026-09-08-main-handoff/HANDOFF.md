# Main cutover and fresh-agent handoff

Current runtime update: the user subsequently authorized stopping the 7e46
instance and restarting from canonical main. This is completed; the binding now
selects `/Users/scottchu/Projects/personal/CAD-workbench`, instance
`21834b4148066f30e0379325`. See [RUNTIME_RELOCATION.md](RUNTIME_RELOCATION.md).
The earlier runtime-preservation instructions below are historical and superseded.

Date: 2026-09-08. The user explicitly requested merging this thread's work into
main and handing off under a new worktree. The three implementation PRs are now
MERGED, verified through GitHub after exact-head merge commands:

| Repository | PR | Merge commit |
| --- | --- | --- |
| CAD-workbench | [1](https://github.com/scottchu/CAD-workbench/pull/1) | `3ed377ed98e18d9945b854043ffb27b4c8c851b8` |
| design-projects | [23](https://github.com/scottchu/design-projects/pull/23) | `cf8ec46cffc24d8beb26d3908bb6023843824f1f` |
| sticker-projects | [1](https://github.com/scottchu/sticker-projects/pull/1) | `cd20668470811e744a09d7ffa485f39cd0883a71` |

Workbench previously had default setup/foundation and no main. Root created main
from the existing foundation, set it as default, retargeted PR1 and merged it.
The old foundation branch and all recovery/history refs are preserved. The final
handoff documentation is a separate PR on codex/next-agent-handoff; inspect its
merged Git history for the final main tip rather than treating the table as a
permanent latest-HEAD claim.

## Consumer cutover

Both consumers now bind the exact reconciled provider commit
`1d7f4fcd65e04136bb6bad24e90015ca36d97f2f`, reachable from Workbench main, and policy
index SHA-256 `b95f77ef16d317366d1c93f7ff76dee92c0e69976ce55facec10512e23b6c3cf`.
Root and independent reviewer read all 33 declared policy entries from that Git
commit and verified their hashes. Design commit `1780798fdfa3c12f6db44ca939becff9aa092470`
and sticker commit `766b44377a73643477712bf898fb0ac0cee94a92` changed only binding and
root continuity. Project and recovery trees remain unchanged. REVIEW.md records
independent scope acceptance and exact identities.

The canonical design checkout's dirty branch and original sticker-pilot WIP remain
untouched. Their working directories were not reset or switched to main. Remote
main consolidation covers this thread's reviewed migration, not arbitrary unrelated
branches. The retained separation checkout is
`/Users/scottchu/Projects/personal/design-projects-workflow-separation`; sticker
checkout is `/Users/scottchu/Projects/personal/sticker-projects`.

## New worktree and runtime boundary

New development path: `/Users/scottchu/Projects/personal/CAD-workbench-next`.
Branch: `codex/next-agent-handoff`, created from merged origin/main. The final
handoff PR is merged before delivery and this branch is fast-forwarded to the
resulting origin/main. NEXT_AGENT.md provides the fresh-session starting point.
Use current repository evidence without reconstructing the old chat.

Root uv/npm environments were initialized from committed locks. No registry,
project build, installed-service state or private binding was copied here. The
installed plugin remains `0.2.0+codex.20260908111035`; documentation-only handoff
changes do not require another reinstall.

The live runtime remains `/Users/scottchu/.codex/worktrees/7e46/CAD-workbench`.
Its user-local binding at `~/.config/cad-workbench/runtime.json` selects instance
`ca3daa81c9c60ef20aa7f16b`. Preserve that worktree and use its absolute `.venv/bin/python`
with its working directory for owned lifecycle commands. Do not install a second
service or rebind the daemon from the new worktree. Local URL localhost4179;
private Tailscale Serve https://mac-mini.duckbill-ionian.ts.net:8454/ . Final old-root
status remained loaded, healthy, managed and installed_for_login. No network or
service configuration changed. The user already confirmed phone access.

## Checks and remaining work

Executed for this delivery:

- Workbench `uv run python -m unittest discover -s tests -v`: 29 pass.
- `npm run test:simulator`: 11 pass; `npm run check:simulator`: zero errors/warnings.
- Design `uv run pytest tests/test_repository_structure.py`: 10 pass, one unchanged
  baseline failure: Laifen CURRENT points at 2026-09-06-pattern-reference-intake
  without VALIDATION.md. No check was skipped or project evidence fabricated.
- After repinning, `CAD_WORKBENCH_CHECKOUT=/Users/scottchu/.codex/worktrees/7e46/CAD-workbench uv run pytest tests/test_repository_structure.py -k 'external_workflow or bound_workflows'`:
  two pass. Independent and root Git-blob policy checks both pass.
- Sticker `npm test`: 14 pass. No project art/source generation ran.
- New-worktree `uv sync --locked --all-packages --all-groups`,
  `npm ci --ignore-scripts`, `uv run python scripts/doctor.py`,
  `uv run python scripts/check_registry.py` and Svelte check passed. Doctor confirms
  its own root .venv, Python3.12.13 and cadgen0.5.0. Locks are unchanged. npm reports
  three low-severity advisories; no dependency upgrade was bundled into handoff.
  Sticker's previously recorded sharp advisory remains separate.

Next agent: invoke workbench-flow in the new conversation, resolve the existing
runtime and open Laifen, recording actual skill invocation and server reuse.
No full portable design-to-print execution, mobile export acceptance or reboot
acceptance is claimed. Continue roadmap work only from its current contracts.
