# Protocol: Migrating SPA Lessons to a Brightspace Quiz

This guide explains how to convert an interactive lesson stored in `spa_site/` into a Brightspace‑compatible quiz CSV using the quiz builder module.

## 1. Prepare the Environment
1. Ensure Python 3.8+ is available.
2. Place `module_quiz_builder_to_csv.py` in `D2L_LMS_Quiz_and_Lesson_Builder/` (already in the repo).
3. Install any required packages (none beyond the standard library).

## 2. Generate the CSV
1. Navigate to the lesson folder. Example for Week 5:
   ```bash
   cd online-lessons/pol201_lesson_week5_all_files
   ```
2. Run the helper script to convert `questions.json`:
   ```bash
   python3 export_to_d2l_csv.py spa_site/questions.json lesson_week5.csv
   ```
   The script cleans unsupported `<meta>`, `<style>` and `<title>` tags and exports a CSV containing `SectionHeader` rows for informational slides and `MultipleChoice` rows for questions.

## 3. Import into Brightspace
1. In Brightspace, open the course quiz tool and choose **Import / Upload a File**.
2. Select the generated `lesson_week5.csv` and complete the import.
3. Each slide appears in order; questions have all options worth 0 points so the lesson functions as ungraded interactive content.

## 4. Customisation Notes
- Edit `export_to_d2l_csv.py` if you need to change how slides are labelled or assign points.
- The script uses the `QuestionBank` API documented in `module_quiz_builder_to_csv.py`.

This process preserves the lesson text while adapting it to the Brightspace quiz format without any JavaScript.
