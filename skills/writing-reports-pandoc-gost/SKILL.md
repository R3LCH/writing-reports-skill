---
name: writing-reports-pandoc-gost
description: Use when preparing Russian GOST-style student reports, lab reports, course reports, or strict DOCX/PDF outputs with Pandoc, cover pages, page numbering, source listings, formatting guidelines from files or URLs, and strict formatting checks.
---

# Writing GOST Reports With Pandoc

## Core Rule

Build a GOST-style report only after the target format is known. If the standard, output format, cover-page role, or credentials are unclear, ask a narrow question before generating.

Use restrained formatting: black body text, no decorative colors. Red is allowed only for short unknown-data placeholders.

All the formatting principals SHOULD BE TAKEN AS THE SOURCE OF TRUTH, FOLLOWING EVERY SINGLE ONE OF THEM IS MANDATORY.

## Required Inputs

Identify before building:

- output files requested (`.docx`, `.pdf`, Markdown source);
- formatting source: institution URL/file, provided standard, or approved GOST defaults;
- cover page role: **cover-only** or full report example;
- credentials: student, group, teacher, department, course, lab number, title, variant, year.

Never invent credentials. Missing fixed-layout credentials use short red placeholders: `FIO`, `GR.`, `TEACHER`, `ROLE`.

## URL Guideline Intake

When the formatting source is an institution/course URL, treat it as evidence that must be fetched, extracted, and preserved before building the final report.

1. Fetch each provided URL with the available web/browser/network tool. Prefer official institution or course pages over reposts and summaries.
2. If the URL cannot be fetched because network access, authentication, JavaScript rendering, or file download is blocked, ask the user to paste the guideline text or upload the file. Do not fall back to memory.
3. Preserve a local guideline note such as `report-guidelines.md` with:
   - source URL;
   - retrieval date;
   - page or document title when available;
   - content type (`html`, `pdf`, `docx`, `text`, or unknown);
   - extracted requirements and unresolved ambiguities.
4. Extract only actionable GOST/report requirements: margins, font, line spacing, paragraph indent, alignment, title-page layout, page numbering, heading rules, table/figure rules, listing rules, required sections, bibliography rules, and output formats.
5. If URL rules conflict with local files or defaults, apply this precedence:
   - explicit user instruction;
   - official institution/course URL;
   - uploaded/local standard or template;
   - prior full report example;
   - approved GOST defaults.
   Surface visible formatting conflicts before generating final files.
6. Cite the guideline source in the final response with URL and retrieval date. Do not add the source citation to the report body unless the user asks.

## GOST Defaults

When no stricter institutional rule is provided, use:

- A4;
- margins: left 30 mm, right 10 mm, top/bottom 20 mm;
- Times New Roman 14;
- 1.5 line spacing;
- first-line indent 1.25 cm;
- justified body text;
- page number in footer;
- title page counted but without visible number.

## Pandoc Is Mandatory

Use Pandoc for every conversion/build step. Do not hand-build the final report as a substitute for Pandoc unless the user explicitly forbids Pandoc.

Before generating the report:

1. Run `pandoc --version`.
2. If Pandoc is missing, install it using the available package manager or a portable release, asking for required permissions when needed.
3. If `pandoc` is present but broken, such as a Chocolatey shim pointing to a missing executable, fix the install, locate the real executable, or download a portable copy.
4. If system repair is blocked by permissions, install portable Pandoc inside the workspace, for example `.tools/pandoc-*`, and invoke that path directly.
5. Record the exact working Pandoc path in the final response.
6. Do not claim completion until the working Pandoc executable has successfully built the requested output.

## Deterministic DOCX Route

1. Search assets: `rg --files` for cover/reference/metadata files.
2. Verify, install, or repair Pandoc according to **Pandoc Is Mandatory**.
3. Create and preserve semantic `report.md` with YAML frontmatter.
4. Create/use a dedicated `reference.docx` for the body. Do **not** use a cover-only DOCX as `--reference-doc`.
5. Convert body:

```bash
pandoc report.md -o report-body.docx --reference-doc reference.docx
```

6. If a DOCX cover is provided, preserve it as cover-only unless the user explicitly says it is a full report example.
7. Merge cover + body by prepending cover body elements before the Pandoc body. Do not add an extra page break if the body already begins on the next page/section.

## DOCX Cover, TOC, And Tables

For GOST-style DOCX reports, check these details explicitly:

- First page: title page is counted but must not show a page number or footer. Keep the cover as its own section with no `w:footerReference`; start the body section at page 2. Use a section break (`w:type nextPage`) between cover and body, not a blind paragraph page break that can create a blank page.
- Cover page tables: if a title page uses a table only for alignment, preserve the original table geometry from the cover file but hide its borders. Do not apply body-table width, border, or wrapping fixes to cover layout tables.
- Table of contents: use a real Word TOC field. If Word field updating is unavailable, include visible TOC result entries inside the field so the user does not see a placeholder. TOC text must be black, entries must use right-aligned tab stops with dot leaders, and the TOC heading should match the report language (for Russian reports: `ОГЛАВЛЕНИЕ`, text must be black). Add a page break after the TOC.
- Headings: Do not have the numbering convention, unless provided in standard/example. If the user says section titles must have leading numbers, do not rely on Pandoc automatic numbering; use unnumbered heading text and verify no `Heading1`/body heading begins with `^\d+\s+`.
- Body tables: ensure every report table is a real Word table (`<w:tbl>`), has visible borders, readable column widths, centered cell text when requested, and no inherited paragraph/style offset inside cells. For body table cells, remove literal tabs (`w:tab`), tab stops (`w:tabs`), numbering (`w:numPr`), paragraph style (`w:pStyle`) when it creates offsets, first-line/hanging/left/right indents, cell margins (`w:tcMar`), and before/after spacing unless the standard explicitly requires them. Do not apply these body-cell cleanups to cover layout tables.
- Table and figure captions: create visible captions as ordinary paragraphs, not only image alt text. GOST-style table captions normally go above tables and are left-aligned; figure captions go below figures and are centered. Center figure paragraphs themselves. If Pandoc cannot convert SVG images because `rsvg-convert` is unavailable, generate or convert diagrams to PNG before building the DOCX.
- Text color: remove all unapproved text colors and highlights from document XML and styles. Keep body text black.
- Page breaks: verify there is no accidental blank page after the cover and that required breaks, especially after TOC, are present.
- Spreadsheet data: when an Excel/ODS file contains source calculations, read data from the spreadsheet instead of copying stale numbers from a prior report. Distinguish sourced data, expert-entered values, and computed values in the report text when the assignment requires explanation. If you create data yourself to complete a lab, state that it is expert/educational data and optionally preserve it in an `.xlsx` calculations workbook.

## Listings

For source listings:

- listing headings for tables are left-aligned;
- listing headings for code are left-aligned;
- listing captions should be used for everything else and be centered;
- code left-aligned;
- monospaced font;
- no bold in code;
- no syntax colors unless explicitly requested.

Use `--no-highlight` or remove color/bold from all Pandoc `*Tok` styles.

## Verification Gate

Do not claim completion until verified. For DOCX, inspect XML if visual rendering is unavailable:

- file exists and is nonzero;
- required sections exist;
- no corrupted text such as `????`;
- no blank page after cover;
- page-number field exists;
- margins/font/spacing/indent are present;
- URL-sourced rules were fetched or the user supplied an equivalent pasted/uploaded source;
- extracted guideline source, retrieval date, and applied rules are preserved;
- no colors except approved red placeholders;
- no bold in listing code, including `*Tok` styles;
- real Word tables exist for report tables, body table borders are visible, and table cell text does not wrap word-by-word because of inherited paragraph indents;
- body table cell XML has no leading whitespace before text, no `w:tab`, no `w:tabs`, no `w:numPr`, no offsetting `w:pStyle`, zero/absent paragraph indents, zero cell margins when requested, and zero before/after spacing when requested;
- cover-only layout tables keep their original geometry and have hidden borders when the example uses them for alignment;
- TOC is a real Word TOC field with visible entries, black text, dot leaders, and not only a placeholder; required page break after TOC is present;
- title page has no visible footer/page number while subsequent pages have page numbering;
- figures and figure captions are centered when required; table captions are left-aligned when required;
- Markdown source, reference DOCX, Pandoc body, and final DOCX are preserved.

If verification is incomplete, state the exact gap.

## Code Snippets

# To remove all the unnecassary spacing before and after the text in table's cells: 

'''
tcmar = tcpr.find("w:tcMar", NS)
            if tcmar is None:
                tcmar = ET.SubElement(tcpr, q("tcMar"))
            for side in ["top", "left", "bottom", "right"]:
                node = tcmar.find(f"w:{side}", NS)
                if node is None:
                    node = ET.SubElement(tcmar, q(side))
                node.set(q("w"), "0")
                node.set(q("type"), "dxa")
            valign = tcpr.find("w:vAlign", NS)
'''

and

'''
ppr = ensure_ppr(p)
            spacing = ppr.find("w:spacing", NS)
            if spacing is None:
                spacing = ET.SubElement(ppr, q("spacing"))
            spacing.set(q("before"), "0")
            spacing.set(q("after"), "0")
'''
