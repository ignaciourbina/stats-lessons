#!/usr/bin/env python3
"""
qsf_to_html.py

Convert a Qualtrics Survey Format (QSF) export into a set of linked HTML
pages (one page per question) plus an index.html. All files are bundled
into a ZIP archive for convenient download.

Usage:
    python qsf_to_html.py <path_to_qsf> [--out-dir OUTPUT_DIR]

Requirements: Python 3.8+
"""

from __future__ import annotations

import argparse
import html
import json
import pathlib
import sys
import zipfile
from typing import Generator, Iterable, List, Dict, Any

###############################################################################
# Survey‑flow helpers
###############################################################################

def parse_survey_flow(
    flow_nodes: Iterable[dict],
    *,
    include_branch_flows: bool = True,
) -> Generator[str, None, None]:
    """Yield *Block IDs* in the left‑to‑right order Qualtrics presents them.

    Parameters
    ----------
    flow_nodes
        The list under ``SurveyElements ▸ FL ▸ Payload ▸ Flow``.
    include_branch_flows
        Traverse children inside *Branch* or *Randomizer* nodes when *True*
        (default).  If *False* they are skipped.
    """
    for node in flow_nodes:
        node_type = node.get("Type")
        node_id = node.get("ID", "")

        # Simple single‑block entries
        if node_type in {"Standard", "Block"} and node_id.startswith("BL_"):
            yield node_id

        # Composite nodes – descend recursively
        elif node_type in {"Branch", "Randomizer"} and include_branch_flows:
            yield from parse_survey_flow(node.get("Flow", []))

        # Ignore EndSurvey, EmbeddedData, etc.
        else:
            continue


def extract_pages(qsf_path: pathlib.Path) -> List[str]:
    """Return question HTML fragments in true survey‑flow order."""
    with qsf_path.open(encoding="utf-8") as f:
        qsf_data = json.load(f)

    elements: List[Dict[str, Any]] = qsf_data["SurveyElements"]

    # Build look‑up tables ----------------------------------------------------
    question_map = {
        q["Payload"]["QuestionID"]: q for q in elements if q["Element"] == "SQ"
    }

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

    # Top‑level flow list -----------------------------------------------------
    flow_list: List[dict] = next(
        e["Payload"]["Flow"] for e in elements if e["Element"] == "FL"
    )

    ordered_block_ids = list(parse_survey_flow(flow_list))

    # Assemble page list ------------------------------------------------------
    pages: List[str] = []
    for blk_id in ordered_block_ids:
        blk = block_dict.get(blk_id)
        if not blk:
            continue
        for be in blk["BlockElements"]:
            if be.get("Type") == "Question":
                qid = be["QuestionID"]
                payload = question_map[qid]["Payload"]
                pages.append(html.unescape(payload["QuestionText"]))
    return pages

###############################################################################
# HTML generation
###############################################################################

NAV_STYLE = "text-align:center; margin-top:40px;"


def build_site(pages: List[str], out_dir: pathlib.Path) -> None:
    """Create HTML pages and an index in *out_dir*."""
    out_dir.mkdir(parents=True, exist_ok=True)
    total = len(pages)

    for idx, page_html in enumerate(pages, start=1):
        prev_link = f"page{idx-1:02}.html" if idx > 1 else None
        next_link = f"page{idx+1:02}.html" if idx < total else None

        nav_links = []
        if prev_link:
            nav_links.append(
                f'<a href="{prev_link}" style="margin-right:20px;">&laquo; Previous</a>'
            )
        if next_link:
            nav_links.append(f'<a href="{next_link}">Next &raquo;</a>')

        nav_html = (
            f'<nav style="{NAV_STYLE}">' + "".join(nav_links) + "</nav>"
            if nav_links
            else ""
        )

        full_html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <title>Lesson Page {idx}</title>
</head>
<body>
{page_html}
{nav_html}
</body>
</html>"""

        (out_dir / f"page{idx:02}.html").write_text(full_html, encoding="utf-8")

    # Build index.html -------------------------------------------------------
    links = "\n".join(
        f'<li><a href="page{idx:02}.html">Page {idx}</a></li>'
        for idx in range(1, total + 1)
    )
    index_html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head><meta charset=\"UTF-8\"><title>Lesson Index</title></head>
<body>
<h1>Lesson Index</h1>
<ol>
{links}
</ol>
</body>
</html>"""

    (out_dir / "index.html").write_text(index_html, encoding="utf-8")

###############################################################################
# CLI
###############################################################################

def _parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert QSF to HTML lessons")
    parser.add_argument("qsf", type=pathlib.Path, help="Path to .qsf file")
    parser.add_argument(
        "--out-dir",
        type=pathlib.Path,
        default=pathlib.Path("site"),
        help="Destination directory for HTML files (default: ./site)",
    )
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> None:
    args = _parse_args(sys.argv[1:] if argv is None else argv)
    pages = extract_pages(args.qsf)
    build_site(pages, args.out_dir)
    print(f"✓ Wrote {len(pages)} pages to {args.out_dir}/")


if __name__ == "__main__":
    main()
