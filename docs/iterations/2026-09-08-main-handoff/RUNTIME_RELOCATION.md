# Simulator relocated to main

Date: 2026-09-08. User explicitly requested despawning the old simulator, merging
all work into main and restarting from main. Implementation PRs and handoff PR2
were already merged. This follow-up changes runtime ownership and current handoff
records; no application or CAD source changed.

## Completed transition

Canonical checkout `/Users/scottchu/Projects/personal/CAD-workbench` was clean on
setup/foundation. Root fetched origin/main, switched to main and fast-forwarded.
The production build used main `4377bf2a9ded3ef81fed68ca58d6f87b19f731c8`; subsequent
relocation documentation does not alter application inputs.

Executed there: `uv sync --locked --all-packages --all-groups`,
`npm ci --ignore-scripts`, `npm run build:simulator`: PASS. Existing lockfiles were
preserved. npm retains the documented three low-severity advisories.

Before stopping anything, root checked all six registered external Laifen asset
hashes and the source hash, copied the exact registry bytes into canonical main's
ignored `.workbench/simulators.json`, and preserved the old runtime.json and
LaunchAgent plist under `.workbench/runtime-relocation/` with mode0600. Project
source/assets remain in their existing external design checkout.

From old 7e46: `uv run python scripts/simulator_service.py uninstall` returned
stopped=true and installed_for_login=false. From canonical main:
`WORKBENCH_ALLOWED_ORIGIN=https://mac-mini.duckbill-ionian.ts.net:8454 uv run python scripts/simulator_service.py install`
returned loaded/healthy/managed/installed_for_login=true for the new root-derived
instance `21834b4148066f30e0379325`.

After verifying new health and actual plist WorkingDirectory/registry, root
atomically replaced `~/.config/cad-workbench/runtime.json`, preserving mode0600.
It now names canonical main and the new instance. A subsequent bare `ensure`
returned the same healthy managed instance. Tailscale Serve configuration and the
private port8454 -> localhost4179 mapping were not changed.

## Acceptance and handoff

Both localhost and private HTTPS returned the expected new health identity and
HTTP200 for `/`, `/simulators/laifen-customizer` and
`/assets/laifen-customizer/index.html`. Downloaded private WASM SHA-256 matched the
unchanged registry. The actual installed plist points to canonical main, its
production build, and its own registry. This proves server relocation and endpoint
readback, not new browser compilation, phone interaction, reboot or CAD acceptance.
Prior phone/browser evidence remains historical.

The old 7e46 worktree is no longer a live service dependency. It was not deleted;
ignored recovery/build files remain available. Future service operations use the
canonical main root through the current binding. The next-agent development
worktree remains separate. Deliver these updated records through a PR into main,
then fast-forward canonical main and the handoff branch; no rebuild is needed for
that documentation-only change.
