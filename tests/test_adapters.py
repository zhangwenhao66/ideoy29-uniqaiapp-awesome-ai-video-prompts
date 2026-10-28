"""Structure checks shared by every uniqaiapp repo: SKILL.md frontmatter, adapters point at it,
versions match, no forbidden strings, brand-only copyright."""
import json
import os
import re
import subprocess
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = "awesome-ai-video-prompts"
TEXT_EXT = {".md", ".json", ".py", ".yml", ".yaml", ".mdc", ".txt", ".svg", ".cff", ".editorconfig", ".gitattributes", ".gitignore", ""}
# Built from fragments so this file does not itself contain the strings it forbids.
FORBIDDEN = [
    "aeo" + "ria", "rich" + "peach", "/Use" + "rs/", "/Volu" + "mes/", "node_" + "modules",
    "sk-" + "ant-", "sk_" + "live", "api_" + "key=", "API_" + "KEY=<real", "TODO: " + "fill", "lorem " + "ipsum",
]
ALLOW_MARK = "# conventions-allow: abs-path"


def tracked_files():
    try:
        out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
        files = [l for l in out.splitlines() if l]
        if files:
            return files
    except Exception:
        pass
    files = []
    for d, dirs, names in os.walk(ROOT):
        dirs[:] = [x for x in dirs if x not in (".git", "__pycache__")]
        for n in names:
            files.append(os.path.relpath(os.path.join(d, n), ROOT))
    return files


def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert m, "no frontmatter in " + path
    fm = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^(\w[\w-]*):\s*(.*)$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip()
        mm = re.match(r"^\s+version:\s*(\S+)", line)
        if mm:
            fm["version"] = mm.group(1)
    return fm, text


class TestSkill(unittest.TestCase):
    def test_frontmatter(self):
        fm, text = frontmatter(os.path.join(ROOT, "SKILL.md"))
        self.assertEqual(fm["name"], REPO)
        self.assertEqual(fm["name"], os.path.basename(ROOT) if os.path.basename(ROOT) == REPO else REPO)
        desc = fm["description"]
        self.assertTrue(1 <= len(desc) <= 1024, "description length %d" % len(desc))
        self.assertNotIn("\n", desc)
        for trigger in ("Kling", "Veo", "text-to-video", "image-to-video"):
            self.assertIn(trigger, desc)
        self.assertLess(text.count("\n"), 500, "SKILL.md body over 500 lines")

    def test_versions_match(self):
        fm, _ = frontmatter(os.path.join(ROOT, "SKILL.md"))
        plugin = json.load(open(os.path.join(ROOT, ".claude-plugin", "plugin.json"), encoding="utf-8"))
        self.assertEqual(plugin["name"], REPO)
        self.assertEqual(plugin["version"], fm["version"])
        self.assertEqual(plugin["skills"], ["./"])
        changelog = open(os.path.join(ROOT, "CHANGELOG.md"), encoding="utf-8").read()
        top = re.search(r"^## \[(\d+\.\d+\.\d+)\]", changelog, re.M)
        self.assertIsNotNone(top)
        self.assertEqual(top.group(1), fm["version"])
        meta = json.load(open(os.path.join(ROOT, "data", "meta.json"), encoding="utf-8"))
        self.assertRegex(meta["updated"], r"^\d{4}-\d{2}-\d{2}$")
        self.assertIn("schema_version", meta)

    def test_adapters_point_at_skill(self):
        mdc = open(os.path.join(ROOT, ".cursor", "rules", REPO + ".mdc"), encoding="utf-8").read()
        self.assertIn("@SKILL.md", mdc)
        self.assertTrue(mdc.startswith("---\ndescription:"))
        for rel in ("AGENTS.md", os.path.join("codex", "INSTRUCTIONS.md")):
            self.assertIn("SKILL.md", open(os.path.join(ROOT, rel), encoding="utf-8").read(), rel)

    def test_repo_metadata(self):
        meta = json.load(open(os.path.join(ROOT, ".github", "repo.json"), encoding="utf-8"))
        self.assertEqual(meta["name"], REPO)
        self.assertTrue(meta["description"])
        self.assertLessEqual(len(meta["topics"]), 20)
        self.assertIn("utm_campaign=" + REPO, meta["homepage"])


class TestHygiene(unittest.TestCase):
    def test_no_forbidden_strings(self):
        hits = []
        for rel in tracked_files():
            ext = os.path.splitext(rel)[1].lower()
            if ext not in TEXT_EXT or rel.endswith(".png"):
                continue
            path = os.path.join(ROOT, rel)
            if not os.path.isfile(path):
                continue
            try:
                lines = open(path, encoding="utf-8").read().splitlines()
            except UnicodeDecodeError:
                continue
            for n, line in enumerate(lines, 1):
                low = line.lower()
                for s in FORBIDDEN:
                    if s.lower() in low and not (ALLOW_MARK in line and s == "/Volu" + "mes/"):
                        hits.append("%s:%d contains %r" % (rel, n, s))
        self.assertEqual(hits, [])

    def test_copyright_is_brand_only(self):
        for rel in tracked_files():
            path = os.path.join(ROOT, rel)
            if os.path.splitext(rel)[1].lower() not in TEXT_EXT or not os.path.isfile(path):
                continue
            try:
                text = open(path, encoding="utf-8").read()
            except UnicodeDecodeError:
                continue
            needle = "Copyright " + "(c)"
            for line in text.splitlines():
                if needle in line:
                    self.assertIn("UniqAI", line, "%s: %s" % (rel, line))

    def test_readme_links_and_footer(self):
        readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
        self.assertEqual(readme.count("Made by <a"), 1, "exactly one Made by UniqAI footer")
        for url in re.findall(r"https://uniqai\.app[^\s)\"'<>]*", readme):
            self.assertIn("utm_source=github", url, url)
            self.assertIn("utm_campaign=" + REPO, url, url)
        self.assertLessEqual(len(set(re.findall(r"https://uniqai\.app[^\s)\"'<>]*", readme))), 3)
        # relative links resolve
        for target in re.findall(r"\]\((?!https?://|#|mailto:)([^)#]+)", readme):
            self.assertTrue(os.path.exists(os.path.join(ROOT, target)), "broken relative link: " + target)


if __name__ == "__main__":
    unittest.main()
