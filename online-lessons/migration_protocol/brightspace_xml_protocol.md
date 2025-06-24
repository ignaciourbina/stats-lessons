# Brightspace XML to HTML Protocol

This guide documents how to convert a Brightspace quiz XML export into a modular
HTML lesson compatible with the existing online problem set format.

1. **Run the converter**

   Use `python3 scripts/brightspace_xml_to_html.py INPUT_XML OUTPUT_DIR`.
   The script extracts each `<section>` from the XML and writes `PageN.html`
   fragments along with `index.html` and `scripts.js` in the specified output
   directory.

2. **Page structure**

   - `index.html` loads a single `#content` container and pulls in shared
     `styles.css` from the repo root.
   - `scripts.js` contains the `loadPage` function and an auto-generated
     `answers` object used by `sendSelectedResponse` for instant feedback.
   - Each `PageN.html` contains the HTML from the lesson section plus any
     questions converted from the Brightspace items.

3. **Editing**

   Pages may be modified manually after generation to clean up formatting or
   adjust content. Update `README.md` in the lesson folder with any notes.

Use this protocol when migrating additional Brightspace lessons.
