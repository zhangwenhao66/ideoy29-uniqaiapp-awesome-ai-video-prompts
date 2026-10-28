<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="awesome-ai-video-prompts by UniqAI" src="assets/banner.svg" width="1280" height="320">
</picture>

[![License: CC BY 4.0](https://img.shields.io/badge/license-CC_BY_4.0-d1fe17?style=flat-square&labelColor=0d0f12)](LICENSE)
[![Claude Code skill](https://img.shields.io/badge/Claude_Code-skill-d1fe17?style=flat-square&labelColor=0d0f12)](#インストール)
[![Cursor](https://img.shields.io/badge/Cursor-rules-d1fe17?style=flat-square&labelColor=0d0f12)](#インストール)
[![Codex](https://img.shields.io/badge/Codex-AGENTS.md-d1fe17?style=flat-square&labelColor=0d0f12)](#インストール)
[![Made by UniqAI](https://img.shields.io/badge/made_by-UniqAI-fdfc07?style=flat-square&labelColor=0d0f12)](https://uniqai.app/?utm_source=github&utm_medium=readme-ja&utm_campaign=awesome-ai-video-prompts)

**Kling 3.0、Veo 3、Wan 2.5、Runway、Seedance 向けの厳選 AI動画プロンプト集。モデル、設定、そして各プロンプトが効く理由付き。**

[クイックスタート](#クイックスタート) · [プロンプト一覧](#プロンプト一覧) · [仕組み](#仕組み) · [例](#例) · [インストール](#インストール) · [FAQ](#faq)

</div>

[English](README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Español](README.es.md) · [Português (BR)](README.pt-BR.md) · 日本語 · [한국어](README.ko.md)

# Awesome AI Video Prompts：AI動画プロンプト集、Kling 3.0・Veo 3・Wan・Runway・Seedance

Kling 3.0、Veo 3、Wan 2.5、Runway Gen-4、Seedance 2.x 向けの AI動画プロンプト（テキストから動画、画像から動画）を厳選したリストです。Flux、Nano Banana、GPT Image 向けの画像プロンプトも少数収録しています。各エントリには、コードブロック内のプロンプト、対象モデル、モード、長さ、アスペクト比、その構造が効く理由のメモ、そして誰かが実際のレンダリングを報告するまで空のままの `rendered_on` フィールドがあります。データは JSON で、Markdown ページと下の件数はそこから生成されます。

| **汎用ではなくモデル別** | **結果について正直** | **エージェントのスキルとして動く** |
|:---|:---|:---|
| 各プロンプトはベンダー自身のガイド（日付付きで引用）に従います。Kling はカメラワークをひとつだけ、Veo は音声を独立した一文に、Seedance はショットにラベルを付けます。 | 「対象モデル」と「レンダリング済みモデル」は別のフィールドです。この README の件数は `scripts/stats.py` の出力で、手入力ではありません。 | `SKILL.md` により、Claude Code、Cursor、Codex がリストを検索し、最も近いプロンプトをあなたのショットに合わせて調整できます。 |

## クイックスタート

```bash
git clone https://github.com/uniqaiapp/awesome-ai-video-prompts
cd awesome-ai-video-prompts
python3 scripts/find.py --model kling-3 --use-case product
```

該当するプロンプトがテキストで表示され、それぞれに `Why it works` の行と、レンダリング報告の有無が付きます。インストールするパッケージはありません。Python 3.9+ が必要です。ターミナルなしで見る場合は[モデル別](prompts/by-model/)または[用途別](prompts/by-use-case/)へ。

## デモ

<img alt="awesome-ai-video-prompts demo: searching the list with scripts/find.py and printing one entry" src="assets/demo.svg" width="820">

## リストの内容

<!-- generated:stats:start -->
| モデル | 対象プロンプト数 |
|:---|---:|
| Kling 3.0 (`kling-3`) | 32 |
| Veo 3 (`veo-3`) | 7 |
| Wan 2.5 (`wan-2.5`) | 12 |
| Runway Gen-4 family (`runway-gen-4`) | 3 |
| Seedance 2.x (`seedance-2`) | 6 |
| Flux (`flux`) | 6 |
| Nano Banana (Gemini image) (`nano-banana`) | 8 |
| GPT Image (`gpt-image`) | 8 |

| 用途 | プロンプト数 |
|:---|---:|
| カメラワーク | 9 |
| 商品 | 6 |
| ポートレート | 5 |
| 自然 | 5 |
| アクション | 5 |
| 広告 | 4 |
| アニメ | 4 |
| 画像から動画 | 6 |
| 静止画（画像プロンプト） | 8 |

| モード | プロンプト数 |
|:---|---:|
| テキストから動画 (`t2v`) | 38 |
| 画像から動画 (`i2v`) | 6 |
| テキストから画像 (`t2i`) | 6 |
| 画像編集 (`i2i`) | 2 |

合計 52 件のプロンプト：動画 44 件、画像 8 件。7 件にはレンダリング報告があり（`rendered_on` が空ではありません）、45 件はベンダーのプロンプトガイドまたは UniqAI のライブラリに基づいていますが、レンダリング報告はまだありません。
<!-- generated:stats:end -->

## プロンプト一覧

1 プロンプトにつき 1 行。リンク先にはプロンプト本文、効く理由のメモ、レンダリング報告があれば、それが載った完全なエントリがあります。モデルキー：`kling-3` Kling 3.0、`veo-3` Veo 3、`wan-2.5` Wan 2.5、`runway-gen-4` Runway Gen-4 ファミリー、`seedance-2` Seedance 2.x、`flux`、`nano-banana`、`gpt-image`。モード：`t2v` テキストから動画、`i2v` 画像から動画、`t2i` テキストから画像、`i2i` 画像編集。

<!-- generated:list:start -->
### カメラワーク

- [Brass compass, push in](prompts/by-use-case/camera-moves.md#brass-compass-push-in) · kling-3 · `t2v` · 5 s
- [Lit candle, pull back](prompts/by-use-case/camera-moves.md#lit-candle-pull-back) · kling-3 · `t2v` · 5 s
- [Harbour boats, pan left](prompts/by-use-case/camera-moves.md#harbour-boats-pan-left) · kling-3 · `t2v` · 5 s
- [Hiker on a ridge, tilt up](prompts/by-use-case/camera-moves.md#hiker-on-a-ridge-tilt-up) · kling-3 · `t2v` · 5 s
- [Bronze horse, orbit](prompts/by-use-case/camera-moves.md#bronze-horse-orbit) · kling-3 · `t2v` · 5 s
- [Lighthouse at dusk, dolly in with sound](prompts/by-use-case/camera-moves.md#lighthouse-at-dusk-dolly-in-with-sound) · veo-3 · `t2v` · 8 s
- [Old town rooftops, crane up](prompts/by-use-case/camera-moves.md#old-town-rooftops-crane-up) · wan-2.5, kling-3 · `t2v` · 5 s
- [Handheld follow through a corridor](prompts/by-use-case/camera-moves.md#handheld-follow-through-a-corridor) · runway-gen-4, seedance-2 · `t2v` · 5 s
- [Chrome droplet over a neon street, push in](prompts/by-use-case/camera-moves.md#chrome-droplet-over-a-neon-street-push-in) · kling-3 · `t2v` · 8 s

[「カメラワーク」のプロンプトをすべて全文で見る →](prompts/by-use-case/camera-moves.md)

### 商品

- [Headphones on a turntable](prompts/by-use-case/product.md#headphones-on-a-turntable) · kling-3 · `t2v` · 5 s
- [Perfume bottle, macro water drop](prompts/by-use-case/product.md#perfume-bottle-macro-water-drop) · kling-3 · `t2v` · 5 s
- [Sneaker, quarter orbit](prompts/by-use-case/product.md#sneaker-quarter-orbit) · kling-3 · `t2v` · 5 s
- [Coffee pour, slow motion with sound](prompts/by-use-case/product.md#coffee-pour-slow-motion-with-sound) · veo-3 · `t2v` · 8 s
- [Watch, two connected shots](prompts/by-use-case/product.md#watch-two-connected-shots) · seedance-2 · `t2v` · 10 s
- [Skincare jar, slow rotate on marble](prompts/by-use-case/product.md#skincare-jar-slow-rotate-on-marble) · kling-3, wan-2.5 · `t2v` · 5 s

[「商品」のプロンプトをすべて全文で見る →](prompts/by-use-case/product.md)

### ポートレート

- [Studio portrait, blink and smile](prompts/by-use-case/portrait.md#studio-portrait-blink-and-smile) · kling-3 · `t2v` · 5 s
- [Golden hour, push in to close-up](prompts/by-use-case/portrait.md#golden-hour-push-in-to-close-up) · kling-3 · `t2v` · 5 s
- [Dancer, track forward](prompts/by-use-case/portrait.md#dancer-track-forward) · kling-3 · `t2v` · 5 s
- [Portrait with one line of dialogue](prompts/by-use-case/portrait.md#portrait-with-one-line-of-dialogue) · veo-3 · `t2v` · 8 s
- [Rain on a window, portrait behind it](prompts/by-use-case/portrait.md#rain-on-a-window-portrait-behind-it) · wan-2.5, kling-3 · `t2v` · 5 s

[「ポートレート」のプロンプトをすべて全文で見る →](prompts/by-use-case/portrait.md)

### 自然

- [Mountain lake at sunrise, static wide](prompts/by-use-case/nature.md#mountain-lake-at-sunrise-static-wide) · kling-3 · `t2v` · 5 s
- [Coastal dune, tilt down](prompts/by-use-case/nature.md#coastal-dune-tilt-down) · kling-3 · `t2v` · 5 s
- [Autumn pond, push in](prompts/by-use-case/nature.md#autumn-pond-push-in) · kling-3 · `t2v` · 5 s
- [Thunderstorm over a plain, with sound](prompts/by-use-case/nature.md#thunderstorm-over-a-plain-with-sound) · veo-3 · `t2v` · 8 s
- [Tide pool, macro](prompts/by-use-case/nature.md#tide-pool-macro) · wan-2.5, kling-3 · `t2v` · 5 s

[「自然」のプロンプトをすべて全文で見る →](prompts/by-use-case/nature.md)

### アクション

- [Cyclist in the rain, tracking shot](prompts/by-use-case/action.md#cyclist-in-the-rain-tracking-shot) · kling-3 · `t2v` · 5 s
- [Wok flame, static camera](prompts/by-use-case/action.md#wok-flame-static-camera) · kling-3 · `t2v` · 5 s
- [Skateboarder, low-angle pass](prompts/by-use-case/action.md#skateboarder-low-angle-pass) · runway-gen-4, seedance-2 · `t2v` · 5 s
- [Alley chase, two connected shots](prompts/by-use-case/action.md#alley-chase-two-connected-shots) · seedance-2 · `t2v` · 10 s
- [Horse galloping on a beach, side tracking](prompts/by-use-case/action.md#horse-galloping-on-a-beach-side-tracking) · wan-2.5, kling-3, veo-3 · `t2v` · 5 s

[「アクション」のプロンプトをすべて全文で見る →](prompts/by-use-case/action.md)

### 広告

- [UGC-style handheld product talk, with disclosure](prompts/by-use-case/ads.md#ugc-style-handheld-product-talk-with-disclosure) · veo-3 · `t2v` · 8 s
- [Vertical product hero reveal](prompts/by-use-case/ads.md#vertical-product-hero-reveal) · kling-3, wan-2.5 · `t2v` · 5 s
- [App promo, three beats](prompts/by-use-case/ads.md#app-promo-three-beats) · seedance-2 · `t2v` · 10 s
- [Fabric in slow motion, space left for a logo](prompts/by-use-case/ads.md#fabric-in-slow-motion-space-left-for-a-logo) · runway-gen-4, kling-3, wan-2.5 · `t2v` · 5 s

[「広告」のプロンプトをすべて全文で見る →](prompts/by-use-case/ads.md)

### アニメ

- [Anime rooftop, wind and hair](prompts/by-use-case/anime.md#anime-rooftop-wind-and-hair) · wan-2.5, kling-3 · `t2v` · 5 s
- [Anime rain street, slow pan](prompts/by-use-case/anime.md#anime-rain-street-slow-pan) · kling-3, wan-2.5 · `t2v` · 5 s
- [Anime two-shot, reaction without dialogue](prompts/by-use-case/anime.md#anime-two-shot-reaction-without-dialogue) · seedance-2 · `t2v` · 10 s
- [Mecha hangar, tilt up](prompts/by-use-case/anime.md#mecha-hangar-tilt-up) · kling-3, wan-2.5 · `t2v` · 5 s

[「アニメ」のプロンプトをすべて全文で見る →](prompts/by-use-case/anime.md)

### 画像から動画

- [Portrait photo: blink and breeze](prompts/by-use-case/image-to-video.md#portrait-photo-blink-and-breeze) · kling-3 · `i2v` · 5 s
- [Table or still-life photo: steam and flame](prompts/by-use-case/image-to-video.md#table-or-still-life-photo-steam-and-flame) · kling-3 · `i2v` · 5 s
- [Landscape photo: clouds and ripples, pan](prompts/by-use-case/image-to-video.md#landscape-photo-clouds-and-ripples-pan) · kling-3 · `i2v` · 5 s
- [Illustration: gentle natural motion, keep the style](prompts/by-use-case/image-to-video.md#illustration-gentle-natural-motion-keep-the-style) · kling-3, wan-2.5 · `i2v` · 5 s
- [Product photo: quarter turn with sound](prompts/by-use-case/image-to-video.md#product-photo-quarter-turn-with-sound) · veo-3 · `i2v` · 8 s
- [City photo: traffic and lights come alive](prompts/by-use-case/image-to-video.md#city-photo-traffic-and-lights-come-alive) · wan-2.5, kling-3 · `i2v` · 5 s

[「画像から動画」のプロンプトをすべて全文で見る →](prompts/by-use-case/image-to-video.md)

### 静止画（画像プロンプト）

- [Catalogue product shot: stoneware teapot](prompts/by-use-case/stills.md#catalogue-product-shot-stoneware-teapot) · nano-banana, flux, gpt-image · `t2i` · レンダリング済み
- [Editorial studio portrait, real skin](prompts/by-use-case/stills.md#editorial-studio-portrait-real-skin) · flux, nano-banana, gpt-image · `t2i` · レンダリング済み
- [Golden-hour field portrait](prompts/by-use-case/stills.md#golden-hour-field-portrait) · flux, nano-banana, gpt-image · `t2i` · レンダリング済み
- [Neon night portrait, anamorphic](prompts/by-use-case/stills.md#neon-night-portrait-anamorphic) · flux, nano-banana, gpt-image · `t2i` · レンダリング済み
- [Black-and-white character study](prompts/by-use-case/stills.md#black-and-white-character-study) · flux, nano-banana, gpt-image · `t2i` · レンダリング済み
- [Edit: enhance a dim phone photo, change nothing else](prompts/by-use-case/stills.md#edit-enhance-a-dim-phone-photo-change-nothing-else) · nano-banana, gpt-image · `i2i` · レンダリング済み
- [Edit: selfie to business headshot, keep the face](prompts/by-use-case/stills.md#edit-selfie-to-business-headshot-keep-the-face) · nano-banana, gpt-image · `i2i`
- [Beauty portrait, freckles kept](prompts/by-use-case/stills.md#beauty-portrait-freckles-kept) · flux, nano-banana, gpt-image · `t2i` · レンダリング済み

[「静止画（画像プロンプト）」のプロンプトをすべて全文で見る →](prompts/by-use-case/stills.md)

### モデル別

- [Kling 3.0](prompts/by-model/kling-3.md) · 32 件 · 無音クリップ
- [Veo 3](prompts/by-model/veo-3.md) · 7 件 · 音声あり
- [Wan 2.5](prompts/by-model/wan-2.5.md) · 12 件 · 音声あり
- [Runway Gen-4 family](prompts/by-model/runway-gen-4.md) · 3 件 · 無音クリップ
- [Seedance 2.x](prompts/by-model/seedance-2.md) · 6 件 · 無音クリップ
- [Flux](prompts/by-model/flux.md) · 6 件 · 画像モデル
- [Nano Banana (Gemini image)](prompts/by-model/nano-banana.md) · 8 件 · 画像モデル
- [GPT Image](prompts/by-model/gpt-image.md) · 8 件 · 画像モデル
<!-- generated:list:end -->

## 仕組み

1. **すべてのモデルに共通の構造。** 被写体とその動作 → 舞台 → カメラワークひとつ（または「static camera」）→ レンズと光 → ムード。Kuaishou の Kling ガイドはまさにこの順序と「5 秒の動画に適した」動きを求め、Google の Veo ガイドは同じ要素を挙げたうえで音声を独立した一文として加えています。順序はモデル間で同じで、構文の細部が異なります。[`references/model-notes.md`](references/model-notes.md) にベンダーのページと確認日付きで一覧があります。
2. **動きはひとつ、カメラワークもひとつ。** すべての動画プロンプトは、速度と安定性の語を添えたカメラワークをひとつ（「slow, stable push in, no sudden motion」）と、5〜8 秒で完結する被写体の動作をひとつだけ指定します。副次的な動きは、髪を揺らす風、湯気、漂う塵、回転する光線といった安価で連続的なものから得ます。
3. **何が静止しているかを書く。** ネガティブプロンプト（多くのフロントエンドで Kling にはありません）の代わりに、エントリは変わってはいけないものを明記します。「static camera, product centred」、画像から動画なら「keep the framing, background and art style exactly as in the photo」のように。
4. **モデルが対応する場合のみ音声とマルチショット。** Veo のエントリは `Audio: …` と `No music` で終わり、セリフは `She says: "…"` と書きます。Seedance のエントリは `Shot 1` と `Shot 2` にラベルを付け、衣装・レンズ・光をショット間で同一に保ちます。
5. **JSON が唯一のソース。** `data/prompts/<use-case>.json` がレコードを持ち、`data/schema.json` が仕様、`scripts/validate.py` がそれを検証し、`scripts/build.py` が `prompts/**/*.md` とこの README の生成セクション 2 つを書き出します。ずれがあればテストが失敗します。

```
data/prompts/*.json  ──validate.py──▶  ok
        │
        └──build.py──▶  prompts/by-model/*.md
                        prompts/by-use-case/*.md
                        README.md (stats + list sections)
```

同じプロンプトを Kling 3.0、Veo 3、Wan 2.5 で並べて比較するには、[UniqAI がひとつの入力欄から 3 つすべてを実行できます](https://uniqai.app/video?utm_source=github&utm_medium=readme-ja&utm_campaign=awesome-ai-video-prompts)。これらのモデルを提供する他のツールでも同じように使えます。

## 例

<details>
<summary><b>曖昧なプロンプト → カメラワークひとつの Kling 3.0 プロンプト</b></summary>

**Before**

```text
A perfume bottle, cinematic, luxury, 4k, slow motion, beautiful lighting.
```

**After**（`kling-perfume-macro-drop`）

```text
A glass bottle of amber perfume standing on wet black slate, a single water drop running down the glass. Slow push in on the bottle. 90 mm macro lens, soft backlight through the liquid, small specular highlights. Elegant, quiet atmosphere.
```

動きひとつ（滴）、カメラワークひとつ（push in）、レンズ、光の方向、ムード。「4k」と「cinematic」は消えました。これらは設定と形容詞であって、指示ではありません。

</details>

<details>
<summary><b>Sora 風プロンプト → 音声付きの Veo 3 プロンプト</b></summary>

**Before**

```text
A golden retriever runs along a beach at sunset, cinematic, shallow depth of field.
```

**After**

```text
Tracking shot at ground level: a golden retriever runs along a wet beach at sunset, waves rolling in behind it. Shallow depth of field, warm light. Sound: surf and paws on sand.
```

カメラワークに名前があり、動きが具体的で、音が列挙されています。Sora プロンプトの移行については [`references/sora-alternatives.md`](references/sora-alternatives.md) を参照してください。

</details>

<details>
<summary><b>写真 → 画像から動画のプロンプト</b></summary>

**Before**

```text
Make this photo move.
```

**After**（`kling-i2v-portrait-blink-breeze`）

```text
The person blinks and smiles slightly, hair moving in a light breeze. Static camera.
```

写真の場合、プロンプトは動きだけを記述します。被写体、光、構図はすでに写真にあるからです。挙げた 3 つの動きは、顔を崩さずに済むものです。

</details>

<details>
<summary><b>エージェントから使う</b></summary>

```text
You: I need a vertical product reveal for earbuds, Kling, 5 seconds.
Agent (with the skill): runs python3 scripts/find.py --use-case ads --model kling-3,
  picks kling-hero-product-reveal-vertical, swaps "earbud case" details for yours,
  returns the prompt in a code block and notes that the source entry has no render report yet.
```

</details>

## インストール

指示ファイルを読むエージェントならどれでも使えます。お使いのものを選んでください。

<details open>
<summary><b>Claude Code</b>（スキルとして）</summary>

```bash
git clone https://github.com/uniqaiapp/awesome-ai-video-prompts ~/.claude/skills/awesome-ai-video-prompts
```

その後、Claude Code で `/awesome-ai-video-prompts` と入力するか、タスクを説明するだけで、スキルの説明文がトリガーになります。グローバルではなくプロジェクト単位で使う場合は、プロジェクト内の `.claude/skills/awesome-ai-video-prompts` にクローンします。

uniqaiapp マーケットプレイスの公開後は、プラグインとして：

```
/plugin marketplace add uniqaiapp/skills
/plugin install awesome-ai-video-prompts@uniqaiapp
```

</details>

<details>
<summary><b>Cursor</b></summary>

`SKILL.md`、`scripts/`、`data/`、`references/`、[`.cursor/rules/awesome-ai-video-prompts.mdc`](.cursor/rules/awesome-ai-video-prompts.mdc) をプロジェクトにコピーします。ルールファイルにスキルが埋め込まれています。

</details>

<details>
<summary><b>Codex / AGENTS.md を読む任意のエージェント</b></summary>

`SKILL.md`、`scripts/`、`data/`、`references/` を `.agents/skills/awesome-ai-video-prompts/` にコピーし、[`codex/INSTRUCTIONS.md`](codex/INSTRUCTIONS.md) のスニペットを自分の `AGENTS.md` に追加します。

</details>

<details>
<summary><b>エージェントなしで</b></summary>

各スクリプトは単体で動きます：`python3 scripts/find.py --help`、`python3 scripts/stats.py`、`python3 scripts/validate.py`。または [`SKILL.md`](SKILL.md) を任意のモデルのシステムプロンプトに貼り付けてください。frontmatter 以外にエージェント固有の構文はありません。

</details>

要件：Python 3.9+。インストールするパッケージはありません。

## 制限と正直な注記

- **「対象モデル」は「レンダリング済み」ではありません。** ほとんどのエントリは `rendered_on` が空の状態から始まります。引用付きのベンダーガイドに従うか UniqAI のプロンプトライブラリから来たものであり、それは構造についての主張であって、見られるクリップについての主張ではありません。報告のあるエントリは本文中にそう書いてあります。「Report a render」issue テンプレートが報告を集める手段です。
- **画像プロンプトは GPT Image でレンダリングされました。** UniqAI サイト向けです（日付は `rendered_on` にあります）。Flux と Nano Banana については、正しい語彙ではあっても検証済みの結果ではありません。
- **このリリースでは Runway に引用できるガイドがありません。** Runway のヘルプセンターが取得を拒否したため、Runway のエントリは一般的な慣行に従い、その旨を明記しています。
- **バージョンは動きます。** 各 `guide` には確認日が付いています。Kling 4.0 は 2026 年 10 月に発表されました（プレスリリースは `references/model-notes.md` の出典に引用）。Kling のエントリは 3.0 のガイドに基づいて書かれています。
- この README のすべての数字は `data/prompts/` に対する `python3 scripts/stats.py` が生成します。生成ブロックが古いか、手書きの文章に件数が現れると、テストスイートが失敗します。

## FAQ

<details>
<summary><b>Kling 3.0 のプロンプトはどのくらいの長さにすべきですか？</b></summary>

短い文を 2〜4 つ。被写体とその動作、舞台、カメラワークひとつ、そしてレンズ、光、ムードです。Kuaishou のガイドは語数ではなく、簡単な言葉と短い文を求めています。互いに競合する指示を長く並べると、ひとつの明快なシーンより予測しにくいレンダリングになります。

</details>

<details>
<summary><b>Kling のプロンプトを Veo 3 で使えますか？</b></summary>

おおむね使えます。`Audio:` の一文を加え（Veo は音を生成し、指定しなければ勝手に作ります）、音楽が不要なら `No music` で締めてください。Veo は Kling よりカメラワークの重ね掛けに強いですが、それでもひとつのほうがきれいに出ます。

</details>

<details>
<summary><b>ネガティブプロンプトはどこですか？</b></summary>

ありません。いくつかのフロントエンドは Kling にネガティブ欄を用意していないため、エントリは代わりに何が静止すべきかを記述します。「static camera, product centred」は「no camera shake」より効果があり、どのモデルにも移植できます。

</details>

<details>
<summary><b>これは Sora のプロンプト集ですか？</b></summary>

いいえ。OpenAI の廃止一覧ページでは、Sora 2 API モデルは 2026 年 9 月 24 日に削除されたとされています。Sora プロンプトの構造は移植できます。[`references/sora-alternatives.md`](references/sora-alternatives.md) に、各種プロンプトの今の行き先があります。

</details>

<details>
<summary><b>なぜ Markdown だけでなく JSON なのですか？</b></summary>

エージェントやスクリプトがモデル・モード・タグで絞り込めるように、スキーマが「理由」とレンダリングのフィールドを必須にできるように、そして Markdown がデータと食い違わないようにするためです。それでも Markdown はコミットしています。GitHub で awesome リストを読むのはそういう形だからです。

</details>

## 関連プロジェクト

- [`video-director`](https://github.com/uniqaiapp/video-director)：一行のアイデアを AI動画モデル（Kling、Veo、Sora など）向けのショットごとのプロンプトに変換。カメラ、ライティング、動きの語彙付き。絵コンテにはこちらを、個々のショットにはこのリストを。
- [`no-plastic`](https://github.com/uniqaiapp/no-plastic)：自然に見える AI ポートレートのためのプロンプトルールとチェッカー。肌の質感、ライティング、レンズ選びでプラスチック感を避けます。
- [`ai-video-pricing`](https://github.com/uniqaiapp/ai-video-pricing)：手作業で確認した AI動画生成の料金表。秒単位とクリップ単位で、各行に出典 URL と確認日付き。

## コントリビュート

issue と pull request を歓迎します。「理由」付きの新しいプロンプト、レンダリング報告、修正した出典など。エントリの形式とローカルでのチェックは [CONTRIBUTING.md](CONTRIBUTING.md) を参照してください（`python3 tests/run.py`、依存パッケージなし）。

## ライセンス

プロンプト、データ、参考資料：[CC BY 4.0](LICENSE)、表記は「UniqAI, https://github.com/uniqaiapp/awesome-ai-video-prompts」。スクリプトとテスト：[MIT](LICENSE) © UniqAI。

---

<div align="center">

<sub>制作：<a href="https://uniqai.app/?utm_source=github&utm_medium=readme-ja&utm_campaign=awesome-ai-video-prompts">UniqAI</a>、AI写真・動画・チャットのアプリ。Kling のエントリは、私たちが自社ユーザー向けに公開しているプロンプトライブラリそのものです。</sub>

</div>
