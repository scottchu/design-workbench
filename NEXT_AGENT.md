# Resume CAD Workbench

Read `AGENTS.md`, `README.md`, `PROJECT_STATE.md`, decisions 0001/0002 and the active [workflow ownership handoff](docs/iterations/2026-09-07-workflow-ownership/HANDOFF.md) before editing. Inspect current Git status and remote refs; do not infer delivery from this plan.

The accepted boundary is a workflow plugin plus one local SvelteKit simulator host. External design repositories own source, models and simulation logic. Orca owns printer/slicer MCP, API, dashboard and widgets. Provider installs, services and Tailscale routes remain separate.

The migration review pins Workbench `36f4171`, source `b8b0f5d` and sticker `33fcac4`. Consumer bindings intentionally retain that provider revision when newer plugin packaging is added. Read migration VALIDATION/REVIEW and plugin/simulator receipts separately.

The active source checkout is `/Users/scottchu/Projects/personal/design-projects-workflow-separation`. The old 0868 path disappeared externally; canonical dirty design WIP and original sticker live-pilot worktree remain untouched. The superseded workflow-library draft remains recoverable.

Use root uv/npm tooling. `npm run dev:simulator` binds 127.0.0.1:4179; the app README documents explicit external registration. Generated packages, local registry and build outputs are ignored. Stop the dev process before check/build commands that regenerate the same SvelteKit output, then restart it for browser acceptance.

No merge, plugin installation, deployment, printer operation or Tailscale change is implied by PR delivery. The generic CAD foundation is previously validated; rerun its expensive checks only when relevant changes justify it. Roadmap milestones describe remaining contracts, not shipped capabilities.
