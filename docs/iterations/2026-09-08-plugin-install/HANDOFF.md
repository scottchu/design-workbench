# Installed Workbench plugin

Status: migration completeness repairs independently reviewed; updated plugin
installed/enabled. Current version: `0.2.0+codex.20260908111035`.
Maintained source: `/Users/scottchu/plugins/cad-workbench`; cache:
`/Users/scottchu/.codex/plugins/cache/personal/cad-workbench/0.2.0+codex.20260908111035`.
The personal marketplace and existing simulator binding are unchanged.

See [completeness review](MIGRATION_COMPLETENESS_REVIEW.md) for the 40 migrated / 20
retained baseline paths and additive divergent-branch policy audit, and
[reconciliation evidence](RECONCILIATION.md) for the repair and installation checks.
Both findings are resolved. This covers the audited baseline and divergent shared
guidance, not every historical project lesson or every possible branch.

Current cutover update: the three migration PRs merged on 2026-09-08, and both
consumers now pin the reconciled provider `1d7f4fc`. See
[main handoff](../2026-09-08-main-handoff/HANDOFF.md) and root NEXT_AGENT.md for the
new worktree and observed merge identities. A new conversation should exercise
the installed skill; full portable CAD-to-print execution remains unverified.
The user subsequently authorized and completed relocation to canonical main; see
[relocation evidence](../2026-09-08-main-handoff/RUNTIME_RELOCATION.md). Earlier
old-root installation records below remain historical.

## Original installation record

The following records the initial version `0.2.0+codex.20260908102059` and its receipt;
the current update and receipt are in RECONCILIATION.md.

## Exact setup and checks

Root read the current plugin-creator skill and its installing-and-updating reference,
validated marketplace name `personal`, and confirmed no Workbench entry/source existed.
The existing U1 entry and marketplace metadata were preserved exactly. The initial
marketplace snapshot remains ignored at `.workbench/plugin-install/marketplace-before.json`.

```sh
uv run python /Users/scottchu/.codex/skills/.system/plugin-creator/scripts/update_plugin_cachebuster.py packaging/cad-workbench
uv run python scripts/package_plugin.py --output .workbench/plugin/install-20260908/cad-workbench
uv run python /Users/scottchu/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .workbench/plugin/install-20260908/cad-workbench
uv run python /Users/scottchu/.codex/skills/.system/plugin-creator/scripts/create_basic_plugin.py cad-workbench --with-marketplace
codex plugin add cad-workbench@personal
codex plugin list --marketplace personal --json
```

After the scaffold, root verified its sole created file was the new default manifest,
then copied the complete reviewed package over that owned scaffold. Source package
readback passed before installation. Marketplace readback, removing only the new
Workbench entry, equaled the complete saved original. CLI add succeeded and list
reported installed=true, enabled=true for the stated version; existing U1 remained
installed/enabled at its previous version.

Package receipt SHA-256:
`1e7c3e0cd694f091d11b0a09a5c9a335a6b89560fcc142b61fb2f2aa6e6d1cfa`.
All 67 source files plus receipt/input inventory were compared byte-for-byte between
reviewed source and installed cache. The bundled plugin validator passed directly
on the cache. Our source-package checker initially rejected the cache folder's
version-based name (it requires outer name cad-workbench); a byte-identical cache
copy at ignored `.workbench/plugin-install/cache-readback/cad-workbench` passed full
package reference/hash validation. No checker or identity requirement was disabled.

Three cached skills are present: workbench-flow, design-reflection and
sticker-pack-production. The workbench-flow quick validator, catalog checker and
four registry tests passed after the binding-document change. REVIEW.md covers
valid, absent and mismatched binding scenarios independently. No runtime controller,
HTTP policy, launchd or Tailscale code/configuration was changed in this iteration.

## Existing runtime binding

Machine-local file: `~/.config/cad-workbench/runtime.json`, mode0600. Version1 binds
this canonical Workbench root, instance `ca3daa81c9c60ef20aa7f16b` and local URL
`http://127.0.0.1:4179`. It was created only after actual managed/healthy status and
root-derived identity matched; an existing differing file would have been preserved.
The binding is excluded from the package and from Git.

Following the installed skill's instructions, root read/validated the binding,
then invoked status and ensure with the original runtime root's absolute
`.venv/bin/python` and working directory. Both returned the matching healthy,
managed instance; lsof confirmed the same PID17805 before and after. No environment
was created in the installed plugin cache. Private HTTPS health at
https://mac-mini.duckbill-ionian.ts.net:8454/health returned the matching instance.

The root runtime path is still this worktree. Preserve it until explicit runtime
relocation; plugin cache updates do not transfer service ownership. See the previous
simulator-service iteration for owned stop/uninstall and private endpoint removal.

## New conversation handoff

Codex needs a new conversation to pick up the newly installed skills. CLI/cache
verification does not establish actual invocation in a fresh agent session. Suggested
first request: use cad-workbench:workbench-flow to open the existing Laifen simulator
through its runtime binding. This should reuse the server and require no plugin,
runtime, Tailscale or printer reconfiguration. No merge or fresh model/print/platform
acceptance is claimed by plugin installation.
