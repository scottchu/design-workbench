# Project state

Updated: 2026-09-06. Active iteration: [foundation](docs/iterations/2026-09-06-foundation/BRIEF.md).
Working branch: `setup/foundation`. Repository began empty; no remote is configured.

## Current implementation

The foundation includes a root uv workspace, root npm workspace, pinned asdf tools, environment diagnostics, a real cadgen STEP fixture and focused software checks. There is no editor UI, slicer integration, printer integration or installed Workbench plugin yet.

asdf manages Node.js 26.7.0, Bun 1.4.0 and uv 0.12.5. uv manages CPython 3.12.13 and the sole root `.venv`. npm is the JavaScript package manager; Bun is available but unused by the foundation.

Foundation validation and independent review passed. Existing-host setup, environment diagnostics, five focused software tests, actual STEP generation/readback, centered through-hole checks, snapshot generation/visual inspection and three explicit failure-receipt paths passed. No source repairs were required. Consult the [validation](docs/iterations/2026-09-06-foundation/VALIDATION.md), [review](docs/iterations/2026-09-06-foundation/REVIEW.md) and [handoff](docs/iterations/2026-09-06-foundation/HANDOFF.md) for the exact evidence and its limits. This was not a clean-machine installation test.

## Boundaries and next action

Actual designs remain in their existing repositories. No Orca or OpenSCAD editor source was migrated, and no printer/service/remote operation is part of this iteration. Generated smoke files under `.workbench/` are reproducible developer evidence, not print-ready deliverables.

The next scoped implementation is roadmap milestone 1: open an existing Laifen model, change real parameters, regenerate it, and bind displayed/exported geometry to the same candidate. Inspect its current source and physical observations before choosing the exact integration baseline. See [NEXT_AGENT.md](NEXT_AGENT.md).
