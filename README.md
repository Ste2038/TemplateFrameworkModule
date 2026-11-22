# Framework Laptop 13 module template

Personal KiCad starting point for Stefano's future Framework Laptop 13 modules. Requires KiCad 9 (created with 9.0.9).

Open `TemplateFrameworkModule.kicad_pro` in KiCad Project Manager. The PCB includes the official printed-enclosure outline, mounting holes and 0.8 mm thickness. The schematic remains empty. This is a reusable mechanical baseline, not a validated working module.

## Start a module

1. Create a repository using **Use this template → Create a new repository** on GitHub, then clone your new repository (see [GitHub guide](docs/GITHUB.md)).
2. Close KiCad. Run `python3 scripts/new_module.py MyModule` in the new repository. This renames the project trio and updates project metadata; it refuses to run in this source folder.
3. Before design work, complete [template tracking](docs/TEMPLATE_TRACKING.md) using the [version and upgrade guide](docs/TEMPLATE_UPGRADES.md). Record the exact source version/commit permanently. Open `MyModule.kicad_pro`, fill in [module requirements](docs/MODULE.md), and define the electrical function before adding circuitry. Read [mechanical guidance](docs/MECHANICAL.md) before changing the existing outline.
4. Follow [editing and verification](docs/WORKFLOW.md). Replace this README introduction with your module's purpose and retain links to the guides.

## Repository map

| Path | Purpose |
| --- | --- |
| `*.kicad_pro` | Shared project and design settings |
| `*.kicad_sch` | Root schematic |
| `*.kicad_pcb` | PCB layout |
| `sym-lib-table`, `fp-lib-table` | Project-local library registrations |
| `libraries/` | Custom symbols, footprints, and 3D models |
| `docs/FRAMEWORK_REFERENCES.md` | Pinned official electrical and mechanical references |
| `docs/TEMPLATE_TRACKING.md` | Permanent creation baseline and append-only upgrade ledger |
| `docs/TEMPLATE_UPGRADES.md` | How to reconcile existing prototypes with newer templates |
| `docs/MODULE.md` | Requirements, pinout, mechanical and validation records |
| `docs/WORKFLOW.md` | How to modify and validate the design |
| `docs/GITHUB.md` | Publish this template and create independent module repos |
| `AGENTS.md` | Instructions for future agents |
| `meta/info.html` | KiCad template browser description |
| `scripts/new_module.py` | One-time project rename in a generated repository |
| `outputs/` | Ignored local reports and manufacturing exports |

## Template status

Confirmed target: **Framework Laptop 13 DIY Edition, Intel Core Ultra Series 1, 3D-printed enclosure**. The official enclosure STL/STEP files and source drawing are bundled in `references/framework/`. See [mechanical guidance](docs/MECHANICAL.md) for printing, dimensions and a source drawing discrepancy requiring fit validation.

Connector selection, pinout, circuitry, power budget and fabrication clearances remain module-specific. See [technical references](docs/FRAMEWORK_REFERENCES.md) and [third-party notices](THIRD_PARTY_NOTICES.md). Original-work licensing remains undecided.

This folder also contains KiCad's `meta/info.html` format for **File → New Project from Template**. GitHub generation is the preferred route for retaining the whole repository workflow; see the GitHub guide for the distinction.
# TemplateFrameworkModule
