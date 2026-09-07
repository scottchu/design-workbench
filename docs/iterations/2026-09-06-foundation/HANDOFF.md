# Foundation handoff

Updated: 2026-09-06. Status: foundation implementation, independent validation and formal review complete/pass. Resolve the local delivery commit with `git log -1` on `setup/foundation`; source identity is also recorded in the immutable candidate manifest.

## Baseline and ownership

Started from the user's empty local `CAD-workbench` Git repository with no remote. Work is on `setup/foundation`. F0-D authored the foundation contract and documentation; F0-I implemented the workspace and developer tools; F0-V independently validates the candidate; F0-R independently reviews it; root coordinates and maintains these state indexes. No existing design/tool repository was changed.

The user's asdf steering deliberately revised the initial contract. The final decision file is covered by `CANDIDATE.sha256`. That manifest covers source, tests, configuration, locks, AGENTS.md and decision 0001. Mutable status/evidence records and general explanatory documentation are outside the runtime-validation fingerprint; the reviewer checks documentation separately.

## Implemented and observed

- asdf pins Node.js 26.7.0, Bun 1.4.0 and uv 0.12.5. The current host had those tools but no asdf Python installed; uv manages pinned CPython 3.12.13 and the root `.venv`.
- Runtime lock includes cadgen 0.5.0, build123d 0.11.1, cadquery-ocp 7.9.3.1.1 and Playwright 1.62.0.
- Developer commands: `uv sync --all-packages --all-groups`, `npm install`, `uv run python scripts/doctor.py`, `uv run python -m unittest discover -s tests -v`, `uv run python scripts/cad_smoke.py`, `uv run python -m playwright install chromium`, and `uv run python scripts/cad_smoke.py --snapshot` all returned success in implementation verification.
- Written STEP measured one valid solid, dimensions 20 x 12 x 6 mm, volume 1364.6017763138423 mm3. Source fixture SHA-256: `67d1f40285d0dfe9a8eb32e9923317021078325e523df10d7ca7dd2d114e6a2d`.
- Initial STEP SHA-256: `e7530afc078c861deeca26da07661b130e4cebdc9a05baec6072385af652b281`. Initial snapshot SHA-256: `5389a414e6623402adf2a4af45dd71542754c7c7f9b607a145b21c8a38851c8c`. Independent receipts supersede these if their own generated outputs differ.
- Artifacts and JSON receipt live in ignored `.workbench/smoke/`; cache is isolated in `.workbench/cache`. CAD smoke uses transient bounded workers, with no persistent Viewer launch.

## Acceptance and limitations

F0-V independently passed existing-host setup, doctor, five focused unit tests, actual STEP generation/readback, a centered through-hole geometry check, and snapshot visual inspection. Three injected software failure paths replaced prior successful receipts with explicit failures. F0-R joined that evidence with source/configuration/documentation review and accepted the foundation without findings or source repair cycles.

Final candidate manifest SHA-256: `7b1ca058152b370f5e8226fc7a2642bd0990fe167150adec24129340eeed9b62`; all 13 declared files verified unchanged. `VALIDATION.md` SHA-256: `7f52743b75ef2611a1d478d7bb4392c0a995a2037b4ba7454a039ec195bf9468`. `REVIEW.md` SHA-256: `128c9184ff97a611b48db9e45da4f0710baa40617f25242ab654d67d7756ff0c`. These independent records preserve exact commands, artifact identities and bounded conclusions. Snapshot visual inspection showed the intended plate and central opening with no visible rendering error; the through-hole conclusion comes from geometry.

This was an existing-host check, not a clean-machine bootstrap test. Concurrent invocation and interactive Viewer behavior were not evaluated. This generic fixture establishes a software foundation only; slicer and physical acceptance remain untested.

No editor UI, real-project integration, slicing, printer operations, Workbench plugin, upstream fork, remote publication or repository migration was delivered. Next action: start the bounded Laifen integration milestone under a new iteration and freshly inspected design baseline.

## Publication follow-up

After foundation delivery, the user explicitly requested a private GitHub repository and a push. Root ran `gh repo create scottchu/CAD-workbench --private --source=. --remote=origin`, verified `isPrivate: true`, and ran `git push -u origin setup/foundation`. `git ls-remote origin refs/heads/setup/foundation` confirmed foundation commit `4dcf9deb7cfddd9ea27889efb82bf7c52a5e3a42` on GitHub. Remote: `git@github.com:scottchu/CAD-workbench.git`. GitHub's initial default branch is `setup/foundation`; no `main` or PR merge was created. This follow-up changes publication/status records only; the validated candidate files and acceptance evidence remain unchanged.
