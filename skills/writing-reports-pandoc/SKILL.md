---
name: writing-reports-pandoc
description: Use when creating, formatting, converting, or updating reports with Pandoc, DOCX/PDF/HTML/Markdown, reference documents, cover pages, citations, templates, or user-provided report guidelines.
---

# Writing Reports With Pandoc

## Core Rule

Generate the final report only after the target output and formatting authority are clear. If output format, template role, cover role, credentials, citation style, or acceptance criteria are unclear, ask a narrow question first.

Default to clean report formatting: black body text, restrained typography, no decorative colors, and no visual noise unless the provided rules/template require it.

## Required Inputs

Identify:

- requested outputs: `.docx`, `.pdf`, `.html`, `.md`;
- report type, language, audience, and required sections;
- formatting authority: written rules, prior report, `reference.docx`, LaTeX template, CSS, or approved defaults;
- role of each template asset: cover-only, body-style reference, complete example, or reusable source;
- credentials: author, organization, course/project/client, reviewer, title, date;
- citation/bibliography requirements.

Never invent credentials or source content. Ask for missing required data, or use explicit placeholders only when the user accepts them. In fixed-layout areas, keep placeholders short enough not to disturb formatting.

## Find And Classify Assets

Search the workspace first:

```bash
rg --files
rg --files | rg -i "cover|first[-_ ]?page|title[-_ ]?page|template|reference|example|sample|metadata|author|bibliography|csl|css|tex"
```

Classify before use:

- cover/title/first-page DOCX: cover-only unless the user says it represents the full report;
- `reference.docx` or complete prior report: body style source only if its body formatting should govern output;
- Markdown/LaTeX/HTML source: preferred semantic source if available;
- bibliography/CSL/CSS/assets: attach only when required by the output.

Do not use a cover-only file as Pandoc `--reference-doc`.

## Deterministic Routes

Prefer one semantic source per report. Preserve it beside generated outputs.

- DOCX: `pandoc report.md -o report.docx --reference-doc reference.docx`
- PDF: `pandoc report.md -o report.pdf --pdf-engine=xelatex`
- HTML: `pandoc report.md -o report.html --standalone --css style.css`

Verify Pandoc with `pandoc --version`. If the shell command points to a broken shim, locate the real executable and report the path used.

For DOCX cover + Pandoc body, generate the body with Pandoc, then prepend/merge the cover. Avoid accidental blank pages by inspecting section/page breaks instead of blindly adding one.

## Source Discipline

Use semantic Markdown/YAML where possible: headings, tables, figures, captions, citations, cross-references, and explicit page breaks only where required. Do not silently drop missing content; ask or mark a clear placeholder.

For listings/code when relevant, keep code monospaced and left-aligned unless the target style says otherwise. Disable or remove syntax colors/bold when the report requires plain listings (`--no-highlight` or edit Pandoc token styles).

## Verification Gate

Do not claim completion until checked:

- Pandoc command succeeded;
- each requested output exists and is nonzero;
- required sections, credentials, citations, figures/tables, and placeholders are present;
- no text corruption such as `????`;
- formatting authority was actually applied;
- template/cover roles were respected;
- no unexpected blank pages, colors, bold code, or decorative styling;
- all requested outputs came from the same source unless divergence was explicitly required.

For DOCX, inspect XML with `python-docx` or ZIP/XML checks when visual rendering is unavailable. If a check cannot be performed, state the exact limitation.

