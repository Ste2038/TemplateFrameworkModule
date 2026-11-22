# Template tracking record

Complete this document in every generated prototype before design work. Follow [TEMPLATE_UPGRADES.md](TEMPLATE_UPGRADES.md). These placeholders describe the template itself, not an already-created prototype.

## Original creation baseline — preserve permanently

| Field | Value |
| --- | --- |
| Prototype name / repository | NOT YET CREATED |
| Creation date | NOT YET CREATED |
| Source template repository URL | https://github.com/Ste2038/TemplateFrameworkModule |
| Source template release/tag | v1.0 (verify the actual revision copied) |
| Exact source template commit SHA | TO RECORD in each prototype: resolve v1.0^{commit} in the source repository if created from that release |
| Source had local modifications? | TO VERIFY when creating the prototype; NO only for an unmodified release checkout |
| Immutable source snapshot location and SHA-256 (if needed) | Not needed for an unmodified tagged checkout; required for a modified local copy |
| Original template project basename | TemplateFrameworkModule |
| Prototype project basename | TO RECORD |
| KiCad version used at creation | TO RECORD (template baseline: 9.0.9) |
| Evidence used to identify source revision | TO RECORD |

## Current reconciliation state

- Last fully reconciled template tag and full commit SHA: NOT YET INITIALIZED (set to the verified creation baseline when starting).
- Target template tag and full commit SHA: NONE.
- Status: NOT YET CREATED (later: aligned, partial, or under review).
- Outstanding deviations/deferred changes: TO RECORD.

Do not overwrite the original creation baseline when updating these fields.

## Migration ledger — append one section per attempted upgrade

No upgrades yet. Copy the following structure for each upgrade:

### YYYY-MM-DD — baseline → target

- Agent/maintainer:
- Old template tag and full SHA / snapshot checksum:
- New template tag and full SHA / snapshot checksum:
- Prototype checkpoint/branch before upgrade:
- Template comparison evidence and release notes:

| Template change | Affected prototype files | Disposition (applied/adapted/deferred/not applicable) | Reason / implementation |
| --- | --- | --- | --- |
| Fill in each change | | | |

- Validation commands, results and report locations:
- Visual / physical validation performed or outstanding:
- Conflicts, intentional deviations and deferred work:
- Outcome: partial or fully reconciled, with rationale:
- Prototype migration commit(s):
- Last fully reconciled baseline after this attempt:
