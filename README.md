# Institute for Extraterrestrial Inquiry

Static research site on whether extraterrestrial life is real. Pages live in `content/*.md`; `python3 build.py` regenerates `public/`.

## Front matter
```
---
title: Page title
slug: url-slug
category: Life in the Universe | The Search | UAP & Encounters | Claims & Verdicts
published: YYYY-MM-DD
updated: YYYY-MM-DD      (optional; set when revising a page)
verdict: Confirmed | Unexplained | Explained | Disputed   (optional; shown as badge)
summary: One sentence.
---
```
Body: `## headings`, paragraphs, `- lists`, `**bold**`, `*italic*`, `[links](https://...)`. End every page with a `## Sources` list of real, checked sources.

## Images and figures
Put image files in `static/images/` (web-sized, under 400 KB; JPG for photos, PNG for charts). On its own line write:
```
![Alt text describing the image](file-name.jpg)
*Caption. Credit: Who made it, via [Source](https://...), License.*
```
The italic line directly below becomes the caption (links allowed). Alternatively: `![alt](file.jpg "Plain caption")`. Every image needs a credit and license (public domain, CC BY, CC BY-SA, or our own chart). Charts made by us must plot only real data and cite the data source in the caption. The build renders a bordered `<figure>` with `<figcaption>`.

## Daily bot routine
1. Pick ONE topic: a new page, or an update to an existing one (bump `updated:`).
2. Research with real sources; never invent facts, quotes or numbers. Mark uncertainty clearly; give a `verdict:` only for specific claims.
3. Include at least one sourced visual: a free-licensed image (NASA, ESA, NSF, Wikimedia Commons with a compatible license; verify the license and that the image actually shows the subject) or an original chart of real, cited data. Never fabricate data. Label artist's concepts as illustrations.
4. Save as `content/YYYY-MM-DD-slug.md` (new) or edit the existing file.
5. Run `python3 build.py`. The newest/updated page becomes "Today's page" on the home page.

Preview: `python3 -m http.server 8083 --directory public`
