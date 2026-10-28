"""Every record validates, ids and prompts are unique, generated Markdown is in sync, and
the README quotes only numbers that scripts/stats.py produces."""
import os
import re
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from _lib import load_meta, load_records, load_schema  # noqa: E402
from stats import compute  # noqa: E402
from validate import validate  # noqa: E402


class TestData(unittest.TestCase):
    def test_validates(self):
        errors = validate(load_records(with_file=True), load_schema())
        self.assertEqual(errors, [])

    def test_validator_catches_bad_records(self):
        schema = load_schema()
        bad = [({"id": "Bad ID", "title": "x", "use_case": "nope", "mode": "t2v", "models": ["kling-3"],
                 "aspect": "16:9", "prompt": "short", "why": "short", "tags": [], "rendered_on": [], "added": "2026"}, "data/prompts/product.json")]
        errors = validate(bad, schema)
        joined = "\n".join(errors)
        for needle in ("kebab-case", "use_case", "duration_s", "shorter than", "needs at least", "ISO date"):
            self.assertIn(needle, joined)

    def test_every_entry_has_why_and_structure(self):
        for r in load_records():
            self.assertTrue(r["why"].strip().endswith("."), r["id"])
            if r["mode"] in ("t2v", "i2v"):
                low = r["prompt"].lower()
                self.assertTrue(
                    any(k in low for k in ("camera", "push in", "pull back", "pan ", "tilt", "orbit", "track", "dolly", "crane", "handheld", "shot")),
                    "%s: video prompt names no camera" % r["id"])
            if "veo-3" in r["models"] and r["mode"] in ("t2v", "i2v") and "audio" in r["tags"]:
                self.assertIn("Audio:", r["prompt"], r["id"])
            if "seedance-2" in r["models"] and "multi-shot" in r["tags"]:
                self.assertIn("Shot 2", r["prompt"], r["id"])

    def test_meta_covers_enums(self):
        meta, schema = load_meta(), load_schema()
        self.assertEqual(set(meta["models"]), set(schema["record"]["models"]["items"]["enum"]))
        self.assertEqual(set(meta["use_cases"]), set(schema["record"]["use_case"]["enum"]))

    def test_generated_files_in_sync(self):
        p = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "build.py"), "--check"], capture_output=True, text=True, cwd=ROOT)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)

    def test_readme_numbers_come_from_stats(self):
        readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
        stats = compute(load_records(), load_meta())
        start, end = readme.index("<!-- generated:stats:start -->"), readme.index("<!-- generated:stats:end -->")
        self.assertIn("%d prompts in total" % stats["total"], readme[start:end])
        # the hand-written parts of the README must not quote a prompt count
        hand = readme[:start] + readme[readme.index("<!-- generated:list:end -->"):]
        hand = hand.split("<!-- generated:list:start -->")[0] if "<!-- generated:list:start -->" in hand else hand
        for m in re.findall(r"\b(\d{2,})\s+prompts?\b", hand):
            self.fail("hand-written README text quotes a prompt count (%s); use the generated stats block" % m)


if __name__ == "__main__":
    unittest.main()
