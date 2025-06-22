# AGENTS.md – weekly-quizzes

## Mission
Store Brightspace-ready quiz CSV files for each week and track the LaTeX question sets that produce them.

## Key References
- `readme.md` summarises the folder purpose.
- Use the quiz builder instructions in `weekly-quizzes/quiz-builder-module-protocol.md` and the API in `scripts/module_quiz_builder_to_csv.py` when creating new quizzes.
- Follow `question_set_protocol.md` to build the LaTeX question set for each week before converting to CSV.
- All quiz questions should meet the quality standards in that protocol: verify answers, write in clear grammar, embed real-world context, and use plausible distractors for multiple-choice.

## Workflow Summary
1. **Create question sets** – generate a `.tex` file using `question_set_protocol.md`. These question sets capture new material from the lecture slides.
2. **Transform to CSV** – convert completed question sets to Brightspace CSV format using the quiz builder script. This step is separate from authoring the questions.

## Common Tasks
- Add or update LaTeX question sets (`weekXX_quiz.tex`) as new material is covered.
- Produce Brightspace-ready CSV files named by week (e.g., `week01_quiz.csv`).
- Record each question source and manual edits in `question_log.md`.
- Include a brief notes file for each week describing slide references and choices of question types.

These steps keep weekly quizzes organised from draft questions to final CSV imports.
