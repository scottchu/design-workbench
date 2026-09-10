# Design Workbench

Help people and agents produce, inspect and revise designs from project-owned
specifications while preserving intent, consistency, evidence and approval.

The product is an installable design workflow plugin, with focused skills, documented
workflows and executable tools for CAD, images and future design outcomes. Its
Playground hosts project-built interactive review pages. Projects retain their
actual designs, references, requirements, page logic, artifacts and approvals.

Start with the [product definition](docs/product.md) for **why → how → what**, or
read the [architecture](docs/architecture.md#intent-source-implementation-delivery-and-runtime)
for the boundary between intent source, implementation, deliverables and runtime.
The [current state](PROJECT_STATE.md) records what is delivered and verified;
[the roadmap](docs/roadmap.md) records pending work.

## Find the owning material

| Question | Where to read |
| --- | --- |
| What should the product do, and why? | [Product](docs/product.md), [architecture](docs/architecture.md), and their linked decisions. |
| What tasks and procedures can an agent use? | [Capability catalog](catalog/CAPABILITIES.md), `skills/` and `workflows/`. The catalog indexes capabilities; it does not execute them. |
| What information must components exchange? | [Contracts](contracts/project-binding.md); `templates/` supplies blank project records, not actual project status. |
| Where is the software implemented and checked? | `apps/playground/`, executable `scripts/`, software `tests/` and generic `fixtures/`. `tools/` currently preserves [legacy Viewer maintenance source](tools/LEGACY_VIEWER.md). |
| What gets shipped? | [Packaging](packaging/README.md): explicit package inputs, outputs and receipts. |
| What is running or accepted now? | [PROJECT_STATE](PROJECT_STATE.md) and its evidence links. [NEXT_AGENT](NEXT_AGENT.md) is a startup pointer. |
| How should an agent work on this repository? | [AGENTS](AGENTS.md) and [documentation ownership](docs/documentation.md). |

The current source package contains five skills and Playground source. It does
not automatically prepare or start a runtime, and no owned Workbench MCP is
implemented yet. CAD and printer providers are separately maintained. General
CAD editing and end-to-end fabrication acceptance remain pending. Local root
folder names and compatibility identifiers such as `cad-workbench` are retained.

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

The root uv workspace pins `cadgen[snapshot]==0.5.0` and uses the root `.venv`. Keeping the already selected uv-managed Python avoids a second Python installation; asdf owns Node.js, Bun and uv. The root npm workspace includes `apps/playground`. After building and registering an external simulator, run `uv run python scripts/simulator_service.py open` to start or reuse the local production server and open http://127.0.0.1:4179/. The [service guide](apps/playground/SERVICE.md) covers login persistence and optional private Tailscale access. `npm run dev:playground` remains the development command. Local use needs no Tailscale. Node.js is also relevant to upstream mesh/DXF builders. Bun is available but is not a second package manager: the foundation uses npm and has no Bun lockfile. Setup does not change global toolchain configuration.

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
