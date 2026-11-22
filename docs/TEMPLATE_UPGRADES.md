# Template provenance and future upgrades

## Required for every prototype

Before changing a generated project, the next agent must complete `docs/TEMPLATE_TRACKING.md` and commit it with the initial project setup. This applies to GitHub-generated repositories, ZIP copies and native KiCad template projects.

Record the template repository URL, release/tag, full source commit SHA, creation date, original project basename and the new module basename. Obtain the SHA from the source template repository at the revision actually copied, not from the generated project's new Git history. A branch name such as main is not a stable version identifier. Keep an untouched archive or checkout of that exact source revision available for later comparisons.

If starting from an unpublished or modified local copy, record that fact, its source commit if any, and preserve an immutable snapshot of the actual copied files with a SHA-256 checksum. A commit alone does not identify uncommitted changes. Do not invent a release or SHA. Resolve unknown provenance before assuming any automatic upgrade is safe.

The creation baseline is permanent. Never replace it with a newer template version. Track the most recently fully reconciled template revision separately, and append a migration record for every later update. The prototype's hardware revision is independent of the template version.

## Current source status

This folder has no Git repository or release tag yet. CHANGELOG.md contains the initial 0.1.0 scaffold and subsequent unreleased changes; the KiCad TEMPLATE_VERSION text variable still identifies that initial scaffold. Neither value alone uniquely identifies the current files. Record the eventual published source commit/tag or a checksummed local snapshot when creating a prototype. v1 and v2 below are examples, not releases that already exist.

## Publishing template versions

For each release, maintain an immutable version tag tied to a specific commit. Update CHANGELOG.md, the KiCad TEMPLATE_VERSION variable and release documentation consistently. Include migration notes explaining affected files, behavioral/mechanical changes, compatibility constraints and required checks. Never move an old release tag to new contents. Keep old versions accessible so agents can compare them with later versions.

## Reconcile an existing v1 prototype with v2

1. Read its provenance and migration ledger. Preserve current work and create a dedicated upgrade branch/checkpoint in the prototype repository.
2. Obtain clean source snapshots of the recorded baseline (or last fully reconciled revision) and the desired newer template revision. Verify their commit IDs or snapshot checksums. Compare those two template versions to identify only changes introduced by the template.
3. Compare each template change against the existing prototype. Account for renamed project files using the recorded basename mapping. Review all three versions: old template, new template, and current prototype. Do not overwrite the prototype with the new template, re-run the naming script, or merge unrelated histories wholesale.
4. List each relevant change in the migration ledger as applied, adapted, deferred or not applicable, with reasons and affected files. Preserve module-specific circuitry, routing, UUIDs, libraries, constraints, documentation and manufacturing revisions. Reassess mechanical fit when outlines, holes, connector placement or enclosure CAD change.
5. Run checks appropriate to the adopted changes: KiCad load/export, ERC, DRC, schematic/PCB consistency, library portability and visual review. Mechanical/electrical changes may require renewed fit or hardware testing. Record commands, results, reports and limitations; unresolved safety or fit questions remain open.
6. Commit the reconciled design and ledger together. Record the resulting migration commit in a subsequent documentation commit if needed (a commit cannot contain its own final hash).
7. Advance the fully reconciled baseline only after every change in that template interval is accounted for and required validation passes. Deferred or unresolved changes mean the target remains partially adopted; retain the old fully reconciled baseline and the per-change ledger to avoid applying work twice. Deliberately not-applicable changes may be closed with justification.

For a later v3 update, use the last fully reconciled version and ledger, while always preserving the original v1 creation record. If the project was partially updated toward v2, explicitly consider the already adopted v2 changes in the three-way review.
