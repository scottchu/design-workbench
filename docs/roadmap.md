# Roadmap

## Why: a trustworthy path from intent to accepted outcomes

Help a user turn project intent into reviewable candidates, revise them without
losing approved properties, and trace each outcome to its source, checks and
approval. Support CAD and image projects through focused tasks and real tools.

The project owns what is being made and what the user approved. Workbench owns
reusable production/review procedures and the execution interfaces it actually
maintains. External providers retain their engines and services.

## How: context selects a focused method

Document each layer as **why -> how -> what**. Each skill explains the problem it
solves, the context in which it applies, its procedure and its concrete result.
Workflow Markdown explains why the sequence exists, how context selects tasks and
routes failures, and what evidence allows each gate to advance. Tools enforce
executable contracts. Project records supply purpose, requirements, current stage,
source/candidate identity, available providers and existing evidence.

Use task-level polymorphism: the same bounded task, such as candidate validation,
may select an image or CAD implementation. Share an evidence envelope where useful;
preserve domain-specific methods, fields and acceptance. A CAD screenshot may need
visual review while its dimensions still require geometry checks. Artifact file
type alone is insufficient routing context. Start with documented routing and
small adapters; do not introduce a universal engine or a skill full of unrelated
image/CAD branches.

Focus and consistency are principles, not automatically standalone meta-skills.
Only extract a cross-domain skill after independently useful repeated tasks prove
its inputs, output and failure semantics. A workflow may help discover a design
choice; the resulting choice and approval still belong to the project.

## Current evidence baseline

This roadmap is an intended sequence, not an implementation inventory. Current
state comes from [PROJECT_STATE.md](../PROJECT_STATE.md), active iteration records
and the exact source/package identities. No date-based completion promises.

| Area | Recorded state as of 2026-09-08 |
| --- | --- |
| Foundation, ownership extraction and host relocation | Delivered in main through `d92816a`; historical evidence linked by current state. |
| Focused playground skills | Local commit `6466d15` adds simulator-server and simulator-page; five-skill package and isolated page operations verified. Submitted in PR4; not installed or live-invocation accepted. |
| Installed plugin | Existing three-skill package; unchanged by the local extraction. |
| Workbench MCP | Planned; no Workbench MCP server implemented or registered. The current SvelteKit host is an HTTP service, not MCP. |
| Consistent-image workflow | Planned extraction from sticker production; current G0-G3 safeguards remain authoritative. |
| CAD milestone 1 | Still incomplete: measured parameter regeneration and displayed/exported identity need proof. |
| Portable recipes | Neither the CAD nor sticker recipe has complete portable end-to-end acceptance. |

The twelve-category catalog and two mapped recipes remain discovery documents.
Do not infer runtime availability from them. No project migration or mandatory
engine conversion is introduced by this roadmap.

## Ordered next work

### R1. Finish the focused playground skill pilot

**Why:** establish independently usable tasks before expanding the interface.

**How:** review and deliver the existing local extraction through the repository PR
route. Give any installable update a distinct release identity, then separately
scope installation and a fresh-session invocation using the current runtime
binding. Preserve the existing healthy host and historical phone evidence.

**What / completion gate:** installed discovery finds the intended skills; a fresh
agent can inspect the owned runtime and open one registered Laifen page through
the appropriate tasks, returning actual identity and availability evidence.
Source package, installation, live service reuse and browser behavior are separate
recorded results. This does not complete CAD milestone 1. The already tested
isolated registration/update/removal paths need no live mutation merely to repeat
those checks.

### R2. Workbench MCP for the playground

**Why:** expose owned operations through typed, inspectable calls instead of asking
each agent to reconstruct shell and local registry-edit procedures.

**How:** define the operation contracts first; reuse the existing lifecycle and
registry implementation behind a thin adapter. Start with read-only server status,
page list and page inspection. Then add scoped page registration/update/removal
and the needed server ensure/open/stop operations. Treat login persistence,
relocation, installation and private-network configuration as distinct operations
with explicit scope, not side effects of opening a page.

**What / completion gate:** real MCP client calls exercise read-only discovery and
one bounded page lifecycle on generic isolated fixtures. Inputs select the bound
runtime, registry and project build; outputs identify operation, candidate and
actual result. Failure cases cover ownership conflict, stale source/assets,
duplicate IDs, invalid paths, unintended sibling changes and registry drift.
Update/remove need a supported, validated mutation boundary; do not publish a
concurrent-safe API backed only by an unchecked read-then-rename procedure.
Read-only calls do not start services or sync dependencies. Return a selected
page URL explicitly; browser launch is a requested effect, not proof of review.

First checkpoint: a real client can request status/list/inspection and receive
identified results and truthful failures without changing service configuration.
This read-only slice is sufficient before returning to CAD milestone 1; completing
MCP mutation operations is not a prerequisite for that CAD work.

Choose and record transport/runtime/tool names in the implementation brief after
inspecting supported interfaces. No arbitrary shell/G-code proxy, duplicate server
lifecycle, printer API, private assets or provider credentials belong in this MCP.
Source protocol tests do not authorize registration into the installed plugin or
live service mutation. Keep the existing CLI useful and the HTTP playground host
separate from its MCP control interface. Do not wait for a broad tool platform
before returning to the real Laifen CAD milestone 1 below.

### R3. Extract consistent-image production

**Why:** reusable production should support project-defined identity, style and
theme across image sets; a sticker pack is one outcome intent.

**How:** inventory each current sticker rule as general image production,
sticker/output-specific procedure, or project-owned requirement. Generalize the
workflow into reference/spec intake -> bounded contract -> representative pilot ->
bounded generation -> independent review -> targeted revision. Extract only focused
tasks with explicit inputs/results: contract preparation, candidate production,
consistency/defect review and bounded revision. Exact names and split count follow
that inventory, not a quota. Deterministic text composition is separate when needed.

**What / completion gate:** one small project-authorized image case and an isolated
non-sticker fixture exercise the same reusable process with different requirements.
The project chooses which identity/style/theme properties are fixed and which may
vary. Verify actual candidates against those requirements; facial consistency is
not mandatory for image sets that do not require it. Preserve source hashes,
exact-text authority, pilot coverage, passing candidates, bounded retries,
independent review and user design approval. Demonstrate that an intentional change
invalidates only affected checks; a revision cannot silently inherit old approval.
No private project art or requirements are copied into Workbench.

Retain a sticker outcome recipe/procedure for selected platform partition,
transparency, border, dimensions, text composition and delivery gates. The project
selects platforms and requirements; reusable tooling performs those checks. Keep
G0-G3 limits until the replacement procedure has independent equivalence review;
renaming a skill is not acceptance. Native art generation or edits require a
project-scoped request and are not authorized by writing this roadmap.

### R4. Prove shared contracts across image and CAD

**Why:** reuse context and evidence handling without flattening domain expertise.

**How:** compare the image pilot with actual CAD milestone 1 evidence. Begin from
existing project bindings and receipts. Document task selection using purpose,
requirements, candidate type, available providers and requested evidence.

**What / completion gate:** both domains use an explicit candidate identity and
report checked requirements, failures, evidence references and pending approval.
Their validators remain domain-specific: visual judgments/pixel checks versus
geometry/constraint/readback checks. A fresh agent can select the correct validator
without reconstructing chat; missing context or an unavailable provider is reported
rather than replaced with a plausible result. Add a common skill/schema extension
only for a demonstrated gap. Do not make R4 infrastructure a prerequisite for the
first real image or CAD pilot.

### R5. Extract proven reusable outcome tools

**Why:** make repeated operations reliable across projects without embedding one
project's assumptions in reusable software.

**How:** inspect existing project audit/composition/export scripts. Move only
verified generic operations into a versioned package with explicit configuration;
project-specific generators, simulation math, wording, font selection and release
choices remain project-owned. Expose an operation through Workbench MCP only when
Workbench owns and validates it; otherwise use the external provider binding.

**What / completion gate:** the original project and a generic second fixture use
the same tool version successfully; source/artifact readback and a credible failure
case pass. Project bindings identify exact tools and inputs. Export, preflight and
publication are separate tasks; a generated image or accepted master does not
imply platform release. Preserve original project observations when promoting the
general lesson into workflow or tools.

## Sequencing and dependencies

1. Deliver/accept the existing R1 pilot, then implement the R2 read-only MCP slice.
2. Return to CAD milestone 1; pursue R3 as the image-domain pilot in its own bounded
   iteration. Neither pilot requires completed R2 mutation operations or a
   generalized orchestration engine.
3. R4 follows real evidence from both pilots. R5 is justified by demonstrated reuse
   and may proceed for a specific operation without waiting for all of R4.
4. Continue CAD milestones 2-6 below with their original observable gates.

The reviewed local source is now submitted as
[PR4](https://github.com/scottchu/design-workbench/pull/4). The single next action is
**review/merge PR4**. Installed-plugin changes and live acceptance remain
separate from source PR delivery. The next implementation brief after R1
should freeze the read-only R2 tool contract before adding mutation operations.

## Preserved CAD roadmap and acceptance gates

The original CAD milestone numbers remain stable for existing references. Their
requirements below are retained; the new reusable-software work does not replace
the measured-build, manufacturing or physical-acceptance goals.

## 0. Reproducible foundation

**Why:** Reproduce and diagnose real CAD generation before depending on an interactive UI.

**How / what:** Provide the pinned root Python environment, root npm workspace, doctor and generic CAD smoke/readback path described in decision 0001.

Done when a fresh local setup can diagnose its environment, generate the fixture, verify the written STEP and produce a provenance receipt. Requested snapshots must either succeed with an identified image or fail explicitly. Record actual local test results and limitations.

## 1. One real Laifen interaction

**Why:** Make parameter exploration trustworthy by proving displayed and exported geometry comes from the same actual source build.

**How / what:** Open the existing Laifen source from its project repository. Expose device length, outer diameter and split distance. Regenerate the actual OpenSCAD model, display the resulting geometry and export that candidate. Evaluate the existing local/private browser path before introducing another service or wrapper.

Done when each of the three edits changes measured regenerated geometry and the exported candidate matches the displayed build identity. Render-only transforms do not satisfy this gate. Show the active parameter preset, including any intentional simplification. Private mobile review must not require public publishing.

## 2. Trustworthy build revisions

**Why:** Keep the selected candidate and its evidence truthful across asynchronous changes and failures.

**How / what:** Add only the state handling needed for rapid parameter changes, failed builds, cancellation and reopening a selected candidate.

Done when a deliberately delayed older build cannot replace a newer selected result; an invalid configuration reports failure and retains the previous successful candidate under its original identity; reopening recovers the selected build and evidence. Verify source/export identity instead of relying on UI labels alone.

## 3. One Python mechanical case and useful evidence

**Why:** Prove the artifact boundary supports a real mechanical problem and domain-specific evidence.

**How / what:** Integrate build123d through the same small artifact boundary. Choose one bounded existing mechanism with actual hardware and one critical motion or service state. Introduce source-feature selection only where the case needs it.

Done when written artifacts agree with the generated solids, a concrete known defect fails a targeted check, and its responsible correction passes the affected checks. Selection resolves meaningfully or reports ambiguity. CAD, export and physical states remain distinct. Use a small human-confirmable diagram/section before costly redesign when intent is uncertain.

## 4. Preparation handoff

**Why:** Trace manufacturing preparation back to the exact reviewed CAD candidate.

**How / what:** Send an identified exported candidate to a real slicer preparation path. Reuse proven Orca capabilities where available; implement absent behavior as explicit new work. Printer control is not required for this milestone.

Done when preparation names its exact input artifact, tool mapping/settings, output and validation evidence. A failed preparation cannot inherit success from an earlier artifact. The user can trace the prepared result back to the selected CAD build.

## 5. Printer observation and separately authorized operations

**Why:** Connect fresh device and physical evidence without conflating observation with control or design acceptance.

**How / what:** Connect existing read-only device observation first. Add upload/start or other operations only as separately scoped capabilities with their own authorization and current-state checks.

Done when observation truthfully identifies its acquisition and freshness, and physical observations can be attached to the relevant manufactured revision. Device progress must not be presented as CAD or assembly acceptance.

## 6. Package what repeated use proves useful

**Why:** Make useful workflows reproducible by a fresh agent and measure actual design progress.

**How / what:** Extract stable CLI/API entry points and concise skills from repeated successful workflows. Consolidate owned software only when it simplifies maintenance without collapsing domain boundaries.

Done when a fresh agent session can reopen a project, reproduce a selected build, explain its evidence and name remaining acceptance gaps from durable records. Evaluate progress by time to a reviewable result, useful early user corrections, regeneration reliability and escaped defects—not wrapper count, test count or agent count.

## Delivery and progress measures

Each material iteration records its why, context-dependent method, bounded outputs,
non-goals and falsifiable acceptance gate before implementation. Keep one writer
per namespace and independent acceptance for substantial changes. Run relevant
local tests and actual artifact readback; no repository-hosted CI. Maintain project
records and deliver intended trunk changes on a non-main branch through a PR.

Measure time to a reviewable result, useful early corrections, regeneration
reliability, post-contract rework and defects escaping review. Skill/tool counts,
passing package checks and screenshots alone are not product acceptance.
