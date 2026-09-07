# CAD Workbench

CAD Workbench provides a workflow plugin and one local SvelteKit server for project simulators. Actual designs and simulation logic remain in their project repositories; the separate printer/slicer project owns its MCP, API, dashboard and widgets.

Workbench also owns the shared [capability catalog](catalog/CAPABILITIES.md), [sticker production](workflows/sticker-production.md) and [CAD fabrication](workflows/cad-fabrication.md) recipes, [project binding contract](contracts/project-binding.md), reusable skills and project-record templates. Project repositories select a specific workflow revision and retain their source, assets, commands and evidence. The catalog distinguishes documented methods from runtime capabilities and does not imply that a recipe has been executed successfully.

Check this catalog locally with `uv run python scripts/check_registry.py`. Its current extraction and acceptance status is recorded in [workflow ownership](docs/iterations/2026-09-07-workflow-ownership/HANDOFF.md). Preserved [legacy Viewer controller source](tools/cad-viewer-service/README.md) retains its original host dependencies; this extraction does not install or operate that service.

The foundation supplies a reproducible environment, diagnostics and a real CAD generation/export check. The [workflow plugin](packaging/README.md) now packages three skills and their shared contracts. The [local simulator host](apps/simulator/README.md) serves explicitly registered external builds; Laifen OpenSCAD WASM is the first integration. A general CAD editor and end-to-end fabrication acceptance remain future work.

## Local setup

Prerequisites: Git and asdf with its `nodejs`, `bun` and `uv` plugins. The setup host already has these plugins and tools. `.tool-versions` pins Node.js 26.7.0, Bun 1.4.0 and uv 0.12.5. uv manages CPython 3.12.13 from `.python-version`, the repository environment and Python dependencies. The commands below are the foundation interface; use the [current project state](PROJECT_STATE.md) and [iteration handoff](docs/iterations/2026-09-06-foundation/HANDOFF.md) for their verified status. Run all commands from the repository root:

```sh
asdf install
uv sync --all-packages --all-groups
npm install
uv run python scripts/doctor.py
uv run python scripts/cad_smoke.py
uv run python -m unittest discover -s tests -v
```

The root uv workspace pins `cadgen[snapshot]==0.5.0` and uses the root `.venv`. Keeping the already selected uv-managed Python avoids a second Python installation; asdf owns Node.js, Bun and uv. The root npm workspace includes `apps/simulator`. After building and registering an external simulator, run `uv run python scripts/simulator_service.py open` to start or reuse the local production server and open http://127.0.0.1:4179/. The [service guide](apps/simulator/SERVICE.md) covers login persistence and optional private Tailscale access. `npm run dev:simulator` remains the development command. Local use needs no Tailscale. Node.js is also relevant to upstream mesh/DXF builders. Bun is available but is not a second package manager: the foundation uses npm and has no Bun lockfile. Setup does not change global toolchain configuration.

The smoke command builds a generic 20 x 12 x 6 mm plate with a centered 4 mm through-hole using cadgen. It reopens the written STEP and checks solid validity, solid count, bounding dimensions and material volume. It writes ignored `.workbench/smoke/plate.step` and `.workbench/smoke/receipt.json`, with `.workbench/smoke/plate.png` when a snapshot is requested. Its cache is isolated under `.workbench/cache`.

For an optional image of that same STEP, install the Chromium browser once, then request a snapshot:

```sh
uv run python -m playwright install chromium
uv run python scripts/cad_smoke.py --snapshot
```

The Chromium installation is an optional one-time browser download for snapshots. Snapshots also depend on upstream snapshot tooling and its runtime prerequisites. A requested snapshot failure is reported as failure. The normal geometry check does not require launching a persistent viewer.

Installing the Python distribution supplies runtime code and command-line capabilities. It does **not** install or register a Codex plugin, skill or MCP server. Build the reviewable skills package with `uv run python scripts/package_plugin.py`; this refuses an existing output. Packaging does not install or register it. CAD and U1 providers remain separately maintained dependencies. Do not copy installed skill text into the runtime dependency model.

## Scope and evidence

The smoke fixture is a software integration example, not a print-ready product. A successful CAD/export check does not establish slicer behavior, manufacturing suitability or physical fit. Snapshot success establishes image creation; interpreting that image is a separate review action.

Existing project source remains authoritative. Future parameter controls must rebuild that source, and the viewer/export must identify the resulting build. Explanatory overlays and prechecks must not become an independently maintained copy of the geometry.

- [Architecture and ownership](docs/architecture.md)
- [Foundation decision and command contract](docs/decisions/0001-foundation.md)
- [Roadmap with completion gates](docs/roadmap.md)
- [Foundation iteration brief](docs/iterations/2026-09-06-foundation/BRIEF.md)
- [Current state](PROJECT_STATE.md) and [next-agent handoff](NEXT_AGENT.md)

The iteration validation and handoff records distinguish completed checks from planned behavior. Local tests are required for delivery; this repository does not use hosted CI.
