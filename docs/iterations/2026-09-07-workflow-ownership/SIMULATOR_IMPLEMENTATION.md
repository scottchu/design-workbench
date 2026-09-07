# I5 local simulator host implementation

Owner: `/root/sticker_migration`, bounded I5 implementation. User steering places
one local SvelteKit simulator host in Workbench; Orca retains its separate
printer/slicer MCP/API/dashboard/widgets. This work does not install a plugin,
MCP, tunnel, background service, or printer endpoint.

## Implemented contract

`apps/simulator/` is an actual SvelteKit application with a discoverable list,
selected simulator view and registered static asset endpoint. External project
source/model logic remains untouched; the host does not implement geometry.
Local CLI registration records exact built asset hashes, selected source hash,
source Git revision and explicit allowlisted asset roots. Ignored runtime config
is `.workbench/simulators.json`; a generic non-executable placeholder example and
setup instructions live with the app. No HTTP registration/write API exists.

Only manifest-listed files within the real registered roots are served, with hash
readback, supported MIME mapping, no-store, COOP/COEP and same-origin headers.
Path traversal, encoded/backslash/hidden paths, symlink escapes, changed source or
asset hashes, unregistered roots/files and unsupported MIME types are rejected.
Dev/start defaults bind 127.0.0.1:4179 and refuse port substitution. Hostnames and
cross-origin requests are checked. CSP forbids remote origin dependencies; no URL
proxy exists. Registered simulator code is trusted local code: the same-origin
frame supports existing workers/downloads and is not a hostile-code sandbox.
Selected-source hashing is not a complete source/dependency build attestation;
retain the external project's complete build/evidence receipt for that claim.

## Exact existing integration

- External checkout: `/Users/scottchu/Projects/personal/design-projects-workflow-separation`.
- Observed Git revision: `b8b0f5d9e38a2b2d1f1f6b07b9ec6f9f283c8565`.
- Source: `projects/laifen-wave-case/openscad/laifen_case_customizer_v1.scad`.
- Source SHA-256: `497098afa555092a0ed85a3a7213cd270852aa76f9001e1478c209cd8469bc42`.
- Built asset root: `/Users/scottchu/Projects/personal/design-projects-workflow-separation/tmp/workbench-laifen-simulator-dist`.
- Registration: `laifen-customizer`; six original built files, served unchanged.
- Local host: `http://127.0.0.1:4179/simulators/laifen-customizer`.
- Dev process started with `npm run dev:simulator`, tool session 57845. Root owns
  this task-specific process handoff; no existing live service was touched.

Read Laifen README, PROJECT_STATE, NEXT_AGENT and active pattern-reference-intake
BRIEF/HANDOFF before build. Used existing root npm dependencies and documented
commands from the external checkout:

```sh
npm run setup:openscad-wasm --workspace laifen-wave-case
npm run build:openscad-simulator --workspace laifen-wave-case -- --outDir /Users/scottchu/Projects/personal/design-projects-workflow-separation/.workbench/laifen-simulator-dist --emptyOutDir
```

The verified official WASM installer completed. The project built 20 modules/six
files with its existing relative base `./`. A chunk-size advisory remains. The
initial new output was moved intact to `tmp/workbench-laifen-simulator-dist`
after discovering external `.workbench` was not ignored; `git check-ignore`
confirms final build output and vendor dependencies are ignored. No source,
project package/lock or existing deployment output was changed. External
`git diff --exit-code -- projects/laifen-wave-case` and project status are clean.
Use that final tmp output path for subsequent isolated builds.

### Built file SHA-256

- `assets/index-glg6xAxA.js`: `a5866ab371b6d46b4916a5bb56e89e810043b5ff1a6a32941b812750d72c0d71`
- `assets/index-iRxz8EXK.css`: `bb0c812317830060d51da5e56d7412a8b911cf75ab6ddc7c68c588e5285ace67`
- `assets/openscad-CutNEzGH.js`: `904a47f29e63afb597bedef747da3b457d8ea17cc793c462c6c8b444e918a62e`
- `assets/openscad-DIKIGOy4.wasm`: `f72ce246c02c0e501990837102be383326b153fd761774ebfacce5c80c5ecf26`
- `assets/openscad.worker-Csx1v_-i.js`: `cf543214d381e56ac230d6853810786ae70c52977d408e64695db595574fd46e`
- `index.html`: `3845efdea8db81003569971cfb2b2594c5c783b0de96dc46323b22204b1ecafa`

## Local implementation verification

From Workbench root:

```sh
npm install
npm run check:simulator
npm run build:simulator
npm run test:simulator
node apps/simulator/scripts/register.mjs --id laifen-check --title 'Laifen registration check' --asset-root /Users/scottchu/Projects/personal/design-projects-workflow-separation/tmp/workbench-laifen-simulator-dist --source-root /Users/scottchu/Projects/personal/design-projects-workflow-separation --source-entry projects/laifen-wave-case/openscad/laifen_case_customizer_v1.scad --config .workbench/simulators-registration-check.json
```

- Svelte check: zero errors and zero warnings.
- Actual client/server production build and adapter-node output: PASS.
- Six focused Node tests: 6/6 PASS. Coverage includes real file readback and
  MIME/hash, traversal/hidden/encoded paths, root/ID allowlist, symlink escape,
  source/output drift and unlisted files. Test fixtures are generic OS-temp files.
- Registration CLI: actual six-file external output registered into separate
  ignored check config; runtime live config unchanged.
- HTTP GET list: 200. WASM HEAD: 200, application/wasm, expected SHA ETag,
  COOP same-origin and COEP require-corp. Encoded traversal request: 404.
- `git diff --check`: PASS. Host `.svelte-kit`/build and local config are ignored.
- `npm audit --json`: exit 1 with three low-severity entries from cookie and
  transitive SvelteKit/adapter attribution (GHSA-pxg6-pf52-xh8x). No automatic
  downgrade/force-fix. No authentication or cookie-writing feature was added.

Versions are explicit in workspace package.json/root package-lock: SvelteKit
2.70.3, Svelte 5.57.0, Vite 8.2.2, adapter-node 5.5.7. npm remains the only JS
package manager. Application routing/build uses supported SvelteKit interfaces;
upstream reference: https://svelte.dev/docs/kit/adapter-node.

## Independent acceptance handoff

Root/V3 must inspect the actual browser list, selected tool, WASM generation,
parameter change and current STL download before claiming that interactive path
passed through this host. Existing Laifen source history is not new host-browser
acceptance. No new geometry/physical/slicer/printer acceptance is asserted here.
All external project source remains authoritative. No commits/push/deployment or
changes to existing Tailscale/services/printers were performed by I5.

## R2-1 focused repair

The initial registry joined all filesystem/source checks in one rejection domain.
Per R2, source/root failures are now scoped to each registration. The index keeps
unavailable entries visible with a reason alongside healthy cards; selection of an
unavailable entry fails closed, and its asset reads remain blocked. Global schema
and duplicate-ID ambiguity still reject the whole registry. The registration CLI
requires the newly added entry to be available without requiring stale siblings
to recover first. No hash or path validation was relaxed.

`npm run test:simulator`: 8/8 PASS after repair. New two-entry regression changes
A's source then removes A's asset root: A stays listed as unavailable and cannot
serve assets, while B remains listed and readable. A second regression invokes the
actual registration CLI to add C while A remains stale and B healthy. The prior
security and drift tests also pass. No live registry/project source was changed.
Per root coordination, no build/check was run during its browser session; root
will stop the dev server before final check/build/restart and independent review.
