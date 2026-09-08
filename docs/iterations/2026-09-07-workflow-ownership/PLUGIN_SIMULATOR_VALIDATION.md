# Independent plugin and simulator validation (V3)

Status: **PASS for package integrity, read-only workflow behavior, simulator static/build checks and HTTP asset readback.** Root owns the separate browser generation/parameter-change/download acceptance. This record does not claim that browser gate, provider execution, installation or physical acceptance.

## Package acceptance

Independently ran from Workbench root:

```sh
uv run python scripts/package_plugin.py --check .workbench/plugin/cad-workbench
uv run python -m unittest discover -s tests -p test_package_plugin.py -v
```

Readback PASS; five focused tests PASS (relocated package, tampered output, missing support file, escaping input symlink, existing-output preservation). Separate Python hashlib readback compared every actual output file to the recorded SHA-256 and its current authoritative source: **44 copied files / 46 total package files PASS**. All **46 declared inputs**, including builder and scope addendum, still match their manifest. No unexpected output files, app/server code, project assets, environments or legacy viewer service were found. Plugin metadata exposes skills only; no own MCP/apps/hooks registration exists.

- Package input manifest SHA-256: `0b0d0871fd4f9a1484d34422562b42b95ab8e98f1bf0363ee7570f8178e12d1e`.
- Package receipt SHA-256: `082ea1c85522e44417a2c4b6d568e2dd32c7e707226949891dbef7cde3f016ca`.
- Packaged policy manifest SHA-256: `c09d963068ba69107adaf16aa550a4039fcd6d91bbf10c8c1988ab428e0e3e55`.

Both actual project bindings still identify migration provider `36f41715ee2257c0f2e41e40329216e3d2b2747f` and original policy SHA `6f1ab6580b67cd9e58dd2302f07cdc65a3a2bfa2213e650139a7ce4542bf9536`; packaging has not silently upgraded those accepted consumers.

## Read-only behavioral scenarios

The validator read the actual packaged/source workbench-flow instructions and provider table, applied the following fictional user requests and availability facts, and assessed the resulting route. These are explicit independent instruction walkthroughs, not mocked live provider execution or a claim of installed-plugin behavior. No tools were invoked against a slicer, printer, image generator or external service.

| Fictional input and provider facts | Applied result | Disposition |
| --- | --- | --- |
| “Prepare this exact mesh only”; supported external preparation provider exists with explicit slicer/profile/tool mapping | Resolve mesh/source hash and runtime, prepare and statically validate through that provider; finish with identified G-code/evidence. No upload/start/monitor operation is authorized by preparation. | PASS |
| “Observe current printer/camera only”; read-only observation exists while CAD build is failing | Use only independently available fresh read-only observation/camera; CAD failure does not block that scope or grant control. Snapshot provenance and current telemetry are required. | PASS |
| “Start this exact validated G-code”; current callable inventory contains only observe_printer/open_printer_camera | Report actual operations provider unavailable. An installed start skill, source README or catalog entry is insufficient. Do not invent an endpoint, generic HTTP request, G-code relay, plugin installation or fallback control. Independent authorized work may continue. | PASS |
| “Start artifact A with SHA A”; actual supported operations provider and external authorized-start workflow are available | Resolve that workflow/provider identity and current target, verify artifact A/hash and fresh preflight. Only the explicitly authorized exact artifact may proceed under its workflow; no control executed in this walkthrough. | PASS |
| Same authorization for A, but a newly generated artifact B/hash B replaces the candidate | A's authorization does not transfer to B. Resolve fresh exact-artifact authority before a start; neither shared context nor preparation success permits substitution. | PASS |

The package remains thin guidance. Actual provider availability/version and runtime correctness must be established per invocation. A CAD/U1 skill folder does not establish a running interface. Acceptance layers remain distinct: source/CAD, written artifact/slicer, physical acceptance, machine audit, independent human judgment and user intent.

## Simulator independent checks

Executed sequentially at Workbench root:

```sh
npm run check:simulator
npm run build:simulator
npm run test:simulator
```

- Svelte check: **0 errors, 0 warnings**.
- Real SvelteKit client/server build plus adapter-node output: **PASS**. Generated empty `chunks/env.js` notice is nonfatal.
- Node tests: **6/6 PASS**, including exact MIME/hash file readback, path encodings/traversal/hidden paths, root/ID restrictions, symlink escapes, changed source/artifacts, unlisted files and unsupported MIME.
- No service was started or stopped by V3. Existing root-owned loopback dev server was used for HTTP-only checks.

Independent Python urllib requests fetched all six registered Laifen assets and SHA-256 compared actual HTTP response bodies against registration values; all matched, totaling **10,311,618 bytes**. Files were 562,016-byte JS, 7,133-byte CSS, 124,567-byte OpenSCAD JS, 9,603,115-byte WASM, 1,823-byte worker and 12,964-byte HTML. Every response had the expected ETag, no-store, COOP same-origin, COEP require-corp and nosniff. WASM MIME was application/wasm.

| HTTP check on existing 127.0.0.1:4179 | Observed |
| --- | --- |
| GET / | 200 |
| GET /simulators/laifen-customizer | 200 |
| GET each of six manifest-listed assets | 200; byte hashes match |
| Encoded traversal /assets/laifen-customizer/%2e%2e/AGENTS.md | 404 |
| Unlisted asset | 404 |
| Origin: https://example.invalid | 403 |
| Host: example.invalid | 403 |

The local frame serves explicitly trusted registered code; it is not a hostile-code sandbox. Registration hashes a selected source entrypoint and exact built assets, not a complete dependency/build attestation. App/provider API ownership remains separated from Orca's printer/slicer MCP/dashboard/widgets.

## Concurrent dev/build limitation

The production build updated `.svelte-kit/output/server/index.js` at `2026-09-07T03:39:23.135Z` and adapter output at `03:39:24.187Z`. Root subsequently reported a SvelteKit/Vite “An impossible situation occurred” error during browser WASM compilation. Shared `.svelte-kit` output being rewritten by check/build while dev is running is a plausible cause, not established by this validator. V3 immediately stopped further build/check calls and notified root; root owns restarting the dev process and repeating the actual browser gate. Run check/build before starting the review dev session. The earlier HTTP readback is evidence of served bytes, not browser execution recovery.

## Limits

No external project source/configuration, registration, live service or printer was mutated. Focused tests generated only their existing temporary fixtures and normal ignored app build outputs. No new dependency or plugin installation occurred. Existing dependency advisories from implementation are not resolved by this gate. Runtime skill dispatch, start/preparation operations, actual browser generation/export and CAD/physical/platform acceptance require their separately scoped evidence. V1/V2 preservation and original migration provider acceptance remain unchanged.

## Frozen V3 source identities

The following SHA-256 values bind the source/configuration read for this gate. App rows reflect the final independently checked R2-1 repair below; package rows remain the previously accepted unchanged inputs. Package output identities above additionally bind all packaged files.

| Repository-relative file | SHA-256 |
| --- | --- |
| `scripts/package_plugin.py` | `44f5795944ee8ed88e47be32be41c982f9cebc50dc8fa88fc76dadb1bc38375d` |
| `tests/test_package_plugin.py` | `37a0f0e040a21ddc70427193a7b67d9853a6bd853af5d814f10fce272765242f` |
| `packaging/cad-workbench/.codex-plugin/plugin.json` | `607f9e3a5d52da651fd88a33b769692e0143eaa5ab121f89cec2c5d02fba80d7` |
| `packaging/README.md` | `c0b86d578cca3dbff1a1fb76c97e5ea08a68e40a8dda6c58a4c117d22bb9609e` |
| `skills/workbench-flow/SKILL.md` | `e52280da70eea94d4c784c09e756d0dbd60f49e2dd17df134924eaab7ccf68e2` |
| `skills/workbench-flow/references/providers.md` | `823927e82af0f7d176203dcc2acdbe673d710feda8f25ceb4ca2805f9085d9c7` |
| `catalog/POLICY.sha256` | `c09d963068ba69107adaf16aa550a4039fcd6d91bbf10c8c1988ab428e0e3e55` |
| `package.json` | `4b81bfe8353c0c42c8c3c08abb06df79e24b9e714feaaf0a1dcefeceece6c9de` |
| `package-lock.json` | `b2873f5c4b62292365f6775a50c782a561abef370aee6d83aa95ebafce325187` |
| `apps/simulator/.gitignore` | `4aebbec05edaf48712508f9a0f5e0ebd3a85e5f8d334b783bdbbb31539bf6295` |
| `apps/simulator/README.md` | `21d4b7ad443d605b19a37927131f3a6875e3de05ca79985c4ce98ea01181a313` |
| `apps/simulator/config.example.json` | `ae5f8caa066d28afcf4ece02eba248655623a43f321dcd89d074a44dbd1e5833` |
| `apps/simulator/jsconfig.json` | `05f1d86a0443f26a6566794cebd4cc3fbced260803bf77c16ade2c77cdd443f6` |
| `apps/simulator/package.json` | `9f6e57032aa878c6846fde0bd691854729aeab775814a33e597e415a2ea85fe3` |
| `apps/simulator/scripts/register.mjs` | `31a0c0b8052eadbcc6fd7963ebc328943a6a3b24cfc007d453f384e062a2e8dc` |
| `apps/simulator/src/app.html` | `766f0dee89ebce227fdde18cf421fc19abcaee8f2361d9b842c79acc37148215` |
| `apps/simulator/src/hooks.server.js` | `399c4bdd65876cc0313ddd82c9d921b1010f853e791009372181e5ce6c880015` |
| `apps/simulator/src/lib/server/registry.js` | `9b1bbd3b991ee085361791def721187e599caa6a7eafa9a72c9b60946ea488d7` |
| `apps/simulator/src/routes/+page.server.js` | `3c358a3e8ba9fdf0255e02c575f0bef44c1953bbf047433d7e87010db6b099e1` |
| `apps/simulator/src/routes/+page.svelte` | `ccfd2ceddf285561cbf829631625d8da017668a5ba08787c5dac58a0c59bcd49` |
| `apps/simulator/src/routes/assets/[id]/[...asset]/+server.js` | `5a3b18383614b1f82a0f1bb08af53b05f1d66ab2a4dafd834a973ca20aeb1543` |
| `apps/simulator/src/routes/simulators/[id]/+page.server.js` | `41646dc7b52e2a445fd33f6c7a241c8cbbee0781d08776fda7c8463a4aa958f1` |
| `apps/simulator/src/routes/simulators/[id]/+page.svelte` | `74c7ee4fe22d9386c220131f9a2c2ef862abddeefd99609c85a14c3375956d98` |
| `apps/simulator/svelte.config.js` | `5a870ce9c08f6d87a9f12bdbc69ce9d870ee158e23d9ff36f0b73939d4e499c0` |
| `apps/simulator/tests/registry.test.js` | `b192f8fdd77477d6d3d63f19b11336311b0d139bdebf2692ca5a8acbdfb2053a` |
| `apps/simulator/vite.config.js` | `001dd122d02f2e5d5eff1d483d002073ea90f31f48aafffe5127d4a6cee9d5b7` |

Recorded UTC: 2026-09-07T03:41:51.413726+00:00.

## Final simulator repair acceptance (R2-1)

**PASS.** After root confirmed its dev process stopped (session 88310, exit 130), V3 independently repeated the exact sequential commands `npm run check:simulator`, `npm run build:simulator`, and `npm run test:simulator` from the Workbench root. Svelte reported **0 errors / 0 warnings**; real client/server production build and adapter-node output passed; **8/8 tests passed** in 79.845 ms. Root was immediately notified that build/check were complete and that dev restart was safe. V3 performs no further build or check while root's review server runs.

The two new regressions demonstrate entry-scoped failure: changed source or missing asset root makes A visible as unavailable and blocks its asset reads while healthy B remains listed/readable. An actual CLI invocation adds healthy C alongside stale A without requiring A's recovery. Global duplicate identity/schema ambiguity still rejects the registry; existing path, hash, unsupported-MIME and symlink checks remain active. Source review confirmed the list retains unavailable cards, unavailable selection fails closed, and registration requires the new entry to be available. No authoritative source or live registration was modified by V3.

This final eight-test result supersedes the earlier six-test app candidate; the earlier HTTP readback remains explicitly a pre-repair HTTP observation. Unchanged package checks were reused without repetition. Root separately reported successful browser generation and download with the 180 mm parameter and measured artifact differences; exact browser hashes/measurements belong to ROOT_BROWSER_ACCEPTANCE.md, not this independent static/build record. V3 does not promote a delegated browser report into its own direct observation.

Final repair five-file identity manifest SHA-256: `9296543e6553d8899c8434d97590bc16c6898bd204676fa0e79a4bd32e9bfc05`. The corresponding file hashes appear in the source table above.
Final repair validation UTC: 2026-09-07T03:45:01.512258+00:00.
