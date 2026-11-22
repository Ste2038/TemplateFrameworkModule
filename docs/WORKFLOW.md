# Editing and verifying a module

## Project and schematic

Open the .kicad_pro in KiCad Project Manager. Edit the .kicad_sch using Schematic Editor. Set title, revision, company/author and notes in Page Settings. Use Project Text Variables for shared values. Add hierarchical sheets only when the circuit needs them; commit all sheet files. Annotate, assign footprints, and run Electrical Rules Checker before updating the PCB.

Use symbol properties for manufacturer, manufacturer part number, supplier reference, datasheet, and assembly notes. Mark DNP parts consistently and document how they are filtered from exports. Verify pin numbering against the component datasheet rather than trusting a similarly named symbol.

## PCB and design rules

Open the .kicad_pcb in PCB Editor. Configure Board Setup: layers and physical stackup, constraints, net classes, widths/vias, and any custom rules. Use the confirmed fabrication capabilities and electrical requirements in MODULE.md. The initial two-layer, 0.8 mm board follows the official printable reference; other manufacturing settings still require review. Read MECHANICAL.md before changing geometry.

Preserve the imported closed outline on Edge.Cuts unless deliberately adapting the enclosure. Put mechanical guidance on appropriate drawing/keepout layers. Add mounting features and connector placement from an explicit datum. Use **Tools → Update PCB from Schematic**, review the changes, place and route, refill zones, then run DRC. Inspect 3D orientation and component heights.

If custom rules are needed, keep the same-basename .kicad_dru file in Git. Review rule changes together with the PCB and project settings.

## Libraries and portability

Create custom symbol libraries under libraries/symbols/ and footprint libraries (*.pretty) under libraries/footprints/. Register them with **Preferences → Manage Symbol/Footprint Libraries → Project Specific Libraries**. Use `${KIPRJMOD}/libraries/...` paths. Put redistributable 3D models under libraries/3dmodels/ and reference them using `${KIPRJMOD}`. The footprint table registers FrameworkMechanical for the mounting holes; the symbol table is empty; standard KiCad libraries remain available through the user's global tables. Install KiCad's standard libraries when prompted.

Document every imported asset's URL, version and license in libraries/README.md. Avoid absolute paths and dependencies on another checkout. Check portability from a fresh clone.

## Command-line verification (KiCad 9)

From the repository root, substitute your actual project basename:

```sh
mkdir -p outputs
kicad-cli version
kicad-cli sch export netlist -o outputs/netlist.net MyModule.kicad_sch
kicad-cli sch export svg -o outputs/schematic/ MyModule.kicad_sch
kicad-cli sch erc --exit-code-violations -o outputs/erc.rpt MyModule.kicad_sch
kicad-cli pcb drc --exit-code-violations -o outputs/drc.rpt MyModule.kicad_pcb
```

Read the reports even if the command completes. The mechanical baseline currently passes DRC; a missing/open outline is a regression. These commands write outputs; keep them ignored. Also inspect the project in the GUI: parsing and rule checks cannot prove connector orientation or mechanical fit. Record results in MODULE.md.

## Manufacturing and releases

Follow [RELEASE_WORKFLOW.md](RELEASE_WORKFLOW.md): prepare on develop, merge approved release work into master, tag the master commit and return to develop.

Only export manufacturing data after the release checklist is complete. Generate Gerbers, drill files, BOM and placement files through KiCad's fabrication/export dialogs with settings agreed with the fabricator. Verify units, origin, board revision, bottom-side rotation conventions, DNP handling and layer mapping. Inspect outputs in Gerber Viewer. Archive reviewed outputs with a release tag and commit identifier, for example as GitHub release attachments; do not use local ignored outputs as the sole release record.

## Maintaining the template

Keep the shared mechanical baseline generic and add circuitry only when its function and constraints are established. When shared circuitry is approved, include source references and validation evidence. Version shared changes in CHANGELOG.md. Generated repositories do not automatically receive later template updates: selectively port and revalidate the relevant changes.

Before starting or updating a prototype, read [TEMPLATE_UPGRADES.md](TEMPLATE_UPGRADES.md) and its [tracking record](TEMPLATE_TRACKING.md). Keep the original creation version immutable and record each later reconciliation separately.

## PCB revision marking

The PCB has `${PCB_REVISION}` text on F.SilkS. Set PCB_REVISION in Project Text Variables to the exact intended Git release tag before validation, committing and tagging. This template release uses v1.0. Check the rendered silkscreen and fabrication output; do not leave unresolved variables or a previous release number on a changed board. New module initialization sets v0.1-dev; use development-suffixed revisions for unreleased hardware.

TEMPLATE_VERSION records the template baseline and is separate from the module's PCB_REVISION. Retain original source provenance in TEMPLATE_TRACKING.md even after updating the current template baseline. A prototype release tag belongs to that prototype's repository, not the source template repository.
