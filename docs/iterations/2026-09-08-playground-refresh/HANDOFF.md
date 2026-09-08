# PR4 merge and running Playground refresh

Date: 2026-09-08. User authorized merge and explicitly selected source plus running
Playground refresh; installed skills plugin excluded. Runtime root is unchanged:
`/Users/scottchu/Projects/personal/CAD-workbench`. Development root remains
`/Users/scottchu/Projects/personal/CAD-workbench-next`.

## Merge and preparation

Both worktrees were clean. PR4 was open/mergeable with head
`58b35cb6de5d263148180821db0d6c5333031afc`, matching the remote branch and reviewed
local source. Executed:

```sh
gh pr merge 4 --repo scottchu/design-workbench --merge --match-head-commit 58b35cb6de5d263148180821db0d6c5333031afc
gh pr view 4 --repo scottchu/design-workbench --json state,mergedAt,mergeCommit,url
git fetch origin main
git -C /Users/scottchu/Projects/personal/CAD-workbench merge --ff-only origin/main
git merge --ff-only origin/main
```

PR4 readback: MERGED at 2026-09-08T16:35:46Z, merge commit
`92a74cc30d194a0152c23551446327c0bf506b86`. Both roots fast-forwarded to it.
No folder or branch deletion occurred.

Used the repository's simulator-server source guidance and service contract for
this operation; it was not an invocation of newly installed plugin skills.
The absolute root interpreter's `scripts/simulator_service.py status` confirmed
healthy managed ownership, instance `21834b4148066f30e0379325`, login persistence,
and the same-root legacy apps/simulator build before update.

Created mode0700 ignored recovery directory
`.workbench/playground-refresh/pr4-92a74cc` in the runtime root, preserving
mode0600 runtime.before.json, service.before.plist and registry.before.json.
`before.json` records selected identities. Read the source/asset registry through
apps/playground/src/lib/server/registry.js: Laifen source hash and all six assets
passed before any service update. No external project assets were copied.

From canonical main:

```sh
npm install --ignore-scripts
npm run build:playground
/Users/scottchu/Projects/personal/CAD-workbench/.venv/bin/python scripts/simulator_service.py install
/Users/scottchu/Projects/personal/CAD-workbench/.venv/bin/python scripts/simulator_service.py ensure
```

All passed. npm replaced the workspace link and retained the documented three low
advisories; tracked lock/source files remained clean. Used install to deliberately
switch the existing owned job to the new build while preserving saved private
origin and registry. Install and subsequent ensure both reported loaded, healthy,
managed and installed_for_login true. No Tailscale or plugin installation command ran.

## Actual post-update readback

Read the installed plist and asserted the entrypoint is
`apps/playground/build/index.js`, with unchanged root, instance, registry and
allowed private origin. Python urllib GETs to both localhost4179 and private
HTTPS8454 returned:

- /health: HTTP200, service cad-workbench-simulator and expected instance.
- /: HTTP200 with Playground in the returned home HTML.
- /simulators/laifen-customizer: HTTP200.
- All six registered /assets/laifen-customizer/... files: HTTP200 and SHA-256
  matching every registry entry, including the WASM binary.

Binding and registry bytes are unchanged. Exact before/after receipts remain under
the ignored recovery directory. The prior build remains preserved; no cleanup or
root relocation was performed.

| Identity | SHA-256 |
| --- | --- |
| Runtime binding, before/after | `ebc0145e394acad27f76e5bde868e179c07ff5307adfeb28a66132e4b3e8afec` |
| Simulator registry, before/after | `176351101929718ac3c1d33ca1219726c4b8382748e7d269ba64edf27bc40b5c` |
| Old build entry | `754ddab6cdd23c3848bcc2aafa0d76709106689bbcd301067ecc09b26b887932` |
| New build entry | `46c970b39eb53d99ce93a14de6f41205fcee8a82ed68042ba96be6cac8aa06c2` |
| New installed plist | `398b4a4e39920dfc68c1dff02755e2cb8b1697cb051adcf4a21e6ea106f2018b` |
| Laifen source | `497098afa555092a0ed85a3a7213cd270852aa76f9001e1478c209cd8469bc42` |

## Current boundary and handoff

Source delivery and live HTTP/assets are accepted for this refresh. This does not
establish browser compilation/interaction, new phone testing, reboot behavior,
five-skill installed discovery, CAD parameter/export parity or physical acceptance.
Installed plugin and consumer bindings remain unchanged. Source still contains
five skills; last verified installation contains three.

The user then asked to understand repository folders and continuity documents.
NEXT_AGENT now points to state and operating rules rather than duplicating a task
list. PROJECT_STATE holds current status and links historical evidence; earlier
migration, package and project evidence remains in its original iterations and Git
history. No folder consolidation is performed. Next is the requested explanation,
not automatic MCP implementation or plugin installation.
