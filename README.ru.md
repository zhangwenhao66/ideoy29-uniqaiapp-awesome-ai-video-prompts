<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="awesome-ai-video-prompts by UniqAI" src="assets/banner.svg" width="1280" height="320">
</picture>

[![License: CC BY 4.0](https://img.shields.io/badge/license-CC_BY_4.0-d1fe17?style=flat-square&labelColor=0d0f12)](LICENSE)
[![Claude Code skill](https://img.shields.io/badge/Claude_Code-skill-d1fe17?style=flat-square&labelColor=0d0f12)](#установка)
[![Cursor](https://img.shields.io/badge/Cursor-rules-d1fe17?style=flat-square&labelColor=0d0f12)](#установка)
[![Codex](https://img.shields.io/badge/Codex-AGENTS.md-d1fe17?style=flat-square&labelColor=0d0f12)](#установка)
[![Made by UniqAI](https://img.shields.io/badge/made_by-UniqAI-fdfc07?style=flat-square&labelColor=0d0f12)](https://uniqai.app/?utm_source=github&utm_medium=readme-ru&utm_campaign=awesome-ai-video-prompts)

**Отобранные промпты для ИИ-видео: Kling 3.0, Veo 3, Wan 2.5, Runway и Seedance, с моделью, настройками и объяснением, почему каждый из них работает.**

[Быстрый старт](#быстрый-старт) · [Список](#список) · [Как это работает](#как-это-работает) · [Примеры](#примеры) · [Установка](#установка) · [FAQ](#faq)

</div>

[English](README.md) · Русский · [简体中文](README.zh-CN.md) · [Español](README.es.md) · [Português (BR)](README.pt-BR.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

# Awesome AI Video Prompts: промпты для ИИ-видео, Kling 3.0, Veo 3, Wan, Runway, Seedance

Подборка промптов для генерации видео нейросетями (текст в видео и картинка в видео) для Kling 3.0, Veo 3, Wan 2.5, Runway Gen-4 и Seedance 2.x, плюс небольшой набор промптов для картинок под Flux, Nano Banana и GPT Image. У каждой записи есть сам промпт в блоке кода, модель, под которую он написан, режим, длительность, соотношение сторон, заметка о том, почему такая структура работает, и поле `rendered_on`, которое остаётся пустым, пока кто-нибудь не сообщит о реальном рендере. Данные хранятся в JSON; Markdown-страницы и цифры ниже генерируются из них.

| **Под конкретную модель, а не вообще** | **Честно о результатах** | **Работает как скилл агента** |
|:---|:---|:---|
| Каждый промпт следует гайду самого вендора (со ссылкой и датой): одно движение камеры для Kling, звук отдельным предложением для Veo, размеченные кадры для Seedance. | «Написан под» и «отрендерен на» — разные поля. Цифры в этом README берутся из `scripts/stats.py`, а не с клавиатуры. | `SKILL.md` позволяет Claude Code, Cursor или Codex искать по списку и подгонять ближайший промпт под ваш кадр. |

## Быстрый старт

```bash
git clone https://github.com/uniqaiapp/awesome-ai-video-prompts
cd awesome-ai-video-prompts
python3 scripts/find.py --model kling-3 --use-case product
```

Вы получите подходящие промпты текстом, у каждого — строка `Why it works` и отметка, сообщал ли кто-нибудь о рендере. Ставить ничего не нужно; Python 3.9+. Можно смотреть и без терминала: [по моделям](prompts/by-model/) или [по категориям](prompts/by-use-case/).

## Демо

<img alt="awesome-ai-video-prompts demo: searching the list with scripts/find.py and printing one entry" src="assets/demo.svg" width="820">

## Что в списке

<!-- generated:stats:start -->
| Модель | Промптов для модели |
|:---|---:|
| Kling 3.0 (`kling-3`) | 32 |
| Veo 3 (`veo-3`) | 7 |
| Wan 2.5 (`wan-2.5`) | 12 |
| Runway Gen-4 family (`runway-gen-4`) | 3 |
| Seedance 2.x (`seedance-2`) | 6 |
| Flux (`flux`) | 6 |
| Nano Banana (Gemini image) (`nano-banana`) | 8 |
| GPT Image (`gpt-image`) | 8 |

| Категория | Промптов |
|:---|---:|
| Движения камеры | 9 |
| Предметная съёмка | 6 |
| Портрет | 5 |
| Природа | 5 |
| Экшен | 5 |
| Реклама | 4 |
| Аниме | 4 |
| Фото в видео | 6 |
| Картинки (промпты для изображений) | 8 |

| Режим | Промптов |
|:---|---:|
| текст в видео (`t2v`) | 38 |
| картинка в видео (`i2v`) | 6 |
| текст в картинку (`t2i`) | 6 |
| редактирование картинки (`i2i`) | 2 |

Всего 52 промпта: 44 для видео, 8 для картинок. У 7 есть отчёт о рендере (`rendered_on` заполнено); 45 написаны по гайду вендора или взяты из библиотеки UniqAI, но отчёта о рендере пока нет.
<!-- generated:stats:end -->

## Список

Одна строка на промпт; ссылка открывает полную запись с текстом промпта, заметкой «почему работает» и отчётами о рендере, если они есть. Ключи моделей: `kling-3` Kling 3.0, `veo-3` Veo 3, `wan-2.5` Wan 2.5, `runway-gen-4` семейство Runway Gen-4, `seedance-2` Seedance 2.x, `flux`, `nano-banana`, `gpt-image`. Режимы: `t2v` текст в видео, `i2v` картинка в видео, `t2i` текст в картинку, `i2i` редактирование картинки.

<!-- generated:list:start -->
### Движения камеры

- [Brass compass, push in](prompts/by-use-case/camera-moves.md#brass-compass-push-in) · kling-3 · `t2v` · 5 s
- [Lit candle, pull back](prompts/by-use-case/camera-moves.md#lit-candle-pull-back) · kling-3 · `t2v` · 5 s
- [Harbour boats, pan left](prompts/by-use-case/camera-moves.md#harbour-boats-pan-left) · kling-3 · `t2v` · 5 s
- [Hiker on a ridge, tilt up](prompts/by-use-case/camera-moves.md#hiker-on-a-ridge-tilt-up) · kling-3 · `t2v` · 5 s
- [Bronze horse, orbit](prompts/by-use-case/camera-moves.md#bronze-horse-orbit) · kling-3 · `t2v` · 5 s
- [Lighthouse at dusk, dolly in with sound](prompts/by-use-case/camera-moves.md#lighthouse-at-dusk-dolly-in-with-sound) · veo-3 · `t2v` · 8 s
- [Old town rooftops, crane up](prompts/by-use-case/camera-moves.md#old-town-rooftops-crane-up) · wan-2.5, kling-3 · `t2v` · 5 s
- [Handheld follow through a corridor](prompts/by-use-case/camera-moves.md#handheld-follow-through-a-corridor) · runway-gen-4, seedance-2 · `t2v` · 5 s
- [Chrome droplet over a neon street, push in](prompts/by-use-case/camera-moves.md#chrome-droplet-over-a-neon-street-push-in) · kling-3 · `t2v` · 8 s

[Все промпты категории «Движения камеры» с полным текстом →](prompts/by-use-case/camera-moves.md)

### Предметная съёмка

- [Headphones on a turntable](prompts/by-use-case/product.md#headphones-on-a-turntable) · kling-3 · `t2v` · 5 s
- [Perfume bottle, macro water drop](prompts/by-use-case/product.md#perfume-bottle-macro-water-drop) · kling-3 · `t2v` · 5 s
- [Sneaker, quarter orbit](prompts/by-use-case/product.md#sneaker-quarter-orbit) · kling-3 · `t2v` · 5 s
- [Coffee pour, slow motion with sound](prompts/by-use-case/product.md#coffee-pour-slow-motion-with-sound) · veo-3 · `t2v` · 8 s
- [Watch, two connected shots](prompts/by-use-case/product.md#watch-two-connected-shots) · seedance-2 · `t2v` · 10 s
- [Skincare jar, slow rotate on marble](prompts/by-use-case/product.md#skincare-jar-slow-rotate-on-marble) · kling-3, wan-2.5 · `t2v` · 5 s

[Все промпты категории «Предметная съёмка» с полным текстом →](prompts/by-use-case/product.md)

### Портрет

- [Studio portrait, blink and smile](prompts/by-use-case/portrait.md#studio-portrait-blink-and-smile) · kling-3 · `t2v` · 5 s
- [Golden hour, push in to close-up](prompts/by-use-case/portrait.md#golden-hour-push-in-to-close-up) · kling-3 · `t2v` · 5 s
- [Dancer, track forward](prompts/by-use-case/portrait.md#dancer-track-forward) · kling-3 · `t2v` · 5 s
- [Portrait with one line of dialogue](prompts/by-use-case/portrait.md#portrait-with-one-line-of-dialogue) · veo-3 · `t2v` · 8 s
- [Rain on a window, portrait behind it](prompts/by-use-case/portrait.md#rain-on-a-window-portrait-behind-it) · wan-2.5, kling-3 · `t2v` · 5 s

[Все промпты категории «Портрет» с полным текстом →](prompts/by-use-case/portrait.md)

### Природа

- [Mountain lake at sunrise, static wide](prompts/by-use-case/nature.md#mountain-lake-at-sunrise-static-wide) · kling-3 · `t2v` · 5 s
- [Coastal dune, tilt down](prompts/by-use-case/nature.md#coastal-dune-tilt-down) · kling-3 · `t2v` · 5 s
- [Autumn pond, push in](prompts/by-use-case/nature.md#autumn-pond-push-in) · kling-3 · `t2v` · 5 s
- [Thunderstorm over a plain, with sound](prompts/by-use-case/nature.md#thunderstorm-over-a-plain-with-sound) · veo-3 · `t2v` · 8 s
- [Tide pool, macro](prompts/by-use-case/nature.md#tide-pool-macro) · wan-2.5, kling-3 · `t2v` · 5 s

[Все промпты категории «Природа» с полным текстом →](prompts/by-use-case/nature.md)

### Экшен

- [Cyclist in the rain, tracking shot](prompts/by-use-case/action.md#cyclist-in-the-rain-tracking-shot) · kling-3 · `t2v` · 5 s
- [Wok flame, static camera](prompts/by-use-case/action.md#wok-flame-static-camera) · kling-3 · `t2v` · 5 s
- [Skateboarder, low-angle pass](prompts/by-use-case/action.md#skateboarder-low-angle-pass) · runway-gen-4, seedance-2 · `t2v` · 5 s
- [Alley chase, two connected shots](prompts/by-use-case/action.md#alley-chase-two-connected-shots) · seedance-2 · `t2v` · 10 s
- [Horse galloping on a beach, side tracking](prompts/by-use-case/action.md#horse-galloping-on-a-beach-side-tracking) · wan-2.5, kling-3, veo-3 · `t2v` · 5 s

[Все промпты категории «Экшен» с полным текстом →](prompts/by-use-case/action.md)

### Реклама

- [UGC-style handheld product talk, with disclosure](prompts/by-use-case/ads.md#ugc-style-handheld-product-talk-with-disclosure) · veo-3 · `t2v` · 8 s
- [Vertical product hero reveal](prompts/by-use-case/ads.md#vertical-product-hero-reveal) · kling-3, wan-2.5 · `t2v` · 5 s
- [App promo, three beats](prompts/by-use-case/ads.md#app-promo-three-beats) · seedance-2 · `t2v` · 10 s
- [Fabric in slow motion, space left for a logo](prompts/by-use-case/ads.md#fabric-in-slow-motion-space-left-for-a-logo) · runway-gen-4, kling-3, wan-2.5 · `t2v` · 5 s

[Все промпты категории «Реклама» с полным текстом →](prompts/by-use-case/ads.md)

### Аниме

- [Anime rooftop, wind and hair](prompts/by-use-case/anime.md#anime-rooftop-wind-and-hair) · wan-2.5, kling-3 · `t2v` · 5 s
- [Anime rain street, slow pan](prompts/by-use-case/anime.md#anime-rain-street-slow-pan) · kling-3, wan-2.5 · `t2v` · 5 s
- [Anime two-shot, reaction without dialogue](prompts/by-use-case/anime.md#anime-two-shot-reaction-without-dialogue) · seedance-2 · `t2v` · 10 s
- [Mecha hangar, tilt up](prompts/by-use-case/anime.md#mecha-hangar-tilt-up) · kling-3, wan-2.5 · `t2v` · 5 s

[Все промпты категории «Аниме» с полным текстом →](prompts/by-use-case/anime.md)

### Фото в видео

- [Portrait photo: blink and breeze](prompts/by-use-case/image-to-video.md#portrait-photo-blink-and-breeze) · kling-3 · `i2v` · 5 s
- [Table or still-life photo: steam and flame](prompts/by-use-case/image-to-video.md#table-or-still-life-photo-steam-and-flame) · kling-3 · `i2v` · 5 s
- [Landscape photo: clouds and ripples, pan](prompts/by-use-case/image-to-video.md#landscape-photo-clouds-and-ripples-pan) · kling-3 · `i2v` · 5 s
- [Illustration: gentle natural motion, keep the style](prompts/by-use-case/image-to-video.md#illustration-gentle-natural-motion-keep-the-style) · kling-3, wan-2.5 · `i2v` · 5 s
- [Product photo: quarter turn with sound](prompts/by-use-case/image-to-video.md#product-photo-quarter-turn-with-sound) · veo-3 · `i2v` · 8 s
- [City photo: traffic and lights come alive](prompts/by-use-case/image-to-video.md#city-photo-traffic-and-lights-come-alive) · wan-2.5, kling-3 · `i2v` · 5 s

[Все промпты категории «Фото в видео» с полным текстом →](prompts/by-use-case/image-to-video.md)

### Картинки (промпты для изображений)

- [Catalogue product shot: stoneware teapot](prompts/by-use-case/stills.md#catalogue-product-shot-stoneware-teapot) · nano-banana, flux, gpt-image · `t2i` · есть рендер
- [Editorial studio portrait, real skin](prompts/by-use-case/stills.md#editorial-studio-portrait-real-skin) · flux, nano-banana, gpt-image · `t2i` · есть рендер
- [Golden-hour field portrait](prompts/by-use-case/stills.md#golden-hour-field-portrait) · flux, nano-banana, gpt-image · `t2i` · есть рендер
- [Neon night portrait, anamorphic](prompts/by-use-case/stills.md#neon-night-portrait-anamorphic) · flux, nano-banana, gpt-image · `t2i` · есть рендер
- [Black-and-white character study](prompts/by-use-case/stills.md#black-and-white-character-study) · flux, nano-banana, gpt-image · `t2i` · есть рендер
- [Edit: enhance a dim phone photo, change nothing else](prompts/by-use-case/stills.md#edit-enhance-a-dim-phone-photo-change-nothing-else) · nano-banana, gpt-image · `i2i` · есть рендер
- [Edit: selfie to business headshot, keep the face](prompts/by-use-case/stills.md#edit-selfie-to-business-headshot-keep-the-face) · nano-banana, gpt-image · `i2i`
- [Beauty portrait, freckles kept](prompts/by-use-case/stills.md#beauty-portrait-freckles-kept) · flux, nano-banana, gpt-image · `t2i` · есть рендер

[Все промпты категории «Картинки (промпты для изображений)» с полным текстом →](prompts/by-use-case/stills.md)

### По моделям

- [Kling 3.0](prompts/by-model/kling-3.md) · 32 промпта · клипы без звука
- [Veo 3](prompts/by-model/veo-3.md) · 7 промптов · генерирует звук
- [Wan 2.5](prompts/by-model/wan-2.5.md) · 12 промптов · генерирует звук
- [Runway Gen-4 family](prompts/by-model/runway-gen-4.md) · 3 промпта · клипы без звука
- [Seedance 2.x](prompts/by-model/seedance-2.md) · 6 промптов · клипы без звука
- [Flux](prompts/by-model/flux.md) · 6 промптов · модель для картинок
- [Nano Banana (Gemini image)](prompts/by-model/nano-banana.md) · 8 промптов · модель для картинок
- [GPT Image](prompts/by-model/gpt-image.md) · 8 промптов · модель для картинок
<!-- generated:list:end -->

## Как это работает

1. **Одна структура для всех моделей.** Объект и что он делает → место → одно движение камеры (или «static camera») → объектив и свет → настроение. Гайд Kuaishou по Kling просит ровно такой порядок и движение, «подходящее для 5-секундного видео»; гайд Google по Veo перечисляет те же элементы и добавляет звук отдельным предложением. Порядок одинаковый у всех моделей, детали синтаксиса различаются, и [`references/model-notes.md`](references/model-notes.md) перечисляет их со ссылкой на страницу вендора и датой проверки.
2. **Одно движение, один план.** Каждый видеопромпт называет одно движение камеры со скоростью и словом про стабильность («slow, stable push in, no sudden motion») и одно действие объекта, которое укладывается в 5–8 секунд. Второстепенное движение берётся из дешёвых непрерывных вещей: ветер в волосах, пар, летящая пыль, вращающийся луч.
3. **Говорите, что остаётся неподвижным.** Вместо негативного промпта (у Kling во многих интерфейсах его нет) записи указывают, что не должно меняться: «static camera, product centred» или, для картинки в видео, «keep the framing, background and art style exactly as in the photo».
4. **Звук и несколько кадров там, где модель это умеет.** Записи для Veo заканчиваются `Audio: …` и `No music`; диалог записывается как `She says: "…"`. Записи для Seedance размечают `Shot 1` и `Shot 2` и сохраняют одежду, объектив и свет одинаковыми в обоих кадрах.
5. **Источник — JSON.** `data/prompts/<use-case>.json` хранит записи, `data/schema.json` — спецификация, `scripts/validate.py` её проверяет, `scripts/build.py` пишет `prompts/**/*.md` и две генерируемые секции этого README. Если они расходятся, тест падает.

```
data/prompts/*.json  ──validate.py──▶  ok
        │
        └──build.py──▶  prompts/by-model/*.md
                        prompts/by-use-case/*.md
                        README.md (stats + list sections)
```

Чтобы сравнить один и тот же промпт на Kling 3.0, Veo 3 и Wan 2.5 рядом, [UniqAI запускает все три из одного окна](https://uniqai.app/video?utm_source=github&utm_medium=readme-ru&utm_campaign=awesome-ai-video-prompts); любой другой инструмент с доступом к этим моделям работает так же.

## Примеры

<details>
<summary><b>Размытый промпт → промпт для Kling 3.0 с одним движением камеры</b></summary>

**До**

```text
A perfume bottle, cinematic, luxury, 4k, slow motion, beautiful lighting.
```

**После** (`kling-perfume-macro-drop`)

```text
A glass bottle of amber perfume standing on wet black slate, a single water drop running down the glass. Slow push in on the bottle. 90 mm macro lens, soft backlight through the liquid, small specular highlights. Elegant, quiet atmosphere.
```

Одно движение (капля), одно движение камеры (push in), объектив, направление света, настроение. «4k» и «cinematic» исчезли: это настройки и прилагательные, а не инструкции.

</details>

<details>
<summary><b>Промпт в стиле Sora → промпт для Veo 3 со звуком</b></summary>

**До**

```text
A golden retriever runs along a beach at sunset, cinematic, shallow depth of field.
```

**После**

```text
Tracking shot at ground level: a golden retriever runs along a wet beach at sunset, waves rolling in behind it. Shallow depth of field, warm light. Sound: surf and paws on sand.
```

Движение камеры названо, движение объекта конкретное, звук перечислен. Подробнее о переносе промптов из Sora — в [`references/sora-alternatives.md`](references/sora-alternatives.md).

</details>

<details>
<summary><b>Фото → промпт «картинка в видео»</b></summary>

**До**

```text
Make this photo move.
```

**После** (`kling-i2v-portrait-blink-breeze`)

```text
The person blinks and smiles slightly, hair moving in a light breeze. Static camera.
```

Для фото промпт описывает только движение: объект, свет и кадрирование уже есть на снимке. Три названных движения — те, при которых лицо остаётся целым.

</details>

<details>
<summary><b>Использование из агента</b></summary>

```text
You: I need a vertical product reveal for earbuds, Kling, 5 seconds.
Agent (with the skill): runs python3 scripts/find.py --use-case ads --model kling-3,
  picks kling-hero-product-reveal-vertical, swaps "earbud case" details for yours,
  returns the prompt in a code block and notes that the source entry has no render report yet.
```

</details>

## Установка

Работает с любым агентом, который читает файлы инструкций. Выберите свой.

<details open>
<summary><b>Claude Code</b> (как скилл)</summary>

```bash
git clone https://github.com/uniqaiapp/awesome-ai-video-prompts ~/.claude/skills/awesome-ai-video-prompts
```

Затем в Claude Code наберите `/awesome-ai-video-prompts` или просто опишите задачу; скилл сработает по своему описанию. Локально для проекта вместо глобальной установки: клонируйте в `.claude/skills/awesome-ai-video-prompts` внутри проекта.

Как плагин, когда маркетплейс uniqaiapp будет опубликован:

```
/plugin marketplace add uniqaiapp/skills
/plugin install awesome-ai-video-prompts@uniqaiapp
```

</details>

<details>
<summary><b>Cursor</b></summary>

Скопируйте `SKILL.md`, `scripts/`, `data/`, `references/` и [`.cursor/rules/awesome-ai-video-prompts.mdc`](.cursor/rules/awesome-ai-video-prompts.mdc) в свой проект. Файл правила встраивает скилл.

</details>

<details>
<summary><b>Codex / любой агент с AGENTS.md</b></summary>

Скопируйте `SKILL.md`, `scripts/`, `data/` и `references/` в `.agents/skills/awesome-ai-video-prompts/` и добавьте сниппет из [`codex/INSTRUCTIONS.md`](codex/INSTRUCTIONS.md) в свой `AGENTS.md`.

</details>

<details>
<summary><b>Без агента</b></summary>

Каждый скрипт работает сам по себе: `python3 scripts/find.py --help`, `python3 scripts/stats.py`, `python3 scripts/validate.py`. Или вставьте [`SKILL.md`](SKILL.md) в системный промпт любой модели; вне frontmatter в нём нет синтаксиса под конкретного агента.

</details>

Требования: Python 3.9+. Ставить ничего не нужно.

## Ограничения и честность

- **«Написан под» — не то же, что «отрендерен на».** У большинства записей `rendered_on` сначала пустое. Они следуют гайду вендора по ссылке или взяты из библиотеки промптов UniqAI, а это утверждение о структуре, а не о клипе, который можно посмотреть. Записи с отчётом говорят об этом прямо в тексте; шаблон issue «Report a render» — способ его получить.
- **Промпты для картинок рендерились на GPT Image** для сайта UniqAI (даты в `rendered_on`); для Flux и Nano Banana это правильный словарь, а не проверенный результат.
- **У Runway нет гайда по ссылке** в этом релизе: центр помощи Runway не отдал страницу, поэтому записи для Runway следуют общей практике и так и говорят.
- **Версии меняются.** У каждого `guide` есть дата проверки. Kling 4.0 анонсирован в октябре 2026 (пресс-релиз указан в источниках `references/model-notes.md`); записи для Kling написаны по гайдам 3.0.
- Каждое число в этом README производит `python3 scripts/stats.py` по `data/prompts/`; тесты падают, если сгенерированный блок устарел или если число промптов появилось в рукописном тексте.

## FAQ

<details>
<summary><b>Какой длины должен быть промпт для Kling 3.0?</b></summary>

Два–четыре коротких предложения: объект и что он делает, место, одно движение камеры, затем объектив, свет и настроение. Гайд Kuaishou просит простые слова и короткие предложения, а не определённое число слов. Длинный список конкурирующих инструкций рендерится менее предсказуемо, чем одна ясная сцена.

</details>

<details>
<summary><b>Можно использовать промпт для Kling на Veo 3?</b></summary>

В основном да. Добавьте предложение `Audio:` (Veo генерирует звук и придумает свой, если вы не укажете) и закончите `No music`, если не хотите музыку. Veo терпимее Kling к нескольким движениям камеры подряд, но одно движение всё равно читается чище.

</details>

<details>
<summary><b>Где негативные промпты?</b></summary>

Их нет. Несколько интерфейсов не дают поля для негативного промпта у Kling, поэтому записи вместо этого описывают, что должно оставаться неподвижным: «static camera, product centred» работает лучше, чем «no camera shake», и переносится на любую модель.

</details>

<details>
<summary><b>Это список промптов для Sora?</b></summary>

Нет. На странице устаревших продуктов OpenAI модели Sora 2 API значатся удалёнными 24 сентября 2026. Структура промпта для Sora переносится; [`references/sora-alternatives.md`](references/sora-alternatives.md) показывает, куда теперь идёт каждый тип промпта.

</details>

<details>
<summary><b>Почему JSON, а не просто Markdown?</b></summary>

Чтобы агенты и скрипты могли фильтровать по модели, режиму и тегу, чтобы схема могла требовать поле «почему» и поле рендера, и чтобы Markdown никогда не расходился с данными. Markdown всё равно закоммичен, потому что именно так awesome-списки читают на GitHub.

</details>

## Похожие проекты

- [`video-director`](https://github.com/uniqaiapp/video-director): превращает идею в одну строку в покадровый промпт для моделей ИИ-видео (Kling, Veo, Sora и другие) со словарём камеры, света и движения. Используйте его для раскадровки, а этот список — для отдельных кадров.
- [`no-plastic`](https://github.com/uniqaiapp/no-plastic): правила промптов и чекер для естественных ИИ-портретов: текстура кожи, свет и выбор объектива, которые убирают «пластиковый» вид.
- [`ai-video-pricing`](https://github.com/uniqaiapp/ai-video-pricing): проверенная вручную таблица цен на генерацию ИИ-видео, за секунду и за клип, со ссылкой на источник и датой проверки в каждой строке.

## Участие

Issue и pull request приветствуются: новый промпт с его «почему», отчёт о рендере или исправленный источник. Формат записи и локальные проверки описаны в [CONTRIBUTING.md](CONTRIBUTING.md) (`python3 tests/run.py`, без зависимостей).

## Лицензия

Промпты, данные и справочные материалы: [CC BY 4.0](LICENSE), атрибуция «UniqAI, https://github.com/uniqaiapp/awesome-ai-video-prompts». Скрипты и тесты: [MIT](LICENSE) © UniqAI.

---

<div align="center">

<sub>Сделано в <a href="https://uniqai.app/?utm_source=github&utm_medium=readme-ru&utm_campaign=awesome-ai-video-prompts">UniqAI</a>, приложении для ИИ-фото, видео и чата. Записи для Kling — это библиотека промптов, которую мы публикуем для своих пользователей.</sub>

</div>
