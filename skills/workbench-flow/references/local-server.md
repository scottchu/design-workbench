# Required local runtime for simulation

Read this for a simulator or interactive design-review request. The simulator is
bundled source, not a remotely hosted URL or an automatically installed process.
Pure observation/preparation routes that need no simulator skip this dependency.

Resolve the installed plugin/package root, then read its
[service contract](../../../apps/simulator/SERVICE.md) and
[registration instructions](../../../apps/simulator/README.md). Do not substitute
the external design repository as the service root. Project source and built
simulator assets stay external and are selected by explicit local registration.

From the resolved package root, prepare the pinned tools and sole root runtimes
when missing, using `uv sync --locked --all-packages --all-groups`, `npm ci` and
`npm run build:simulator`. These are setup steps, not evidence of CAD correctness.
No nested install, copied environment or untracked project assets belong in the
package. Configuration and lifecycle state live under ignored `.workbench/`.

Use the packaged lifecycle instead of creating another dev-server process:

```sh
uv run python scripts/simulator_service.py status
uv run python scripts/simulator_service.py ensure
uv run python scripts/simulator_service.py open
```

When login persistence is requested, use the documented `install` command for
the owned per-user LaunchAgent; lazy `ensure` alone does not register future logins.
Use `uninstall` only for deliberate removal of that owned login registration.

`ensure` requires the actual build and verifies the owned local service; report a
missing build/tool or ownership/health conflict and repair that prerequisite
before retrying. Do not kill an unknown process, change an existing Tailscale
service, or run another server on a different port to hide a conflict. The explicit
`stop` command applies to this owned service only. Follow SERVICE.md for status,
current supported configuration, instance identity and lifecycle limits.

Open the requested registered simulator only after health succeeds. Record exact
project/source/artifact identity; stale or missing registrations remain unavailable
without blocking healthy siblings. The host serves actual external outputs and
must not become a second implementation of project geometry or parameter math.

Tailscale is optional and private only. Use it only when the user explicitly
requests private remote access and supplies/selects the intended tailnet origin;
follow the service contract's origin allowlist. Never enable Funnel/public access
or reuse/alter another project's tunnel incidentally. Loopback needs no Tailscale.
No server setup confers printer or slicer control authority.
