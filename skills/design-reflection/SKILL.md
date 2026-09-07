---
name: design-reflection
description: Reflect on repository evidence from a parametric CAD or 3D-print project and identify the smallest falsifiable next experiment. Use for daily or on-demand design reflection; do not use as authority to edit designs, artifacts, or continuity records.
---

# Design Reflection

Produce an evidence-grounded reflection for one project without changing the repository. This skill is read-only by default. A request to reflect, including a scheduled reflection, does not authorize edits to parametric source, tests, generated artifacts, project continuity, issues, pull requests, or GitHub Projects.

Resolve an explicit external repository root, project root, revision and optional workshop inventory path using [the binding contract](../../contracts/project-binding.md). Read its AGENTS.md, then the bound Workbench [continuity](../../workflows/policies/PROJECT_CONTINUITY.md) and [CAD workflow](../../workflows/policies/CAD_WORKFLOW.md) policies. Inventory is optional context, never candidate validation; if unbound report it unknown. Do not reproduce those policies in the reflection.

## Establish scope

Name the target and evidence window before drawing conclusions. Resolve an on-demand target deterministically: use an explicit project path or name; otherwise select the sole project in the supplied binding; if multiple targets remain and cannot be inferred, ask the user. Never infer the target from the Workbench checkout.

A scheduled run selects every project with decision-bearing evidence in the anchored window and produces a separate project-scoped reflection for each. Process them sequentially or use at most three workers concurrently; concurrency never caps coverage. If the declared run budget expires before all selected projects are processed, report every remaining exact project path. Never silently omit a project or combine evidence across projects.

Anchor a scheduled window to the scheduler-provided logical occurrence date in `America/Toronto`. A midnight occurrence reflects on the preceding Toronto calendar day. A retry retains the original logical occurrence and window. If the scheduler does not provide that occurrence, report that the deterministic window is missing and request it; never substitute actual execution time.

For each target, read its full canonical record set before reflecting:

- `PROJECT_STATE.md` and `NEXT_AGENT.md`;
- `docs/REQUIREMENTS.md` and `docs/EXPERIENCE.md`;
- `docs/decisions/README.md` and the current, non-superseded decisions it identifies;
- `docs/iterations/CURRENT`;
- the selected current iteration's `BRIEF.md`, `DESIGN.md`, `VALIDATION.md`, `REVIEW.md`, and `HANDOFF.md`.

Missing, stale, internally inconsistent, or candidate-mismatched records reduce confidence and remain visible in the reflection. Do not silently repair or route around them.

Keep projects isolated. Evidence from another project may suggest a question or method, but it cannot validate the target project's geometry, interface, material behavior, or acceptance state. Label any cross-project analogy as `INFERRED` and cite both project paths.

## Authority and evidence

Keep normative authority separate from empirical claim authority.

For intent and constraints, apply explicit user direction for the current request, then the target's stable requirement IDs, invariants, non-goals, and current decisions, followed by the active iteration's frozen `BRIEF.md` and selected contract in `DESIGN.md`. `PROJECT_STATE.md` and `NEXT_AGENT.md` point to this authority; they do not replace it. Chat history, agent recollection, and summaries may help locate records but cannot silently create or change a requirement.

For empirical claims, use evidence matched to the claim and exact candidate. Parametric source and deterministic geometry checks support intended CAD/source claims. Written STEP/mesh/3MF and slicer evidence support only the exact fingerprinted outputs they inspect. Measured physical observations support physical fit, force, heat, wear, print quality, and assembly behavior and outrank nominal CAD assumptions only for those physical behaviors. A failed print is evidence that the tested candidate or process failed; it never silently changes user intent, requirements, or invariants. Preserve contradictions explicitly when the records do not resolve them.

## Build the reflection

Make a compact evidence ledger. Every material statement must carry one label and an exact repository path, requirement/decision/iteration ID, command result, artifact fingerprint, or physical observation:

- `OBSERVED`: directly measured or physically reported.
- `VALIDATED`: demonstrated by a recorded deterministic check against the named candidate.
- `INFERRED`: reasoned from evidence but not directly checked.
- `UNKNOWN`: unresolved or unsupported.

Never promote `INFERRED` to `VALIDATED`. If evidence is absent, stale, contradictory, or points to different candidate fingerprints, say so; do not invent progress, measurements, acceptance, or a design narrative. With no decision-bearing evidence in the window, return a short `no evidence to reflect on` result and list what was inspected. The one next experiment may then be the minimal evidence-capture step that would unblock reflection.

Summarize only the relationships that changed or matter now:

- ontology: assembly, part, interface, datum, purchased hardware, material, process, and requirement category;
- topology: part/interface relationships and critical motion, assembly, insertion, removal, and service states;
- hypothesis/evidence DAG: which claim depends on which check or observation and which branch is blocked;
- provenance chain: authoritative source -> generated artifact -> slicer evidence -> physical print/assembly observation.

State acceptance separately as `CAD/source`, `written artifact/slicer`, and `physical print/assembly`. An earlier layer never proves a later one.

End with exactly one smallest responsible experiment. It must test one named uncertainty, be falsifiable, and be independently printable or digitally testable where possible. Specify the hypothesis, minimal subsystem/coupon or focused check, controlled parameters, measurement and pass/fail criterion, and which requirement or DAG edge the result updates. Prefer the cheapest experiment that can change the next design decision; do not prescribe broad redesign or a large test suite.

Treat inventory from the explicitly bound workshop inventory path as `workshop context`, not project evidence, unless the target project's records bind the candidate to that printer, nozzle, material, or process. Do not infer a slicer profile, tolerance, strength, or fit from availability alone.

## Output and mutation boundary

Return a concise reflection containing:

1. target, evidence window, and candidate fingerprint/status;
2. evidence ledger and unresolved contradictions;
3. changed ontology/topology or hypothesis DAG;
4. the three acceptance layers;
5. exactly one smallest falsifiable experiment.

Summarize durable facts; never create raw chat transcripts, agent diaries, or speculative history. Do not edit source, artifacts, tests, continuity records, or external systems unless the user separately and explicitly authorizes that mutation. If authorized later, follow the repository's delegation, continuity, and pull-request delivery contracts rather than treating the reflection as implementation approval.
