# Workflow: Creating a Quiz Question Set

This guide explains how to draft a new quiz question set, log the source slides and export a Brightspace compatible CSV. Review the folder `weekly-quizzes/` and its `AGENTS.md` for context.

## Relevant Files and Protocols
- **weekly-quizzes/question_set_protocol.md** – quality standards and LaTeX format for questions.
- **weekly-quizzes/quiz-builder-module-protocol.md** – instructions for converting questions to CSV using `scripts/module_quiz_builder_to_csv.py`.
- **weekly-quizzes/question_log.md** – running log linking each question to the lecture slides.
- **weekly-quizzes/readme.md** – overview of quiz files per week.
- **scripts/AGENTS.md** – reminders on using the quiz builder module and validation scripts.
- **lecture-slides/slide_review_protocol.md** – how to review slides when collecting references.

## Step-by-Step Procedure
1. **Gather Input**
   - The user should specify which lecture slides the quiz will cover and provide any notes on question mix.
   - Locate the PDFs in `lecture-slides/` and review them, following `slide_review_protocol.md` if detailed notes are required.
2. **Draft Questions**
   - Follow the guidelines in `question_set_protocol.md` to write clear, technically correct questions with real-world context and plausible distractors.
   - Create a LaTeX file named `weekXX_quiz.tex` inside `weekly-quizzes/`, replacing `XX` with the week number.
   - List questions inside an `enumerate` environment as shown in existing quiz files.
3. **Create Answer Key**
   - In a separate file `weekXX_answers.tex`, record the correct option letter for each question.
4. **Add Notes and Log**
   - Summarise slide references and design choices in `weekXX_notes.md`.
   - Append an entry to `question_log.md` mapping each question to the corresponding slide numbers.
5. **Validate Numeric Answers** (if applicable)
   - Run the week-specific validator (e.g. `python3 scripts/validate_week04.py`) to ensure computed results match the recorded answers.
6. **Convert to CSV**
   - When the LaTeX set is final, use the workflow in `quiz-builder-module-protocol.md` and the API in `scripts/module_quiz_builder_to_csv.py` to export a Brightspace CSV.
7. **Store Results**
   - Keep the `.tex`, answer key, notes and generated `.csv` in `weekly-quizzes/`.
   - Commit changes and update any index files mentioned in `weekly-quizzes/readme.md`.

Following these steps ensures each quiz question set is well documented, validated and ready for upload to Brightspace.
