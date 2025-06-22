# AGENTS.md – scripts

## Mission
Provide utilities for quiz building and problem set validation.

## Key References
- `validation_protocol.md` explains how to verify numeric answers.
- `module_quiz_builder_to_csv.py` is the API for generating Brightspace quiz CSVs.
- `Module_Quiz_Builder_to_CSV_py.txt` may contain the latest text version of the module.

## Common Tasks
- Run `python3 validate_intro_inference.py` to check the introduction to inference problem set. Results appear in `intro_inference_validation.csv`.
- When asked to build quizzes from LaTeX/HTML, read the quiz builder module, create the Python script using its classes, and show how to call `export_csv()`.
