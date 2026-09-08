# I4 plugin implementation receipt

Owner: workbench_implementation. Candidate packaging only; no commits, marketplace registration, installation, own MCP server, provider network/printer calls or changes to old skill/policy source bytes. Original project migration bindings remain at `36f41715ee2257c0f2e41e40329216e3d2b2747f`.

## Authoritative source

- `packaging/cad-workbench/.codex-plugin/plugin.json`: plugin metadata, generated initially with bundled plugin scaffold then refined.
- `scripts/package_plugin.py`: explicit allowlisted package assembly, symlink/path checks, source stability checks, output readback and receipt.
- `skills/workbench-flow/SKILL.md` and `references/providers.md`: thin provider-aware flow; old two skills are reused unchanged.
- `packaging/README.md`: source/build/runtime boundaries.
- `tests/test_package_plugin.py`: five focused packaging tests.
- `catalog/POLICY.sha256`: refreshed only to add the new skill references. No silent upgrade of original source/sticker bindings.

The package copies existing authoritative policies, catalog, contracts and templates with relative paths intact. It contains precisely the generic doctor/smoke scripts, fixture, tool/Python pins, root Python dependency manifest/lock and historical foundation validation document referenced by the catalog. These optional sources are not installed runtimes or auto-run hooks. No legacy host-specific viewer config, private project assets, environments, upstream CAD/U1 skills or MCP configuration is included. The dedicated SvelteKit simulator stays a separate Workbench app; printer/slicer MCP APIs, dashboard and widgets stay in Orca.

## Output identities

Ignored reviewed artifact: `.workbench/plugin/cad-workbench/`, forty-four copied files plus input manifest and receipt.

| Identity | SHA-256 |
| --- | --- |
| `catalog/POLICY.sha256` | `c09d963068ba69107adaf16aa550a4039fcd6d91bbf10c8c1988ab428e0e3e55` |
| `PACKAGE_INPUTS.sha256` | `0b0d0871fd4f9a1484d34422562b42b95ab8e98f1bf0363ee7570f8178e12d1e` |
| `PACKAGE_RECEIPT.json` | `082ea1c85522e44417a2c4b6d568e2dd32c7e707226949891dbef7cde3f016ca` |
| manifest source | `607f9e3a5d52da651fd88a33b769692e0143eaa5ab121f89cec2c5d02fba80d7` |

Receipt source revision is the actual build-time Git HEAD plus a decision-bearing input manifest, which includes then-uncommitted package source and scope addendum bytes. This distinguishes the artifact from a claimed clean released revision. If declared source changes, build a new candidate/output and update evidence. Existing output is refused. The first manifest candidate is retained at `.workbench/plugin/initial-manifest-candidate/` as rejected diagnostic evidence, not an install candidate.

## Checks and repairs

- `uv run python scripts/package_plugin.py`: PASS, fresh artifact generated and read back.
- `uv run python scripts/package_plugin.py --check .workbench/plugin/cad-workbench`: PASS, file inventory/hash and contained Markdown/catalog reference readback.
- `uv run python -m unittest discover -s tests -p test_package_plugin.py -v`: 5 PASS, covering relocation, tampered output, missing runtime support fixture, escaping source symlink and preservation of existing output. Initial run encountered macOS `/var` symlink in the temporary test root; test now uses the canonical temporary path while production checks continue rejecting symlink output ancestors.
- `uv run python /Users/scottchu/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .workbench/plugin/cad-workbench`: PASS after supplying required interface metadata identified by initial validator failure. No runtime component was added to satisfy metadata validation.
- `uv run python /Users/scottchu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/workbench-flow`: PASS. The same validator ran on all three packaged skills; all PASS.
- `uv run python scripts/check_registry.py`: PASS, twelve categories, two recipes, local references and policy hashes.
- Root `uv run python` independently recomputed all forty-four current source hashes against output receipt rows: PASS.
- `git diff --check`: PASS for tracked changes; new package source formatting was inspected with the focused validators.

## Limits and independent join

These are package/discovery checks, not real recipe execution or a behavioral skill acceptance pass. The flow explicitly resolves installed provider versions independently of maintained source. text-to-CAD 0.5 supplies skills, cadgen runtime is separate; currently inspected U1 public MCP is read-only observation/camera; packaged U1 CLI setup/doctor/mcp does not implement slicing/start. Preparation and authorized start require their actual external providers and preserve their scope. An absent interface is unavailable, never replaced by invented tools or a generic HTTP/G-code proxy.

Independent review should exercise preparation-only, observation-only, absent-start-provider and explicit exact-artifact start requests against these instructions read-only. CAD, artifact/slicer, physical/platform acceptance remain separate and unexecuted in this packaging task. No simulator runtime check belongs to this receipt.
