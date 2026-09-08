# Independent playground rename review

Date: 2026-09-08. Reviewer: `review_skills`. Reviewed the iteration BRIEF,
workspace/lock diffs, package builder mapping/validation, service controller and
bounded lifecycle tests, service compatibility documentation, and focused skills.
Only this record and ignored scratch were written. No live lifecycle, binding,
registry, browser, network or external project operation was used.

## Results

Workspace naming is consistent: `apps/playground/package.json` identifies
`@design-workbench/playground`, the lock entry and workspace symlink target match,
and all four original simulator npm commands route to their playground aliases.
The source package map, required-file validation and component source-file inventory
all select `apps/playground`; historical simulator receipt/service identity names
remain compatibility identifiers, not references to missing source files.

The controller accepts only new or legacy build paths beneath the same canonical
root, preserving the existing label, instance derivation and exact loaded
program/arguments/environment verification. Main routes ensure/start/open through
`desired(..., reuse=True)` and installation through the new-entry default. A missing
saved legacy build fails before mutation rather than falling forward to the new
build. Explicit installation still verifies loaded and saved ownership before
stopping or changing configuration. Status does not select a new entrypoint.

Read the implementing agent's tests for healthy legacy status/reuse, explicit
new-build installation, missing saved legacy build and foreign legacy ownership.
The implementing agent owns the complete Python/Svelte/build/package runs; this
review does not claim those runs independently.

## Independent executable probes

Command, run from `/Users/scottchu/Projects/personal/CAD-workbench-next`:

```sh
uv run python .workbench/review-playground/probe.py
```

Exit 0, with four PASS results:

- `lazy_legacy_restart`: create isolated legacy installed configuration using the
  bounded fake launchctl/health fixture; stop its fake job; resolve desired with
  reuse and ensure. The saved legacy entrypoint and exact configuration survive.
- `missing_new_install`: with a verified legacy fake service, remove the new build
  fixture. Preparing explicit installation fails `built server missing`; existing
  plist bytes survive and no bootstrap/bootout occurs.
- `foreign_explicit_install`: alter the loaded fake entrypoint to another root's
  legacy path while preserving owned disk configuration. Explicit installation
  rejects the loaded mismatch, preserving plist bytes and performing no mutation.
- `workspace lock names paths aliases`: assert current workspace name and lock
  link equality, old lock workspace absence, and all four alias chains.

The probe imports the existing fake fixture through an explicit local module path;
its Service calls inject fake launchctl, health and port functions. The actual
service CLI is never invoked. Temporary roots are cleaned by the fixture.

Scratch runner SHA-256, measured using
`shasum -a 256 .workbench/review-playground/probe.py`:
`746946aef5e654bf8c363e34924031d9ecd1a1a76998f42aa1204e4bd8eb78bb`.

## Finding

The first page-skill revision described legacy fallback for registration CLI and
service docs but left the update/remove registry-module import as a literal
`apps/playground/src/lib/server/registry.js`. Requested one resolved app root
for all runtime tools and registry imports, so a current skill can still operate
against an older bound runtime without upgrading it. Final disposition follows.

This verifies source compatibility and fake transition behavior only. It does not
establish actual service update/reuse, installation, browser appearance or page
availability, and does not authorize them.

## Final disposition

Reread the final page skill: it now resolves one complete runtime app root by
checking both CLI and registry module, uses that root for documents, commands and
imports, and fails incomplete prerequisites without mixing revisions. Finding
resolved. Root ignore rules also explicitly retain legacy `build/` and
`.svelte-kit/` as generated output after the source directory rename; they do not
move or remove those artifacts. `git diff --check` exited 0.

No remaining blocking finding within this source-rename and compatibility scope.
Live runtime acceptance remains separately scoped and unperformed here.
