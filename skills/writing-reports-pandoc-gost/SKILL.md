---
name: writing-reports-pandoc-gost
description: Use when preparing Russian GOST-style student reports, lab reports, course reports, or strict DOCX/PDF outputs with Pandoc, cover pages, page numbering, source listings, formatting guidelines from files or URLs, and strict formatting checks.
---

# Writing GOST Reports With Pandoc

## Core Rule

Build a GOST-style report only after the target format is known. If the standard, output format, cover-page role, or credentials are unclear, ask a narrow question before generating.

Use restrained formatting: black body text, no decorative colors. Red is allowed only for short unknown-data placeholders.

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

## Deterministic DOCX Route

1. Search assets: `rg --files` for cover/reference/metadata files.
2. Verify Pandoc: `pandoc --version`. If a shim is broken, find the real executable and report the exact path.
3. Create and preserve semantic `report.md` with YAML frontmatter.
4. Create/use a dedicated `reference.docx` for the body. Do **not** use a cover-only DOCX as `--reference-doc`.
5. Convert body:

```bash
pandoc report.md -o report-body.docx --reference-doc reference.docx
```

6. If a DOCX cover is provided, preserve it as cover-only unless the user explicitly says it is a full report example.
7. Merge cover + body by prepending cover body elements before the Pandoc body. Do not add an extra page break if the body already begins on the next page/section.

## Listings

For source listings:

- listing headings/captions left-aligned when requested;
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
- Markdown source, reference DOCX, Pandoc body, and final DOCX are preserved.

If verification is incomplete, state the exact gap.
