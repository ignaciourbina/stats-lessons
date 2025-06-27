#!/usr/bin/env python3
"""Generate single-page app files from a QSF export."""

from __future__ import annotations

import argparse
import html
import json
import pathlib
import shutil

from qsf_to_html import extract_pages, parse_survey_flow


def build_questions(qsf_path: pathlib.Path) -> list[dict]:
    with qsf_path.open(encoding="utf-8") as f:
        qsf = json.load(f)

    elements = qsf["SurveyElements"]
    question_map = {e["Payload"]["QuestionID"]: e for e in elements if e["Element"] == "SQ"}
    block_dict = {
        blk["ID"]: blk
        for blk in (
            val
            for e in elements
            if e["Element"] == "BL"
            for val in e["Payload"].values()
            if isinstance(val, dict) and "BlockElements" in val
        )
    }
    flow_list = next(e["Payload"]["Flow"] for e in elements if e["Element"] == "FL")
    ordered_block_ids = list(parse_survey_flow(flow_list))

    questions: list[dict] = []
    for blk_id in ordered_block_ids:
        blk = block_dict.get(blk_id)
        if not blk:
            continue
        for be in blk["BlockElements"]:
            if be.get("Type") == "Question":
                qid = be["QuestionID"]
                payload = question_map[qid]["Payload"]
                q_html = html.unescape(payload["QuestionText"])
                choices = []
                if "Choices" in payload:
                    order = payload.get("ChoiceOrder") or list(payload["Choices"].keys())
                    for cid in order:
                        choice = payload["Choices"][str(cid)]
                        choices.append({"id": cid, "text": html.unescape(choice["Display"])})
                required = (
                    payload.get("Validation", {}).get("Settings", {}).get("ForceResponse")
                    == "ON"
                )
                questions.append({"id": qid, "html": q_html, "choices": choices, "required": required})
    return questions


def build_spa(qsf_path: pathlib.Path, out_dir: pathlib.Path) -> None:
    pages = extract_pages(qsf_path)
    questions = build_questions(qsf_path)
    if len(pages) != len(questions):
        raise ValueError("Question count mismatch")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "questions.json").write_text(json.dumps(questions, indent=2), encoding="utf-8")
    template_dir = pathlib.Path(__file__).parent / "spa_site"
    for name in ["index.html", "script.js"]:
        src = template_dir / name
        dst = out_dir / name
        if src.resolve() != dst.resolve():
            shutil.copy2(src, dst)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build SPA lesson")
    parser.add_argument("qsf", type=pathlib.Path, help="Path to QSF file")
    parser.add_argument("--out-dir", type=pathlib.Path, default=pathlib.Path("spa_site"), help="Output directory")
    args = parser.parse_args()
    build_spa(args.qsf, args.out_dir)
    print(f"\u2713 Wrote SPA files to {args.out_dir}/")
