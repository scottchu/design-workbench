# Project state

Repository identity update, 2026-09-08: GitHub renamed to
`scottchu/design-workbench` to reflect CAD, image and future design domains.
Local `origin` updated; repository ID, main commit, privacy, local folders and
runtime binding are unchanged. This does not rename the installed plugin or
publish the pending local source commits.

Updated: 2026-09-08. Active handoff:
[roadmap compilation](docs/iterations/2026-09-08-roadmap/HANDOFF.md).
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

Latest request compiles the accepted discussion into [the roadmap](docs/roadmap.md):
why -> how -> what, focused context-selected tasks, planned owned playground MCP,
consistent-image production and preserved CAD milestones. This is documentation,
not implementation of those new capabilities. The next step remains authorized
PR delivery of local work, followed by separately scoped installed/live acceptance.
See the active roadmap brief and handoff; do not execute all future milestones
under the roadmap-writing request.

Current user-directed work supersedes the earlier next-action ordering below:
[decision 0003](docs/decisions/0003-composable-skills.md) and the local step 2 pilot
are implemented on `codex/composable-skills`. Source now has five skills, including
simulator-server and simulator-page; workbench-flow routes to those task owners.
The candidate package passed local readback and focused checks; see
[validation](docs/iterations/2026-09-08-composable-skills/VALIDATION.md) and
[independent review](docs/iterations/2026-09-08-composable-skills/REVIEW.md).
The installed three-skill plugin and runtime are unchanged. No remote delivery or
consumer repinning occurred. Next: deliver this reviewed source through the PR
route once remote push is authorized, then separately scope installed-skill/live
invocation acceptance. Sticker splitting remains deferred until the playground
pilot is accepted. The historical fresh-session invocation gate remains pending.

Earlier gate: actual invocation of the installed skill in a new conversation. Resolve
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
