# Roadmap

This is an intended sequence, not an implementation inventory. Advance by observable completion gates. Keep existing designs outside this software repository; no mandatory migration or engine conversion is required.

User priority update, 2026-09-07: the [workflow ownership iteration](iterations/2026-09-07-workflow-ownership/BRIEF.md) precedes milestone 1. Its gate is a discoverable twelve-category catalog and two mapped recipes with explicit providers, project bindings and separate acceptance, plus independently verified project/history/WIP preservation and removal of embedded shared workflow authority from design-projects. It does not implement a workflow engine or establish end-to-end recipe execution.

## 0. Reproducible foundation

Provide the pinned root Python environment, root npm workspace, doctor and generic CAD smoke/readback path described in decision 0001.

Done when a fresh local setup can diagnose its environment, generate the fixture, verify the written STEP and produce a provenance receipt. Requested snapshots must either succeed with an identified image or fail explicitly. Record actual local test results and limitations.

## 1. One real Laifen interaction

Open the existing Laifen source from its project repository. Expose device length, outer diameter and split distance. Regenerate the actual OpenSCAD model, display the resulting geometry and export that candidate. Evaluate the existing local/private browser path before introducing another service or wrapper.

Done when each of the three edits changes measured regenerated geometry and the exported candidate matches the displayed build identity. Render-only transforms do not satisfy this gate. Show the active parameter preset, including any intentional simplification. Private mobile review must not require public publishing.

## 2. Trustworthy build revisions

Add only the state handling needed for rapid parameter changes, failed builds, cancellation and reopening a selected candidate.

Done when a deliberately delayed older build cannot replace a newer selected result; an invalid configuration reports failure and retains the previous successful candidate under its original identity; reopening recovers the selected build and evidence. Verify source/export identity instead of relying on UI labels alone.

## 3. One Python mechanical case and useful evidence

Integrate build123d through the same small artifact boundary. Choose one bounded existing mechanism with actual hardware and one critical motion or service state. Introduce source-feature selection only where the case needs it.

Done when written artifacts agree with the generated solids, a concrete known defect fails a targeted check, and its responsible correction passes the affected checks. Selection resolves meaningfully or reports ambiguity. CAD, export and physical states remain distinct. Use a small human-confirmable diagram/section before costly redesign when intent is uncertain.

## 4. Preparation handoff

Send an identified exported candidate to a real slicer preparation path. Reuse proven Orca capabilities where available; implement absent behavior as explicit new work. Printer control is not required for this milestone.

Done when preparation names its exact input artifact, tool mapping/settings, output and validation evidence. A failed preparation cannot inherit success from an earlier artifact. The user can trace the prepared result back to the selected CAD build.

## 5. Printer observation and separately authorized operations

Connect existing read-only device observation first. Add upload/start or other operations only as separately scoped capabilities with their own authorization and current-state checks.

Done when observation truthfully identifies its acquisition and freshness, and physical observations can be attached to the relevant manufactured revision. Device progress must not be presented as CAD or assembly acceptance.

## 6. Package what repeated use proves useful

Extract stable CLI/API entry points and concise skills from repeated successful workflows. Consolidate owned software only when it simplifies maintenance without collapsing domain boundaries.

Done when a fresh agent session can reopen a project, reproduce a selected build, explain its evidence and name remaining acceptance gaps from durable records. Evaluate progress by time to a reviewable result, useful early user corrections, regeneration reliability and escaped defects—not wrapper count, test count or agent count.
