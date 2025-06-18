# Migration Protocol from Google Apps Script to HTML/JavaScript

This document describes the basic steps used to migrate the lesson app from Google Apps Script (GAS) into a standalone HTML + JavaScript project suitable for embedding in Brightspace.

1. **Create a new project folder** for the HTML version. All migrated pages and scripts live in this folder. For example `pol201_lesson_week4_part1_htmljs`.
2. **Copy each GAS HTML file** (e.g., `Page1.html`, `Page2.html`, etc.) into the new folder. Remove any `<style>` blocks and replace class based styling with small inline `style` attributes because Brightspace does not support custom stylesheets.
3. **Replace server side calls.** GAS used `google.script.run` to load pages and verify answers. In the new version, a simple `fetch` loads each page fragment and answer validation is handled entirely in a `scripts.js` file on the client.
4. **Use a modular design.** Each question or video remains in its own HTML file. `index.html` contains an empty `<div id="content"></div>` and the script dynamically fetches and injects the desired page when navigation buttons are pressed.
5. **Implement the check logic in JavaScript.** Create a `checkAnswer` function replicating the original GAS logic. This keeps behaviour the same without any server calls.
6. **Ensure responsive layout.** Videos and question blocks use simple `div` containers and inline styles such as `width:100%` so that the content adjusts on mobile screens. No external CSS is required.
7. **Maintain documentation.** Store these instructions along with a database of videos and questions (see `DATABASE.md`) inside the `migration_protocol` folder so future lessons can follow the same approach.

Following these guidelines allows any lesson originally built with Apps Script to be converted into a lightweight HTML package ready for LMS deployment.
