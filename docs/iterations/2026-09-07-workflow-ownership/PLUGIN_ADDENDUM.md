# Plugin and server scope update

The user requested packaging Workbench as a plugin with end-to-end skills including CAD, slicer and printer capabilities, then asked whether text-to-CAD should be installed separately, controlled by us or cloned/rewritten. The recommended first architecture is separately installed providers coordinated by Workbench. The user accepted that direction and asked for an eventual server powering simulator, dashboard and MCP.

The user's subsequent explicit decision supersedes the broader shared-backend proposal: printer and slicer MCP remain a separate project with their existing API/dashboard/widgets. CAD Workbench owns the workflow plugin and one dedicated local SvelteKit simulator dev server that can host existing project simulations, avoiding separate per-project Tailscale endpoints. This delivery includes that bounded local host. It does not add another printer/slicer MCP or dashboard backend, move services, or rewrite simulator geometry. Existing project simulators are loaded through explicit local bindings, starting with an inspected real example.

## Ownership

- Workbench plugin: discoverable end-to-end skills and explicit provider selection, source/artifact identity, gate/evidence handoff.
- text-to-CAD: separately installed upstream skills and pinned cadgen runtime. Installing either does not install the other. No fork, clone or upstream rewrite.
- Existing Orca/U1: separately owned preparation, authorized-start and observation paths. The currently connected public MCP tools observed in this task are read-only `observe_printer` and `open_printer_camera`; do not invent slicing or start MCP tools.
- Workbench local simulator host: SvelteKit dev server for explicitly registered external project simulators and their assets. Existing project source/math stays authoritative. Default loopback access requires no Tailscale; mobile/off-network access is a separate connectivity requirement.
- Existing printer/slicer project: retains its API, dashboard, widgets and MCP. Workbench does not create competing services or move those capabilities into this repository.

Plugin packaging and the local simulator host are source/artifact/local-development work only. No marketplace registration, plugin installation, existing external service/auth/Tailscale modification or printer operation. Actual end-to-end print execution remains separately scoped and requires its artifact and authorization gates.

## Documentation basis

Official OpenAI plugin architecture: https://developers.openai.com/plugins/concepts/plugins (read 2026-09-07). A plugin may package skills using existing tools, with its own MCP/UI added when needed. Official skill guidance: https://developers.openai.com/plugins/build/skills. Workflow guidance and live controlled behavior have separate responsibilities.

## Bounded follow-up

The read-only provider assessment selects a portable package layout without duplicate maintained policy sources. I4/workbench_implementation owns packaging and an end-to-end entry skill. I5/sticker_migration owns apps/simulator and root npm configuration only; its prior sticker namespace is frozen. Independent acceptance checks package-contained references, instruction behavior, local server boundaries and an actual existing interactive simulator; this does not prove CAD/slicing/printer execution. The original migration V2 gate remains bound to provider commit `36f41715ee2257c0f2e41e40329216e3d2b2747f`; plugin additions receive their own fingerprint rather than silently upgrading project bindings.
