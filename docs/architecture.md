# Architecture and ownership

## Product boundary

CAD Workbench connects design intent, generated geometry and review evidence. The long-term application may include preparation and printer observation, with CAD, preparation and printer operations remaining separate domains. Sharing a repository does not require sharing a process or granting CAD tools printer authority.

| Owner | Responsibility |
| --- | --- |
| External design repositories, including design-projects | Authoritative CAD source, design parameters, requirements, design decisions, project checks, release artifacts and physical observations. |
| CAD Workbench | Reusable application and backend adapters, parameter controls, artifact/provenance presentation, workflow catalog and recipes, shared policies/templates/skills, generic software fixtures and integration tests. |
| Pinned text-to-CAD/cadgen runtime | Existing supported generation, inspection, export and snapshot capabilities. |
| Orca preparation and printer-operation domains | Slicer preparation and device workflows, connected through identified artifacts when implemented. Existing Orca architecture documentation does not establish that every planned capability is available. |

No existing repository is migrated by the foundation. Small software fixtures here must be independently understandable and contain no private design, printer or credential data.

The subsequent workflow-ownership iteration explicitly extracts reusable workflow content from design-projects into Workbench. Project repositories retain their source, generators, tests, instantiated records, assets, workshop facts and physical observations. They select external workflow versions through small bindings; historical records continue to identify their original sources. Catalog entries distinguish a bounded capability, a recipe joining capabilities, agent instructions, executable providers, and project instances. A catalog entry does not establish successful execution or project acceptance.

The existing host-specific CAD Viewer controller is preserved as legacy maintenance source during extraction. Its existing installed service and canonical Python dependency are not relocated or operated by this work. Moving its source does not demonstrate a portable runtime. The separate workflow-library draft and empty private remote remain recoverable superseded work, not a second active workflow authority.

## Foundation implementation boundary

asdf pins Node.js, Bun and uv in `.tool-versions`. uv manages CPython 3.12.13 from `.python-version` and the sole root environment that hosts the pinned cadgen runtime. This scoped Python choice preserves the already selected installation without adding another base interpreter. Bun is available; npm remains the JavaScript workspace package manager. A diagnostic script verifies the required environment. A separate smoke script builds one source fixture and measures the written STEP. Ignored artifacts carry a receipt describing their source, command, runtime and checks.

The root npm workspace prepares dependency ownership for a later TypeScript application. It does not justify creating empty UI packages. There is no application server, generalized job manager or persistent viewer service in the foundation.

The Python runtime installation and agent skill/plugin installation are separate concerns. A future skill should explain when and how to use a small supported command; it should not be the only place where reproducibility, argument validation or artifact identity are enforced.

## Planned integration model

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
