# AGENTS.md – online-lessons

## Mission
Maintain the fully online lesson packages.

## Key References
- `readme.md` in this folder describes the purpose of the subdirectories.
- Many lessons were migrated from Google Apps Script per `./migration_protocol/`.

## Common Tasks
- Update HTML/JS lesson packages when content changes.
- Keep each lesson self-contained for easy embedding in Brightspace.
- Reference `./migration_protocol/` if additional lessons need conversion.
- When editing a lesson, update the README in that lesson's folder so
  instructions stay current.
- Test `index.html` locally using a simple web server (e.g. `python3 -m
  http.server`) before committing changes to ensure pages load as expected.
