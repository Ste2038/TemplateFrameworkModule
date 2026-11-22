# Framework Laptop 13 Expansion Card references

Confirmed by owner on 2026-11-22: the target is the [Framework Laptop 13](https://frame.work/it/en/laptop13), with four Expansion Card slots. Earlier “Framework14” wording was a naming mistake. The owner subsequently confirmed the DIY Edition with Intel Core Ultra Series 1 and selected a 3D-printed enclosure.

## Authoritative design package

Framework publishes [ExpansionCards](https://github.com/FrameworkComputer/ExpansionCards), with electrical and mechanical design files rather than one comprehensive module datasheet. Inspected on 2026-11-22 at commit `2904a95d60d4ba771c5c3c56d6fdba7078243fe8`. The links below are pinned to that revision.

| Reference | Use |
| --- | --- |
| [Electrical guide](https://github.com/FrameworkComputer/ExpansionCards/blob/2904a95d60d4ba771c5c3c56d6fdba7078243fe8/Electrical/README.md) | Explains the two template variants and reference design limitations |
| [Printable-enclosure KiCad schematic PDF](https://github.com/FrameworkComputer/ExpansionCards/blob/2904a95d60d4ba771c5c3c56d6fdba7078243fe8/Electrical/KiCad_templates/Expansion_Card/Expansion_Card.pdf) | Circuit reference; review before adapting |
| [Printable-enclosure PCB](https://github.com/FrameworkComputer/ExpansionCards/blob/2904a95d60d4ba771c5c3c56d6fdba7078243fe8/Electrical/KiCad_templates/Expansion_Card/Expansion_Card.kicad_pcb) | Board geometry and connector placement for the printable housing |
| [Retrofit PCB](https://github.com/FrameworkComputer/ExpansionCards/blob/2904a95d60d4ba771c5c3c56d6fdba7078243fe8/Electrical/KiCad_templates/Expansion_Card_Retrofit/Expansion_Card_Retrofit.kicad_pcb) | Smaller board for existing Framework card housings |
| [Mechanical guide](https://github.com/FrameworkComputer/ExpansionCards/blob/2904a95d60d4ba771c5c3c56d6fdba7078243fe8/Mechanical/README.md) | Explains printable, parametric and retrofit choices |
| [Printable drawing PDF](https://github.com/FrameworkComputer/ExpansionCards/blob/2904a95d60d4ba771c5c3c56d6fdba7078243fe8/Mechanical/Printable/2D/ExpansionCard_Printable_M2.pdf) | Drawing reference for the printable variant |
| [Printable outline DXF](https://github.com/FrameworkComputer/ExpansionCards/blob/2904a95d60d4ba771c5c3c56d6fdba7078243fe8/Mechanical/Printable/2D/ExpansionCard_Printable_Outline.dxf) | Outline reference; verify units and datum before importing |
| [Retrofit drawing PDF](https://github.com/FrameworkComputer/ExpansionCards/blob/2904a95d60d4ba771c5c3c56d6fdba7078243fe8/Mechanical/Retrofit/2D/ExpansionCard_Retrofit.pdf) | Drawing reference for reused housings |
| [Threaded-insert enclosure STEP](https://github.com/FrameworkComputer/ExpansionCards/blob/2904a95d60d4ba771c5c3c56d6fdba7078243fe8/Mechanical/Printable/3D/ExpansionCard_ThreadedInsert.stp) | Mechanical integration reference |
| [Parametric enclosure](https://github.com/FrameworkComputer/ExpansionCards/blob/2904a95d60d4ba771c5c3c56d6fdba7078243fe8/Mechanical/OpenSCAD/ExpansionCard.scad) | Editable enclosure geometry and nominal dimensions |
| [USB-C plug footprint](https://github.com/FrameworkComputer/ExpansionCards/blob/2904a95d60d4ba771c5c3c56d6fdba7078243fe8/Electrical/KiCad_templates/Expansion_Card/Expansion_Card.pretty/USB_C_Plug_Molex_105444.kicad_mod) | Upstream connector footprint reference; verify selected orderable part and datasheet |

The host-facing connection uses a USB-C plug. Upstream electrical examples are two-layer USB 2.0 designs; they do not establish a USB4, DisplayPort, or high-power design baseline. Framework notes additional solder pads beside the plug for mechanical strength. The upstream microcontroller example's current revision is marked untested.

## Nominal mechanical starting values

The OpenSCAD source defines a 30 × 32 × 6.8 mm enclosure base and a typical 26 × 30 × 0.8 mm PCB. These are model parameters, not a complete toleranced drawing or a universal PCB outline. Rails, latch geometry, connector projection, mounting features and internal clearances require the matching CAD. Do not draw a simple rectangular board from these dimensions alone.

Selected family: **Printable / Expansion_Card**. The retrofit family is retained above only as a reference; do not use its geometry for this template.

## Host-specific electrical capabilities

Framework's [Laptop 13 USB port definition matrix](https://knowledgebase.frame.work/usb-port-definition-matrix-framework-laptop-13-HkHVUHaTge), checked 2026-11-22, lists all four Intel Core Ultra Series 1 ports as Thunderbolt 4, DisplayPort 2.0, and PD 3.0. It also lists USB 3.2 Gen 2x1 and multifunction USB-C support. Listed power roles are up to 20 V / 5 A input to the laptop and 5 V / 3 A output. The first port requesting 3 A can receive it; remaining ports then support 1.5 A. Full Thunderbolt capability requires current BIOS according to Framework. These host capabilities do not confer those capabilities on a custom card; power negotiation and circuit limits must be designed per module. Laptop charging input is not a 20 V supply available to a card.

## Implemented mechanical baseline

See [MECHANICAL.md](MECHANICAL.md) for imported geometry, enclosure files, coordinates, known drawing discrepancy and how to add a connector without duplicating board edges. The schematic is intentionally empty and no connector copper, regulator, CC resistors, signal wiring or power circuit has been adopted yet.

## Provenance and licensing

The upstream [license](https://github.com/FrameworkComputer/ExpansionCards/blob/2904a95d60d4ba771c5c3c56d6fdba7078243fe8/LICENSE) and README identify Expansion Cards © 2021 Framework Computer Inc under CC BY 4.0. The OpenSCAD file has its own author notice. Preserve applicable attribution, license references, and a record of modifications when importing/adapting assets. Upstream files are now bundled under references/framework with their license and SHA-256 manifest; see THIRD_PARTY_NOTICES.md. Original-work licensing remains undecided.

## Verification scope

Upstream source files are pinned and checksummed. The printable PDF was visually reviewed and the adapted outline was inspected in an exported SVG. KiCad 9.0.9 DRC passed with zero findings after importing all outline segments, including those embedded in upstream P1. No GUI 3D fit inspection or physical print/hardware validation was performed. See MODULE.md for current validation evidence.
