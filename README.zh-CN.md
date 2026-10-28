<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="awesome-ai-video-prompts by UniqAI" src="assets/banner.svg" width="1280" height="320">
</picture>

[![License: CC BY 4.0](https://img.shields.io/badge/license-CC_BY_4.0-d1fe17?style=flat-square&labelColor=0d0f12)](LICENSE)
[![Claude Code skill](https://img.shields.io/badge/Claude_Code-skill-d1fe17?style=flat-square&labelColor=0d0f12)](#安装)
[![Cursor](https://img.shields.io/badge/Cursor-rules-d1fe17?style=flat-square&labelColor=0d0f12)](#安装)
[![Codex](https://img.shields.io/badge/Codex-AGENTS.md-d1fe17?style=flat-square&labelColor=0d0f12)](#安装)
[![Made by UniqAI](https://img.shields.io/badge/made_by-UniqAI-fdfc07?style=flat-square&labelColor=0d0f12)](https://uniqai.app/?utm_source=github&utm_medium=readme-zh-cn&utm_campaign=awesome-ai-video-prompts)

**精选 AI 视频提示词：Kling 3.0、Veo 3、Wan 2.5、Runway 和 Seedance，每条都注明模型、参数设置，以及它为什么有效。**

[快速开始](#快速开始) · [提示词列表](#提示词列表) · [工作原理](#工作原理) · [示例](#示例) · [安装](#安装) · [FAQ](#faq)

</div>

[English](README.md) · [Русский](README.ru.md) · 简体中文 · [Español](README.es.md) · [Português (BR)](README.pt-BR.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

# Awesome AI Video Prompts：AI 视频提示词大全，Kling 3.0、Veo 3、Wan、Runway、Seedance

一份精选的 AI 视频提示词列表（文生视频和图生视频），面向 Kling（可灵）3.0、Veo 3、Wan 2.5、Runway Gen-4 和 Seedance 2.x，另附一小组面向 Flux、Nano Banana 和 GPT Image 的图像提示词。每个条目都包含代码块中的提示词、所针对的模型、模式、时长、画幅比例、一条关于这种结构为什么有效的说明，以及一个 `rendered_on` 字段，在有人报告真实渲染结果之前它一直为空。数据是 JSON；Markdown 页面和下面的统计数字都由它生成。

| **针对具体模型，而非泛泛而谈** | **对结果诚实** | **可作为 agent skill 使用** |
|:---|:---|:---|
| 每条提示词都遵循厂商自己的指南（附引用和日期）：Kling 只用一个运镜，Veo 的音频单独成句，Seedance 用带标签的分镜。 | “为谁编写”和“在哪渲染”是两个独立字段。本 README 中的数字来自 `scripts/stats.py`，不是手敲的。 | `SKILL.md` 让 Claude Code、Cursor 或 Codex 可以搜索列表，并把最接近的提示词改成你要的镜头。 |

## 快速开始

```bash
git clone https://github.com/uniqaiapp/awesome-ai-video-prompts
cd awesome-ai-video-prompts
python3 scripts/find.py --model kling-3 --use-case product
```

你会得到匹配的提示词文本，每条带一行 `Why it works`，并标明是否有人报告过渲染结果。无需安装任何包；Python 3.9+。不想用终端也可以直接浏览：[按模型](prompts/by-model/)或[按用途](prompts/by-use-case/)。

## 演示

<img alt="awesome-ai-video-prompts demo: searching the list with scripts/find.py and printing one entry" src="assets/demo.svg" width="820">

## 列表里有什么

<!-- generated:stats:start -->
| 模型 | 为其编写的提示词数 |
|:---|---:|
| Kling 3.0 (`kling-3`) | 32 |
| Veo 3 (`veo-3`) | 7 |
| Wan 2.5 (`wan-2.5`) | 12 |
| Runway Gen-4 family (`runway-gen-4`) | 3 |
| Seedance 2.x (`seedance-2`) | 6 |
| Flux (`flux`) | 6 |
| Nano Banana (Gemini image) (`nano-banana`) | 8 |
| GPT Image (`gpt-image`) | 8 |

| 用途 | 提示词数 |
|:---|---:|
| 运镜 | 9 |
| 产品 | 6 |
| 人像 | 5 |
| 自然风光 | 5 |
| 动作 | 5 |
| 广告 | 4 |
| 动漫 | 4 |
| 图生视频 | 6 |
| 静态图（图像提示词） | 8 |

| 模式 | 提示词数 |
|:---|---:|
| 文生视频 (`t2v`) | 38 |
| 图生视频 (`i2v`) | 6 |
| 文生图 (`t2i`) | 6 |
| 图像编辑 (`i2i`) | 2 |

共 52 条提示词：视频 44 条，图像 8 条。其中 7 条附有渲染报告（`rendered_on` 非空）；45 条依据厂商提示词指南或 UniqAI 提示词库编写，但尚无渲染报告。
<!-- generated:stats:end -->

## 提示词列表

每条提示词一行；链接打开完整条目，包含提示词文本、“为什么有效”的说明和已有的渲染报告。模型键：`kling-3` Kling 3.0，`veo-3` Veo 3，`wan-2.5` Wan 2.5，`runway-gen-4` Runway Gen-4 系列，`seedance-2` Seedance 2.x，`flux`，`nano-banana`，`gpt-image`。模式：`t2v` 文生视频，`i2v` 图生视频，`t2i` 文生图，`i2i` 图像编辑。

<!-- generated:list:start -->
### 运镜

- [Brass compass, push in](prompts/by-use-case/camera-moves.md#brass-compass-push-in) · kling-3 · `t2v` · 5 s
- [Lit candle, pull back](prompts/by-use-case/camera-moves.md#lit-candle-pull-back) · kling-3 · `t2v` · 5 s
- [Harbour boats, pan left](prompts/by-use-case/camera-moves.md#harbour-boats-pan-left) · kling-3 · `t2v` · 5 s
- [Hiker on a ridge, tilt up](prompts/by-use-case/camera-moves.md#hiker-on-a-ridge-tilt-up) · kling-3 · `t2v` · 5 s
- [Bronze horse, orbit](prompts/by-use-case/camera-moves.md#bronze-horse-orbit) · kling-3 · `t2v` · 5 s
- [Lighthouse at dusk, dolly in with sound](prompts/by-use-case/camera-moves.md#lighthouse-at-dusk-dolly-in-with-sound) · veo-3 · `t2v` · 8 s
- [Old town rooftops, crane up](prompts/by-use-case/camera-moves.md#old-town-rooftops-crane-up) · wan-2.5, kling-3 · `t2v` · 5 s
- [Handheld follow through a corridor](prompts/by-use-case/camera-moves.md#handheld-follow-through-a-corridor) · runway-gen-4, seedance-2 · `t2v` · 5 s
- [Chrome droplet over a neon street, push in](prompts/by-use-case/camera-moves.md#chrome-droplet-over-a-neon-street-push-in) · kling-3 · `t2v` · 8 s

[查看全部「运镜」提示词（含完整文本）→](prompts/by-use-case/camera-moves.md)

### 产品

- [Headphones on a turntable](prompts/by-use-case/product.md#headphones-on-a-turntable) · kling-3 · `t2v` · 5 s
- [Perfume bottle, macro water drop](prompts/by-use-case/product.md#perfume-bottle-macro-water-drop) · kling-3 · `t2v` · 5 s
- [Sneaker, quarter orbit](prompts/by-use-case/product.md#sneaker-quarter-orbit) · kling-3 · `t2v` · 5 s
- [Coffee pour, slow motion with sound](prompts/by-use-case/product.md#coffee-pour-slow-motion-with-sound) · veo-3 · `t2v` · 8 s
- [Watch, two connected shots](prompts/by-use-case/product.md#watch-two-connected-shots) · seedance-2 · `t2v` · 10 s
- [Skincare jar, slow rotate on marble](prompts/by-use-case/product.md#skincare-jar-slow-rotate-on-marble) · kling-3, wan-2.5 · `t2v` · 5 s

[查看全部「产品」提示词（含完整文本）→](prompts/by-use-case/product.md)

### 人像

- [Studio portrait, blink and smile](prompts/by-use-case/portrait.md#studio-portrait-blink-and-smile) · kling-3 · `t2v` · 5 s
- [Golden hour, push in to close-up](prompts/by-use-case/portrait.md#golden-hour-push-in-to-close-up) · kling-3 · `t2v` · 5 s
- [Dancer, track forward](prompts/by-use-case/portrait.md#dancer-track-forward) · kling-3 · `t2v` · 5 s
- [Portrait with one line of dialogue](prompts/by-use-case/portrait.md#portrait-with-one-line-of-dialogue) · veo-3 · `t2v` · 8 s
- [Rain on a window, portrait behind it](prompts/by-use-case/portrait.md#rain-on-a-window-portrait-behind-it) · wan-2.5, kling-3 · `t2v` · 5 s

[查看全部「人像」提示词（含完整文本）→](prompts/by-use-case/portrait.md)

### 自然风光

- [Mountain lake at sunrise, static wide](prompts/by-use-case/nature.md#mountain-lake-at-sunrise-static-wide) · kling-3 · `t2v` · 5 s
- [Coastal dune, tilt down](prompts/by-use-case/nature.md#coastal-dune-tilt-down) · kling-3 · `t2v` · 5 s
- [Autumn pond, push in](prompts/by-use-case/nature.md#autumn-pond-push-in) · kling-3 · `t2v` · 5 s
- [Thunderstorm over a plain, with sound](prompts/by-use-case/nature.md#thunderstorm-over-a-plain-with-sound) · veo-3 · `t2v` · 8 s
- [Tide pool, macro](prompts/by-use-case/nature.md#tide-pool-macro) · wan-2.5, kling-3 · `t2v` · 5 s

[查看全部「自然风光」提示词（含完整文本）→](prompts/by-use-case/nature.md)

### 动作

- [Cyclist in the rain, tracking shot](prompts/by-use-case/action.md#cyclist-in-the-rain-tracking-shot) · kling-3 · `t2v` · 5 s
- [Wok flame, static camera](prompts/by-use-case/action.md#wok-flame-static-camera) · kling-3 · `t2v` · 5 s
- [Skateboarder, low-angle pass](prompts/by-use-case/action.md#skateboarder-low-angle-pass) · runway-gen-4, seedance-2 · `t2v` · 5 s
- [Alley chase, two connected shots](prompts/by-use-case/action.md#alley-chase-two-connected-shots) · seedance-2 · `t2v` · 10 s
- [Horse galloping on a beach, side tracking](prompts/by-use-case/action.md#horse-galloping-on-a-beach-side-tracking) · wan-2.5, kling-3, veo-3 · `t2v` · 5 s

[查看全部「动作」提示词（含完整文本）→](prompts/by-use-case/action.md)

### 广告

- [UGC-style handheld product talk, with disclosure](prompts/by-use-case/ads.md#ugc-style-handheld-product-talk-with-disclosure) · veo-3 · `t2v` · 8 s
- [Vertical product hero reveal](prompts/by-use-case/ads.md#vertical-product-hero-reveal) · kling-3, wan-2.5 · `t2v` · 5 s
- [App promo, three beats](prompts/by-use-case/ads.md#app-promo-three-beats) · seedance-2 · `t2v` · 10 s
- [Fabric in slow motion, space left for a logo](prompts/by-use-case/ads.md#fabric-in-slow-motion-space-left-for-a-logo) · runway-gen-4, kling-3, wan-2.5 · `t2v` · 5 s

[查看全部「广告」提示词（含完整文本）→](prompts/by-use-case/ads.md)

### 动漫

- [Anime rooftop, wind and hair](prompts/by-use-case/anime.md#anime-rooftop-wind-and-hair) · wan-2.5, kling-3 · `t2v` · 5 s
- [Anime rain street, slow pan](prompts/by-use-case/anime.md#anime-rain-street-slow-pan) · kling-3, wan-2.5 · `t2v` · 5 s
- [Anime two-shot, reaction without dialogue](prompts/by-use-case/anime.md#anime-two-shot-reaction-without-dialogue) · seedance-2 · `t2v` · 10 s
- [Mecha hangar, tilt up](prompts/by-use-case/anime.md#mecha-hangar-tilt-up) · kling-3, wan-2.5 · `t2v` · 5 s

[查看全部「动漫」提示词（含完整文本）→](prompts/by-use-case/anime.md)

### 图生视频

- [Portrait photo: blink and breeze](prompts/by-use-case/image-to-video.md#portrait-photo-blink-and-breeze) · kling-3 · `i2v` · 5 s
- [Table or still-life photo: steam and flame](prompts/by-use-case/image-to-video.md#table-or-still-life-photo-steam-and-flame) · kling-3 · `i2v` · 5 s
- [Landscape photo: clouds and ripples, pan](prompts/by-use-case/image-to-video.md#landscape-photo-clouds-and-ripples-pan) · kling-3 · `i2v` · 5 s
- [Illustration: gentle natural motion, keep the style](prompts/by-use-case/image-to-video.md#illustration-gentle-natural-motion-keep-the-style) · kling-3, wan-2.5 · `i2v` · 5 s
- [Product photo: quarter turn with sound](prompts/by-use-case/image-to-video.md#product-photo-quarter-turn-with-sound) · veo-3 · `i2v` · 8 s
- [City photo: traffic and lights come alive](prompts/by-use-case/image-to-video.md#city-photo-traffic-and-lights-come-alive) · wan-2.5, kling-3 · `i2v` · 5 s

[查看全部「图生视频」提示词（含完整文本）→](prompts/by-use-case/image-to-video.md)

### 静态图（图像提示词）

- [Catalogue product shot: stoneware teapot](prompts/by-use-case/stills.md#catalogue-product-shot-stoneware-teapot) · nano-banana, flux, gpt-image · `t2i` · 已渲染
- [Editorial studio portrait, real skin](prompts/by-use-case/stills.md#editorial-studio-portrait-real-skin) · flux, nano-banana, gpt-image · `t2i` · 已渲染
- [Golden-hour field portrait](prompts/by-use-case/stills.md#golden-hour-field-portrait) · flux, nano-banana, gpt-image · `t2i` · 已渲染
- [Neon night portrait, anamorphic](prompts/by-use-case/stills.md#neon-night-portrait-anamorphic) · flux, nano-banana, gpt-image · `t2i` · 已渲染
- [Black-and-white character study](prompts/by-use-case/stills.md#black-and-white-character-study) · flux, nano-banana, gpt-image · `t2i` · 已渲染
- [Edit: enhance a dim phone photo, change nothing else](prompts/by-use-case/stills.md#edit-enhance-a-dim-phone-photo-change-nothing-else) · nano-banana, gpt-image · `i2i` · 已渲染
- [Edit: selfie to business headshot, keep the face](prompts/by-use-case/stills.md#edit-selfie-to-business-headshot-keep-the-face) · nano-banana, gpt-image · `i2i`
- [Beauty portrait, freckles kept](prompts/by-use-case/stills.md#beauty-portrait-freckles-kept) · flux, nano-banana, gpt-image · `t2i` · 已渲染

[查看全部「静态图（图像提示词）」提示词（含完整文本）→](prompts/by-use-case/stills.md)

### 按模型

- [Kling 3.0](prompts/by-model/kling-3.md) · 32 条提示词 · 无声片段
- [Veo 3](prompts/by-model/veo-3.md) · 7 条提示词 · 生成音频
- [Wan 2.5](prompts/by-model/wan-2.5.md) · 12 条提示词 · 生成音频
- [Runway Gen-4 family](prompts/by-model/runway-gen-4.md) · 3 条提示词 · 无声片段
- [Seedance 2.x](prompts/by-model/seedance-2.md) · 6 条提示词 · 无声片段
- [Flux](prompts/by-model/flux.md) · 6 条提示词 · 图像模型
- [Nano Banana (Gemini image)](prompts/by-model/nano-banana.md) · 8 条提示词 · 图像模型
- [GPT Image](prompts/by-model/gpt-image.md) · 8 条提示词 · 图像模型
<!-- generated:list:end -->

## 工作原理

1. **所有模型共用一套结构。** 主体及其动作 → 场景 → 一个运镜（或“static camera”）→ 镜头与光线 → 氛围。快手的 Kling 指南要求的正是这个顺序，并要求动作“适合 5 秒视频”；Google 的 Veo 指南列出同样的要素，并把音频作为单独一句加上。顺序在各模型间一致，语法细节有差异，[`references/model-notes.md`](references/model-notes.md) 逐一列出，附厂商页面和检查日期。
2. **一个动作，一个运镜。** 每条视频提示词只写一个运镜，带速度和稳定性描述（“slow, stable push in, no sudden motion”），以及一个能在 5 到 8 秒内完成的主体动作。次要动态来自廉价而连续的元素：风吹头发、蒸汽、飘动的灰尘、旋转的光束。
3. **说清什么保持不动。** 条目不用负面提示词（Kling 在很多前端里根本没有这一项），而是写明什么不能变：“static camera, product centred”，或者图生视频时的“keep the framing, background and art style exactly as in the photo”。
4. **模型支持时才用音频和多镜头。** Veo 条目以 `Audio: …` 和 `No music` 结尾；对白写成 `She says: "…"`。Seedance 条目标注 `Shot 1` 和 `Shot 2`，并在两个镜头间保持服装、镜头和光线一致。
5. **JSON 是唯一来源。** `data/prompts/<use-case>.json` 存放记录，`data/schema.json` 是规范，`scripts/validate.py` 负责校验，`scripts/build.py` 写出 `prompts/**/*.md` 和本 README 的两个生成区块。一旦不一致，测试就会失败。

```
data/prompts/*.json  ──validate.py──▶  ok
        │
        └──build.py──▶  prompts/by-model/*.md
                        prompts/by-use-case/*.md
                        README.md (stats + list sections)
```

想把同一条提示词在 Kling 3.0、Veo 3 和 Wan 2.5 上并排比较，[UniqAI 可以在一个输入框里同时跑这三个模型](https://uniqai.app/video?utm_source=github&utm_medium=readme-zh-cn&utm_campaign=awesome-ai-video-prompts)；任何提供这些模型的其他工具用法相同。

## 示例

<details>
<summary><b>模糊的提示词 → 只有一个运镜的 Kling 3.0 提示词</b></summary>

**之前**

```text
A perfume bottle, cinematic, luxury, 4k, slow motion, beautiful lighting.
```

**之后**（`kling-perfume-macro-drop`）

```text
A glass bottle of amber perfume standing on wet black slate, a single water drop running down the glass. Slow push in on the bottle. 90 mm macro lens, soft backlight through the liquid, small specular highlights. Elegant, quiet atmosphere.
```

一个动作（水滴）、一个运镜（push in）、一个镜头、一个光线方向、一种氛围。“4k”和“cinematic”没了：它们是参数和形容词，不是指令。

</details>

<details>
<summary><b>Sora 风格的提示词 → 带声音的 Veo 3 提示词</b></summary>

**之前**

```text
A golden retriever runs along a beach at sunset, cinematic, shallow depth of field.
```

**之后**

```text
Tracking shot at ground level: a golden retriever runs along a wet beach at sunset, waves rolling in behind it. Shallow depth of field, warm light. Sound: surf and paws on sand.
```

运镜有了名字，动作具体了，声音也列出来了。关于迁移 Sora 提示词的更多内容见 [`references/sora-alternatives.md`](references/sora-alternatives.md)。

</details>

<details>
<summary><b>照片 → 图生视频提示词</b></summary>

**之前**

```text
Make this photo move.
```

**之后**（`kling-i2v-portrait-blink-breeze`）

```text
The person blinks and smiles slightly, hair moving in a light breeze. Static camera.
```

对于照片，提示词只描述动作；主体、光线和构图照片里已经有了。点名的这三个动作正是能让面部保持完整的那几个。

</details>

<details>
<summary><b>从 agent 里使用</b></summary>

```text
You: I need a vertical product reveal for earbuds, Kling, 5 seconds.
Agent (with the skill): runs python3 scripts/find.py --use-case ads --model kling-3,
  picks kling-hero-product-reveal-vertical, swaps "earbud case" details for yours,
  returns the prompt in a code block and notes that the source entry has no render report yet.
```

</details>

## 安装

任何会读取指令文件的 agent 都能用。选你的那个。

<details open>
<summary><b>Claude Code</b>（作为 skill）</summary>

```bash
git clone https://github.com/uniqaiapp/awesome-ai-video-prompts ~/.claude/skills/awesome-ai-video-prompts
```

然后在 Claude Code 里输入 `/awesome-ai-video-prompts`，或者直接描述任务；skill 会根据自己的描述触发。想只在项目内安装而非全局：克隆到项目里的 `.claude/skills/awesome-ai-video-prompts`。

作为插件，等 uniqaiapp marketplace 发布后：

```
/plugin marketplace add uniqaiapp/skills
/plugin install awesome-ai-video-prompts@uniqaiapp
```

</details>

<details>
<summary><b>Cursor</b></summary>

把 `SKILL.md`、`scripts/`、`data/`、`references/` 和 [`.cursor/rules/awesome-ai-video-prompts.mdc`](.cursor/rules/awesome-ai-video-prompts.mdc) 复制到你的项目里。规则文件内嵌了这个 skill。

</details>

<details>
<summary><b>Codex / 任何读取 AGENTS.md 的 agent</b></summary>

把 `SKILL.md`、`scripts/`、`data/` 和 `references/` 复制到 `.agents/skills/awesome-ai-video-prompts/`，并把 [`codex/INSTRUCTIONS.md`](codex/INSTRUCTIONS.md) 中的片段加到你的 `AGENTS.md`。

</details>

<details>
<summary><b>不用 agent</b></summary>

每个脚本都能独立运行：`python3 scripts/find.py --help`、`python3 scripts/stats.py`、`python3 scripts/validate.py`。或者把 [`SKILL.md`](SKILL.md) 粘贴到任何模型的系统提示词里；除 frontmatter 外，它没有任何特定 agent 的语法。

</details>

要求：Python 3.9+。无需安装任何包。

## 局限与诚实说明

- **“为谁编写”不等于“在哪渲染”。** 大多数条目的 `rendered_on` 一开始是空的。它们遵循有引用的厂商指南，或来自 UniqAI 提示词库，这是对结构的声明，而不是你能观看的片段。有报告的条目会在正文里说明；“Report a render”issue 模板就是获得报告的途径。
- **图像提示词是在 GPT Image 上渲染的**，用于 UniqAI 网站（日期在 `rendered_on` 中）；对 Flux 和 Nano Banana 来说，它们是正确的措辞，而不是经过验证的结果。
- **本版本中 Runway 没有可引用的指南**：Runway 的帮助中心拒绝了抓取，所以 Runway 条目遵循通用做法，并如实注明。
- **版本在变。** 每个 `guide` 都带有检查日期。Kling 4.0 于 2026 年 10 月发布（新闻稿引用见 `references/model-notes.md` 的来源）；Kling 条目是按 3.0 指南编写的。
- 本 README 中的每个数字都由 `python3 scripts/stats.py` 基于 `data/prompts/` 生成；如果生成区块过期，或手写文本里出现了数量，测试套件会失败。

## FAQ

<details>
<summary><b>Kling 3.0 的提示词该多长？</b></summary>

两到四个短句：主体及其动作、场景、一个运镜，然后是镜头、光线和氛围。快手的指南要求用简单的词和短句，而不是规定字数。一长串互相竞争的指令比一个清晰的场景渲染得更不可预测。

</details>

<details>
<summary><b>Kling 的提示词能用在 Veo 3 上吗？</b></summary>

基本可以。加一句 `Audio:`（Veo 会生成声音，你不写它就自己编），不想要配乐的话以 `No music` 结尾。Veo 比 Kling 更能容忍叠加的运镜，但一个运镜仍然更干净。

</details>

<details>
<summary><b>负面提示词在哪？</b></summary>

没有。好几个前端没有给 Kling 提供负面提示词字段，所以条目改为描述什么应该保持不动：“static camera, product centred”比“no camera shake”效果更好，而且能迁移到任何模型。

</details>

<details>
<summary><b>这是 Sora 的提示词列表吗？</b></summary>

不是。OpenAI 的弃用页面显示 Sora 2 API 模型已于 2026 年 9 月 24 日下线。Sora 提示词的结构可以迁移；[`references/sora-alternatives.md`](references/sora-alternatives.md) 说明了每类提示词现在该去哪里。

</details>

<details>
<summary><b>为什么用 JSON 而不只是 Markdown？</b></summary>

这样 agent 和脚本可以按模型、模式和标签筛选，schema 可以强制要求“为什么”和渲染字段，Markdown 也永远不会和数据不一致。Markdown 仍然提交到仓库，因为人们就是这样在 GitHub 上阅读 awesome 列表的。

</details>

## 相关项目

- [`video-director`](https://github.com/uniqaiapp/video-director)：把一句话的想法变成 AI 视频模型（Kling、Veo、Sora 等）逐镜头的提示词，带运镜、灯光和运动词汇表。用它做分镜脚本，用本列表做单个镜头。
- [`no-plastic`](https://github.com/uniqaiapp/no-plastic)：让 AI 人像看起来自然的提示词规则和检查器：皮肤质感、光线和镜头选择，避免“塑料感”。
- [`ai-video-pricing`](https://github.com/uniqaiapp/ai-video-pricing)：人工核对的 AI 视频生成价格表，按秒和按片段计价，每一行附来源 URL 和检查日期。

## 参与贡献

欢迎提交 issue 和 pull request：带“为什么”的新提示词、渲染报告或修正后的来源。条目格式和本地检查见 [CONTRIBUTING.md](CONTRIBUTING.md)（`python3 tests/run.py`，零依赖）。

## 许可证

提示词、数据和参考资料：[CC BY 4.0](LICENSE)，署名“UniqAI, https://github.com/uniqaiapp/awesome-ai-video-prompts”。脚本和测试：[MIT](LICENSE) © UniqAI。

---

<div align="center">

<sub>由 <a href="https://uniqai.app/?utm_source=github&utm_medium=readme-zh-cn&utm_campaign=awesome-ai-video-prompts">UniqAI</a> 出品，一款集 AI 图片、视频和聊天于一体的应用。Kling 条目就是我们发布给自己用户的提示词库。</sub>

</div>
