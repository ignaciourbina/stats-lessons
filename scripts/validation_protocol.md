# Quiz Validation Protocol

This document explains how to verify that multiple-choice answers match the numeric computations used in the course materials. Validation supports both interactive HTML problem sets and the LaTeX question sets for weekly quizzes. Save validation outputs to `/answer-validations`

## Utility Modules
- `scripts/inference_utils.py` contains helpers for standard errors, confidence intervals and hypothesis tests.
- `scripts/quiz_validator.py` implements `HtmlQuizValidator` and `LatexQuizValidator` used by the command line tool.

## Command Line Scripts
Create a validator script for each quiz by subclassing `HtmlQuizValidator` or
`LatexQuizValidator` from `quiz_validator.py`. Run that script to generate a
CSV report with columns `question_id`, `file_answer`, `calculated_answer` and
`match`.

### HTML Example
```bash
python3 scripts/validate_intro_inference.py
```

### LaTeX Example
```bash
python3 scripts/validate_week04.py
```
