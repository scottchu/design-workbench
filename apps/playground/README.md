# Local project playground

Playground is the shared project exploration/review application. Its current
implementation lists explicitly registered external simulators and opens
an existing built app in a full-height frame. It serves the original bytes; no
project geometry, parameter logic, sources or design assets are copied here.
Printer/slicer MCP/API/dashboard/widgets remain in Orca. Optional private
Tailscale Serve access forwards one explicitly selected HTTPS port to this host. Only trusted local simulator code should be registered:
the same-origin frame is compatibility isolation, not a hostile-code sandbox.

From Workbench root:

```sh
npm ci
npm run check:playground
npm run test:playground
npm run build:playground
npm run dev:playground
```

Open http://127.0.0.1:4179/. The default dev/start commands bind only loopback;
strictPort avoids silently selecting another port. Development uses the foreground
Vite process. For normal plugin use, build once and use the managed production
server described in [SERVICE.md](SERVICE.md). The launcher supports lazy ensure/open
and an explicitly installed macOS user LaunchAgent for login persistence.

## Naming and compatibility

Source lives at `apps/playground`, workspace `@design-workbench/playground`.
Canonical root scripts are `dev:playground`, `check:playground`,
`test:playground` and `build:playground`; the old `*:simulator` scripts remain
forwarding aliases. Existing `/simulators/<id>` and `/assets/<id>/...` URLs,
registry schema, environment keys and service identity remain stable. Renaming the
host does not add generic image-review features or change project simulation logic.

## Register an existing project

Read its active project records, then run its documented build from its own root,
using its own runtime. Build with relative asset URLs (`base: './'` for Vite) into
an ignored directory in that project. Root-absolute asset URLs require the
project's supported build-base override; this host never rewrites HTML or proxies
an arbitrary URL. Preserve prior releases and services.

Run the explicit registration utility from Workbench root:

```sh
node apps/playground/scripts/register.mjs \
  --id example --title 'Example simulator' \
  --asset-root /absolute/project/tmp/simulator-dist \
  --source-root /absolute/project \
  --source-entry relative/path/to/authoritative/source.scad
```

This writes ignored `.workbench/simulators.json`; [config.example.json](config.example.json)
shows its shape but its placeholder hashes intentionally cannot pass validation.
The CLI records all built asset hashes and the selected source hash plus observed
Git revision. It refuses duplicate IDs and symlinks; updating a registration is an
explicit local edit/re-registration after review. A source hash identifies that
entrypoint, not a complete dependency/build-proof contract. Preserve a project's
full build receipt separately. Host display does not establish project acceptance.

Optional `--entrypoint`, `--description`, `--config` select local values. Set
`WORKBENCH_SIMULATORS` to an absolute registry file for a different local catalog.
Without it, npm workspace commands resolve the root `.workbench/simulators.json`.
No registration or filesystem-write API is exposed over HTTP.

Every served file must belong to the exact allowlisted built root and its manifest,
retain its hash, and have a supported MIME type. Traversal, hidden paths, symlink
escapes, changed bytes, unsupported file types and unregistered requests fail.
The source entry hash is rechecked on each request. A missing/changed source or
asset root marks only that simulator unavailable, with its reason on the list.
Healthy simulators remain accessible, and the CLI can add another valid entry.
The unavailable entry cannot serve its old assets. Malformed global schema or
duplicate IDs still reject the registry because ownership is ambiguous.
WASM uses application/wasm;
COOP/COEP and same-origin resource headers support browser workers. Asset CSP
permits local/blob execution and downloads, but no remote origin dependencies.
This does not execute source on the server or infer physical acceptance.

## Current integration evidence

The workflow-ownership iteration's SIMULATOR_IMPLEMENTATION.md records the exact
Laifen OpenSCAD WASM source/build registration and validation limits. Its current
local registration is ignored machine-specific state, not a bundled private fixture.

## Optional private access

The server always listens on loopback. `WORKBENCH_ALLOWED_ORIGIN` can allow one
exact HTTPS `*.ts.net` origin, including its selected port. Requests must carry the
matching Host and, when present, browser Origin. Other hosts, origins and forwarded
host spoofing fail closed. The setting grants no public access by itself. Configure
Tailscale Serve separately; do not use Funnel for a private endpoint. Inspect
existing Serve settings and preserve unrelated routes. All users permitted by the
tailnet access policy can reach this endpoint; no additional app login is added.

The identified `/health` endpoint supports launcher readiness and reuse. It proves
server identity, not that every registered external simulator is available.
