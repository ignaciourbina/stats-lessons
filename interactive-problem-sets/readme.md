# Interactive Problem Sets

This folder collects small web-based problem sets. Each subfolder contains a self-contained `index.html` that can run directly in a browser or learning management system.

Current directories:

- **probability/** – interactive questions covering basic probability theory.
- **inference-one-proportion/** – placeholder for a future exercise.
- **style.css** – minimal shared styling used by the sets.

## Implementation Overview

Each problem set is built from a single HTML page with inline JavaScript. The layout relies on **Tailwind CSS** loaded via CDN along with the **Inter** Google Font. **MathJax** typesets any formulas. The main container centers the quiz and keeps the design mobile friendly.

### Page Structure

- `index.html` contains a header, a `#quiz-area` for questions and a hidden `#results-container` shown after submission.
- Questions live in a `questions` array of objects with `id`, `text`, an array of `options`, a `correctAnswer`, and an `explanation`.
- Navigation buttons (previous, next, submit) are inserted dynamically below the question block.

### Script Behaviour

1. `renderQuestion()` populates the current question and shuffles options.
2. `handleOptionChange()` records the selected response.
3. `prevQuestion()` and `nextQuestion()` move through the quiz while `renderNavigation()` updates the controls.
4. `submitQuiz()` reveals the results section and re-runs MathJax so formulas display correctly.

## Creating a New Problem Set

1. **Duplicate an existing folder** such as `probability` and rename it to your topic (e.g. `inference-two-proportions`).
2. **Update `index.html`**:
   - Change the page title and header text.
   - Replace the `questions` array with your own questions using the same object structure.
3. **Add formulas** directly in the `text` or `explanation` fields using LaTeX syntax if needed.
4. **Test locally** by opening `index.html` in a browser. No build step is required since everything is plain HTML and JavaScript.

Following these guidelines, you can quickly author additional interactive problem sets without modifying the underlying script logic.
