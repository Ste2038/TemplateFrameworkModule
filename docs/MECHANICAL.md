# Printed enclosure baseline

Target: Framework Laptop 13 DIY Edition, Intel Core Ultra Series 1. Owner selected printed enclosure on 2026-11-22.

## Files to use

Unmodified upstream sources are in `references/framework/`; commit, source URLs and SHA-256 hashes are in `references/framework/manifest.json`. Keep these as reference originals. Edit copies for each module and record modifications.

- `Mechanical/Printable/3D/ExpansionCard_SelfTapping.stl` and `.stp`: enclosure for self-tapping M2 screws; simplest initial prototype option.
- `Mechanical/Printable/3D/ExpansionCard_ThreadedInsert.stl` and `.stp`: alternative enclosure with threaded inserts.
- `Mechanical/OpenSCAD/ExpansionCard.scad`: editable parametric alternative; its settings are not interchangeable with a different housing without checking fit.
- `Mechanical/Printable/2D/ExpansionCard_Printable_M2.pdf`: dimensioned PCB drawing.

Both fastening variants are included; choose matching hardware before printing/assembly. Print one fit sample first; record printer, material, orientation, slicer settings and measured shrinkage in MODULE.md. Check insertion, latch engagement, plug alignment, component clearance and screw engagement without forcing the laptop connector. The enclosure front opening and module-specific cutouts still need design.

## Editable PCB baseline

The root PCB now contains the full outline copied from the official printable KiCad template, two 2.2 mm non-plated mounting holes, and 0.8 mm board thickness. The board remains two-layer. Original project/schematic identities are retained; no electrical circuitry was imported.

Coordinates remain in the upstream KiCad datum, in mm:

| Feature | Coordinate / size |
| --- | --- |
| Outline extrema | X 127–153, Y 127–157 (26 × 30 overall) |
| H1 center | X 128.7, Y 146.5 |
| H2 center | X 151.3, Y 146.5 |
| Hole center spacing | 22.6 |
| Mounting drill | 2.2, NPTH |
| Reference USB-C P1 origin | X 140, Y 129, rotation 0 degrees |

Holes are board-only, excluded from BOM and placement output, with a project-local FrameworkMechanical library. Preserve them during schematic updates. The USB-C origin is guidance on Dwgs.User, not an installed electrical footprint.

IMPORTANT: Nine Edge.Cuts segments in the original design belong to its USB-C footprint. These were transferred into board-level geometry to close the outline without adopting that connector's circuitry. When placing a connector footprint later, remove its duplicate Edge.Cuts graphics or deliberately replace the corresponding board segments; never leave overlapping contours. Verify the chosen footprint's datum and orientation against upstream P1.

## Drawing discrepancy to resolve in fit testing

The bundled PDF drawing revision A (2021-04-06) specifies 26.05 ±0.20 mm width and 29.70 ±0.20 mm height, while the upstream PCB has a 26 × 30 mm outline envelope. Its 22.60 mm hole spacing agrees, but the PDF's 10.20 mm bottom-to-hole dimension differs from the PCB's 10.5 mm. Do not claim dimensional agreement or silently alter the source. This template follows the actual upstream KiCad PCB; reconcile with the chosen enclosure CAD and a fit prototype before fabrication. The PDF also marks 0.80 ±0.08 mm thickness and top/bottom component-height limits; inspect it when placing components.

## Next electrical work

Choose each module's function and required USB protocol, power budget and protection. The official example is USB 2.0; a Thunderbolt-capable laptop does not make that example a high-speed interface. Validate the actual connector manufacturer's drawing and part availability before adopting its footprint. Add matching schematic symbols and footprints, then run ERC, update PCB from schematic, and run DRC.
