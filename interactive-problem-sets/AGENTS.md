# AGENTS.md – interactive-problem-sets

## Mission
Create and maintain small web-based problem sets that run directly in the browser.

## Key References
- `readme.md` in this folder explains the quiz object format and page structure.
- Styling comes from the repo root `styles.css` and `DESIGN_README.md`.

## Common Tasks
- Duplicate an existing set (e.g., `probability/`) and update `index.html` with new questions.
- Keep the JavaScript question objects in the same shape (`id`, `text`, `options`, `correctAnswer`, `explanation`).
- Test locally by opening `index.html`. No build step is required.
- If a folder contains `question_index.csv`, update it whenever you add or remove questions so IDs stay in sync.
 - When modifying numeric problems (e.g., the Introduction to Inference set), run `python3 scripts/validate_quiz.py html path/to/index.html` to verify computed answers.

Follow these guidelines when authoring new interactive exercises.
