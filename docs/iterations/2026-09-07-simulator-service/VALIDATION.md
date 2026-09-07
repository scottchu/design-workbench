# Managed simulator validation

Root live acceptance, 2026-09-07. Independent source review and receipt readback
are in REVIEW.md; package identities are in PACKAGE.md.

## Actual setup and lifecycle

After checking PID/cwd, root stopped only the previous task-owned Vite PID7868.
Root commands:

```sh
npm run check:simulator
npm run test:simulator
npm run build:simulator
WORKBENCH_ALLOWED_ORIGIN=https://mac-mini.duckbill-ionian.ts.net:8454 uv run python scripts/simulator_service.py install
uv run python scripts/simulator_service.py status
uv run python .workbench/service-evidence/check_lifecycle.py
uv run python -m unittest discover -s tests -v
```

Svelte check: zero errors/warnings. Eleven app tests passed, including exact local
and remote Host/Origin restrictions. Actual adapter-node build passed. The final
root suite passed all 29 tests (12 lifecycle, 8 packaging, 4 registry, 5 foundation).
The first joined suite found that the registry's isolated fixture omitted the two
new app-document references; adding those exact documents repaired the fixture.
No production link check was disabled. The full suite then passed.

The installed user LaunchAgent is
`~/Library/LaunchAgents/com.scottchu.cad-workbench.simulator.plist`.
Label: `com.scottchu.cad-workbench.simulator`; instance:
`ca3daa81c9c60ef20aa7f16b`; owner root is this Workbench checkout. Absolute Node:
`/Users/scottchu/.asdf/installs/nodejs/26.7.0/bin/node`; actual entrypoint:
`apps/simulator/build/index.js`. It listens only on 127.0.0.1:4179. RunAtLoad and
KeepAlive were read back from the actual plist. The external registry is recorded
as this checkout's absolute `.workbench/simulators.json`.

The live lifecycle script invokes the real helper through the root Python
interpreter, parses each JSON response, and checks the real listener with lsof.
Two bare ensure calls reused PID15871. Owned stop removed the job and listener;
status reported loaded=false, healthy=false, installed_for_login=true. Bare ensure
then started PID17805, reporting managed/healthy=true. A further ensure reused that
PID. The configured private origin survived without repeating its environment
variable. Receipt: `.workbench/service-evidence/lifecycle.json`.

R2 found and repaired two issues before this stop/restart sequence: compare the
actual loaded job's arguments, working directory and explicit environment against
its owned plist; reject noncanonical private origins before any mutation. Final
parser was also checked against actual launchctl print/status. No foreign process
or service was stopped. Helpers were tested for foreign ownership, an occupied
port, configuration drift, missing build, bootstrap failure and health timeout.

## Private Tailscale add-on

Used installed Tailscale1.102.2 and its actual serve help. Official behavior:
https://tailscale.com/docs/reference/tailscale-cli/serve.

```sh
tailscale serve status --json
tailscale serve --bg --https=8454 http://127.0.0.1:4179
tailscale serve status --json
curl --fail --silent --show-error https://mac-mini.duckbill-ionian.ts.net:8454/health
```

The command reported Available within your tailnet. The exact pre-apply config
matched the initial snapshot. Afterward, the ONLY semantic additions were
TCP8454 HTTPS and Web `mac-mini.duckbill-ionian.ts.net:8454` mapping `/` to
`http://127.0.0.1:4179`. Removing those two keys reproduces the complete original
configuration. AllowFunnel is unchanged and has no permission for8454. Existing
public443 behavior belongs to another service and was not modified. No tailnet
ACL change, public Funnel setup or printer/slicer endpoint operation occurred.

| Ignored configuration evidence | SHA-256 |
| --- | --- |
| tailscale-before.json | 0d8e7d5a0f73c8f52d890d3fac651f123521c47836f8e67a4c3d13986022b3ca |
| tailscale-after.json | 3da0d3ef2e35a162238f0aa3f3025364ad1249923d9752bf48359a3a224cd5a6 |

Both files are under `.workbench/service-evidence/`. Exact endpoint-only removal:
`tailscale serve --https=8454 off`; do not reset all Serve configuration.

Private HTTPS health/list/selected simulator and actual9,603,115-byte WASM asset
returned200. WASM SHA-256 remained
`f72ce246c02c0e501990837102be383326b153fd761774ebfacce5c80c5ecf26`, with
application/wasm, COOP same-origin and COEP require-corp. Invalid Host, the same
Tailscale hostname on unconfigured443, and an unrelated Origin all returned403.
HTTP receipt: `.workbench/service-evidence/http.json`. HTTPS health succeeded
again after actual stop/restart.

## Browser and limits

Root used actual Chrome CUA to open the private HTTPS launcher, select Laifen and
wait for its real OpenSCAD WASM build. Preview up to date, inside height213mm,
outside39x219mm and an enabled blob download on the private origin were observed.
The compiled cutaway was visually inspected and the tab retained for the user.
The prior local-browser two-STL dimension/readback acceptance is unchanged; this
iteration introduces no model or export logic.

This is a macOS per-user login service, not a pre-login system daemon. Login
persistence is configured and its plist verified; no logout/reboot was performed.
Private access was verified through the real endpoint on this Mac, not a separate
phone or off-tailnet device. Existing tailnet access policy controls which peers
can connect; no separate application login was added. A stopped service is started
by ensure/open or next login, not by a Tailscale request itself. The Mac must be
awake for remote access. Plugin source is packaged, but no Codex plugin install or
marketplace registration occurred. No new CAD, slicer or physical acceptance is
claimed.
