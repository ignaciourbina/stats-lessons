# Weekly Quizzes

This folder stores the LaTeX question sets and supporting notes used to build weekly Brightspace quizzes.

Current files include material for Week&nbsp;4:

- `week04_quiz.tex` – multiple choice questions in LaTeX format.
- `week04_answers.tex` – solutions for the Week&nbsp;4 quiz.
- `week04_notes.md` – slide references and additional notes.
- `question_log.md` – running list mapping each question to its source slide.
- `question_set_protocol.md` – guidelines for preparing new question sets.

Convert question sets to CSV using `scripts/module_quiz_builder_to_csv.py` when ready for Brightspace import. See `AGENTS.md` for the full workflow and run the appropriate validation script (e.g. `python3 scripts/validate_week04.py`) to confirm numeric solutions before exporting.
