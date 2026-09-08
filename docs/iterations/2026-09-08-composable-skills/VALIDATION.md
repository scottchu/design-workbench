# Composable skills: local source validation

Date: 2026-09-08. Working directory for all commands below:
`/Users/scottchu/Projects/personal/CAD-workbench-next`, branch
`codex/composable-skills`, base Git revision `d92816a`. Inputs include uncommitted
source; exact packaged bytes are identified by the manifest below.

## Final candidate commands and results

| Command | Observed result |
| --- | --- |
| `uv run python /Users/scottchu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/simulator-server` | PASS |
| `uv run python /Users/scottchu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/simulator-page` | PASS |
| `uv run python /Users/scottchu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/workbench-flow` | PASS |
| `uv run python scripts/check_registry.py` | PASS: 12 capabilities, 2 mapped recipes, references and policy hashes |
| `uv run python -m unittest discover -s tests -p 'test_package_plugin.py' -v` | 8 pass |
| `uv run python -m unittest discover -s tests -p 'test_registry.py' -v` | 4 pass |
| `uv run python scripts/package_plugin.py --output .workbench/composable-skills/candidate-2/cad-workbench` | PASS: actual output built and read back |
| `uv run python scripts/package_plugin.py --check .workbench/composable-skills/candidate-2/cad-workbench` | PASS |

Final candidate directory: `.workbench/composable-skills/candidate-2/cad-workbench`.
70 source/output file pairs are bound in its receipt. Discovery inventory:
`design-reflection`, `simulator-page`, `simulator-server`,
`sticker-pack-production`, `workbench-flow`.

| Identity | SHA-256 |
| --- | --- |
| `catalog/POLICY.sha256` | `481715af7dfd845b581892f2bb46f7b6a4e383e21459c68f9300a6b23425610a` |
| `PACKAGE_INPUTS.sha256` | `af80c4422e9a47bb2b048e7223dcd14db39ba36de2827eb2cf99120f21a439f3` |
| `PACKAGE_RECEIPT.json` | `40cfe52e4db95a817dc5b0daaa4a03e1f6f3851979a64100fddccf2333e1485a` |

Candidate 1 was an earlier passing package before the final status/interpreter
clarification. Candidate 2 supersedes it; both ignored outputs were preserved.
Independent forward-test commands and exact fixture identities are recorded in
[REVIEW.md](REVIEW.md). No new production script or application behavior was added;
existing package/registry checks and actual fixture operations target the credible
failures for this extraction. No new geometry or application UI claim requires
CAD generation or Svelte rebuild here.

## Limits

This verifies local source structure, package containment/readback and isolated
page operations. It does not install five skills in Codex, execute the new skills
against the live service, test browser rendering, prove CAD/export parity, verify
phone/reboot behavior or complete a portable fabrication/sticker recipe. No
runtime configuration, installed plugin, external project or consumer binding was
changed. Release version selection and remote PR delivery remain separate.
