# Contributing

Prompts, render reports and corrections are welcome. The list is only useful if every entry is specific and every claim is true, so the bar is: a prompt you would paste yourself, and a result note you actually observed.

## Add a prompt

1. Pick the use-case file in `data/prompts/` (`camera-moves`, `product`, `portrait`, `nature`, `action`, `ads`, `anime`, `image-to-video`, `stills`). Add one object with every field from `data/schema.json`:
   - `id` kebab-case, unique, starting with the first model key (`kling-…`, `veo-…`);
   - `prompt` verbatim, in English, no placeholders except "the photo" in image-to-video entries;
   - `models` the model(s) it is written for; `mode`; `duration_s` for video; `aspect`;
   - `why` one to three sentences about structure (which motion, which camera move, why that order), not adjectives;
   - `rendered_on` a list of `{model, date, result}`; leave it `[]` if you have not rendered it;
   - `guide` the vendor page the entry follows, with the date you checked it, if any; `added` today's date.
2. Run the checks and regenerate the Markdown:
   ```bash
   python3 scripts/validate.py
   python3 scripts/build.py
   python3 tests/run.py
   ```
   Commit the JSON together with the regenerated `prompts/**/*.md`, `README.md` and the translated `README.<lang>.md` files (`build.py` refreshes their generated blocks too, using the labels in `scripts/readme_i18n.py`; the hand-written text around the markers is translated by a person). If you changed the output of a command in `examples/README.md`, regenerate that file too.
3. Open a PR with the prompt in the description and, if you rendered it, a line on what you saw.

What is not accepted: prompts copied from another list or a vendor gallery (write your own; CC BY 4.0 applies to what you contribute), prompts that depend on readable text or logos, prompts naming real people or brands, and "cinematic, 8k, masterpiece" style tag soups.

## Report a render

The most valuable contribution. Use the "Report a render" issue template or edit `rendered_on` directly:

```json
{ "model": "kling-3", "date": "2026-11-02", "result": "5 s, 16:9. Orbit held, dust drifted as asked; laces jittered on the far side in 1 of 3 runs." }
```

Say what went wrong as well as what worked; that is what the next reader needs. One report per model per entry is enough; later reports replace earlier ones for the same model if the model changed.

## Fix a note or a source

Model guides move. If a `guide` URL is dead or the vendor changed the rule, update `references/model-notes.md` and the affected entries with the new date. Do not cite a page you did not open.

## Checks

`python3 tests/run.py` runs everything CI runs: schema validation, generated files in sync (`scripts/build.py --check`), examples reproduce byte-for-byte, structure and forbidden-string checks. Python 3.9+, no packages. Under ten seconds, no network.

## Deviations from org conventions

- The README follows the shared design-kit template (animated banner, badge row, `<details>` sections) rather than the older banner layout in CONVENTIONS section 5; the install block from section 4.1 is kept.
- The list is a data repo, so `LICENSE` is dual: CC BY 4.0 for `data/`, `prompts/` and `references/`, MIT for `scripts/` and `tests/`.
- `prompts/**/*.md` is generated and committed (awesome lists are read on GitHub, not built), with a test that fails when it drifts.
- Full translations of the README (`README.ru.md`, `README.zh-CN.md`, `README.es.md`, `README.pt-BR.md`, `README.ja.md`, `README.ko.md`) instead of the short `README.ru.md` from CONVENTIONS section 4.2; prompt titles, model names and keys stay English inside the generated list because they link into the English prompt pages.
