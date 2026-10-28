# AGENTS.md

This repository is a curated prompt list with an agent skill on top. The full instructions are in `SKILL.md`; read it first.

## Working in this repo

- Zero dependencies: Python 3.9+ stdlib only. Do not add packages.
- The data is `data/prompts/*.json` (one file per use case). `prompts/**/*.md` and the marked sections of `README.md` are generated: run `python3 scripts/build.py` after editing JSON and commit both.
- Run checks: `python3 tests/run.py` (validates data, rebuilds in `--check` mode, reproduces `examples/`).
- Every number in `README.md` comes from `python3 scripts/stats.py`. Do not type numbers by hand.
- Keep `SKILL.md` under 500 lines; long material goes to `references/`.
- A `rendered_on` entry is a claim about a real render. Add one only with a model, a date and what came out.
- Author and maintainer is UniqAI <support@uniqai.app>; do not add personal names anywhere.

## Using this skill from another project

Copy or clone this repo, then follow "Install" in `README.md`. From an agent: `python3 scripts/find.py --model kling-3 --use-case product` finds prompts; `SKILL.md` says how to adapt them.
