# Local simulator service

This is a macOS user launchd service for the already-built adapter-node simulator,
listening on `127.0.0.1:4179`. It runs neither Vite nor a printer/slicer proxy.
Run the CLI from the selected Workbench root using its root uv environment:

```sh
uv run python scripts/simulator_service.py ensure
uv run python scripts/simulator_service.py open
uv run python scripts/simulator_service.py status
uv run python scripts/simulator_service.py stop
```

`start` is an alias for `ensure`. `ensure` bootstraps only when absent and reuses
only the exact owned launchd configuration with matching health identity. `open`
first ensures that service is healthy, then opens its local URL. Dependencies and
`apps/simulator/build/index.js` must already exist; run the repository's documented
npm setup/build separately. The CLI never installs dependencies or auto-builds.
Node is resolved to an absolute executable using `asdf which node` in this root.

For launch at subsequent user logins, explicitly install the user LaunchAgent:

```sh
uv run python scripts/simulator_service.py install
uv run python scripts/simulator_service.py uninstall
```

`install` writes an owned plist to
`~/Library/LaunchAgents/com.scottchu.cad-workbench.simulator.plist`, with RunAtLoad
and KeepAlive, and starts it in the current GUI login domain. If an owned lazy job
is already running, installation transitions that exact job to the login plist.
This may briefly interrupt this simulator only. Foreign existing plist/job ownership
is refused before mutation. `stop` removes the current launchd job; an installed
plist remains and starts again at the next login. `uninstall` stops the owned job
and removes only its owned login plist. This is a per-user agent, not a system
daemon; it requires a logged-in macOS GUI user. Lazy `ensure` alone survives terminal
closure but does not register the next-login LaunchAgent.

## Identity, configuration and conflict behavior

The label is stable across checkouts: `com.scottchu.cad-workbench.simulator`.
A different checkout cannot silently replace or stop it. The CLI verifies the
loaded plist path and actual launchctl program, arguments, working directory and
explicit environment against the owned saved configuration. Inherited/default
environment blocks are not substituted for actual job configuration; same Node
executable plus an owned on-disk plist is insufficient. Health at
`http://127.0.0.1:4179/health` must return JSON with `service` equal to
`cad-workbench-simulator` and `instance` equal to the first 24 hex characters of
SHA-256 over the canonical absolute Workbench root. That value is supplied as
`WORKBENCH_INSTANCE_ID`. Readiness has a bounded ten-second wait. A missing or
mismatched health result never becomes a successful open. An occupied port without
an owned launchd job is refused, even if it reports a matching instance. No arbitrary
process is killed or adopted.

Ignored `.workbench/service/` contains the lazy plist, stdout/stderr logs and
lifecycle lock. Do not move a running checkout: stop/uninstall from its original
root first, then explicitly install the selected replacement. These files contain
local paths and are not committed or distributed. Existing registered simulators
and their assets remain in external project roots.

`WORKBENCH_SIMULATORS` must be an existing absolute registry file. It defaults to
this root's `.workbench/simulators.json` on first setup. The plist always records
its exact absolute value. Later `ensure`/`open` calls reuse the stored owned registry
and private origin when those environment variables are absent, so callers need
not repeat machine configuration. Explicitly changed configuration is rejected
while running; `install` is the deliberate update/restart path. An explicitly empty
`WORKBENCH_ALLOWED_ORIGIN` removes that private origin when reinstalling.

An optional private Tailscale origin can be configured during explicit install:

```sh
WORKBENCH_ALLOWED_ORIGIN=https://mac-mini.duckbill-ionian.ts.net:8454 \
  uv run python scripts/simulator_service.py install
```

Only an exact HTTPS `*.ts.net` origin with optional valid port and no credentials,
path, query or fragment is accepted. The string must already be canonical: lower
case scheme/hostname, with default HTTPS port 443 omitted. Noncanonical input is
rejected before any service is stopped or configuration changed. The plist passes `WORKBENCH_ALLOWED_ORIGIN`
and adapter-node `ORIGIN`; the listener stays loopback. The CLI does not configure
Tailscale, publish a public endpoint, trust forwarded headers or open firewall
ports. Private Tailscale Serve setup and application Host/origin checks are separate
explicit actions. The chosen private origin is not itself evidence of reachability.

## Lifecycle implementation evidence

`uv run python -m unittest discover -s tests -p test_simulator_service.py -v`
exercises exact reuse, foreign job/port refusal, install-to-login transition,
stop versus uninstall, preserved foreign plist, missing build, configuration drift,
private-origin reuse, noncanonical-origin rejection, owned-disk/foreign-loaded-job
conflicts, timeout and launchctl failure through bounded fake launchctl
and health providers. These tests do not start or modify a live launchd service.
Real launchd health, browser access, login persistence and private-tailnet access
require separate root acceptance evidence. No lifecycle command was executed by
the implementation worker.

## Installed plugin and existing runtime

A plugin cache update must not relocate an already running server. A user-local
`~/.config/cad-workbench/runtime.json` can bind the installed skill to the existing
runtime, using `version: 1`, `runtime_root` (canonical absolute root), `instance`
(the root-derived identity described above), and `local_url` (the fixed URL).
The skill validates that binding and runs this unchanged controller from the
bound root with its existing uv environment. The controller does not automatically
read this file or weaken its checkout ownership checks. Missing/mismatched
bindings require explicit setup; they never justify adopting another process.

This file is machine-local setup, not part of a plugin package. An existing binding
is preserved unless relocation is explicitly requested. A fresh plugin install
can therefore reuse a healthy service without installing another runtime in its
cache or changing launchd/Tailscale configuration.
