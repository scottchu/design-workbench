# Start here: CAD Workbench

Continue from this repository's current records. Do not reconstruct the old chat or
repeat the completed migration/install audit unless new evidence identifies a
specific discrepancy. Read AGENTS.md, README.md, PROJECT_STATE.md and
[the main handoff](docs/iterations/2026-09-08-main-handoff/HANDOFF.md).

## Workspace and delivered state

Fresh development worktree: `/Users/scottchu/Projects/personal/CAD-workbench-next`,
branch `codex/next-agent-handoff`, based on `origin/main`. Root uv/npm dependencies
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

Use `cad-workbench:workbench-flow` in the new conversation to resolve the existing
runtime binding and open the registered Laifen simulator. Verify skill invocation
and reuse of the existing server; record only that result. Preserve the confirmed
phone-access evidence. After that, select the next task from docs/roadmap.md and
current project records; do not infer authority to slice or start a print.

Known limits: full portable design-to-print execution, detailed mobile exports and
reboot behavior remain unverified. Design-projects has one preexisting missing
Laifen VALIDATION.md record (10 passing root checks, one failure); do not invent
project evidence to silence it. Canonical dirty design work and sticker pilot WIP
are intentionally preserved outside the merged scope.
