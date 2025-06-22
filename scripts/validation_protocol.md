# Quiz Validation Protocol

This document explains how to verify that multiple-choice answers match the numeric computations used in the course materials. Validation supports both interactive HTML problem sets and the LaTeX question sets for weekly quizzes.

## Utility Modules
- `scripts/inference_utils.py` contains helpers for standard errors, confidence intervals and hypothesis tests.
- `scripts/quiz_validator.py` implements `HtmlQuizValidator` and `LatexQuizValidator` used by the command line tool.

## Command Line Tool
Use `scripts/validate_quiz.py` with the desired format and file paths.

### HTML Example
```bash
python3 scripts/validate_quiz.py html interactive-problem-sets/introduction-to-inference/index.html -o intro_inference_validation.csv
```

### LaTeX Example
```bash
python3 scripts/validate_quiz.py latex weekly-quizzes/week04_quiz.tex weekly-quizzes/week04_answers.tex -o week04_validation.csv
```

The script writes a CSV report with columns `question_id`, `file_answer`, `calculated_answer` and `match`. The helper `validate_intro_inference.py` remains as a shortcut for validating the Introduction to Inference set.
