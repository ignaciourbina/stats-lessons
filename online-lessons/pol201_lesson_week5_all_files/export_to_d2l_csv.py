"""Convert lesson JSON into a Brightspace compatible quiz CSV."""

import json
import logging
from pathlib import Path
import sys

from typing import Any, List

# Ensure the quiz builder module is importable when running this script
ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR / "D2L_LMS_Quiz_and_Lesson_Builder"))

from module_quiz_builder_to_csv import (
    QuestionBank,
    MultipleChoice,
    MCOption,
    SectionHeader,
)

from bs4 import BeautifulSoup

ALLOWED_TAGS = {
    "p",
    "b",
    "strong",
    "em",
    "i",
    "ul",
    "ol",
    "li",
    "br",
    "span",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "img",
    "div",
}


def clean_html(text: str) -> str:
    """Sanitise lesson HTML removing unsupported tags and attributes."""
    soup = BeautifulSoup(text, "html.parser")
    for tag in soup.find_all(True):
        if tag.name not in ALLOWED_TAGS:
            tag.decompose()
            continue
        # Drop event handlers and inline styles
        tag.attrs = {
            k: v
            for k, v in tag.attrs.items()
            if not k.lower().startswith("on") and k.lower() not in {"style"}
        }
    return str(soup).strip()

def convert(json_path: Path, csv_path: Path, *, points: int = 0) -> None:
    """Convert `json_path` into a Brightspace CSV saved to `csv_path`."""
    try:
        data: List[dict[str, Any]] = json.loads(json_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        logging.error("Invalid JSON: %s", exc)
        raise SystemExit(1)

    bank = QuestionBank()
    slide_num = 1
    qnum = 1
    for idx, item in enumerate(data, 1):
        if "html" not in item:
            logging.warning("Item %s missing 'html' key; skipping", idx)
            continue
        html = clean_html(str(item.get("html", "")))
        choices = item.get("choices")
        if isinstance(choices, list) and choices:
            options = []
            for c in choices:
                if "text" not in c:
                    logging.warning("Question %s has choice without text", idx)
                    continue
                options.append(MCOption(percent=0, text=c["text"], html_used=True))
            mc = MultipleChoice(
                title=f"Question {qnum}",
                question_text=html,
                points=points,
                options=options,
                html_used=True,
            )
            bank.add(mc)
            qnum += 1
        else:
            bank.add(SectionHeader(title=f"Slide {slide_num}", body_html=html))
            slide_num += 1

    bank.export_csv(csv_path)
    logging.info("Wrote %s", csv_path)
    logging.info("Processed %d slides and %d questions", slide_num - 1, qnum - 1)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert lesson JSON to D2L CSV")
    parser.add_argument("json", type=Path, help="Path to questions.json")
    parser.add_argument("csv", type=Path, help="Output CSV path")
    parser.add_argument("--points", type=int, default=0, help="Point value for each question")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING, format="%(levelname)s: %(message)s")

    convert(args.json, args.csv, points=args.points)
