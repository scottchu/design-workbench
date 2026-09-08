# Start here: CAD Workbench

Repository name update, 2026-09-08: GitHub is now
`scottchu/design-workbench`; shared `origin` points to that repository. The user
explicitly requested keeping local folder names unchanged. Runtime roots, plugin
IDs and bindings retain their existing names. See the active handoff for evidence.

Continue from this repository's current records. Do not reconstruct the old chat or
repeat the completed migration/install audit unless new evidence identifies a
specific discrepancy. Read AGENTS.md, README.md, PROJECT_STATE.md and
[the main handoff](docs/iterations/2026-09-08-main-handoff/HANDOFF.md).

## Workspace and delivered state

Fresh development worktree: `/Users/scottchu/Projects/personal/CAD-workbench-next`,
branch `codex/composable-skills`, based on main `d92816a` for the current local pilot. Root uv/npm dependencies
are initialized; use only this root's `.venv` for development. Workbench main is
now the default branch. Workbench PR1, design-projects PR23 and sticker-projects PR1
are merged. Both consumers pin the reconciled Workbench revision `1d7f4fc` and its
verified policy manifest. Project source and recovery remain in their own repos.

The plugin `cad-workbench@personal` is installed/enabled at
`0.2.0+codex.20260908111035`, with three skills. The reusable migration and policy
repairs passed independent review. The local simulator works; the user confirmed
phone access. Do not reinstall plugins or redo repository separation as setup.

## Live runtime: canonical main checkout

The user explicitly requested relocation after the initial handoff. The old 7e46
instance was uninstalled and replaced by the service rooted at
`/Users/scottchu/Projects/personal/CAD-workbench`, checked out on `main`.
`~/.config/cad-workbench/runtime.json` now binds that canonical root and instance
`21834b4148066f30e0379325`. Use its absolute `.venv/bin/python` and working directory
for service operations. This development worktree is not the service root.

Local URL: http://127.0.0.1:4179/ . Private access remains
https://mac-mini.duckbill-ionian.ts.net:8454/ . Local/private health, Laifen routes
and the private served WASM hash passed. Login persistence is installed. No
Tailscale configuration changed. The old 7e46 worktree is no longer a runtime
dependency; it remains on disk pending optional separate cleanup.

See [relocation evidence](docs/iterations/2026-09-08-main-handoff/RUNTIME_RELOCATION.md).
Earlier handoff instructions to preserve 7e46 as the live runtime are superseded.

## Next bounded action

The latest user request compiled the discussion into [the roadmap](docs/roadmap.md).
Read the [active roadmap handoff](docs/iterations/2026-09-08-roadmap/HANDOFF.md)
first. It plans owned MCP and consistent-image capabilities without implementing
them; the original CAD gates remain intact. The underlying skill separation is
recorded in
[decision 0003](docs/decisions/0003-composable-skills.md) and the
[skill extraction handoff](docs/iterations/2026-09-08-composable-skills/HANDOFF.md).
Steps 1 and 2 record the architecture decision and extract simulator-server and
simulator-page in local source. The five-skill candidate is verified but is not the
installed three-skill plugin. Read active VALIDATION.md and REVIEW.md before
continuing. Next is PR delivery after authorization for remote push, followed by
separately scoped installed/live acceptance; do not reinstall or operate the server
as incidental delivery. Sticker splitting remains deferred. Communicate in Chinese.
The previous fresh-session invocation/server-reuse check remains pending, separate
from source-package acceptance and measured-build acceptance. Preserve confirmed
phone-access evidence and the canonical main runtime binding.

Known limits: full portable design-to-print execution, detailed mobile exports and
reboot behavior remain unverified. Design-projects has one preexisting missing
Laifen VALIDATION.md record (10 passing root checks, one failure); do not invent
project evidence to silence it. Canonical dirty design work and sticker pilot WIP
are intentionally preserved outside the merged scope.
