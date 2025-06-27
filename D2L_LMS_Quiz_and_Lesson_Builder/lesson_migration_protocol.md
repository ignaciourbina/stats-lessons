# Protocol: Migrating SPA Lessons to a Brightspace Quiz

This guide explains how to convert an interactive lesson stored in `spa_site/` into a Brightspace‑compatible quiz CSV using the quiz builder module.

## 1. Prepare the Environment
1. Ensure Python 3.8+ is available.
2. Place `module_quiz_builder_to_csv.py` in `D2L_LMS_Quiz_and_Lesson_Builder/` (already in the repo).
3. Install dependencies:
   ```bash
   pip install beautifulsoup4
   ```

## 2. Generate the CSV
1. Navigate to the lesson folder. Example for Week 5:
   ```bash
   cd online-lessons/pol201_lesson_week5_all_files
   ```
2. Run the helper script to convert `questions.json`:
   ```bash
   python3 export_to_d2l_csv.py spa_site/questions.json lesson_week5.csv --verbose
   ```
   The script now sanitises HTML by removing unsupported tags (e.g. `<meta>`, `<style>`, `<title>`, `<script>`, `<iframe>`), strips inline styles and event handlers, and logs warnings for missing fields. Use `--points` to set a non‑zero score per question if desired.
3. Verify the output using the test helper:
   ```bash
   python3 scripts/test_lesson_csv.py spa_site/questions.json lesson_week5.csv
   ```
   This confirms the row count matches the lesson JSON.

## 3. Import into Brightspace
1. In Brightspace, open the course quiz tool and choose **Import / Upload a File**.
2. Select the generated `lesson_week5.csv` and complete the import.
3. Each slide appears in order; questions receive the point value specified with `--points` (default 0).

## 4. Customisation Notes
- The helper accepts `--points` and `--verbose`; editing the script should rarely be necessary.
- The script uses the `QuestionBank` API documented in `module_quiz_builder_to_csv.py`.

This process preserves the lesson text while adapting it to the Brightspace quiz format without any JavaScript.
