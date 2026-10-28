"""Strings for the generated README sections in each README.<lang>.md.

build.py refreshes the two generated blocks (stats, list) in README.md and in every
README.<lang>.md. Prompt titles, model names and keys stay in English in every language,
because they link into the English prompt pages; only labels, headings and the summary
sentence are translated here. Add a language: one entry in STRINGS, one README.<lang>.md.
"""
import re

_README_RE = re.compile(r"^README(?:\.([A-Za-z]{2}(?:-[A-Za-z]{2})?))?\.md$")


def lang_of(filename):
    """'README.md' -> 'en', 'README.zh-CN.md' -> 'zh-CN', anything else -> None."""
    m = _README_RE.match(filename)
    if not m:
        return None
    return m.group(1) or "en"


def _ru_plural(n, one, few, many):
    n10, n100 = n % 10, n % 100
    if n10 == 1 and n100 != 11:
        return one
    if 2 <= n10 <= 4 and not 12 <= n100 <= 14:
        return few
    return many


STRINGS = {
    "en": {
        "stats_model": "| Model | Prompts written for it |",
        "stats_use_case": "| Use case | Prompts |",
        "stats_mode": "| Mode | Prompts |",
        "use_cases": None,  # English names come from data/meta.json
        "modes": {"t2v": "text to video", "i2v": "image to video", "t2i": "text to image", "i2i": "image edit"},
        "summary": lambda s: "%d prompts in total: %d video, %d image. %d carry a render report (`rendered_on` is not empty); "
                             "%d follow a vendor prompt guide or the UniqAI library but have no render report yet."
                             % (s["total"], s["video"], s["image"], s["rendered"], s["unrendered"]),
        "all_link": lambda name: "All %s prompts with the full text →" % name.lower(),
        "rendered": "rendered",
        "by_model": "By model",
        "count": lambda n: "%d prompt%s" % (n, "" if n == 1 else "s"),
        "audio": "generates audio",
        "image_model": "image model",
        "silent": "silent clips",
    },
    "ru": {
        "stats_model": "| Модель | Промптов для модели |",
        "stats_use_case": "| Категория | Промптов |",
        "stats_mode": "| Режим | Промптов |",
        "use_cases": {"camera-moves": "Движения камеры", "product": "Предметная съёмка", "portrait": "Портрет", "nature": "Природа",
                      "action": "Экшен", "ads": "Реклама", "anime": "Аниме", "image-to-video": "Фото в видео", "stills": "Картинки (промпты для изображений)"},
        "modes": {"t2v": "текст в видео", "i2v": "картинка в видео", "t2i": "текст в картинку", "i2i": "редактирование картинки"},
        "summary": lambda s: "Всего %d %s: %d для видео, %d для картинок. У %d есть отчёт о рендере (`rendered_on` заполнено); "
                             "%d написаны по гайду вендора или взяты из библиотеки UniqAI, но отчёта о рендере пока нет."
                             % (s["total"], _ru_plural(s["total"], "промпт", "промпта", "промптов"), s["video"], s["image"], s["rendered"], s["unrendered"]),
        "all_link": lambda name: "Все промпты категории «%s» с полным текстом →" % name,
        "rendered": "есть рендер",
        "by_model": "По моделям",
        "count": lambda n: "%d %s" % (n, _ru_plural(n, "промпт", "промпта", "промптов")),
        "audio": "генерирует звук",
        "image_model": "модель для картинок",
        "silent": "клипы без звука",
    },
    "zh-CN": {
        "stats_model": "| 模型 | 为其编写的提示词数 |",
        "stats_use_case": "| 用途 | 提示词数 |",
        "stats_mode": "| 模式 | 提示词数 |",
        "use_cases": {"camera-moves": "运镜", "product": "产品", "portrait": "人像", "nature": "自然风光", "action": "动作",
                      "ads": "广告", "anime": "动漫", "image-to-video": "图生视频", "stills": "静态图（图像提示词）"},
        "modes": {"t2v": "文生视频", "i2v": "图生视频", "t2i": "文生图", "i2i": "图像编辑"},
        "summary": lambda s: "共 %d 条提示词：视频 %d 条，图像 %d 条。其中 %d 条附有渲染报告（`rendered_on` 非空）；"
                             "%d 条依据厂商提示词指南或 UniqAI 提示词库编写，但尚无渲染报告。"
                             % (s["total"], s["video"], s["image"], s["rendered"], s["unrendered"]),
        "all_link": lambda name: "查看全部「%s」提示词（含完整文本）→" % name,
        "rendered": "已渲染",
        "by_model": "按模型",
        "count": lambda n: "%d 条提示词" % n,
        "audio": "生成音频",
        "image_model": "图像模型",
        "silent": "无声片段",
    },
    "es": {
        "stats_model": "| Modelo | Prompts escritos para él |",
        "stats_use_case": "| Caso de uso | Prompts |",
        "stats_mode": "| Modo | Prompts |",
        "use_cases": {"camera-moves": "Movimientos de cámara", "product": "Producto", "portrait": "Retrato", "nature": "Naturaleza",
                      "action": "Acción", "ads": "Anuncios", "anime": "Anime", "image-to-video": "Imagen a video", "stills": "Imágenes fijas (prompts de imagen)"},
        "modes": {"t2v": "texto a video", "i2v": "imagen a video", "t2i": "texto a imagen", "i2i": "edición de imagen"},
        "summary": lambda s: "%d prompts en total: %d de video, %d de imagen. %d tienen un reporte de render (`rendered_on` no está vacío); "
                             "%d siguen la guía de prompts del proveedor o la biblioteca de UniqAI, pero todavía no tienen reporte de render."
                             % (s["total"], s["video"], s["image"], s["rendered"], s["unrendered"]),
        "all_link": lambda name: "Todos los prompts de %s con el texto completo →" % name.lower(),
        "rendered": "renderizado",
        "by_model": "Por modelo",
        "count": lambda n: "%d prompt%s" % (n, "" if n == 1 else "s"),
        "audio": "genera audio",
        "image_model": "modelo de imagen",
        "silent": "clips sin audio",
    },
    "pt-BR": {
        "stats_model": "| Modelo | Prompts escritos para ele |",
        "stats_use_case": "| Caso de uso | Prompts |",
        "stats_mode": "| Modo | Prompts |",
        "use_cases": {"camera-moves": "Movimentos de câmera", "product": "Produto", "portrait": "Retrato", "nature": "Natureza",
                      "action": "Ação", "ads": "Anúncios", "anime": "Anime", "image-to-video": "Imagem para vídeo", "stills": "Imagens estáticas (prompts de imagem)"},
        "modes": {"t2v": "texto para vídeo", "i2v": "imagem para vídeo", "t2i": "texto para imagem", "i2i": "edição de imagem"},
        "summary": lambda s: "%d prompts no total: %d de vídeo, %d de imagem. %d têm relato de renderização (`rendered_on` preenchido); "
                             "%d seguem o guia de prompts do fornecedor ou a biblioteca da UniqAI, mas ainda não têm relato de renderização."
                             % (s["total"], s["video"], s["image"], s["rendered"], s["unrendered"]),
        "all_link": lambda name: "Todos os prompts de %s com o texto completo →" % name.lower(),
        "rendered": "renderizado",
        "by_model": "Por modelo",
        "count": lambda n: "%d prompt%s" % (n, "" if n == 1 else "s"),
        "audio": "gera áudio",
        "image_model": "modelo de imagem",
        "silent": "clipes sem áudio",
    },
    "ja": {
        "stats_model": "| モデル | 対象プロンプト数 |",
        "stats_use_case": "| 用途 | プロンプト数 |",
        "stats_mode": "| モード | プロンプト数 |",
        "use_cases": {"camera-moves": "カメラワーク", "product": "商品", "portrait": "ポートレート", "nature": "自然", "action": "アクション",
                      "ads": "広告", "anime": "アニメ", "image-to-video": "画像から動画", "stills": "静止画（画像プロンプト）"},
        "modes": {"t2v": "テキストから動画", "i2v": "画像から動画", "t2i": "テキストから画像", "i2i": "画像編集"},
        "summary": lambda s: "合計 %d 件のプロンプト：動画 %d 件、画像 %d 件。%d 件にはレンダリング報告があり（`rendered_on` が空ではありません）、"
                             "%d 件はベンダーのプロンプトガイドまたは UniqAI のライブラリに基づいていますが、レンダリング報告はまだありません。"
                             % (s["total"], s["video"], s["image"], s["rendered"], s["unrendered"]),
        "all_link": lambda name: "「%s」のプロンプトをすべて全文で見る →" % name,
        "rendered": "レンダリング済み",
        "by_model": "モデル別",
        "count": lambda n: "%d 件" % n,
        "audio": "音声あり",
        "image_model": "画像モデル",
        "silent": "無音クリップ",
    },
    "ko": {
        "stats_model": "| 모델 | 해당 모델용 프롬프트 수 |",
        "stats_use_case": "| 용도 | 프롬프트 수 |",
        "stats_mode": "| 모드 | 프롬프트 수 |",
        "use_cases": {"camera-moves": "카메라 무브", "product": "제품", "portrait": "인물", "nature": "자연", "action": "액션",
                      "ads": "광고", "anime": "애니메이션", "image-to-video": "이미지를 영상으로", "stills": "정지 이미지(이미지 프롬프트)"},
        "modes": {"t2v": "텍스트에서 영상", "i2v": "이미지에서 영상", "t2i": "텍스트에서 이미지", "i2i": "이미지 편집"},
        "summary": lambda s: "총 %d개 프롬프트: 영상 %d개, 이미지 %d개. %d개는 렌더링 보고가 있고(`rendered_on`이 비어 있지 않음), "
                             "%d개는 제조사 프롬프트 가이드 또는 UniqAI 라이브러리를 따르지만 아직 렌더링 보고가 없습니다."
                             % (s["total"], s["video"], s["image"], s["rendered"], s["unrendered"]),
        "all_link": lambda name: "「%s」 프롬프트 전체 보기(전문 포함) →" % name,
        "rendered": "렌더링됨",
        "by_model": "모델별",
        "count": lambda n: "%d개 프롬프트" % n,
        "audio": "오디오 생성",
        "image_model": "이미지 모델",
        "silent": "무음 클립",
    },
}


def strings(lang):
    if lang not in STRINGS:
        raise KeyError("no README strings for language %r; add it to scripts/readme_i18n.py" % lang)
    return STRINGS[lang]


def use_case_label(meta, lang, key):
    names = strings(lang)["use_cases"]
    if names and key in names:
        return names[key]
    return meta["use_cases"].get(key, key)
