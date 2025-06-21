# Introduction to Inference Problem Set Validation Protocol

This document describes the procedure used to verify that the hard-coded answers in
`interactive-problem-sets/introduction-to-inference/index.html` match the results of
independent calculations.

## Steps

1. **Utility Module** – `scripts/inference_utils.py`
   - Provides helper functions for standard errors, confidence intervals,
     hypothesis tests and required sample sizes derived from Lecture Slides 7 and 8.
   - Functions rely only on Python's standard library (`math` and `statistics`).

2. **Validation Script** – `scripts/validate_intro_inference.py`
   - Parses the HTML file for each question's `id` and `correctAnswer` letter.
   - Recreates all numeric problems from the HTML with hard-coded parameters and
     computes answers using functions from `inference_utils`.
   - Writes `intro_inference_validation.csv` summarising the HTML answer,
     the calculated answer and whether they match for each numeric question.

3. **Running Validation**

```bash
python3 scripts/validate_intro_inference.py
```

The script produces `intro_inference_validation.csv` in the repository root.
Any discrepancy will appear with `False` in the `match` column.
