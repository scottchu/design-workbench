# Simulator service handoff

Status: implementation and live setup passed; independent review passed; delivered through the existing [Workbench PR 1](https://github.com/scottchu/CAD-workbench/pull/1). This iteration follows the
user's explicit request for a managed local server and optional private Tailscale
access. Earlier no-service-operation statements apply to the completed migration.

The fixed local address is http://127.0.0.1:4179. Private add-on target is
https://mac-mini.duckbill-ionian.ts.net:8454. Port 8454 was absent from the observed
Serve configuration and local listeners. The exact before snapshot is ignored
`.workbench/service-evidence/tailscale-before.json`. Existing configuration includes
other services and a public Funnel permission on 443; none is this simulator's
endpoint and none is to be altered by this iteration.

Root replaced the previous task-owned Vite process (verified PID7868 and cwd) with
the installed adapter-node user LaunchAgent. App check passed with zero errors/warnings,
11 focused tests passed, and the actual production build succeeded. Origin policy
accepts only exact loopback4179 hosts or the explicitly configured HTTPS ts.net
origin; forwarded host headers cannot select it. `/health` names service/instance.

I4 lifecycle and I5 package/skill implementations are complete. R2 ownership and
origin-normalization findings were repaired before live stop/restart. VALIDATION.md
records real same-PID reuse, stop, new-PID restart, preserved private origin,
private HTTPS and browser WASM success. The entire 29-test root suite and 11 app
tests pass. PACKAGE.md identifies the final 67-file source package at ignored
`.workbench/plugin/service-final/cad-workbench`. Original consumer bindings at
36f4171 are unchanged. No external model source, other service, tailnet ACL or
Codex plugin installation was changed.

## Current use and maintenance

Open local http://127.0.0.1:4179/ or private
https://mac-mini.duckbill-ionian.ts.net:8454/. The Mac must be awake and the user
logged in. Actual login plist is
`~/Library/LaunchAgents/com.scottchu.cad-workbench.simulator.plist`, label
`com.scottchu.cad-workbench.simulator`, owner checkout is this worktree, instance
`ca3daa81c9c60ef20aa7f16b`. Treat the checkout as an active runtime dependency;
uninstall from its original root before moving/removing it. Do not silently
switch ownership to another checkout or plugin cache.

`uv run python scripts/simulator_service.py open` ensures readiness and opens the
local launcher; status/stop/ensure are also available. Install persists at future
logins; stop leaves that login registration, uninstall removes it. Tailscale is
optional and independent of local lifecycle. To remove only this private endpoint:
`tailscale serve --https=8454 off`. Never reset all Serve settings.

Stop this owned service before rebuilding app outputs; then ensure it again.
Do not claim reboots, phone acceptance, public availability or arbitrary source
build attestation from current local evidence. Existing CAD export acceptance
remains in the prior workflow-ownership iteration.
