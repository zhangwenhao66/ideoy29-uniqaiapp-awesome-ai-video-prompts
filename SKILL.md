---
name: awesome-ai-video-prompts
description: Picks and adapts a proven AI video or image prompt from a curated, categorised list (Kling 3.0, Veo 3, Wan 2.5, Runway Gen-4, Seedance, Flux, Nano Banana) and rewrites it for the user's model, mode and use case (camera moves, product, portrait, nature, action, ads, anime, image-to-video, stills). Use when the user asks for an AI video prompt, a text-to-video or image-to-video prompt, a Kling, Veo, Wan, Runway or Seedance prompt, "how do I prompt X", a camera-move or product-shot prompt, or pastes a weak prompt and wants it fixed. Not for storyboarding a multi-scene film (use video-director), for fixing plastic skin in portraits (use no-plastic), or for pricing questions (use ai-video-pricing).
license: CC-BY-4.0
metadata:
  version: 0.1.0
  author: UniqAI
  homepage: https://github.com/uniqaiapp/awesome-ai-video-prompts
---

# Awesome AI video prompts: pick, adapt, report

This repo is a curated list of AI video and image prompts stored as JSON in `data/prompts/` and rendered to Markdown in `prompts/`. Every entry has the prompt, the models it was written for, mode (`t2v`, `i2v`, `t2i`, `i2i`), duration, aspect, a "why it works" note, and a `rendered_on` list that is empty until somebody reports a real render. The skill's job is to get the user a prompt that fits their model and use case, written in the structure that these models respond to, and to be honest about which entries are reported as rendered and which are not.

## When to use

- The user asks for a prompt for Kling, Veo, Wan, Runway or Seedance, or says "text to video prompt", "image to video prompt", "AI video prompt".
- The user wants a specific shot: a push in, orbit, tracking shot, product turntable, portrait with a blink, a UGC-style vertical ad, an anime scene.
- The user pastes a vague prompt ("a dog on a beach, cinematic") and wants it to render predictably.
- The user has a photo and wants it animated (image-to-video).
- The user asks which model to write for when audio, multi-shot or a vertical ad matters.

## When NOT to use

- Multi-scene storyboards with continuity across many clips: `video-director` does the shot list; come back here for individual prompts.
- Portrait realism problems (plastic skin, dead eyes) in still images: `no-plastic`.
- "How much does a clip cost" or model pricing: `ai-video-pricing`.
- Prompts for text, code or music models.

## How it works

1. **Identify model, mode, use case.** If the user did not say, ask one question at most, otherwise default to `kling-3`, `t2v`, 5 s, 16:9. Map wording: "animate this photo" = `i2v`; "with sound / dialogue" = `veo-3` or `wan-2.5`; "several shots in one clip" = `seedance-2`; "vertical / TikTok / Reels" = aspect `9:16`.
2. **Search the list first.** Run `python3 scripts/find.py --model <m> --use-case <uc>` (add `--tag`, `--grep`, `--mode`). Read the hits; pick the closest. If nothing fits, use `--list-use-cases` and `--list-tags` to look once more before writing from scratch.
3. **Adapt, keep the structure.** Rewrite the chosen prompt for the user's subject while keeping the order these models expect: *subject and what it does → setting → one camera move (or "static camera") → lens, light → mood*. Rules by model are in `references/model-notes.md`; vocabulary (camera moves, light, motion words) is in `references/vocabulary.md`. Specifically:
   - One main camera move per clip. Name it with a speed and a stability word ("slow, stable push in, no sudden motion").
   - One action the clip can finish in 5 to 8 seconds. No counting, no complex physics.
   - Say what stays still, instead of a negative prompt (Kling in many UIs has no negative field).
   - Veo 3: audio in its own sentence ("Audio: …"); dialogue as `She says: "…"`; add "No music" unless music is wanted.
   - Wan 2.5: 5 s clips, audio supported; keep the prompt in the same order.
   - Seedance: label shots ("Shot 1: … Shot 2: …"), keep clothing, light and lens identical across shots.
   - Image-to-video: describe only the motion, then lock everything else ("keep the framing, background and art style exactly as in the photo").
   - Never ask a model to render readable text or a logo; leave empty space and composite later.
4. **Return the prompt in a code block**, then one or two lines of "why" and one line that says whether the source entry has a render report (`rendered_on`) or not. Do not claim a prompt was tested if its `rendered_on` is empty.
5. **If the user renders it, offer a report.** Ask for model, date and one sentence on what came out (including what went wrong), and either add it to `rendered_on` in the JSON (then run `python3 scripts/build.py` and `python3 scripts/validate.py`) or point them to the "Report a render" issue template.

## Inputs / outputs

| Input | Output |
|:---|:---|
| Model, mode, use case, a subject (or a weak prompt, or a photo description) | One prompt in a code block, in the model's structure; a "why" note; render-report status |
| `python3 scripts/find.py …` | Matching entries as text or `--json` |
| A completed render | A `rendered_on` entry (model, date, result) added by PR |

## Examples

- `python3 scripts/find.py --model kling-3 --use-case product` → `examples/find-kling-product.txt`
- `python3 scripts/find.py --model veo-3 --tag audio --short` → `examples/find-veo-audio.txt`
- `python3 scripts/stats.py` → `examples/stats.txt` (the counts the README quotes)
- Before/after rewrites of weak prompts: README "Examples" section.

## Limits

- "Written for" is not "rendered on". The `rendered_on` field is the only claim of a result; most entries start without one.
- Model behaviour changes with versions. Each vendor guide the list follows is cited with the date it was checked (`guide` field); re-check before relying on syntax details.
- Runway's prompting guide could not be fetched when this list was built, so Runway entries follow general practice (static or simple camera, one motion), not a cited vendor rule.
- The list covers English prompts only.

## References

- `references/model-notes.md`: per-model syntax, durations, audio, cited guides.
- `references/vocabulary.md`: camera moves, lenses, light, motion words that models respond to.
- `references/sora-alternatives.md`: what to use instead of Sora after its API shutdown, with the same prompts.
- `CONTRIBUTING.md`: entry format, render reports, checks.
