# Architecture and ownership

## Intent source, implementation, delivery and runtime

The [product definition](product.md) owns why Design Workbench exists, how it
helps and what it delivers. Versioned product documents govern intended behavior;
implementation and observations must be assessed against that intent.

| Layer | Authority and current home |
| --- | --- |
| Product intent source | `docs/product.md`, architectural constraints, shared contracts and adopted decisions define required behavior and boundaries. Proposals retain their explicit status. |
| Implementation source | `skills/`, `workflows/`, `apps/playground/` and executable tools realize the product. Skill and workflow Markdown is maintained product implementation, even though it is text. Shared rules remain in their owning contracts rather than being copied here. |
| Build and verification source | Packaging code, tests, generic fixtures and build scripts assemble and check declared deliverables. Passing checks supply evidence; they do not redefine intent. |
| Product deliverables | Versioned plugin packages and supporting software builds are outputs. Current packaging assembles sources and receipts; it does not provide an already prepared runtime. |
| Runtime instance | An installed environment, built app, running process, local binding, registry and logs describe a particular deployment. These are separate from the source and release identities. |
| Records and navigation | Current verification summarizes findings and links separately retained evidence; historical iteration records remain where still consumed. `PROJECT_STATE.md` summarizes current delivery and pending work; `NEXT_AGENT.md` routes a successor to the owners. Neither creates new product requirements. |

These are responsibility boundaries, not a requirement for six new folders or
repositories. Current runtime build and environment files remain ignored in the
bound canonical checkout. A source update, package build, plugin installation and
runtime refresh are distinct actions; none silently performs the others. This
documentation change does not relocate the live runtime or select a new release
layout.

Agentic Compiler's documents-as-source direction informs this separation. For
Workbench, consequential product choices belong in versioned intent documents or
explicit configuration, rather than chat memory. Existing implementation code
remains maintained source: no docs-to-code compiler or complete reproducible
docs-to-product pipeline has been demonstrated. Adopting intent authority is not
a claim that implementation can already be discarded and regenerated.

The [source sufficiency target](product.md#source-sufficiency-target) requires
capturing enough behavior in document source to reconstruct declared outputs.
[Current verification](verification.md) records the demonstrated scope and gaps.
Generated models and code remain designated experimental fixtures; production
continues to use its existing implementation.

[Documentation ownership](documentation.md) defines current source, replaceable
technical decisions, evidence and iteration closeout. Git retains revision history;
reconstruction uses the effective source and explicit target inputs at a revision.

Document format does not determine authority. Product requirements, proposed
architecture, agent instructions and observed results can all be Markdown while
having different roles. Give each rule one owner, link to it from other views,
and expose conflicts between intent and observed behavior instead of silently
treating either as the other.

## Planned evolution: purpose, composition and owned execution

The [roadmap](roadmap.md) records the user's subsequent direction. Document each
layer as why -> how -> what; use project purpose, requirements, candidate identity
and evidence needs to select focused domain tasks. Shared task/evidence contracts
do not require identical image and CAD validators or a universal workflow engine.

Planned Workbench ownership expands to a narrow MCP interface for its own
playground operations, reusing the existing tools. This refines the previous
no-own-MCP scope for future implementation; no Workbench MCP exists or is installed
yet. The HTTP simulator host and external CAD/art/printer providers retain their
current boundaries. The first tool contract and transport are still to be defined.

Consistent-image production will be extracted from sticker production, with
project-selected invariants and variation. Sticker outcome procedures retain their
reusable format/preflight knowledge; the project owns actual requirements and
approvals. Existing skills and safeguards remain in force until that extraction
passes its own acceptance gates. These are planned changes, not delivered behavior.

## Workflow and skill composition

[Decision 0003](decisions/0003-composable-skills.md) defines the next incremental
refinement: project records own intent and evidence, workflow Markdown composes
tasks and gates, focused skills guide each task, and tools execute operations.
The local source pilot extracts server and page lifecycle guidance into
`simulator-server` and `simulator-page`, with `workbench-flow` routing to them.
Source packaging now contains five skills; installed-plugin and live invocation
acceptance remain separate from this extraction.

## Product boundary

Design Workbench owns the design workflow plugin and a dedicated local SvelteKit Playground host. It connects project-owned intent, design sources and evidence through explicit provider bindings. The separate printer/slicer project retains its MCP, API, dashboard and widgets; Workbench coordinates those capabilities through skills without absorbing their services. This user decision supersedes the earlier broad application-backend proposal.

| Owner | Responsibility |
| --- | --- |
| External design/image repositories | Authoritative design sources, parameters, references, requirements, design decisions, project checks, release artifacts, approvals and physical observations where applicable. |
| Design Workbench | Design-work plugin, catalog/recipes, shared policies/templates/skills, Playground host, generic software fixtures and integration checks. |
| Pinned text-to-CAD/cadgen runtime | Existing supported generation, inspection, export and snapshot capabilities. |
| Separate Orca preparation and printer-operation project | Slicer/printer runtime, API, MCP, dashboard and widgets. Connected through identified artifacts and actually available interfaces. Existing architecture documentation does not establish that every planned capability is available. |

No existing repository is migrated by the foundation. Small software fixtures here must be independently understandable and contain no private design, printer or credential data.

The subsequent workflow-ownership iteration explicitly extracts reusable workflow content from design-projects into Workbench. Project repositories retain their source, generators, tests, instantiated records, assets, workshop facts and physical observations. They select external workflow versions through small bindings; historical records continue to identify their original sources. Catalog entries distinguish a bounded capability, a recipe joining capabilities, agent instructions, executable providers, and project instances. A catalog entry does not establish successful execution or project acceptance.

The existing host-specific CAD Viewer controller is preserved as legacy maintenance source during extraction. Its existing installed service and canonical Python dependency are not relocated or operated by this work. Moving its source does not demonstrate a portable runtime. The separate workflow-library draft and empty private remote remain recoverable superseded work, not a second active workflow authority.

## Foundation implementation boundary

asdf pins Node.js, Bun and uv in `.tool-versions`. uv manages CPython 3.12.13 from `.python-version` and the sole root environment that hosts the pinned cadgen runtime. This scoped Python choice preserves the already selected installation without adding another base interpreter. Bun is available; npm remains the JavaScript workspace package manager. A diagnostic script verifies the required environment. A separate smoke script builds one source fixture and measures the written STEP. Ignored artifacts carry a receipt describing their source, command, runtime and checks.

The root npm workspace now owns `apps/playground`, a dedicated SvelteKit host. It adds no generalized job manager or persistent viewer service. The original foundation remains a small CLI/runtime layer.

The Python runtime installation and agent skill/plugin installation are separate concerns. A future skill should explain when and how to use a small supported command; it should not be the only place where reproducibility, argument validation or artifact identity are enforced.

## Local simulator and future build integration

The implemented local simulator host discovers only explicitly registered project asset roots. It serves real existing simulators and identifies their source/artifacts, keeping project code and models outside Workbench. Browser-appropriate simulation remains in the browser; a reusable host is not another geometry implementation. Loopback development needs no Tailscale. Remote or phone access is not implied by localhost availability. No printer or slicer API is added to this host.

External source and explicit parameter values produce an identified build through a backend adapter. The application displays the geometry produced by that build and associates exports and evidence with it. A build identity should include source/dependency identity, backend version, parameters and units. File hashes identify the actual written artifacts. This is an intended contract to prove through the first interactive case, not a claim that a generalized build system exists now.

OpenSCAD remains appropriate for existing configurable CSG designs and their actual regeneration. Python/build123d with OCCT is the preferred subsequent mechanical backend because it exposes solids, topology, datums and assembly relationships to code. Both backends retain their native modeling capabilities; a shared artifact boundary must not pretend they expose identical topology or manufacture a universal geometry representation.

The viewer consumes actual geometry. Measurements come from a named geometry or artifact analysis method. Semantic labels, dimensions, keep-outs and selection markers form a distinct explanatory layer. A future topology-to-source mapping must be resolved for its build and report missing or ambiguous references rather than silently reusing stale indices.

Parameters should be supplied to the source's real regeneration path. Browser controls may perform advisory prechecks, but must not maintain another authoritative version of dimension or constraint math. Private mobile use can employ an OpenSCAD WASM adapter when the exact model and dependencies support it; this does not imply that arbitrary Python/OCCT models run in the browser.

## Reuse before ownership expansion

Start with pinned upstream capabilities and small adapters. Reuse an existing viewer before replacing rendering, selection, camera and lifecycle functionality. A selective fork requires a reproducible integration blocker, a bounded patch, compatibility evidence and an upstream/update plan. Rewriting a component becomes justified by demonstrated limitations or maintenance cost, not by the desire to own the whole stack.

Preserve early human validation of ambiguous geometry through a small section, diagram or one/two adjustable relationships. Explain which dimensions are fixed, derived, chosen and physically unknown. Review should address an actual decision; hovering over or selecting geometry does not imply approval.

## Evidence boundaries

- CAD evidence concerns actual source-generated solids and their relevant relationships.
- Artifact evidence concerns written STEP/mesh files and their readback; preparation evidence names the exact artifact and slicer settings.
- Physical evidence concerns observations of a particular manufactured/assembled revision.

Success in one category does not confer acceptance in another. The foundation verifies a generic STEP only; future domain integrations and physical acceptance remain outside its claims.

## Managed simulator runtime

The simulator requires a local Node runtime and the actual adapter-node build.
The plugin packages its intentional source and dependency locks; it does not
implicitly install dependencies or register a login service. The lifecycle helper
identifies one owned macOS user LaunchAgent and refuses another checkout or an
unknown listener on the fixed loopback port. On-demand ensure/open and explicit
login persistence are separate supported modes. Optional Tailscale Serve gives
private HTTPS access through one configured origin; no public Funnel endpoint or
printer/slicer service is introduced. See the 2026-09-07-simulator-service iteration
for live setup evidence.
