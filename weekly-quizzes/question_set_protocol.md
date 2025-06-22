# Weekly Quiz Question Set Protocol

This protocol describes how to generate a set of quiz questions based on specific lecture slides and any instructions on the mix or focus of questions. The goal is to keep each quiz closely tied to the material from the slide decks in `lecture-slides/`.

## 1. Collect Slide References
1. The user will specify which lecture slides are covered for the given week.
2. Locate the PDF files in the `lecture-slides/` folder and review them, using the notes created via `lecture-slides/slide_review_protocol.md` if available.

## 2. Determine Question Mix
1. From the user's instructions, note the desired balance of question types (e.g., multiple choice, true/false, short answer, numeric problems).
2. Decide how many questions to generate of each type. Keep the total manageable for a short weekly quiz.

## 3. Write Questions
1. Use definitions, formulas and examples from the specified slides to craft each question.
2. For numeric questions, verify any calculated answers using helper functions in `scripts/inference_utils.py` when appropriate.
3. Ensure the wording clearly indicates the link to the lecture content so students can relate each question back to the slides.
4. Provide a sentence or two of real-world context for numeric problems so students know what the numbers represent.

## 4. Produce a LaTeX File
1. Use Python to create a `.tex` file containing the questions. A minimal example is shown below. Each question becomes an item in an ordered list.

```python
from pathlib import Path

# Replace with LaTeX strings for each question
questions = [
    r"Explain the difference between a population and a sample.",
    r"$\\sigma^2$ denotes the population variance. Write the formula for the sample variance."
]

content = "\n".join([
    r"\\documentclass{article}",
    r"\\begin{document}",
    r"\\begin{enumerate}",
    *[f"\\item {q}" for q in questions],
    r"\\end{enumerate}",
    r"\\end{document}",
])

Path("weekly-quizzes/weekXX_quiz.tex").write_text(content)
```

2. Replace `weekXX_quiz.tex` with the actual week number.

## 5. Optional Brightspace CSV
If the quiz needs to be uploaded to Brightspace, convert the LaTeX questions to HTML/Unicode and use the quiz builder API in `scripts/module_quiz_builder_to_csv.py`. The step-by-step process is outlined in `instructions/agents/AGENTS.md`.

## 6. Log Your Work
Create a brief Markdown file (e.g., `weekXX_notes.md`) describing which slides were used and any decisions about question focus. Store this log alongside the generated quiz file.

Following this protocol ensures that weekly quiz questions remain closely connected to the lecture material and are easy to convert for Brightspace if needed.

