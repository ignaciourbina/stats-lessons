from pathlib import Path
import argparse

from quiz_validator import HtmlQuizValidator, LatexQuizValidator


def main():
    parser = argparse.ArgumentParser(description="Validate quiz answer files")
    subparsers = parser.add_subparsers(dest="format", required=True)

    html_p = subparsers.add_parser("html", help="Validate HTML problem set")
    html_p.add_argument("html_file", type=Path)
    html_p.add_argument("--output", "-o", type=Path, default=Path("validation_report.csv"))

    tex_p = subparsers.add_parser("latex", help="Validate LaTeX quiz")
    tex_p.add_argument("quiz_file", type=Path)
    tex_p.add_argument("answers_file", type=Path)
    tex_p.add_argument("--output", "-o", type=Path, default=Path("validation_report.csv"))

    args = parser.parse_args()

    if args.format == "html":
        validator = HtmlQuizValidator(args.html_file, args.output)
    else:
        validator = LatexQuizValidator(args.quiz_file, args.answers_file, args.output)

    validator.validate()
    print(f"Report written to {validator.output_csv}")


if __name__ == "__main__":
    main()
