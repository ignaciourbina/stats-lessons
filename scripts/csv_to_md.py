import csv
from pathlib import Path


def csv_to_markdown(csv_path: Path, md_path: Path) -> None:
    """Read a CSV file and write its contents as a markdown table."""
    with csv_path.open(newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        return
    headers, body = rows[0], rows[1:]
    with md_path.open("w") as f:
        f.write("| " + " | ".join(headers) + " |\n")
        f.write("|" + " --- |" * len(headers) + "\n")
        for row in body:
            f.write("| " + " | ".join(row) + " |\n")


if __name__ == "__main__":
    CSV_FILE = Path(
        "interactive-problem-sets/introduction-to-inference/question_index.csv"
    )
    MD_FILE = CSV_FILE.with_suffix(".md")
    csv_to_markdown(CSV_FILE, MD_FILE)
