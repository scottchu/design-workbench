---
name: workbench-flow
description: Coordinate a bound design or sticker project through intent, real source builds, review, optional slicing preparation and separately authorized printer handoff. Use when the user wants the reusable Workbench workflow across available providers; preserve preparation-only and observation-only requests.
---

# Workbench Flow

Resolve the requested outcome and current project gate using the [project binding contract](../../contracts/project-binding.md). Read the external project's current records, exact source revision and declared commands. The installed plugin supplies guidance; the project owns authoritative source, parameters, assets and acceptance. Do not use the plugin's checkout as the project root.

Select the [CAD fabrication recipe](../../workflows/cad-fabrication.md) or [sticker production recipe](../../workflows/sticker-production.md). For CAD reflection use [design-reflection](../design-reflection/SKILL.md). The [catalog](../../catalog/CAPABILITIES.md) records evidence limits; it does not claim a live provider is available.

Read [provider selection](references/providers.md) before choosing an execution tool. Verify the installed provider identity/version and actual callable interface, separately from maintained provider source and from runtime dependencies. A missing provider leaves only its dependent step unavailable. Continue independent authorized work and report the concrete missing capability; do not manufacture a tool, install a plugin implicitly or turn a missing integration into a generic HTTP/G-code proxy.

Keep the route as narrow as the user's request:

- Design/build: clarify materially new intent with one or two relationships, freeze source plus real parameters, invoke its actual generator and read back the written artifact. A screenshot or display transform is not a source rebuild.
- Preparation only: bind the exact artifact and actual slicer/profile/tool mapping, produce and statically validate G-code through the external preparation provider. Finish with identified output and evidence; preparation does not include upload/start.
- Observation only: use read-only observation/camera tools, preserving snapshot provenance and telemetry freshness. A CAD or preparation failure must not interrupt independently requested observation.
- Start when explicitly requested: use the separately installed authorized-start workflow only after resolving an actual operations provider. Verify the exact validated artifact/hash, current target and preflight conditions under that workflow. Authority for a prior artifact never silently transfers to a new artifact. An unavailable start interface remains unavailable.
- After start, ongoing monitoring requires the corresponding read-only workflow and its own request scope. Monitoring cannot acquire control authority from shared context.

Record the [handoff receipt](../../contracts/provenance-and-handoff.md) in the project. Keep source/CAD, written artifact/slicer, physical acceptance, machine audit, human review and user intent decisions separate. State actual commands/results and pending gates; passing package checks or a skill read does not establish recipe execution.

For simulator work, route server status/lifecycle to
[simulator-server](../simulator-server/SKILL.md), and a named project page to
[simulator-page](../simulator-page/SKILL.md). The page task composes server
resolution with page availability checks. Follow the selected recipe's intent and
acceptance gates; page availability is not geometry validation. Pure observation
or preparation that needs no simulator does not start the host. This plugin exposes
no MCP server of its own; printer/slicer services remain external.
