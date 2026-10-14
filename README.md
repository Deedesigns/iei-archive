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

## Daily bot routine
1. Pick ONE topic: a new page, or an update to an existing one (bump `updated:`).
2. Research with real sources; never invent facts, quotes or numbers. Mark uncertainty clearly; give a `verdict:` only for specific claims.
3. Save as `content/YYYY-MM-DD-slug.md` (new) or edit the existing file.
4. Run `python3 build.py`. The newest/updated page becomes "Today's page" on the home page.

Preview: `python3 -m http.server 8083 --directory public`
