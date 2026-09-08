# Rename the application to playground

Why: the shared application hosts project exploration/review; simulator is one
current page type. The user selected playground after discussing the naming.

How: rename apps/simulator to apps/playground in this development worktree, update
the workspace/lock, commands, packaging, current references and focused checks.
Keep old npm simulator commands as compatibility aliases. Preserve existing
service label, health identity, registry schema/routes and runtime binding.
The lifecycle controller must still inspect/reuse a verified same-root legacy
build configuration; a deliberate install selects the new build. Never silently
migrate a running configuration as a side effect of ensure/open.

What: source builds/tests/package readback at the new path, explicit compatibility
checks and current handoff. No broad UI functionality or generic page schema is
added. Historical evidence retains original command/artifact paths. No local root
folder rename, live service call, plugin installation, private registry edit,
project asset move or network configuration change. Canonical main remains the
live runtime owner. This is a follow-up on the already authorized PR4 branch.

Root owns implementation and validation; independent reviewer owns REVIEW.md and
read-only acceptance of source/tests, with scratch output ignored. Verify workspace
lock resolution, Svelte checks, real build, policy hashes, package readback and
legacy/new ownership transitions using bounded lifecycle fakes. Source validation
is separate from any later live service update.
