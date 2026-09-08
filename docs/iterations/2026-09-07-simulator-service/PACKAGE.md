# Simulator runtime package receipt

Implementation owner: `/root/sticker_migration`. This is source packaging and
readback evidence, not plugin installation or service execution acceptance.

Final package: `.workbench/plugin/service-final/cad-workbench/`.
Earlier `.workbench/plugin/cad-workbench/`, `service/cad-workbench/` and
`service-r2/cad-workbench/` artifacts remain intact; no output was overwritten.
The first service candidate predates the independently reviewed lifecycle repairs.

- PACKAGE_RECEIPT.json SHA-256: `7e9e5376b4d82bb0799357b4f720f6aab756658921aa2821237cc10dc76488ee`.
- PACKAGE_INPUTS.sha256 SHA-256: `64c7abd6fb2775d6a409547fd1c3e9c85faec94b25b2fd10515d28448dcd1144`.
- Captured source Git revision: `34fcf348a0a754799547090b2ac2504ff60268f2`; the input manifest
  additionally freezes declared uncommitted inputs.
- POLICY.sha256 SHA-256: `39a4503135fafd0cccfc71faef19ed6baafde0c1194ba1c5241ee1ac225071c1`.
- Files transferred: 67, including 22 simulator/runtime support files.
- Repaired service script SHA-256: `64c3c56d2cf793a56f18db18a826095c763c7a3630d49b3991ad5d1a61dd2332`.
- SERVICE.md SHA-256: `fdb47e9100a94d92a79f0399ec18fa80e89327bc009cdf01ad055d2eed01e5a6`.

Every transferred file has an exact source path and source/output SHA-256 in
PACKAGE_RECEIPT.json. Its simulator component lists the app source (including
health/origin handling), root npm manifests/lock, registration utility and service
helper/docs. Only intentional app source/config files are selected. Generated
builds, `.svelte-kit`, `node_modules`, private registries/service state, external
project assets and installed environments are excluded. No MCP or marketplace
registration is introduced.

Source evidence includes both the older PLUGIN_ADDENDUM.md and current service
BRIEF.md. The newer scope authorizes the required simulator runtime; existing
project bindings to policy revision `36f41715ee2257c0f2e41e40329216e3d2b2747f`
are unchanged. No bound project was silently upgraded.

The flow skill requires this local server only when a simulation/interactive
review is needed. Observation-only/preparation-only routes skip it. Packaged
instructions use root uv/npm setup, explicit build, then managed ensure/open;
login persistence uses explicit install. Tailscale remains optional, explicitly
configured and private-only; Funnel/public exposure is excluded.

## Exact validation

Run from Workbench root:

```sh
uv run python -m unittest discover -s tests -p test_package_plugin.py -v
uv run python scripts/package_plugin.py --output .workbench/plugin/service-final/cad-workbench
uv run python scripts/package_plugin.py --check .workbench/plugin/service-final/cad-workbench
uv run python /Users/scottchu/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .workbench/plugin/service-final/cad-workbench
uv run python /Users/scottchu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/workbench-flow
uv run python scripts/check_registry.py
```

Package tests: 8/8 PASS (relocation, byte tampering, missing support/service,
symlink refusal, exact simulator source transfer, exclusion of injected private
state/caches, and preservation of prior output). Final artifact creation/readback,
plugin validator, skill validator and catalog validation PASS. Source and package
service hashes match the repaired I4 candidate supplied by its owner.

No npm build/install, lifecycle command, Tailscale mutation, plugin installation,
commit or push was performed by this packaging worker. Actual production runtime,
private access, restart and browser outcomes are separate root acceptance records.
Independent final package review is recorded by R2; this receipt does not approve
its own candidate.
