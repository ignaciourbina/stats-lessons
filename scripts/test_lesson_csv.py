"""Simple integration test for lesson CSV conversion."""

import argparse
import csv
import json
import importlib.util
from pathlib import Path


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("converter", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def main(json_path: Path, csv_path: Path, script_path: Path) -> None:
    module = load_module(script_path)
    module.convert(json_path, csv_path)

    expected = len(json.loads(json_path.read_text(encoding="utf-8")))
    with csv_path.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    count = sum(1 for r in rows if r and r[0] == "NewQuestion")
    if count != expected:
        raise SystemExit(f"Row count mismatch: {count} != {expected}")
    print("All tests passed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("json", type=Path, help="Path to questions.json")
    parser.add_argument("csv", type=Path, help="Output CSV path")
    parser.add_argument(
        "--script",
        type=Path,
        default=Path("online-lessons/pol201_lesson_week5_all_files/export_to_d2l_csv.py"),
        help="Path to export_to_d2l_csv.py",
    )
    args = parser.parse_args()
    main(args.json, args.csv, args.script)
