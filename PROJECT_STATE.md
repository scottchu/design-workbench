# Project state

Updated: 2026-09-07. Active iteration: [workflow ownership](docs/iterations/2026-09-07-workflow-ownership/BRIEF.md), implementation in progress.
Working branch: `codex/workflow-ownership`, from `e336afc34bd2fa1709dd1760b5990d4bf3cf0fba`. Private GitHub repository: [scottchu/CAD-workbench](https://github.com/scottchu/CAD-workbench). The completed foundation remains on upstream default `setup/foundation`; no `main` branch is assumed.

## Current implementation

The foundation includes a root uv workspace, root npm workspace, pinned asdf tools, environment diagnostics, a real cadgen STEP fixture and focused software checks. There is no editor UI, slicer integration, printer integration or installed Workbench plugin yet.

asdf manages Node.js 26.7.0, Bun 1.4.0 and uv 0.12.5. uv manages CPython 3.12.13 and the sole root `.venv`. npm is the JavaScript package manager; Bun is available but unused by the foundation.

Foundation validation and independent review passed. Existing-host setup, environment diagnostics, five focused software tests, actual STEP generation/readback, centered through-hole checks, snapshot generation/visual inspection and three explicit failure-receipt paths passed. No source repairs were required. Consult the [validation](docs/iterations/2026-09-06-foundation/VALIDATION.md), [review](docs/iterations/2026-09-06-foundation/REVIEW.md) and [handoff](docs/iterations/2026-09-06-foundation/HANDOFF.md) for the exact evidence and its limits. This was not a clean-machine installation test.

## Boundaries and next action

Actual designs remain in their existing repositories. No Orca or OpenSCAD editor source was migrated, and no printer or service operation is part of this iteration. The later user-authorized publication created the private GitHub remote and pushed the foundation branch. Generated smoke files under `.workbench/` are reproducible developer evidence, not print-ready deliverables.

The user has prioritized reusable workflow ownership and project separation before Laifen UI work. Workbench will own the catalog, recipes, contracts, reusable skills/policy/templates and legacy tool source; design and sticker repositories retain project source, assets and evidence with explicit external workflow bindings. The separate workflow-library draft is superseded as an ownership proposal and retained recoverably. Implementation is not yet accepted. Follow the active [handoff](docs/iterations/2026-09-07-workflow-ownership/HANDOFF.md) for the replacement source checkout, preservation gates and pending delivery. Laifen milestone 1 remains planned after this bounded work.
