---
name: simulator-page
description: Register, inspect, open, update or remove one project-built page in the Workbench simulator host. Use for a named playground page; project page implementation and simulation logic remain project-owned.
---

# Simulator Page

Manage one registered external build. Read the host's
[registration contract](../../apps/playground/README.md) before selecting a tool.
These package-relative links describe current source. Resolve one `app_root` in
the bound runtime by checking its actual registration CLI and registry module:
use `apps/playground` when both exist, otherwise the legacy `apps/simulator` when
both exist there. Use that same resolved root for README/SERVICE documents, CLI
invocations and every registry-module import below. If neither is complete, report
the missing prerequisite; never mix roots or assume a skill update relocated the host.
For a project task, resolve its [binding](../../contracts/project-binding.md) and
current records. Inputs are the requested operation, page ID, project/source
identity, and (for registration/update) its documented build output and entrypoint.
Use the project's own runtime and commands for a requested source build.

Resolve the actual runtime and registry via
[simulator-server](../simulator-server/SKILL.md). Inspection uses read-only status;
opening a page requires healthy server reuse/ensure within the request's scope.
A supplied earlier health result must be rechecked when freshness is uncertain.
The registration CLI defaults to a cwd-relative registry, so always pass the
explicit selected registry with `--config`; it must match the managed service's
registry when working on that service. Never register into the plugin cache by
assuming it is the service root.

## Operations

- Inspect: read the selected entry and availability reason; check source/asset
  identity through the host's registry loader and asset reader or served routes.
  `loadRegistry` checks source and registry metadata; it does not read every built
  asset. Use `readAsset` for the entrypoint and each declared asset before claiming
  complete asset verification. Do not rebuild or
  refresh hashes to make a stale page appear available.
- Register: use the existing `node <app_root>/scripts/register.mjs` from the
  resolved Workbench root with `--id`, `--title`, `--asset-root`, `--source-root`,
  `--source-entry` and explicit `--config`. Supply actual absolute project roots.
  The tool requires a Git source revision and validates the candidate registration.
- Open: after identified health succeeds, check `/simulators/<id>` and its actual
  registered `/assets/<id>/<entrypoint>` availability, then open the selected route
  through an available browser interface. HTTP success alone is not visual review.
- Update/remove: there is no dedicated CLI verb or HTTP write API. For an explicitly
  requested registry edit, preserve the original registry bytes in an ignored
  recovery file, prepare a separate candidate registry and change only the selected
  entry. For update, remove that ID in the candidate then run the registration CLI
  against the candidate with the newly reviewed build. For removal, remove only
  that entry; leave other entries and allowed roots unchanged. Validate the candidate
  with the existing `loadRegistry` and `readAsset` exports from
  `<app_root>/src/lib/server/registry.js`; require the updated entry available
  (or removed ID absent), read every updated asset, and preserve sibling entries
  and their availability.
  Before replacing the selected registry, confirm its bytes still match the
  captured original; if changed, stop and reconcile. Replace atomically on the
  same filesystem, then read back. This local procedure assumes a single writer;
  it is not a concurrent transaction API. If that condition cannot be established,
  leave replacement pending. Do not delete project builds or restart the server.

Use an isolated explicit registry for fixtures; it does not need a live service.
Missing or changed source/assets leave that page unavailable. Preserve healthy
siblings and report global schema/duplicate-ID failure separately. The existing
host serves trusted local apps; its frame is not a hostile-code sandbox.

Return page ID, operation, runtime/registry identity, project revision and source
hash, selected build/asset manifest identity, actual command/results, availability,
and whether browser behavior was inspected. For updates/removal include recovery
and candidate paths and readback outcome. Reuse the project
[receipt contract](../../contracts/provenance-and-handoff.md) when recording is in
scope. Source-entry and asset hashes do not establish complete dependency identity,
parameter-to-geometry correctness, export parity or user approval; keep the full
project build receipt and acceptance separate. Page authoring, simulation math,
controls and experiment conclusions remain project-owned.
