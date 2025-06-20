# Styling Guidelines

This document outlines the design parameters used to refresh the lesson pages.

## Goals
- Keep the HTML pages simple and focused on content.
- Apply a consistent look across all parts using a shared style sheet.
- Avoid complex frameworks; rely on plain CSS.

## Parameters
1. **Typography and Colors**
   - Body font: `Palatino Linotype`, `Palatino`, `Georgia`, `serif`.
   - Background color: `#dcf0fa`.
   - Text color: default browser text color on white containers.

2. **Layout**
   - Lesson content is injected into a `#content` container which centers the active page and limits its width.
   - Each page is wrapped in a box with a subtle border and shadow to separate it from the background.
   - Videos remain responsive using the existing 16:9 wrappers.

3. **Buttons and Forms**
   - Buttons share a single style: blue background, white text, rounded corners.
   - Form elements keep default browser styles for simplicity.

4. **Responsiveness**
   - Containers use `max-width: 800px` so pages look good on phones and desktops.
   - The layout does not rely on external libraries or heavy CSS frameworks.

By separating these styles into a standalone CSS file, we keep page HTML clean and content-oriented while still improving appearance.
