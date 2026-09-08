# Parametric CAD to fabrication evidence

**Workflow:** `WF-CAD-FABRICATION`
**Capabilities:** `CAP-INTENT-GATE`, `CAP-PARAMETRIC-CAD`, `CAP-SIMULATION`,
`CAP-EXPORT`, `CAP-VISUAL-REVIEW`, `CAP-SLICING`, `CAP-PHYSICAL-FEEDBACK`,
`CAP-DESIGN-REFLECTION`, `CAP-HANDOFF`, `CAP-MIGRATION`, `CAP-ENV-DELIVERY`

Use this recipe for a project-owned parametric part or assembly. Workbench owns [CAD policy](policies/CAD_WORKFLOW.md), [continuity policy](policies/PROJECT_CONTINUITY.md) and reusable guidance. Runtime, source, tests and artifacts remain with their selected providers. This mapped recipe has not been run end to end.

## Inputs and contract

Resolve the [external project binding](../contracts/project-binding.md), verify the exact project revision and read its AGENTS.md, project continuity and active iteration. Bind the source's real generator, geometry checks and export/readback commands; do not substitute Workbench smoke for a project build. OpenSCAD need not supply STEP: preserve native backend capability and declare the actual supported export with its evidence limit.

Freeze project, source entrypoint, accepted baseline, version, relevant artifacts,
requirements, use sequence, invariants, derived constraints, design choices,
physical unknowns, non-goals, and output targets in a path-and-content manifest.

When intent or a relationship is materially new, first show the smallest
interactive diagram or simulation that isolates one or two relationships. Tell
the user what is fixed, what is adjustable, what to observe, and ask one explicit
pass/fail question. Record the exact answer. This approves intent only.

## Interactive playground route

For interactive intent review, use [simulator-server](../skills/simulator-server/SKILL.md)
to resolve/reuse the host and [simulator-page](../skills/simulator-page/SKILL.md)
to select and verify the project build. A missing/stale page leaves interactive
review pending; it does not invalidate independently available CAD evidence.
Record the reviewed source/build and exact user disposition in the project.
Page availability and user intent approval do not satisfy the geometry/export
checks below. No simulation is required for an unrelated preparation-only task.

## Build and evidence sequence

1. Design owns numeric parameters, datums, part roles, motion/service states,
   risks, and focused test targets.
2. Implementation edits authoritative parametric source and generates explicit,
   versioned targets. It cannot approve its own candidate.
3. Run cheap requirement, math, and parameter checks; generate the declared primary CAD artifact (STEP where supported);
   then check actual solids for constraints, collisions, hardware, and applicable
   motion, insertion, removal, and service paths.
4. Confirm exact CAD Viewer page and artifact endpoint readiness, then inspect
   assembled, exploded/service, and risk closeups. Record readiness separately
   from visual observations.
5. Generate secondary artifacts and validate source/export parity, occurrence
   counts, transforms, mesh/3MF structure, orientation, and exact slicer settings
   when a fabrication artifact is in scope.
6. Freeze the candidate. Distinct critic and validator inspect the same
   fingerprint; a distinct formal reviewer joins their results.
7. Use the smallest coupon or physical observation for remaining fit, force,
   heat, wear, strength, or print-quality uncertainty.

Every non-trivial CAD candidate needs risk-appropriate evidence in four core
categories: object collision, math, constraint, and user requirement. Add export,
slicer, motion/service, manufacturing, or defect regression checks only when the
current risk requires them.

## Acceptance and reflection

Record `domain_extension.cad` with separate states for `cad_source`,
`written_artifact_slicer`, and `physical_print_assembly`, plus the primary
artifact hash, four core evidence references, reviewer identities, and exactly
one smallest next experiment. An earlier layer never proves a later one.

The Workbench [design-reflection skill](../skills/design-reflection/SKILL.md) may inspect canonical records and propose one
falsifiable next experiment. It is CAD/3D-print specific and read-only; it is not
generic workflow orchestration and cannot mutate project state.

For migration, preserve one project at a time, verify it before starting another,
and keep old evidence linked to its original fingerprint. Repository environment,
tests, and pull-request delivery follow the selected project's own contract.
