"""Each script's --help exits 0; each example in examples/ reproduces its committed output byte-for-byte."""
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = ["validate.py", "build.py", "find.py", "stats.py"]
EXAMPLES = {
    "find-kling-product.txt": ["find.py", "--model", "kling-3", "--use-case", "product"],
    "find-veo-audio.txt": ["find.py", "--model", "veo-3", "--tag", "audio", "--short"],
    "find-id-compass.txt": ["find.py", "--id", "kling-push-in-compass"],
    "stats.txt": ["stats.py"],
    "stats.json": ["stats.py", "--json"],
}


def run(args):
    return subprocess.run([sys.executable, os.path.join(ROOT, "scripts", args[0])] + args[1:],
                          capture_output=True, text=True, cwd="/")


class TestScripts(unittest.TestCase):
    def test_help_exits_zero(self):
        for s in SCRIPTS:
            p = run([s, "--help"])
            self.assertEqual(p.returncode, 0, s)
            self.assertIn("Usage", p.stdout, s)

    def test_examples_reproduce(self):
        for name, args in EXAMPLES.items():
            expected = open(os.path.join(ROOT, "examples", name), encoding="utf-8").read()
            p = run(args)
            self.assertEqual(p.returncode, 0, name + ": " + p.stderr)
            self.assertEqual(p.stdout, expected, name + " is stale; regenerate per examples/README.md")

    def test_find_no_match_exits_one(self):
        p = run(["find.py", "--model", "kling-3", "--tag", "no-such-tag"])
        self.assertEqual(p.returncode, 1)

    def test_find_json(self):
        p = run(["find.py", "--id", "kling-push-in-compass", "--json"])
        self.assertEqual(p.returncode, 0)
        self.assertIn('"id": "kling-push-in-compass"', p.stdout)


if __name__ == "__main__":
    unittest.main()
