# F0-R formal independent review

Date: 2026-09-06 America/Toronto.
Owner: `foundation_review`, independent of implementation and validation.
Disposition: **ACCEPT** the frozen foundation candidate for continuity reconciliation and the authorized local source commit. No finding was identified at blocking, major, moderate or minor severity.

## Reviewed identity and method

Repository: `/Users/scottchu/Projects/personal/CAD-workbench`. Candidate manifest: `docs/iterations/2026-09-06-foundation/CANDIDATE.sha256`, SHA-256 `7b1ca058152b370f5e8226fc7a2642bd0990fe167150adec24129340eeed9b62`. All 13 manifest entries verified at the start and end of review. The separately frozen documentation also matched the supplied identities: README `31febbf0c66fea96c7fe365a85ea74fb02d48a38e016153c1cdddc0b6f5d4093`, architecture `f2713502c17480637cec9d3d141c34eebb31a5cc0e9b5d8b485f1cb7944f73b1`, and roadmap `c06d469bd13fc3cf59264c9abd58508560293c742a62c42f62905f09c8a88bbb`.

The review inspected AGENTS, README, architecture, roadmap, decision 0001, the active brief, toolchain/workspace configuration and locks, fixture, doctor, smoke command and focused tests. It joined the independent F0-V record at `docs/iterations/2026-09-06-foundation/VALIDATION.md`, SHA-256 `7f52743b75ef2611a1d478d7bb4392c0a995a2037b4ba7454a039ec195bf9468`. F0-R did not duplicate F0-V's install, CAD generation, STEP inspection or snapshot suite.

Decisive reviewer commands, run from the repository root, were:

```sh
shasum -a 256 docs/iterations/2026-09-06-foundation/CANDIDATE.sha256
shasum -a 256 -c docs/iterations/2026-09-06-foundation/CANDIDATE.sha256
shasum -a 256 README.md docs/architecture.md docs/roadmap.md docs/iterations/2026-09-06-foundation/BRIEF.md
shasum -a 256 docs/iterations/2026-09-06-foundation/VALIDATION.md
/opt/homebrew/bin/rg -n 'name = "(cadgen|build123d|cadquery-ocp|playwright)"|version = "0\.5\.0"|requires-python|resolution-markers' uv.lock
```

Each command returned exit 0. The manifest check reported all 13 entries `OK`; the supplied candidate and documentation hashes matched. Source inspection used bounded `sed` reads and explicit Homebrew `rg` searches.

## Review conclusions

- Scope and ownership are coherent. CAD Workbench owns reusable software and generic fixtures while actual designs, design evidence and physical observations remain external. The candidate introduces no editor UI, slicer/printer integration, remote deployment, plugin registration, persistent Viewer service or project migration.
- The toolchain contract is internally consistent. asdf pins Node.js 26.7.0, Bun 1.4.0 and uv 0.12.5. `.python-version` selects uv-managed CPython 3.12.13 as the documented exception, uv owns the sole root `.venv` and lock, and npm remains the only JavaScript package manager with one root lock. The doctor deliberately enforces Python 3.12, the root environment and cadgen 0.5.0; exact selected tool versions remain the responsibility of the committed pins and setup step, as decision 0001 specifies.
- The smoke command exercises the intended runtime rather than a mock. It calls the frozen cadgen fixture, reopens the written STEP through the installed kernel, and rejects invalid geometry, an incorrect solid count, wrong bounds or wrong material volume. Its receipt identifies source, command, runtime, execution environment, written artifact and measurements while keeping slicer and physical states unaccepted.
- Requested snapshot behavior is truthful. Success identifies the generated image and retains the need for visual review; a requested failure leaves `ok: false` and `snapshot: failed`. Normal CAD readback does not require a browser or persistent Viewer.
- Documentation describes implemented foundation behavior separately from roadmap intent. The architecture retains source/parameter authority, artifact identity and distinct CAD, preparation and physical evidence boundaries.

F0-V independently confirmed the setup commands on the existing host, doctor result, five focused tests, a newly built valid one-solid 20 x 12 x 6 mm STEP, expected volume `1364.6017763138423` mm³, centered full-height radius-2 bore, CLI geometry validation, same-STEP snapshot generation and visual review. Its injected generation-error, missing-export and requested-snapshot-error cases each returned exit 1, wrote `ok: false`, and replaced an older green receipt. This closes the foundation's install, actual-artifact and failure-receipt gates without relying on the source reviewer's judgment alone.

## Requirement coverage and limits

Decision 0001 contracts 1 through 7 are covered by the frozen source review plus F0-V evidence. The accepted result is an existing-host foundation check. It does not establish clean-machine bootstrap behavior, concurrent-job handling, interactive Viewer behavior, editor functionality, slicing, printer operation, manufacturing suitability or physical fit. The snapshot supports visible appearance; the independent solid intersection and point probes establish the through-hole. Ignored `.workbench/` artifacts and their hashes identify one validation run and may be replaced by later runs.

No source repair cycle was required. F0-R changed only this review record and made no source, configuration, environment, external-repository, remote or commit change.
