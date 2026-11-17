# Academic website redesign

All changes are isolated on `redesign/academic-2026`. The build workflow produces an artifact only; it has no deployment step or write permissions.

## Content and maintenance

- Edit `_data/publications.yml` for the catalogue. Keep each `detail_url` aligned with the existing publication permalink. Dates describe the listed version; working papers are not labelled as journal articles.
- Keep full publication pages and all existing URLs. The catalogue includes all 17 publication pages (15 existing and two newly added).
- Add publication decisions only when confirmed. Recent November 2026 application materials distinguish the JMP under review at JASA and the OSEM paper conditionally accepted at IJF; no published-journal claims have been added for these papers.
- The homepage retains the existing longer research/software/background text. Changes to its opening are limited to the hero and the current job-market cycle, with OSEM use aligned to the November 15 research statement and cover letter.
- `_sass/_modern.scss` contains the visual layer. `_layouts/default.html` exposes front-matter classes to it. Existing navigation, theme templates and PDFs are preserved.
- Search and filters progressively enhance the complete catalogue. Without JavaScript, the full list is visible. Search ignores accents and matches multiple terms across title, author, venue and year.

## Preview

`docs/redesign-mockup.html` is a standalone illustrative review mockup generated from the homepage and publication metadata, with the catalogue's production JavaScript. It is not a Jekyll deployment. The Actions artifact is the full Jekyll build.

The original draft's report link pointed to the wrong PDF; the catalogue now uses `/files/Pictet-Report-2020.pdf` for *Climate change and emerging markets after Covid-19*. Existing detail content is preserved pending a separate content review.

## Validation

The GitHub Pages Jekyll build and browser checks passed at widths 1440 and 390. Checks cover catalogue completeness, all type filters, combined search terms, empty results, keyboard tab order, horizontal overflow and the no-JavaScript fallback. Preview-only URL configuration prevents tests loading the production stylesheet. Browser screenshots are included in the Actions artifact. The production branch remains at its original commit.

Homepage shortened with full background preserved at `/research-background/`. Publication detail pages use `_layouts/publication.html`. OSEM and getspanel retain their top-level navigation links. Teaching suggestions are in `docs/teaching-proposal.md`; teaching content itself is unchanged.
