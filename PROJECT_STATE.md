# Project state

Updated: 2026-09-07. Active iteration: [workflow ownership](docs/iterations/2026-09-07-workflow-ownership/BRIEF.md), migration, plugin and local simulator accepted locally; delivered through open PRs; no merge.
Working branch: `codex/workflow-ownership`, from `e336afc34bd2fa1709dd1760b5990d4bf3cf0fba`. Private GitHub repository: [scottchu/CAD-workbench](https://github.com/scottchu/CAD-workbench). The completed foundation remains on upstream default `setup/foundation`; no `main` branch is assumed.

## Current implementation

The foundation includes a root uv workspace, root npm workspace, pinned asdf tools, environment diagnostics, a real cadgen STEP fixture and focused software checks. The reusable catalog, two recipes and three skills are present. A generated plugin candidate and a local SvelteKit simulator host are implemented; no Workbench plugin is installed. Printer/slicer services remain external.

asdf manages Node.js 26.7.0, Bun 1.4.0 and uv 0.12.5. uv manages CPython 3.12.13 and the sole root `.venv`. npm is the JavaScript package manager; Bun is available but unused by the foundation.

Foundation validation and independent review passed. Existing-host setup, environment diagnostics, five focused software tests, actual STEP generation/readback, centered through-hole checks, snapshot generation/visual inspection and three explicit failure-receipt paths passed. No source repairs were required. Consult the [validation](docs/iterations/2026-09-06-foundation/VALIDATION.md), [review](docs/iterations/2026-09-06-foundation/REVIEW.md) and [handoff](docs/iterations/2026-09-06-foundation/HANDOFF.md) for the exact evidence and its limits. This was not a clean-machine installation test.

## Boundaries and next action

Actual designs remain in their existing repositories. No Orca or OpenSCAD editor source was migrated, and no printer or service operation is part of this iteration. The later user-authorized publication created the private GitHub remote and pushed the foundation branch. Generated smoke files under `.workbench/` are reproducible developer evidence, not print-ready deliverables.

The user has prioritized reusable workflow ownership and project separation before Laifen UI work. Workbench will own the catalog, recipes, contracts, reusable skills/policy/templates and legacy tool source; design and sticker repositories retain project source, assets and evidence with explicit external workflow bindings. The separate workflow-library draft is superseded as an ownership proposal and retained recoverably. Migration V1/V2 preservation checks and R1 review passed for provider `36f4171`, source `b8b0f5d` and sticker `33fcac4`. Source continuity retains one independently confirmed preexisting Laifen missing-VALIDATION failure (10 pass, 1 fail). Follow the active [handoff](docs/iterations/2026-09-07-workflow-ownership/HANDOFF.md) for exact identities, new plugin/simulator acceptance and delivery. Serving the existing Laifen customizer does not complete the separate roadmap milestone 1 measurement/build-identity contract.

Plugin/simulator V3 and R2 passed after isolating unavailable registrations: package tests 5 pass, simulator tests 8 pass, Svelte check zero errors/warnings and production build pass. Root browser generation, changed-height rebuild and two STL downloads/readback passed; see [browser acceptance](docs/iterations/2026-09-07-workflow-ownership/ROOT_BROWSER_ACCEPTANCE.md). Only Laifen is registered currently.

Delivery: [Workbench PR 1](https://github.com/scottchu/CAD-workbench/pull/1), [design PR 23](https://github.com/scottchu/design-projects/pull/23), [sticker PR 1](https://github.com/scottchu/sticker-projects/pull/1). Workbench implementation commit is `91f96fd`; subsequent continuity-only delivery records do not alter the reviewed package or app.
