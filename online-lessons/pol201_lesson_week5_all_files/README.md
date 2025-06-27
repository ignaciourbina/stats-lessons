# Week 5 Lesson Package

This folder contains the Week 5 Qualtrics export (`Lesson_-_Week_5.qsf`) along with generated HTML.

* `site/` – multi-page version built with `qsf_to_html.py`.
* `spa_site/` – single-page version built via `build_spa.py`. It holds `index.html`, `script.js`, and the serialized `questions.json` used for rendering.

Run `python build_spa.py Lesson_-_Week_5.qsf --out-dir spa_site` to regenerate `questions.json`.
