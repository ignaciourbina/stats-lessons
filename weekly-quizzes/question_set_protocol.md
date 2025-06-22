# Weekly Quiz Question Set Protocol

This protocol describes how to generate a set of quiz questions based on specific lecture slides and any instructions on the mix or focus of questions. The goal is to keep each quiz closely tied to the material from the slide decks in `lecture-slides/`.

## Quality Standards
All questions must satisfy these requirements:
1. **Technical correctness** – provide enough information for the intended computation or reasoning and double-check the answer.
2. **Grammatical clarity** – use clean sentences free of typos or awkward phrasing.
3. **Real-world context** – start with one or two sentences that place the problem in a familiar setting instead of opening with raw numbers or formulas.
4. **Multiple-choice design** – when writing MC questions, include strong distractors that use the given numbers incorrectly in subtle ways so they appear plausible.

## 1. Collect Slide References
1. The user will specify which lecture slides are covered for the given week.
2. Locate the PDF files in the `lecture-slides/` folder and review them, using the notes created via `lecture-slides/slide_review_protocol.md` if available.

## 2. Determine Question Mix
1. From the user's instructions, note the desired balance of question types (e.g., multiple choice, true/false, short answer, numeric problems).
2. Decide how many questions to generate of each type. Keep the total manageable for a short weekly quiz.

## 3. Write Questions
1. Use definitions, formulas and examples from the specified slides and clearly reference the lecture content.
2. Start each question with a short scenario that connects the topic to something familiar.
3. Verify numeric answers using helper functions in `scripts/inference_utils.py` when needed so the correct option is beyond doubt.
4. Keep the language concise and grammatically correct.
5. When drafting multiple-choice items, create plausible distractors that misuse the provided numbers or formulas in subtle ways.

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

