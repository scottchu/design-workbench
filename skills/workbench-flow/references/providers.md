# Select the actual provider

Verify the provider that is installed and callable for this run. A Git source tree, README, catalog entry or skill folder alone does not establish a running interface. Record the installed identity/version plus the independently selected project runtime/source/command. Do not silently replace installed skill semantics with a different maintained source revision.

| Domain | Known provider boundary | Resolve before using |
| --- | --- | --- |
| CAD modeling/export/review | text-to-CAD `cad` plugin 0.5.0 supplies skills; it does not supply a CAD MCP server. cadgen runtime installation is separate; Workbench foundation pins cadgen 0.5.0. | Available CAD skill and real project generator/export commands, runtime version, source/parameters and artifact readback. Upstream viewer skills where available; no legacy host service is bundled. |
| U1 observation/camera | Currently inspected public U1 MCP exposes read-only `observe_printer` and `open_printer_camera`. | Fresh callable tool definitions and the external observation skill. Read-only scope does not permit motion, temperatures or job mutation. |
| U1 preparation | `u1-prepare-print` is workflow guidance over a real slicer CLI and profiles. Packaged U1 CLI has setup/doctor/mcp, not a slicing command. | Actual slicer executable/version, profiles, artifact hash and tool mapping. There is no established packaged preparation MCP endpoint. |
| U1 authorized start | `u1-start-print` is workflow guidance requiring an actual external operations provider. It is not proof that packaged U1 MCP/CLI implements start. | Actual supported operations interface plus exact-artifact authorization and fresh preflight. If absent, report unavailable; do not call invented endpoints or use a general request/G-code relay. |
| U1 monitoring | External `u1-monitor-print` workflow, independently runnable with read-only providers. | Installed skill/version and actual telemetry/camera availability. Do not infer printer control from monitoring. |
| Sticker production | Project-owned audit implementation; Workbench owns the reusable skill. | Bound compatible contract/candidate/review commands and project version. Jaelin's command contract is one versioned provider example. |
| Simulator | Bundled Workbench SvelteKit host source; installed runtime is selected separately. | Use simulator-server for bound runtime lifecycle and simulator-page for a registered build. Packaging does not build/start the host; page availability does not prove CAD geometry. |

These facts are a scoped provider assessment for this delivery, not an eternal tool inventory. The installed U1 skill package differs from the maintained Orca source; record which one is being used. Do not copy external CAD/U1 skills, runtime, credentials or network configuration into this package. No installation, provider refresh, printer call or authentication change is implicit in resolving a workflow.
