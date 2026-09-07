# Independent simulator service review

Status: **PASS for the reviewed service/controller/package candidate.** S-R1 and S-R2 are resolved on the repaired identities below. Final packaging independently reads back correctly, with all 67 output entries equal to current declared source bytes. Root live evidence was independently read back as recorded below; browser acceptance remains its separate gate.

Reviewer: `/root/boundary_inventory`, independent of lifecycle implementer `workbench_implementation`, packaging implementer `sticker_migration`, and root live-service acceptance. Review writes only this file. No live lifecycle, Tailscale/configuration, build, authentication or printer command was executed by this reviewer.

## Frozen inspected identities

- `scripts/simulator_service.py`: `83800fc0ed9bf5927e0ba58c3eaaa2c7804ef0d0450cf284a42c6687ff24d935`.
- `apps/simulator/src/lib/server/access.js`: `736b251d5b24105582fa06b96d23a4a2c2d1f962af4646fd68cdec705be43eea`.
- `apps/simulator/src/hooks.server.js`: `25e657bfc37bba0116ddc5f2de2a9630bdd9163d078cf16da0c4fa9e76fdcc0a`.
- `apps/simulator/src/routes/health/+server.js`: `e8d354ec7dbc009080f4f544d50d31efe034dd2c65f90581ef4cb13b544e1dec`.
- Initial service package receipt: `502844e3cfab1fc99c7e43927a66bbb3c2f16a6181896ccd060530de3678b269`, at `.workbench/plugin/service/cad-workbench/PACKAGE_RECEIPT.json`.

## S-R1: verify loaded job ownership, not only current plist bytes (P2)

`Service.loaded()` checks the launchctl-reported plist path and Node executable, then obtains the root, entrypoint and instance identity from the current file on disk. Those bytes are not proof of the already loaded job configuration. The installed plist path and label are shared across checkouts, and the Node executable is commonly identical.

If that standard plist is replaced/edited for checkout B while launchd still runs checkout A, B's `stop`/`uninstall` can treat A as owned and boot it out. No health identity check occurs before `stop`. This contradicts the explicit cross-checkout stop-safety contract.

Require the actual loaded arguments, working directory and instance/environment identity to match this controller's owned root before any stop/replacement. Keep refusing ambiguous/unparseable ownership. Exit gate: a disk plist belonging to this checkout plus a loaded foreign-root job using the same path/Node must reject before any bootout/bootstrap/write; the exact owned loaded job must still pass.

## S-R2: align Python and application origin validation before replacement (P2)

The lifecycle parser accepts origin strings that the HTTP application rejects. Independent direct parser calls demonstrated:

| Input | Python `origin()` | JavaScript `privateOrigin()` |
| --- | --- | --- |
| `https://example.ts.net:443` | accepted unchanged | rejected |
| `https://EXAMPLE.ts.net` | accepted unchanged | rejected |

The application requires exact canonical `URL.origin`, but Python returns the original unnormalized value. `install` may therefore stop an existing healthy owned service, write the accepted invalid configuration and start a server whose hook throws for all requests, including local health.

Use the same exact canonical-origin acceptance rule in both layers before any lifecycle mutation. Exit gate: canonical intended private origin remains accepted; normalization variants rejected by the app are rejected by the controller before bootout/write/bootstrap. No expansion to public origins or arbitrary forwarded headers is requested.

## Checks and scope assessment

- `node --test apps/simulator/tests/access.test.js`: independently **3/3 PASS**. Fixed loopback host/port and one explicitly configured HTTPS ts.net host are accepted; mismatched Origin and spoofed forwarded host are rejected. Tailscale Host preservation still needs actual root HTTPS evidence.
- `uv run python -m unittest discover -s tests -p test_simulator_service.py -v`: independently **10/10 PASS** on the initial candidate, using only fake launchctl/health providers. Existing tests do not cover S-R1's stale loaded-vs-disk identity or S-R2 canonical discrepancies.
- `uv run python scripts/package_plugin.py --check .workbench/plugin/service/cad-workbench`: independently PASS for the initial package.
- Read service BRIEF, lifecycle source/tests/SERVICE.md, access/hooks/health/tests, packaging diff/tests, workflow skill and local-server instructions. Direct Python/Node parser-only invocations established the S-R2 table without any lifecycle command.

Source packaging preserves a single maintained authority and transfers simulator source, npm locks and the lifecycle helper while excluding generated builds, runtime registrations, state, private assets and external printer/slicer providers. No new MCP/dashboard/proxy duplicates Orca. Loopback remains the listener; the helper does not configure Tailscale or kill arbitrary PIDs. Stop and uninstall have deliberately different login-persistence semantics. Package updates must follow the controller repair with a new immutable output and receipt; the initial artifact remains diagnostic history.

## Acceptance join

After controller repair, recheck the focused ownership/origin regressions and regenerate/read back the source package. Root separately records actual production health and instance identity, same-process ensure reuse, owned stop/restart, private port 8454 Serve configuration diff, preservation of every pre-existing route, and absence of Funnel exposure. No reboot/login, other-device or physical acceptance is inferred from source review or a launchd plist.

## Repair re-review and saved live-evidence readback

R reviewed the actual-loaded configuration parser and canonical-origin correction, then independently ran `uv run python -m unittest discover -s tests -p test_simulator_service.py -v`: **12/12 PASS**, exit 0. The new regression refuses stop/uninstall/install before bootout/bootstrap when the disk plist is owned but the loaded arguments, working directory or explicit environment belong elsewhere. The parser distinguishes explicit environment from inherited/default blocks and fails on missing/ambiguous fields. Python rejects explicit default 443, uppercase host/scheme and leading-zero port before constructing an install candidate. S-R1 and S-R2 are closed.

Repaired source SHA-256:

- `scripts/simulator_service.py`: `64c3c56d2cf793a56f18db18a826095c763c7a3630d49b3991ad5d1a61dd2332`.
- `tests/test_simulator_service.py`: `d77d94d9fab08e699c07bab775ee2bb3cac90e35fcd2a8e4762bca7f4795cd07`.
- `apps/simulator/SERVICE.md`: `fdb47e9100a94d92a79f0399ec18fa80e89327bc009cdf01ad055d2eed01e5a6`.

R independently read the root-produced ignored live receipts, without calling live services or launchctl:

- `http.json`, SHA-256 `20b7a1aed0a87a40ac7a1369105940ce677a85f0c7fc2b6a073695575844563c`: private list/selected/health/WASM return 200; WASM has exact expected `f72ce246c02c0e501990837102be383326b153fd761774ebfacce5c80c5ecf26` hash and isolation headers. Unconfigured host, port 443 and cross-origin probes return 403.
- `lifecycle.json`, SHA-256 `12233f5d9631b6f3912e272c0026cbe23340a36f68cdef772972dd5faa668acb`: repeated ensure retains one PID; stop reports no loaded/healthy job while preserving login installation; subsequent ensure starts a new healthy PID with the same owned instance. Root also reports its real `status` passed the repaired loaded-job parser.
- `tailscale-before.json`, SHA-256 `0d8e7d5a0f73c8f52d890d3fac651f123521c47836f8e67a4c3d13986022b3ca`, and `tailscale-after.json`, SHA-256 `3da0d3ef2e35a162238f0aa3f3025364ad1249923d9752bf48359a3a224cd5a6`: a read-only `uv run python -` assertion removed precisely `TCP[8454] = {HTTPS: true}` and the selected host's `Web[:8454]` root handler proxy to `http://127.0.0.1:4179`; the remaining JSON equalled the complete before snapshot. Existing routes and AllowFunnel are therefore unchanged in these saved snapshots. No Funnel permission was added for 8454.

These are independent interpretations of saved root execution evidence, not claims that R performed those live operations. Original rejected controller/package hashes remain above as history. The repaired controller/SERVICE bytes require a new package artifact before final package approval.

## Final package closure

`uv run python scripts/package_plugin.py --check .workbench/plugin/service-final/cad-workbench` independently PASS. A separate standard-library SHA-256 readback compared all 67 receipt source paths to current source bytes: all match. The packaged controller and SERVICE.md match the repaired identities above. No setup/build/install/service action was run from the package by R.

- Final artifact: `.workbench/plugin/service-final/cad-workbench`.
- Receipt SHA-256: `7e9e5376b4d82bb0799357b4f720f6aab756658921aa2821237cc10dc76488ee`.
- Input manifest SHA-256: `64c7abd6fb2775d6a409547fd1c3e9c85faec94b25b2fd10515d28448dcd1144`.

No material review finding remains. Keep source/package, actual managed service, private transport/browser and future login/other-device acceptance separate in delivery records. Later source changes invalidate only their dependent package/service gates.
