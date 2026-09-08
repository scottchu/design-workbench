# Merge migration and hand off a clean worktree

The user explicitly authorized getting this thread's work into main and handing
it to a new agent in a new worktree. This covers Workbench PR1, design PR23 and
sticker PR1, the latest reconciled provider binding, and concise current handoff
records. It does not promote unrelated canonical design WIP or sticker pilot WIP.

Create Workbench main from its existing setup/foundation default, retarget PR1,
and make main the default. Preserve setup/foundation and all recovery/history refs.
Merge reviewed migration branches with merge commits and exact head checks. Pin
both consumers to Workbench 1d7f4fcd65e04136bb6bad24e90015ca36d97f2f and policy index
b95f77ef16d317366d1c93f7ff76dee92c0e69976ce55facec10512e23b6c3cf, which contain the
independently reviewed completeness repairs. Follow up through a documentation PR
with observed merge identities and the new handoff.

Create /Users/scottchu/Projects/personal/CAD-workbench-next on a new non-main branch
from the completed origin/main. Initialize its own root uv/npm development
workspace; do not copy caches, private bindings or simulator registry. The current
worktree /Users/scottchu/.codex/worktrees/7e46/CAD-workbench remains the live runtime
owner and must not be removed, rebound or restarted during handoff. The new agent
reads the runtime binding and uses that root for service operations.

Root owns cutover, records and new worktree. Independent reviewer owns REVIEW.md
only and verifies exact provider hashes and mutation boundaries. Checks: current
Workbench 29 Python tests, 11 simulator tests and Svelte check; sticker npm tests;
design structure checks with its known preexisting Laifen missing VALIDATION
failure reported explicitly; consumer provider Git blob hashes; clean fresh
worktree and remote main reachability; existing runtime health. Prior immutable
migration preservation evidence remains valid because project bytes do not change.
No new CAD, art, release, printing or network configuration is part of delivery.
