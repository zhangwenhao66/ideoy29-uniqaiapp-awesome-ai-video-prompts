#!/usr/bin/env python3
"""Validate every record in data/prompts/*.json against data/schema.json.

Usage:
  python3 scripts/validate.py            # prints a summary, exit 1 on any error
  python3 scripts/validate.py --quiet    # only errors

Hand-written validator, stdlib only (no jsonschema package). Checks: required fields, enums,
string lengths, id uniqueness and format, ISO dates, https URLs, duration present for video
modes, no duplicate prompt text, and that each file holds records of its own use case.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _lib import DATE_RE, ID_RE, ROOT, URL_RE, load_records, load_schema  # noqa: E402


def _check_str(errors, where, field, value, spec):
    if not isinstance(value, str):
        errors.append("%s: %s must be a string" % (where, field))
        return
    if "\n" in value and field in ("id", "title"):
        errors.append("%s: %s must be single-line" % (where, field))
    if "min" in spec and len(value) < spec["min"]:
        errors.append("%s: %s shorter than %d chars" % (where, field, spec["min"]))
    if "max" in spec and len(value) > spec["max"]:
        errors.append("%s: %s longer than %d chars" % (where, field, spec["max"]))
    if "enum" in spec and value not in spec["enum"]:
        errors.append("%s: %s=%r not in %s" % (where, field, value, spec["enum"]))
    if "pattern" in spec and not ID_RE.match(value):
        errors.append("%s: %s=%r is not kebab-case" % (where, field, value))
    if spec.get("type") == "date" and not DATE_RE.match(value):
        errors.append("%s: %s=%r is not an ISO date" % (where, field, value))
    if spec.get("type") == "url" and not URL_RE.match(value):
        errors.append("%s: %s=%r is not an https URL" % (where, field, value))


def validate(records_with_files, schema):
    spec = schema["record"]
    errors = []
    seen_ids = {}
    seen_prompts = {}
    for rec, fname in records_with_files:
        where = "%s#%s" % (fname, rec.get("id", "?"))
        if not isinstance(rec, dict):
            errors.append("%s: record is not an object" % where)
            continue
        for field, fspec in spec.items():
            required = fspec.get("required", False)
            rw = fspec.get("required_when")
            if rw and rec.get("mode") in rw.get("mode", []):
                required = True
            if field not in rec:
                if required:
                    errors.append("%s: missing %s" % (where, field))
                continue
            value = rec[field]
            t = fspec.get("type")
            if t == "string" or t in ("date", "url"):
                _check_str(errors, where, field, value, fspec)
            elif t == "integer":
                if not isinstance(value, int) or isinstance(value, bool):
                    errors.append("%s: %s must be an integer" % (where, field))
                elif value < fspec["min"] or value > fspec["max"]:
                    errors.append("%s: %s=%s outside %d..%d" % (where, field, value, fspec["min"], fspec["max"]))
            elif t == "array":
                if not isinstance(value, list):
                    errors.append("%s: %s must be a list" % (where, field))
                    continue
                if len(value) < fspec.get("min_items", 0):
                    errors.append("%s: %s needs at least %d items" % (where, field, fspec["min_items"]))
                if len(value) > fspec.get("max_items", 10**9):
                    errors.append("%s: %s has more than %d items" % (where, field, fspec["max_items"]))
                if len(value) != len(set(map(str, value))):
                    errors.append("%s: %s has duplicates" % (where, field))
                items = fspec.get("items", {})
                for it in value:
                    if isinstance(it, dict):
                        for sub, sspec in items.items():
                            if sub not in it:
                                if sspec.get("required"):
                                    errors.append("%s: %s item missing %s" % (where, field, sub))
                            else:
                                _check_str(errors, "%s.%s" % (where, field), sub, it[sub], sspec)
                    else:
                        _check_str(errors, where, field + "[]", it, items)
            elif t == "object":
                if not isinstance(value, dict):
                    errors.append("%s: %s must be an object" % (where, field))
                    continue
                for sub, sspec in fspec["fields"].items():
                    if sub not in value:
                        if sspec.get("required"):
                            errors.append("%s: %s.%s missing" % (where, field, sub))
                    else:
                        _check_str(errors, where, "%s.%s" % (field, sub), value[sub], sspec)
        for field in rec:
            if field not in spec:
                errors.append("%s: unknown field %s" % (where, field))
        rid = rec.get("id")
        if rid in seen_ids:
            errors.append("%s: duplicate id (also in %s)" % (where, seen_ids[rid]))
        seen_ids[rid] = fname
        ptxt = " ".join(str(rec.get("prompt", "")).split()).lower()
        if ptxt in seen_prompts:
            errors.append("%s: duplicate prompt text (same as %s)" % (where, seen_prompts[ptxt]))
        seen_prompts[ptxt] = rid
        expected = os.path.splitext(os.path.basename(fname))[0]
        if rec.get("use_case") != expected:
            errors.append("%s: use_case %r but file is %s.json" % (where, rec.get("use_case"), expected))
        if rec.get("mode") in ("t2i", "i2i") and "duration_s" in rec:
            errors.append("%s: duration_s on an image prompt" % where)
        if rec.get("mode") in ("t2v", "i2v") and any(m in ("flux", "nano-banana", "gpt-image") for m in rec.get("models", [])):
            errors.append("%s: image model listed on a video prompt" % where)
        if rec.get("mode") in ("t2i", "i2i") and any(m not in ("flux", "nano-banana", "gpt-image") for m in rec.get("models", [])):
            errors.append("%s: video model listed on an image prompt" % where)
        for r in rec.get("rendered_on", []) or []:
            if isinstance(r, dict) and r.get("model") not in rec.get("models", []):
                errors.append("%s: rendered_on model %r not in models" % (where, r.get("model")))
    return errors


def main(argv):
    quiet = "--quiet" in argv
    if "--help" in argv or "-h" in argv:
        print(__doc__.strip())
        return 0
    recs = load_records(with_file=True)
    errors = validate(recs, load_schema())
    for e in errors:
        print("error: " + e)
    if errors:
        print("%d error(s)" % len(errors))
        return 1
    if not quiet:
        files = sorted({f for _, f in recs})
        print("ok: %d records in %d files under %s" % (len(recs), len(files), os.path.relpath(os.path.join(ROOT, "data", "prompts"), ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
