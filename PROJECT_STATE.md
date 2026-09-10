# Project state

Updated: 2026-09-10. Read [product intent](docs/product.md),
[documentation ownership](docs/documentation.md) and [current verification](docs/verification.md).
This file records the state of Design Workbench software; consumer design/image
projects retain their own requirements, candidates, decisions and approvals.

## Delivered and running

- GitHub repository: `scottchu/design-workbench`, private, default branch main.
  Local folders retain their original CAD-workbench names as requested.
- [PR4](https://github.com/scottchu/design-workbench/pull/4) merged at
  `92a74cc30d194a0152c23551446327c0bf506b86`. It delivers five skill sources,
  focused server/page guidance, apps/playground with legacy service compatibility,
  and the purpose-led roadmap. Both worktrees were synchronized to that merge.
- The running service was built from that merge and now selects
  `apps/playground/build/index.js`. Canonical runtime root:
  `/Users/scottchu/Projects/personal/CAD-workbench`; instance:
  `21834b4148066f30e0379325`. Local/private health, Playground home, Laifen page
  and all six registered assets passed current readback. Login persistence remains
  installed. Binding, registry and private origin were preserved.
- Local: http://127.0.0.1:4179/ . Private:
  https://mac-mini.duckbill-ionian.ts.net:8454/ . No Tailscale configuration changed.
- Installed plugin was excluded from refresh. Its last verified installation is
  `cad-workbench@personal`, `0.2.0+codex.20260908111035`, with three skills. The five
  current skill sources/package are not evidence of a five-skill installation.
- The old 7e46 service remains uninstalled; that root is not a runtime dependency.
  No old root or project recovery assets were deleted in this run.

## Current gate and next action

Merge/source delivery and Playground runtime refresh are complete. Five-skill
installation and fresh-session installed-skill acceptance remain pending and were
explicitly excluded from this refresh. Do not perform them as incidental setup.

Product/source boundaries and the bounded reconstruction are documented in their
current owners. The reconstruction has sampled compatibility evidence for one
module; it does not establish a general compiler or full-product reproduction.
Temporary PR6/PR7 iteration notes have been consolidated. Exact technical evidence
is retained outside docs, linked from current verification.

The separate `CAD-workbench-next` worktree contains uncommitted authoring/model
proposals from another task. They are not included in this delivery and must not
be deleted or treated as adopted source. Resolve those proposals before selecting
another reconstruction experiment. Installed-skill acceptance remains separately
pending; no runtime refresh or new compiler implementation is part of closeout.

The [roadmap](docs/roadmap.md) retains R1 installed-skill acceptance, then a bounded
R2 read-only MCP contract. Workbench MCP and consistent-image production are still
planned. The Laifen measured-parameter/display/export identity milestone remains
incomplete; serving the page does not satisfy it. Full portable recipes, detailed
mobile exports, reboot and physical acceptance remain unverified.

## Evidence and historical continuity

Source acceptance: 32 Python tests, 11 frontend tests, zero-error/warning Svelte
check, real playground build and package readback; see
[source validation](docs/iterations/2026-09-08-playground-name/VALIDATION.md) and
[independent review](docs/iterations/2026-09-08-playground-name/REVIEW.md).
Current live results and exact identities are in the
[runtime refresh handoff](docs/iterations/2026-09-08-playground-refresh/HANDOFF.md). Earlier phone
access is user-confirmed historical evidence, not a new phone test this refresh.

The merged ownership extraction and consumer preservation are recorded in
[main handoff](docs/iterations/2026-09-08-main-handoff/HANDOFF.md) and
[reconciliation](docs/iterations/2026-09-08-plugin-install/RECONCILIATION.md).
Design-projects PR23 and sticker-projects PR1 were merged. Last recorded consumer
binding selects Workbench `1d7f4fcd65e04136bb6bad24e90015ca36d97f2f` and policy hash
`b95f77ef16d317366d1c93f7ff76dee92c0e69976ce55facec10512e23b6c3cf`;
this run did not repin or revalidate consumers. Preserve their unrelated WIP.
Historical design root checks retain a preexisting missing Laifen VALIDATION.md
failure (10 pass, one fail); historical sticker checks report 14 pass. No consumer
checks, new CAD/export generation or printer operations were performed here.
