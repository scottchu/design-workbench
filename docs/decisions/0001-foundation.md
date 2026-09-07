# 0001: A reproducible CAD foundation

Status: accepted for the foundation iteration, 2026-09-06.

## Decision

CAD Workbench owns reusable software. Design source, design requirements, release artifacts and physical observations remain in their project repositories. Start by proving an actual CAD build and written STEP inspection before creating an editor UI.

Use Python 3.12 in one root `uv` workspace and root lockfile, with `cadgen[snapshot]==0.5.0`. Reserve the root npm workspace for future TypeScript application packages; do not create empty application or package scaffolds. Keep the installed upstream runtime behind small task-specific entry points. Installing its Python distribution does not install or register Codex skills, plugins or MCP tools.

User steering on 2026-09-06 adds asdf as the preferred development toolchain manager. The setup inventory selects already available asdf tools: Node.js 26.7.0, Bun 1.4.0 and uv 0.12.5, pinned in `.tool-versions`. No asdf Python is installed; retain the already selected uv-managed CPython 3.12.13, pinned in `.python-version`, as a scoped exception that avoids a second Python setup. uv owns the sole root `.venv` and Python dependency lock. Bun is available as a tool but npm remains the sole JavaScript workspace package manager; do not create a Bun lockfile or package workflow. No global toolchain configuration changes are required.

## Frozen F0-I implementation contract

1. Commit `.tool-versions` for `nodejs 26.7.0`, `bun 1.4.0` and `uv 0.12.5`, plus `.python-version` for `3.12.13`. Document `asdf install`; the setup host already has those plugins/tools. Root workspace configuration and locks support `uv sync --all-packages --all-groups` and `npm install` from the repository root. uv manages CPython and the sole root `.venv`. No nested locks or independently installed frontend workspaces.
2. `uv run python scripts/doctor.py` reports the Python version, executable/environment location and installed cadgen version; returns nonzero for a wrong Python minor version, missing/wrong cadgen version or interpreter outside the root environment. It is diagnostic and does not install packages, launch a viewer or contact a printer. Optional snapshot dependencies may be reported separately.
3. `uv run python scripts/cad_smoke.py` generates a generic parametric plate through the installed cadgen runtime, then opens the written STEP with the installed CAD kernel. The fixture belongs in `fixtures/smoke/plate.py`: a 20 x 12 x 6 mm plate with a centered, 4 mm diameter through-hole. Its named dimensions remain source parameters. Expected material volume is `20 * 12 * 6 - pi * 2**2 * 6` cubic millimeters.
4. The smoke command fails on failed generation, missing export, invalid geometry, wrong solid count, unexpected bounding dimensions or unexpected volume. Expect one valid solid, dimensions within 0.01 mm and volume within 0.1 cubic millimeters. The written STEP, not only in-memory source geometry, is checked.
5. Smoke output records the fixture hash, installed cadgen version, actual generation command, STEP path/hash, measured dimensions, solid count and volume. Include a machine-readable receipt. Place generated files in ignored `.workbench/` by default; source and focused tests are committed. The receipt must not imply slicer or physical acceptance.
6. `--snapshot` requests an optional image of the same generated STEP through installed snapshot tooling. Normal smoke execution does not require a browser. A requested snapshot failure is explicit and returns failure; it must not be silently counted as snapshot success. No persistent viewer service is required.
7. Add focused software checks for credible configuration/verification failures. Run local validation; do not add hosted CI. Do not introduce a UI, generalized job framework, universal geometry IR, slicer/printer integration or full viewer lifecycle wrapper.

The implementer chooses internal cadgen API/CLI calls from the installed version's supported interfaces. If a prescribed fixture, command or environment requirement is unsupported, report the specific blocker before changing this contract.

## Rationale and alternatives

The existing workflow needs evidence that displayed/exported geometry comes from the intended source. A small real build is more informative at this stage than another mock editor. Reusing cadgen preserves existing modeling, export and snapshot capabilities while revealing integration problems cheaply. A fork or replacement requires a reproducible blocker and a bounded maintenance plan; owning a new repository alone is not a reason to rewrite upstream.

OpenSCAD remains the first planned interactive integration for the existing Laifen model. Python/build123d is the preferred later mechanical backend. They will share artifact provenance, not a second hand-maintained geometry implementation. A monorepo may eventually contain owned CAD, preparation and printer-operation software, but the foundation neither migrates Orca nor assumes its documented future integrations exist.

## Evidence boundary

This record defines required behavior, not completed validation. The iteration validation and handoff records identify commands actually run, their outcomes and remaining limitations.
