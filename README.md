# Stats Lessons Repository

This repository stores materials for the POL201 statistics course. The content is organized by type so that lessons, slides and supporting resources can be uploaded to a learning management system.

## Folder Overview

- **interactive-problem-sets/** – small standalone web exercises. Includes a probability set, an introduction to inference set and a placeholder for inference for one proportion.
- **lecture-slides/** – PDF slide decks for each lecture.
- **migration_protocol/** – documentation describing how Google Apps Script lessons were migrated to static HTML/JS along with a database of videos and questions.
- **online-lessons/** – fully online lesson packages. This folder now holds the Week&nbsp;4 lessons in both Google Apps Script and HTML/JS forms.
- **weekly-quizzes/** – LaTeX question sets, notes and logs used to generate Brightspace quiz CSVs.
- **styles.css** – shared CSS used by some of the HTML lesson pages.
- **scripts/** – Python utilities for quiz building and answer validation.
- **instructions/** – assistant protocols referenced by the various `AGENTS.md` files.

The `DESIGN_README.md` file outlines styling guidelines used when refreshing the lesson pages.

For usage instructions see `AGENTS.md` in the repository root. It links to the
`AGENTS.md` files inside each folder and explains how the tools fit together.
When tasks span multiple folders—for example using the validation scripts in
`scripts/` on questions in `interactive-problem-sets`—follow those cross
referenced protocols to ensure the correct workflow.
