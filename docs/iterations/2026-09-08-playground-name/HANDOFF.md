# Playground source rename handoff

User chose `playground` for the shared application. Source now lives at
`apps/playground`, workspace `@design-workbench/playground`, with canonical
`dev/check/test/build:playground` scripts and compatible `*:simulator` aliases.
The catalog heading now says Playground; project routes and registration semantics
remain compatible and no generic image-review capability is claimed.

Package inputs, current source links, registration tests and lifecycle controller
use the new path. Existing technical service identity, script filename, registry
schema/environment variables, plugin ID and package component key remain stable.
Skills resolve the complete app root in the actually bound runtime, including a
legacy source layout. Historical evidence retains its original commands and paths.

The controller recognizes verified same-root legacy build plists. Ensure/start/open
reuse the saved entrypoint; explicit install selects the new playground build.
Missing saved builds fail rather than silently changing candidates. Keep old
ignored build/cache files until a separately authorized runtime update has passed.
Root ignore rules protect them after the old app-local ignore file moves.

This is source work in `/Users/scottchu/Projects/personal/CAD-workbench-next` on
`codex/composable-skills`, delivered as a PR4 follow-up. Canonical main and its
runtime root remain `/Users/scottchu/Projects/personal/CAD-workbench`; no service
operation occurred. Local root folder names remain unchanged as requested.

See [VALIDATION.md](VALIDATION.md) and [REVIEW.md](REVIEW.md). Next is PR4 review/merge,
then separately scope installed-package and live playground acceptance. Do not
rebuild/restart the live service merely because the source PR is merged. The
existing three-skill installation and consumer bindings are unchanged.
