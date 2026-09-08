# Project state

Updated: 2026-09-08. Active handoff:
[main cutover and new worktree](docs/iterations/2026-09-08-main-handoff/HANDOFF.md).
Use [NEXT_AGENT.md](NEXT_AGENT.md) as the fresh-session entrypoint.

## Delivered

CAD Workbench owns the reusable CAD/sticker workflow plugin and one local
SvelteKit simulator host. Project repositories retain source, simulation logic,
assets and evidence. Printer/slicer MCP, API, dashboard and widgets remain with
external providers; text-to-CAD remains separately maintained.

Workbench PR1 merged into main at `3ed377ed98e18d9945b854043ffb27b4c8c851b8`;
main is now the default branch. Design-projects PR23 merged at
`cf8ec46cffc24d8beb26d3908bb6023843824f1f`; sticker-projects PR1 merged at
`cd20668470811e744a09d7ffa485f39cd0883a71`. Both consumers select Workbench
`1d7f4fcd65e04136bb6bad24e90015ca36d97f2f` and policy manifest
`b95f77ef16d317366d1c93f7ff76dee92c0e69976ce55facec10512e23b6c3cf`.

Migration inventory and recovery passed independent validation. All 40 baseline
shared files were accounted for, 20 other root paths classified, and missing
simulation/branch guidance reconciled with independent review. See
[completeness evidence](docs/iterations/2026-09-08-plugin-install/RECONCILIATION.md).
No unrelated canonical project WIP was promoted into main.

Plugin `cad-workbench@personal`, version `0.2.0+codex.20260908111035`, is installed
and enabled; all 67 packaged source files matched the reviewed package. Three
skills are discoverable. The existing user daemon on localhost4179 remains healthy
and has optional private Tailscale Serve8454. User confirmed phone access.

## Current gate and next action

Gate: actual invocation of the installed skill in a new conversation. Next: resolve
the existing runtime binding and open Laifen through workbench-flow, reusing the
current server. User decision needed: none for this bounded check. The separate
roadmap milestone 1 measurement/build-identity contract is still incomplete;
serving the existing customizer does not complete it. The canonical ordered
software roadmap remains [docs/roadmap.md](docs/roadmap.md).

New development worktree: `/Users/scottchu/Projects/personal/CAD-workbench-next`.
The runtime was explicitly relocated to the canonical main checkout
`/Users/scottchu/Projects/personal/CAD-workbench`; its binding selects instance
`21834b4148066f30e0379325`. The old 7e46 service is uninstalled. See
[relocation evidence](docs/iterations/2026-09-08-main-handoff/RUNTIME_RELOCATION.md).

## Evidence and limits

Current delivery checks: 29 Python tests, 11 simulator tests and zero-error/warning
Svelte check; sticker14 tests pass. Consumer provider hashes pass. Design root
checks retain one independently confirmed preexisting missing Laifen VALIDATION.md
failure (10 pass, one fail). Prior actual STEP readback and two browser-generated
STL readbacks remain recorded in their original iterations; no new CAD or printer
operation occurred during cutover. Full recipe execution, mobile parameter/export
coverage, reboot and physical acceptance remain unverified. Dependency audit
limitations and preserved project/recovery identities are linked in the handoff.
