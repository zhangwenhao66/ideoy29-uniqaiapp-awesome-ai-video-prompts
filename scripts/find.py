#!/usr/bin/env python3
"""Find prompts in the list and print them ready to paste.

Usage:
  python3 scripts/find.py --model kling-3 --use-case product
  python3 scripts/find.py --model veo-3 --tag audio --short
  python3 scripts/find.py --grep "push in" --mode t2v
  python3 scripts/find.py --id kling-push-in-compass
  python3 scripts/find.py --rendered                # only entries with a render report
  python3 scripts/find.py --list-models | --list-use-cases | --list-tags

Filters combine with AND. Output is plain text: title, model/mode/duration line, the prompt in a
fenced block, and the "why" note. --short prints one line per hit. --json prints the records.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import MODE_LABEL, load_meta, load_records, model_name  # noqa: E402


def parse(argv):
    opts = {"model": None, "use_case": None, "mode": None, "tag": None, "grep": None, "id": None,
            "rendered": False, "short": False, "json": False, "list": None, "help": False}
    i = 0
    while i < len(argv):
        a = argv[i]
        nxt = argv[i + 1] if i + 1 < len(argv) else None
        if a in ("-h", "--help"):
            opts["help"] = True
        elif a == "--model":
            opts["model"], i = nxt, i + 1
        elif a == "--use-case":
            opts["use_case"], i = nxt, i + 1
        elif a == "--mode":
            opts["mode"], i = nxt, i + 1
        elif a == "--tag":
            opts["tag"], i = nxt, i + 1
        elif a == "--grep":
            opts["grep"], i = nxt, i + 1
        elif a == "--id":
            opts["id"], i = nxt, i + 1
        elif a == "--rendered":
            opts["rendered"] = True
        elif a == "--short":
            opts["short"] = True
        elif a == "--json":
            opts["json"] = True
        elif a in ("--list-models", "--list-use-cases", "--list-tags"):
            opts["list"] = a[7:]
        else:
            raise SystemExit("unknown argument: %s (see --help)" % a)
        i += 1
    return opts


def matches(r, o):
    if o["id"] and r["id"] != o["id"]:
        return False
    if o["model"] and o["model"] not in r["models"]:
        return False
    if o["use_case"] and r["use_case"] != o["use_case"]:
        return False
    if o["mode"] and r["mode"] != o["mode"]:
        return False
    if o["tag"] and o["tag"] not in r["tags"]:
        return False
    if o["rendered"] and not r.get("rendered_on"):
        return False
    if o["grep"]:
        hay = " ".join([r["title"], r["prompt"], r["why"], " ".join(r["tags"])]).lower()
        if o["grep"].lower() not in hay:
            return False
    return True


def header(r, meta):
    models = ", ".join(model_name(meta, m) for m in r["models"])
    parts = [models, MODE_LABEL[r["mode"]]]
    if "duration_s" in r:
        parts.append("%d s" % r["duration_s"])
    parts.append(r["aspect"])
    parts.append("rendered: %s" % ("yes" if r.get("rendered_on") else "no report yet"))
    return " | ".join(parts)


def main(argv):
    o = parse(argv)
    if o["help"]:
        print(__doc__.strip())
        return 0
    meta = load_meta()
    records = load_records()
    if o["list"]:
        if o["list"] == "models":
            for k, v in meta["models"].items():
                print("%-14s %s" % (k, v["name"]))
        elif o["list"] == "use-cases":
            for k, v in meta["use_cases"].items():
                print("%-16s %s" % (k, v))
        else:
            tags = sorted({t for r in records for t in r["tags"]})
            print("\n".join(tags))
        return 0
    hits = [r for r in records if matches(r, o)]
    if o["json"]:
        print(json.dumps(hits, indent=2, ensure_ascii=False))
        return 0 if hits else 1
    if not hits:
        print("no prompts match; try --list-models / --list-use-cases / --list-tags")
        return 1
    for n, r in enumerate(hits):
        if o["short"]:
            print("%-44s %s" % (r["id"], header(r, meta)))
            continue
        if n:
            print()
        print("## %s  (%s)" % (r["title"], r["id"]))
        print(header(r, meta))
        print()
        print("```text")
        print(r["prompt"])
        print("```")
        print()
        print("Why it works: " + r["why"])
        for rep in r.get("rendered_on", []):
            print("Rendered on %s, %s: %s" % (model_name(meta, rep["model"]), rep["date"], rep["result"]))
    if not o["short"]:
        print()
    print("%d prompt(s)" % len(hits))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
