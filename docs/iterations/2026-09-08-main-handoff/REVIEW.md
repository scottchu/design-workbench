# Independent main-cutover review

Reviewer: `/root/boundary_inventory`. Date: 2026-09-08. Read-only acceptance
review; the reviewer wrote only this record and performed no remote, service,
device, installation, or project mutations.

## Pre-merge disposition

**PASS for the reviewed binding/continuity patches and proposed preservation
boundary.** No material source-cutover finding remains. This is permission to
advance the already user-authorized delivery after the coordinator's remaining
checks; it is not evidence that a merge or new-worktree setup has happened.

The reviewed BRIEF has SHA-256
`70454f94318720a3d5f803d28fdc3bd79fed004d968c856b7a0dbbd569e50c06`.
It scopes delivery to Workbench PR 1, design PR 23 and sticker PR 1, preserving
unrelated canonical design WIP, sticker pilot WIP and existing runtime ownership.

Both consumer bindings resolve the same exact Workbench provider:

- Commit: `1d7f4fcd65e04136bb6bad24e90015ca36d97f2f`.
- Policy index: `catalog/POLICY.sha256`.
- Policy index SHA-256:
  `b95f77ef16d317366d1c93f7ff76dee92c0e69976ce55facec10512e23b6c3cf`.
- Design binding SHA-256:
  `ca40302b1e2126bb14a0b991a924d5bb2e04c75458714b9f7fab47f71443a6ca`.
- Sticker binding SHA-256:
  `ca05ac9ae91744e1823f94890d9330b3ea61758fb2275006e9d87bbf8813b011`.

The reviewer independently read the policy index and all 33 declared files using
`git show <exact-provider-commit>:<path>` and verified their SHA-256 values: **33/33
PASS**. Binding identities match those Git bytes, not merely the current working
tree. C1/C2 semantic repairs were independently accepted in the preceding
`2026-09-08-plugin-install/MIGRATION_COMPLETENESS_REVIEW.md`; this cutover adopts
that reviewed policy without changing it.

## Mutation and preservation checks

Design changes from `8c0710c49b60b8c17ff66fc424f608c07d420588` are limited to
`docs/workflows-binding.json` and the root migration HANDOFF. Sticker changes from
`92f82ff5464fd2724c49e4bde201fae2cd76cad4` are limited to its binding, root
PROJECT_STATE/NEXT_AGENT, and root migration HANDOFF. The historical old-pin and
no-merge statements are explicitly identified as historical by the new addenda.
The old candidate/recovery manifests remain historical evidence and are not
silently rewritten to pretend they covered this new pin.

`git diff <above-base> --name-only -- projects recovery` is empty in both consumer
checkouts. Both working diffs pass `git diff --check`. No project generation,
CAD/assets, release evidence or recovery archive changed. Preserved tree identities
before this patch are:

- Design `projects`: `fb60ebaebf4758b2a27b165f57340e4612b11885`.
- Sticker `projects`: `72e996adb8db3d45fcca58312f5badc27bdfd86d`.
- Sticker `recovery`: `cd1b93f218e91c98050f0dd1eb281911ca609b7c`.

Local recovery-ref inspection confirms design's
`recovery/workflow-ownership-71d661c`, both sticker recovery branches and the
historical sticker tag remain present. Prior independent byte/history/restoration
acceptance applies; no costly historical-media audit was repeated. The known
baseline Laifen missing `VALIDATION.md` remains an explicitly reported existing
continuity defect, not a reason to fabricate project evidence during this merge.

## Runtime and new-agent handoff

Read-only runtime-binding inspection still selects
`/Users/scottchu/.codex/worktrees/7e46/CAD-workbench`, instance
`ca3daa81c9c60ef20aa7f16b`, URL `http://127.0.0.1:4179`. The BRIEF preserves that
root and forbids rebinding, removal or restart during handoff. This is consistent
with the lifecycle ownership contract in `apps/simulator/SERVICE.md`.

The fresh `/Users/scottchu/Projects/personal/CAD-workbench-next` checkout must not
inherit private simulator registry/configuration or become a second service owner.
Its own root uv/npm environment is a development setup. The final current handoff
must identify the actual merged commits and clean new branch/root, preserve the old
runtime checkout, and direct lifecycle operations through the verified original
root. Consumer checks from a non-sibling checkout use `CAD_WORKBENCH_CHECKOUT` to
locate a Workbench Git object database containing the pinned commit.

## Remaining coordinator delivery evidence

Coordinator reports current Workbench 29 Python checks, 11 simulator checks and
zero Svelte errors/warnings; design root checks are 10 PASS plus the confirmed
baseline Laifen failure, with both focused binding checks PASS. Sticker npm tests
completed **14/14 PASS** before this record was released.
These results are coordinator provenance and were not duplicated by this reviewer.

The coordinator also reports Workbench PR 1 merged from exact reviewed head
`1d7f4fcd65e04136bb6bad24e90015ca36d97f2f` to merge commit
`3ed377ed98e18d9945b854043ffb27b4c8c851b8`, with `main` now the default. This is
coordinator remote-readback evidence, not a separate reviewer network query.

Before declaring delivery complete, the coordinator merges the remaining exact
reviewed consumer PR heads with merge commits, checks all remote main
refs and provider ancestry, preserves setup/recovery refs and canonical dirty WIP,
creates/verifies the clean new worktree, and records current runtime health without
relocating it. The documentation follow-up updates current state and handoff with
observed results. A later documentation-only commit does not change the provider
identity selected above. No printer, fabrication, fresh full-recipe, or physical
acceptance claim is made by this review.

## Final new-worktree handoff review

**PASS**, reviewer `/root/boundary_inventory`, 2026-09-08. Reviewed the new
worktree's NEXT_AGENT, PROJECT_STATE, this iteration's HANDOFF and the narrow
decision/plugin-handoff updates. The documents give a usable fresh-session entry,
separate the completed migration from the remaining skill-invocation gate, and
explicitly preserve the old runtime root. No misleading runtime takeover, full
recipe, mobile-export, reboot or physical-acceptance claim was found.

Independent local Git readback confirms the recorded remote-tracking merge refs:
Workbench `3ed377ed98e18d9945b854043ffb27b4c8c851b8`, design
`cf8ec46cffc24d8beb26d3908bb6023843824f1f`, sticker
`cd20668470811e744a09d7ffa485f39cd0883a71`. Both consumer `origin/main` bindings
select the exact reviewed `1d7f4fc` provider and `b95f77ef` policy index. Provider
ancestry in Workbench `origin/main` passes. Merged design project and sticker
project/recovery diffs against the reviewed pre-cutover commits remain empty.

`git worktree list --porcelain` confirms the new development branch/root at the
Workbench merge commit, the original foundation checkout, and the preserved old
runtime checkout at `1d7f4fc`. Runtime JSON still identifies that original root and
instance. Root lockfiles are unchanged, and documentation `git diff --check`
passes. Dependency setup, doctor/registry/Svelte checks and live health are the
coordinator's recorded evidence, not rerun by this reviewer.

At this review the final handoff documentation PR and fast-forward to its merged
main tip are still coordinator-owned final delivery actions. The HANDOFF describes
their required completed-delivery state; it must not be reported achieved until
those operations and clean-worktree verification finish. This reviewer releases
the sole REVIEW namespace for that final documentation delivery.
