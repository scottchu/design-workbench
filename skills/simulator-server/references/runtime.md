# Resolve the owned simulator runtime

Read this when using the simulator-server skill. The simulator is
bundled source, not a remotely hosted URL or an automatically installed process.
Pure observation/preparation routes that need no simulator skip this dependency.

Resolve the installed plugin/package root, then read its
[service contract](../../../apps/simulator/SERVICE.md) and
[registration instructions](../../../apps/simulator/README.md). Do not substitute
the external design repository as the service root. Project source and built
simulator assets stay external and are selected by explicit local registration.

Before preparing a runtime, inspect the optional user-local binding at
`~/.config/cad-workbench/runtime.json`. Version 1 contains `runtime_root`,
`instance` and `local_url`. Require an absolute canonical runtime root,
`local_url` equal to `http://127.0.0.1:4179`, and `instance` equal to the first
24 hex characters of SHA-256 over that root. Run the existing root lifecycle
controller there using its existing absolute `.venv/bin/python` and require its
status identity to match. A missing interpreter leaves diagnosis incomplete; do
not sync an environment for a status-only request. A mismatch is an
explicit configuration error; do not replace the binding or adopt another job.
This binding selects an existing runtime; it is not permission to install or
reconfigure a service. Keep it outside the distributed plugin.

When the binding is valid, use that runtime root and its existing root environment
for every lifecycle command below. Do not install dependencies in the plugin cache.
If the binding is absent, use an explicitly selected durable Workbench runtime
root (the package can supply its source). Only for in-scope setup/ensure/open,
prepare its pinned tools and sole
root runtimes when missing, using `uv sync --locked --all-packages --all-groups`, `npm ci` and
`npm run build:simulator`. These are setup steps, not evidence of CAD correctness.
No nested install, copied environment or untracked project assets belong in the
package. Configuration and lifecycle state live under that runtime root's ignored `.workbench/`. Record a user-local binding only after its real status/health
identity is verified. Never silently replace an existing binding.

Use the packaged lifecycle instead of creating another dev-server process:

From the resolved runtime working directory, execute its absolute
`.venv/bin/python` with arguments `scripts/simulator_service.py status`, `ensure`
or `open` as requested. The controller may create its local lifecycle lock even
for status; status does not start or reconfigure the service. Do not run the list
as a sequence for a diagnosis-only request.

When login persistence is requested, use the documented `install` command for
the owned per-user LaunchAgent; lazy `ensure` alone does not register future logins.
Use `uninstall` only for deliberate removal of that owned login registration.

`ensure` requires the actual build and verifies the owned local service; report a
missing build/tool or ownership/health conflict and repair that prerequisite
before retrying. Do not kill an unknown process, change an existing Tailscale
service, or run another server on a different port to hide a conflict. The explicit
`stop` command applies to this owned service only. Follow SERVICE.md for status,
current supported configuration, instance identity and lifecycle limits.

Page registration, selection and asset availability belong to the
[page skill](../../simulator-page/SKILL.md). Return the verified runtime identity
and registry path; a healthy host does not prove a page is available.

Tailscale is optional and private only. Use it only when the user explicitly
requests private remote access and supplies/selects the intended tailnet origin;
follow the service contract's origin allowlist. Never enable Funnel/public access
or reuse/alter another project's tunnel incidentally. Loopback needs no Tailscale.
No server setup confers printer or slicer control authority.
