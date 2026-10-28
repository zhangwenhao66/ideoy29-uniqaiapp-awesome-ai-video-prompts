"""Shared helpers for the awesome-ai-video-prompts scripts. Stdlib only."""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
PROMPTS_DIR = os.path.join(DATA, "prompts")

ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
URL_RE = re.compile(r"^https://[a-z0-9.-]+\.[a-z]{2,}(/[^\s\"'<>]*)?$", re.I)

MODE_LABEL = {"t2v": "text to video", "i2v": "image to video", "t2i": "text to image", "i2i": "image edit"}


def load_meta():
    with open(os.path.join(DATA, "meta.json"), encoding="utf-8") as f:
        return json.load(f)


def load_schema():
    with open(os.path.join(DATA, "schema.json"), encoding="utf-8") as f:
        return json.load(f)


def prompt_files():
    return sorted(
        os.path.join(PROMPTS_DIR, n) for n in os.listdir(PROMPTS_DIR) if n.endswith(".json")
    )


def load_records(with_file=False):
    """All records across data/prompts/*.json, in file order then record order."""
    out = []
    for path in prompt_files():
        with open(path, encoding="utf-8") as f:
            items = json.load(f)
        if not isinstance(items, list):
            raise ValueError("%s: top level must be a list" % os.path.relpath(path, ROOT))
        for rec in items:
            out.append((rec, os.path.relpath(path, ROOT)) if with_file else rec)
    return out


def model_name(meta, key):
    return meta["models"].get(key, {}).get("name", key)


def use_case_name(meta, key):
    return meta["use_cases"].get(key, key)


def slug_anchor(text):
    """GitHub-style heading anchor."""
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s+", "-", text)
