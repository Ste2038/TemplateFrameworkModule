#!/usr/bin/env python3
"""Rename the untouched KiCad scaffold in a newly generated module repository."""
import argparse
import json
from pathlib import Path
import re


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", help="New project basename, e.g. SensorModule")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    old = "TemplateFrameworkModule"
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", args.name) or args.name == old:
        parser.error("Choose a new name: a letter followed by letters, numbers, _ or -.")
    if root.name == old:
        parser.error("Run in a generated module repository with a different folder name, not the source template.")
    extensions = (".kicad_pro", ".kicad_sch", ".kicad_pcb")
    sources = [root / (old + ext) for ext in extensions]
    targets = [root / (args.name + ext) for ext in extensions]
    if not all(p.is_file() for p in sources):
        parser.error("Expected untouched template project trio; project may already be renamed.")
    if any(p.exists() for p in targets):
        parser.error("Target file already exists; nothing changed.")
    if list(root.glob("*.kicad_dru")) or len(list(root.glob("*.kicad_sch"))) != 1:
        parser.error("Rename before adding custom rules or schematic sheets.")
    if any(root.glob("~*.lck")) or any(root.glob("*.lck")):
        parser.error("KiCad lock found; close KiCad before renaming.")
    project = json.loads(sources[0].read_text())
    project.setdefault("meta", {})["filename"] = targets[0].name
    project.setdefault("text_variables", {})["MODULE_NAME"] = args.name
    project["text_variables"]["PCB_REVISION"] = "v0.1-dev"
    renamed = []
    original = sources[0].read_bytes()
    try:
        for source, target in zip(sources, targets):
            source.rename(target)
            renamed.append((source, target))
        targets[0].write_text(json.dumps(project, indent=2) + "\n")
    except Exception:
        for source, target in reversed(renamed):
            target.rename(source)
        sources[0].write_bytes(original)
        raise
    print(f"Open {targets[0].name}. Update README.md, docs/MODULE.md and title blocks before designing.")


if __name__ == "__main__":
    main()
