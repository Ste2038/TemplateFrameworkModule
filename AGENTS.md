# Instructions for agents

## Read first

Read README.md, docs/MODULE.md, docs/FRAMEWORK_REFERENCES.md, docs/WORKFLOW.md, and docs/GITHUB.md before changing files. This repository starts as a KiCad 9 scaffold for Stefano's Framework Laptop 13 modules. The owner confirmed Framework Laptop 13 DIY Edition, Intel Core Ultra Series 1, with printed Expansion Card enclosures. Read docs/MECHANICAL.md and THIRD_PARTY_NOTICES.md before modifying the imported mechanical baseline. Connector circuitry and power requirements remain module-specific.

## Source of truth

The same-basename .kicad_pro/.kicad_sch/.kicad_pcb trio is the editable design. docs/MODULE.md records approved requirements and unresolved choices. Keep requirements and design synchronized. Keep template-wide changes generic; module-specific circuits belong in generated module repositories unless explicitly requested here.

## Template version tracking — mandatory

Before starting a prototype, read docs/TEMPLATE_UPGRADES.md and complete docs/TEMPLATE_TRACKING.md with the actual source template URL, release/tag and full commit SHA (or a checksummed snapshot for an unpublished local copy). Preserve that creation baseline forever. Record subsequent template updates separately with per-change decisions and validation evidence. Never infer the source SHA from the generated repository's history or treat a partial upgrade as fully aligned. Read the tracking record before changing an existing prototype.

## Editing rules

- Inspect git status and existing work before editing; preserve unrelated changes.
- Prefer KiCad editors for circuitry and layout. For scripted edits, use KiCad-compatible APIs/formats, preserve UUIDs and connectivity, and validate with kicad-cli plus visual review when possible.
- Never replace an existing design with a newly generated blank board or schematic.
- Use project-local libraries and ${KIPRJMOD} paths for custom assets. Record source, license, and version of imported assets.
- Do not silently upgrade the KiCad major version. Do not manufacture a board or claim compatibility from a blank-template check.
- Do not invent approved pinouts, net classes, clearances, stackups, or mechanical constraints. Ask for missing authoritative requirements before implementing dependent hardware.
- Do not remove ERC/DRC findings using exclusions without documenting the electrical justification and owner acceptance.
- Keep machine-local files, locks, backups, and generated outputs out of Git. Never discard user backups to clean the repository.
- No license is selected. Do not choose one or copy third-party designs without checking provenance.

## Completion evidence

Report changed files, KiCad version, exact verification performed, remaining ERC/DRC findings, and unresolved requirements. Update docs/MODULE.md and CHANGELOG.md for meaningful changes. If GUI review or hardware tests were unavailable, state that explicitly. GitHub publishing instructions are documented; no remote is configured by this scaffold.
