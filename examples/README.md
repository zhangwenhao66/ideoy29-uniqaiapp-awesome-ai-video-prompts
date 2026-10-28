# Examples

Each file here is the exact output of one command, run from any directory. `tests/test_scripts.py` re-runs the commands and fails if the output differs, so these files are always current and the README's numbers can be checked.

| File | Command | Shows |
|:---|:---|:---|
| `find-kling-product.txt` | `python3 scripts/find.py --model kling-3 --use-case product` | full entries: prompt, why, render status |
| `find-veo-audio.txt` | `python3 scripts/find.py --model veo-3 --tag audio --short` | one line per hit |
| `find-id-compass.txt` | `python3 scripts/find.py --id kling-push-in-compass` | a single entry by id |
| `stats.txt` | `python3 scripts/stats.py` | the Markdown tables embedded in README.md |
| `stats.json` | `python3 scripts/stats.py --json` | the same numbers as JSON |

Regenerate all of them after changing data:

```bash
cd awesome-ai-video-prompts
python3 scripts/find.py --model kling-3 --use-case product > examples/find-kling-product.txt
python3 scripts/find.py --model veo-3 --tag audio --short > examples/find-veo-audio.txt
python3 scripts/find.py --id kling-push-in-compass > examples/find-id-compass.txt
python3 scripts/stats.py > examples/stats.txt
python3 scripts/stats.py --json > examples/stats.json
```

The before/after rewrites in the README "Examples" section are hand-written illustrations of the rules in `SKILL.md`; the "after" prompts are entries from `data/prompts/` so you can find them by id.
