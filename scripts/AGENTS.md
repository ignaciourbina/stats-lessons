# AGENTS.md – scripts

## Mission
Provide utilities for quiz building and problem set validation.

## Key References
- `validation_protocol.md` explains how to verify numeric answers.
- `module_quiz_builder_to_csv.py` is the API for generating Brightspace quiz CSVs.
  The `instructions/agents/AGENTS.md` profile provides a complete workflow for
  turning LaTeX or HTML questions into Python code. Review that guide before
  writing any quiz scripts.

The old text dump `Module_Quiz_Builder_to_CSV_py.txt` is no longer included.
Use the Python module in this folder directly.

## Common Tasks
- Run `python3 validate_intro_inference.py` to check the introduction to inference
  problem set. The script reads `interactive-problem-sets/introduction-to-inference/index.html`,
  computes numeric answers with functions from `inference_utils.py` and writes
  `intro_inference_validation.csv` summarising whether each answer matches the
  HTML.

- When building quizzes, import `module_quiz_builder_to_csv.py` and assemble the
  questions using its dataclasses (`QuestionBank`, `MultipleChoice`, `TFOption`,
  etc.). Call `export_csv()` to save a Brightspace-ready file. Follow the steps
  in `instructions/agents/AGENTS.md` for formatting guidelines.

- `inference_utils.py` offers helper functions such as `se_mean`,
  `confidence_interval_proportion`, and `z_test_proportion`. These mirror
  procedures from the lecture slides and can be reused in new validation scripts
  or Jupyter notebooks.
