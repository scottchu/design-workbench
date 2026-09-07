# Independent preservation validation (V1)

Status: **PASS — accepted path/byte/Git-mode parity and actual isolated recovery readback.** Checked 2026-09-07T03:16:21.978287+00:00. This is the preservation prerequisite for scoped source retirement; final workflow, runtime, history and joined-review gates remain separate.

## Frozen authorities

- Source commit: `71d661c14098860b7a374e13043fb084994be8a0`.
- The original `0868` checkout disappeared before this check. The coordinator recreated the same branch at `/Users/scottchu/Projects/personal/design-projects-workflow-separation`; V1 verified its HEAD and compared its actual index/disk to the frozen source manifest. No new source baseline was substituted.
- Destination: `/Users/scottchu/Projects/personal/sticker-projects`, imported HEAD `dafdb8eb9b0cbc9449dce84a225f2a59f3e3f88b` at check time.
- Original WIP: `/Users/scottchu/.codex/worktrees/3fc3/design-projects`, HEAD `fef4f264d6af6904e8debd99d522ce186bcec49d`; read only. Its status and full-index binary delta were stable before/after checks.

| Frozen destination-relative input | SHA-256 |
| --- | --- |
| `docs/migration/2026-09-06-repository-separation/SOURCE_FILES.sha256` | `afa267e164d926abf21a0fc07a474d3400b27acccc521522cfbe8d66842aa72f` |
| `docs/migration/2026-09-06-repository-separation/SOURCE_INDEX.txt` | `4c8db2f0be160f21271d59b1c1d8a4f9e83a8a3b4011c3a0868f7438fa96543b` |
| `recovery/live-pilot-fef4f264/tracked-delta.patch` | `217a6b03fc4d03d0c465a8faed962f770af7b48b76dd85bdcf45bee3654c4f98` |
| `recovery/live-pilot-fef4f264/untracked-and-ignored.tar` | `3a1326940a91e572792dc4ff7ebf66b8628cad7e8d41007e18b96cbcb87e978e` |
| `recovery/live-pilot-fef4f264/source-project-all-files.sha256` | `712c9245aef52849fa3b03b7eafbaf51631130a88c332252d501b7a89106ba67` |
| `recovery/live-pilot-fef4f264/source-state.txt` | `652a3794110091b1126b17252b772a76bcf7cb3e9972751a2d637b8e859fec54` |
| `recovery/live-pilot-fef4f264/ignored-release-files.sha256` | `a55a9deb7302bec384864c6b1b9d1cc33216ca2e93418c0311e8cd3351ca779f` |
| `recovery/live-pilot-fef4f264/archive-paths.zlist` | `968665dbf3a039da2df995eecccb211e63da2bf5f6a5dce0435f5425641015ca` |

## Results

- **Accepted parity PASS:** 853 paths (848 project files + 5 sticker skill files), 387,650,213 bytes. Every source and destination actual file matches the SHA-256 manifest and Git blob identity; source index matches `SOURCE_INDEX.txt`; imported path/blob/Git-mode tuples equal the source commit. All 853 Git modes are `100644`.
- **Recovery payload PASS:** 186 untracked files total 55,955,458 bytes, plus three explicitly preserved ignored release `.DS_Store` files totaling 24,588 bytes. Every archive payload path, byte sequence and stored POSIX mode matches the original WIP.
- **Archive accounting correction:** the unchanged 56,516,096-byte tar has 378 physical members: 189 payload files and 189 macOS AppleDouble metadata sidecars. Historical wording "189 entries" counts payloads only. Each sidecar maps to an expected payload. Archive bytes were preserved; no repack occurred.
- **Actual isolated restore PASS:** exported the project and sticker-skill trees from `fef4f264`, checked/applied the seven-file binary delta, then extracted the existing recovery tar with macOS `/usr/bin/tar`. All 1,023 restored project files match the complete original WIP path/hash manifest and all five skill files match the original WIP. No real checkout was overlaid.
- **Tracked delta PASS:** exact `git diff --binary --full-index HEAD` equals the preserved patch. Its seven paths are three sticker skill documents plus project `NEXT_AGENT.md`, `PROJECT_STATE.md`, `docs/EXPERIENCE.md`, and `docs/iterations/CURRENT`.
- **Historical checkpoint:** imported baseline contains ten filtered commits; tag `jaelin-v2-anatomy-r1` resolves to `38599e9ba3f382af9bdac13f7c0d6816df84e7fb`. Divergent original `86ce8309edd0dc2d98388cb45a7f9b18b0296763` mapping is owned by I2 and was not accepted by this check.

## Exact execution and evidence

Executed from the Workbench root with its sole uv environment, CPython 3.12.13:

```sh
uv run python .workbench/workflow-ownership/v1/validate.py > .workbench/workflow-ownership/v1/last-run.log
```

The validator used these exact Git operations (explicit `-C` roots as above), plus Python SHA-256/Git-blob and tar readback:

```text
git ls-tree -r -z <source/imported commit> -- projects/jaelin-sticker-pack .agents/skills/sticker-pack-production
git ls-files --stage -- projects/jaelin-sticker-pack .agents/skills/sticker-pack-production
git diff --binary --full-index HEAD -- projects/jaelin-sticker-pack .agents/skills/sticker-pack-production
git archive --format=tar fef4f264d6af6904e8debd99d522ce186bcec49d -- projects/jaelin-sticker-pack .agents/skills/sticker-pack-production
git init -q <isolated-restored-directory>
git -C <isolated-restored-directory> apply --check <absolute-recovery-patch>
git -C <isolated-restored-directory> apply <absolute-recovery-patch>
/usr/bin/tar -xpf <absolute-recovery-tar> -C <isolated-restored-directory>
```

Final script SHA-256: `df19ad208d4b60bd40418cce2fb43d02f34e1f4006c0ab182cb0fe649350b022`. Result SHA-256: `a0a10b5bdd2b8a2c56a1688b66b7bb7d4811f0a080ab906a0507c4adc170ecf8`. Ignored scratch contains the script, frozen-input JSON, full result, and actual restored files at `.workbench/workflow-ownership/v1/restored-verified/`.

## Limits and checker corrections

- This proves project bytes, relative paths, Git file modes and recoverability against the retained source objects/WIP. It is not a clean-machine build, external messaging-platform acceptance, workflow integration review, or proof of complete divergent history.
- Git does not store complete filesystem permissions. The isolated restore has 375 tracked full-POSIX-permission differences (mostly original `0600` versus restored `0644`); executable/type semantics match. Full filesystem metadata preservation is not claimed. Original WIP remains available and untouched; archived payload modes matched exactly.
- Initial checker attempts stopped on the vanished source path and then AppleDouble sidecars. A completed diagnostic run flagged abbreviated-versus-full-index patch headers and full-POSIX-versus-Git mode assumptions. Corrected these check definitions explicitly; the final independent run returned `PASS` with zero errors. No source, destination, or recovery repair was performed.
- V1 owns only this evidence file and ignored scratch. Final delivery must separately verify workflow bindings, destination root configuration, the divergent history map and reviewer findings.
