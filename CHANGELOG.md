# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/).

## [0.1.0] - 2026-10-28

### Added

- Initial prompt list in `data/prompts/` across nine use cases (camera moves, product, portrait, nature, action, ads, anime, image-to-video, stills) for Kling 3.0, Veo 3, Wan 2.5, Runway Gen-4, Seedance 2.x, Flux, Nano Banana and GPT Image. Counts are produced by `scripts/stats.py`.
- `data/schema.json` and a stdlib validator (`scripts/validate.py`).
- `scripts/build.py` generating `prompts/by-model/`, `prompts/by-use-case/` and the README list and stats sections; `scripts/find.py` for searching; `scripts/stats.py` for counts.
- `SKILL.md` for Claude Code with adapters for Cursor, Codex and any `AGENTS.md` agent.
- References: per-model prompt notes with cited vendor guides, a vocabulary of camera, lens, light and motion terms, and Sora alternatives.
- Tests, CI workflow, issue and PR templates, repo metadata, banner, terminal demo and social preview.
