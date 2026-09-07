# Workbench workflow plugin package

Build from the Workbench repository root:

```sh
uv run python scripts/package_plugin.py
```

The ignored output is `.workbench/plugin/cad-workbench/`. Existing output is refused so a reviewed package is not silently replaced; select a new ignored output path for a later candidate. No marketplace registration or plugin installation is performed. The source manifest template lives at `packaging/cad-workbench/.codex-plugin/plugin.json`; `skills/`, `catalog/`, `contracts/`, `workflows/` and `templates/` remain their single maintained authorities. The builder copies them and verifies actual output hashes, contained references and absence of symlinks. `PACKAGE_RECEIPT.json` binds source revision and each source/output identity. `PACKAGE_INPUTS.sha256` identifies source inputs, including the scope addendum as evidence only.

The package supplies three skills and their local references. It contains no own MCP server, generic operations proxy, provider credentials, project assets, legacy viewer configuration or installed environment. CAD/text-to-CAD and U1/Orca providers are separately installed and verified by the flow skill. Preparation/start skills are guidance over external providers, not claims that packaged U1 MCP/CLI offers those operations.

For completeness, generic foundation doctor/smoke scripts, their fixture/tool pins, Python manifests/lock and historical foundation validation document are included because the catalog references them. They are optional developer sources, not auto-run plugin hooks. Their commands require an explicitly prepared package-root uv environment and declared tools; installation of this plugin does not install runtimes or establish current CAD validation. The historical evidence document retains its original paths/hashes as provenance; historical ignored artifacts are not bundled. The simulator app, printer dashboard and widgets are not part of this artifact. Run the dedicated simulator from its Workbench repository documentation; Orca owns printer/slicer API, dashboard and widgets.

Package validation proves discovery structure and source/output parity, not real provider execution, geometric correctness, print readiness or physical/platform acceptance. This source package is reviewable before any separately requested installation.
