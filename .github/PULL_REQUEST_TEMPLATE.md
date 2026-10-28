**What changed**

**How to test**

```bash
python3 scripts/validate.py && python3 scripts/build.py --check && python3 tests/run.py
```

**Honesty check**

- [ ] Any new `rendered_on` entry describes a render I actually did (model, date, what I saw).
- [ ] Any new number in README/notes comes from `scripts/stats.py` or has a cited, dated source.
- [ ] Prompts are my own text (CC BY 4.0), not copied from another list or a vendor gallery.
- [ ] No personal names, secrets or absolute local paths added.
- [ ] I ran `python3 scripts/build.py` and committed the regenerated `prompts/` and `README.md`.
