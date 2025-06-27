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

import json
import html
import pathlib
import zipfile
import argparse
import os
import sys


def extract_pages(qsf_path: pathlib.Path):
    """Return a list of HTML strings (one per survey question) in flow order."""
    with qsf_path.open(encoding="utf-8") as f:
        qsf_data = json.load(f)

    elements = qsf_data["SurveyElements"]
    question_map = {
        q["Payload"]["QuestionID"]: q for q in elements if q["Element"] == "SQ"
    }

    # Collect blocks
    blocks = []
    for e in elements:
        if e["Element"] == "BL":
            for val in e["Payload"].values():
                if isinstance(val, dict) and "BlockElements" in val:
                    blocks.append(val)
    block_dict = {blk["ID"]: blk for blk in blocks}

    # Survey flow (assumes a single FL element)
    flow = next(e["Payload"]["Flow"] for e in elements if e["Element"] == "FL")

    pages = []
    for node in flow:
        if node["Type"] == "Standard" and node["ID"].startswith("BL_"):
            blk = block_dict.get(node["ID"])
            if not blk:
                continue
            for be in blk["BlockElements"]:
                if be["Type"] == "Question":
                    qid = be["QuestionID"]
                    payload = question_map[qid]["Payload"]
                    pages.append(html.unescape(payload["QuestionText"]))
    return pages


def build_site(pages, out_dir: pathlib.Path):
    """Create HTML pages and an index in *out_dir*."""
    out_dir.mkdir(parents=True, exist_ok=True)

    total = len(pages)
    for idx, page_html in enumerate(pages, start=1):
        prev_link = f"page{idx-1:02}.html" if idx > 1 else None
        next_link = f"page{idx+1:02}.html" if idx < total else None

        nav_parts = [
            '<nav style="text-align:center; margin-top:40px;">',
        ]
        if prev_link:
            nav_parts.append(
                f'<a href="{prev_link}" style="margin-right:20px;">&laquo; Previous</a>'
            )
        if next_link:
            nav_parts.append(f'<a href="{next_link}">Next &raquo;</a>')
        nav_parts.append("</nav>")
        nav_html = "".join(nav_parts)

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

    # Build index.html
    links = "\n".join(
        f'<li><a href="page{idx:02}.html">Page {idx}</a></li>' for idx in range(1, total + 1)
    )
    index_html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <title>Lesson Index</title>
</head>
<body>
<h1>Lesson Index</h1>
<ol>
{links}
</ol>
</body>
</html>"""
    (out_dir / "index.html").write_text(index_html, encoding="utf-8")



def package_zip(out_dir: pathlib.Path, zip_path: pathlib.Path):
    """Zip the contents of *out_dir* into *zip_path*."""
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in out_dir.rglob("*"):
            if file.is_file():
                zf.write(file, file.relative_to(out_dir))



def main():
    parser = argparse.ArgumentParser(
        description="Convert QSF to a linked static HTML site (plus ZIP archive)."
    )
    parser.add_argument("qsf", type=pathlib.Path, help="Path to the .qsf file")
    parser.add_argument(
        "--out-dir",
        default="site",
        type=pathlib.Path,
        help="Directory where generated HTML files will be written",
    )
    parser.add_argument(
        "--zip",
        default="site.zip",
        type=pathlib.Path,
        help="Path of the resulting ZIP archive",
    )

    args = parser.parse_args()

    print(f"Reading QSF {args.qsf}")
    pages = extract_pages(args.qsf)
    print(f"Found {len(pages)} pages.")
    if not pages:
        sys.exit("No pages found – is this a valid QSF export?")

    print(f"Building HTML site in {args.out_dir}")
    build_site(pages, args.out_dir)

    print(f"Packaging site as {args.zip}")
    package_zip(args.out_dir, args.zip)
    print("Done.")


if __name__ == "__main__":
    main()
