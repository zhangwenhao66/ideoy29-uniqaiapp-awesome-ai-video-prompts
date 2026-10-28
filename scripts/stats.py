#!/usr/bin/env python3
"""Count the prompt list: by model, by use case, by mode, and how many entries carry a render report.

Usage:
  python3 scripts/stats.py            # Markdown tables (what README.md embeds)
  python3 scripts/stats.py --json     # the same numbers as JSON

Every number in README.md comes from this script on data/prompts/. Nothing is typed by hand.
"""
import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import MODE_LABEL, load_meta, load_records, model_name, use_case_name  # noqa: E402


def compute(records, meta):
    by_model = Counter()
    by_use_case = Counter()
    by_mode = Counter()
    rendered = 0
    for r in records:
        for m in r["models"]:
            by_model[m] += 1
        by_use_case[r["use_case"]] += 1
        by_mode[r["mode"]] += 1
        if r.get("rendered_on"):
            rendered += 1
    video = sum(1 for r in records if r["mode"] in ("t2v", "i2v"))
    return {
        "total": len(records),
        "video": video,
        "image": len(records) - video,
        "rendered": rendered,
        "unrendered": len(records) - rendered,
        "by_model": [(k, by_model[k]) for k in meta["models"] if by_model[k]],
        "by_use_case": [(k, by_use_case[k]) for k in meta["use_cases"] if by_use_case[k]],
        "by_mode": [(k, by_mode[k]) for k in MODE_LABEL if by_mode[k]],
    }


def markdown(stats, meta):
    lines = []
    lines.append("| Model | Prompts written for it |")
    lines.append("|:---|---:|")
    for k, n in stats["by_model"]:
        lines.append("| %s (`%s`) | %d |" % (model_name(meta, k), k, n))
    lines.append("")
    lines.append("| Use case | Prompts |")
    lines.append("|:---|---:|")
    for k, n in stats["by_use_case"]:
        lines.append("| %s | %d |" % (use_case_name(meta, k), n))
    lines.append("")
    lines.append("| Mode | Prompts |")
    lines.append("|:---|---:|")
    for k, n in stats["by_mode"]:
        lines.append("| %s (`%s`) | %d |" % (MODE_LABEL[k], k, n))
    lines.append("")
    lines.append(
        "%d prompts in total: %d video, %d image. %d carry a render report (`rendered_on` is not empty); "
        "%d follow a vendor prompt guide or the UniqAI library but have no render report yet."
        % (stats["total"], stats["video"], stats["image"], stats["rendered"], stats["unrendered"])
    )
    return "\n".join(lines) + "\n"


def main(argv):
    if "--help" in argv or "-h" in argv:
        print(__doc__.strip())
        return 0
    meta = load_meta()
    stats = compute(load_records(), meta)
    if "--json" in argv:
        print(json.dumps(stats, indent=2))
    else:
        sys.stdout.write(markdown(stats, meta))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
