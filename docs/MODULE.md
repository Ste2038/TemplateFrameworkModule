# Module definition and decision record

Status: TEMPLATE / NOT READY FOR FABRICATION
Owner: Stefano
Template baseline: initial scaffold 0.1.0 plus unreleased changes; exact prototype provenance must be recorded in [TEMPLATE_TRACKING.md](TEMPLATE_TRACKING.md).
Module name: TBD (set after generation)

## Requirements to resolve

| Item | Approved value / evidence |
| --- | --- |
| Host identity and interface | Framework Laptop 13, four Expansion Card slots; owner confirmed 2026-11-22. See [references](FRAMEWORK_REFERENCES.md). |
| Installed mainboard/CPU generation and slot capability map | DIY Edition, Intel Core Ultra Series 1; all four ports support TB4 / DP 2.0 per official matrix; power-sharing details in FRAMEWORK_REFERENCES.md |
| Enclosure family | 3D-printed, official Printable / Expansion_Card; self-tapping and threaded-insert files supplied |
| Module purpose and acceptance criteria | TBD |
| Host connector, mating part, orientation and pin numbering | USB-C plug interface confirmed by upstream design; exact part, orientation and pin mapping require review |
| Power rails, tolerance, maximum current, sequencing | TBD |
| Signal levels, protocols, impedance, ESD/protection | TBD |
| Board outline, datum, mounting holes, keepouts and tolerances | Upstream printable outline and 2.2 mm holes imported; see MECHANICAL.md for datum and unresolved drawing discrepancy. Keepouts/tolerances need module review. |
| Component height, enclosure, thermal constraints | TBD |
| Layer stackup, thickness, copper weight, fabricator | Two layers, 0.8 mm per upstream mechanical baseline; copper weight, detailed stackup and fabricator TBD |
| Trace/space, drill, annular ring and voltage clearance rules | TBD |
| Assembly process and sourcing constraints | TBD |
| Hardware, documentation and software licensing | TBD |

Do not treat KiCad defaults as approved manufacturing constraints. Attach authoritative drawings and datasheets (or stable links with revision and retrieval date) before implementing the interface.

## Connector pinout

Populate a table with pin number, host-side name, module net, direction, voltage, current limit, and source reference. Identify the view direction explicitly. Currently no pins are defined.

## Design decisions

- 2026-11-22: Every prototype must retain its original source template version/commit and maintain a separate upgrade ledger; see TEMPLATE_UPGRADES.md and TEMPLATE_TRACKING.md. Documentation-only update; KiCad 9.0.9 files unchanged, ERC/DRC not rerun and previous results remain applicable. No new GUI or hardware testing performed.

- 2026-11-22: Owner selected printed enclosure and confirmed Intel Core Ultra Series 1. Imported official printable mechanical baseline, preserved source files and notices. Earlier pending enclosure/mainboard decisions below are superseded.

- 2026-11-22: Owner identified Framework Laptop 13 Expansion Cards; corrected earlier Framework14 naming. Pinned official CAD references in FRAMEWORK_REFERENCES.md. Enclosure family and mainboard generation remain open; no geometry imported.

- 2026-11-22: Use installed KiCad 9.0.9; blank schematic and board until interface is confirmed.
- 2026-11-22: Keep reusable project at repository root and custom assets under libraries/.
- 2026-11-22: New modules use separate repositories generated from the GitHub template.

## Verification record

Record date, commit, tool version, command/test, result, and report path. A successful parse of the scaffold does not establish hardware correctness. Blank board DRC can report missing outline; resolve this in each actual module rather than excluding it.

### Scaffold verification — 2026-11-22

KiCad CLI 9.0.9, initial uncommitted scaffold:

- Schematic netlist and SVG exports: passed; outputs/netlist.net and outputs/schematic/.
- ERC with --exit-code-violations: passed, zero findings; outputs/erc.rpt.
- PCB DRC with --exit-code-violations: exit 5, one expected invalid_outline finding because Edge.Cuts is empty; zero unconnected pads and footprint errors; outputs/drc.rpt. Not fabrication-ready.
- new_module.py on a disposable ExampleModule copy: passed; all three project files renamed. A second rename was correctly refused.
- GUI review and physical hardware validation: not performed.

### Mechanical baseline verification — 2026-11-22

- KiCad 9.0.9: `kicad-cli pcb drc --exit-code-violations -o outputs/drc-mechanical.rpt TemplateFrameworkModule.kicad_pcb` passed, zero violations/unconnected items. Earlier missing-outline result is superseded.
- `kicad-cli pcb export svg --layers Edge.Cuts,F.SilkS,Dwgs.User --page-size-mode 2 -o outputs/pcb-preview.svg TemplateFrameworkModule.kicad_pcb` passed; rendered outline visually reviewed.
- Upstream PDF visually reviewed; dimensional discrepancy recorded in MECHANICAL.md.
- Schematic unchanged; previous zero-finding ERC applies to the still-empty schematic only.
- No GUI 3D or physical fit/electrical tests performed. DRC does not validate enclosure fit or a functional circuit.

## Release checklist

- [ ] Requirements and host compatibility confirmed with evidence
- [ ] Pinout, power budget, protection and connector orientation reviewed
- [ ] Outline, holes, clearances and height checked against mechanical references
- [ ] Schematic annotations, footprints and BOM properties complete
- [ ] Schematic-to-PCB synchronization verified
- [ ] ERC and DRC findings resolved or individually justified
- [ ] Gerbers, drills, BOM and placement data independently inspected
- [ ] Fabrication revision, tool version and commit recorded
- [ ] Bring-up plan and hardware acceptance measurements documented
