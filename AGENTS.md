# Stats Lessons Assistant Protocol

This repository collects materials for an introduction to statistics course. You are an assistant helping the maintainer create and maintain this content. Typical tasks include writing new problem sets, migrating lesson content, generating quizzes, and summarizing lecture slides.

## Using Folder Specific Guidance

Every major folder contains its own `AGENTS.md` describing modules, APIs and common tasks in that area. When working inside a folder, read its `AGENTS.md` and follow those instructions—they override this root profile. The root file provides a map of the repo and references to the main protocols:
Refer to `README.md` for a quick overview of the folder layout.

- `interactive-problem-sets/` – web-based exercises. See its `AGENTS.md` and `interactive-problem-sets/readme.md` for format and scripting details.
- `lecture-slides/` – PDF slide decks and notes. Follow `lecture-slides/AGENTS.md` and the `slide_review_protocol.md` when summarizing slides.
- `online-lessons/migration_protocol/` – guidelines for converting Google Apps Script lessons to HTML/JS. See `online-lessons/migration_protocol/AGENTS.md`.
- `scripts/` – utility modules and validation scripts. `scripts/AGENTS.md` covers how to run the tools, including quiz building.
- `online-lessons/` – migrated lesson packages. Refer to its `AGENTS.md` when editing these modules.
 - `weekly-quizzes/` – stores Brightspace quiz CSVs **and** the LaTeX question sets that generate them. See its `AGENTS.md` for the workflow from drafting questions to CSV output.
- Styling conventions live in `DESIGN_README.md`.

For building quiz CSV files from LaTeX or HTML, follow the dedicated instructions in `weekly-quizzes/quiz-builder-module-protocol.md`.

Ensure any responses or code snippets reference the relevant protocol so users can follow up locally.
