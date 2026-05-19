# Writing Reports With Pandoc

Use these instructions when a user asks to create, format, convert, or update reports with Pandoc, DOCX, PDF, HTML, Markdown, reference documents, cover pages, citations, templates, or report guidelines.

For detailed workflows, use:

- `skills/writing-reports-pandoc/SKILL.md`
- `skills/writing-reports-pandoc-gost/SKILL.md`

## Core Rules

- Generate the final report only after the target output and formatting authority are clear.
- Identify requested outputs, report type, formatting authority, template roles, credentials, and citation requirements before building.
- Never invent credentials or source content. Ask for missing required data, or use explicit placeholders only when the user accepts them.
- Treat title-page or cover DOCX files as cover-only unless the user says they represent the full report.
- Do not use a cover-only file as a Pandoc `--reference-doc`.
- Preserve the semantic source file beside generated outputs.
- Verify outputs before claiming completion.

## General Pandoc Route

1. Search the workspace for relevant assets:

```bash
rg --files
rg --files | rg -i "cover|first[-_ ]?page|title[-_ ]?page|template|reference|example|sample|metadata|author|bibliography|csl|css|tex"
```

2. Verify Pandoc:

```bash
pandoc --version
```

3. Create or update a semantic Markdown source with YAML frontmatter.
4. Convert from one source into requested outputs:

```bash
pandoc report.md -o report.docx --reference-doc reference.docx
pandoc report.md -o report.pdf --pdf-engine=xelatex
pandoc report.md -o report.html --standalone --css style.css
```

5. Inspect the generated files for required content and formatting.

## GOST-Style Reports

For Russian GOST-style reports, lab reports, course reports, and GUAP-style outputs:

- Use A4 unless a stricter institutional rule says otherwise.
- Use margins: left 30 mm, right 10 mm, top and bottom 20 mm.
- Use Times New Roman 14 pt, 1.5 line spacing, first-line indent 1.25 cm, justified body text.
- Count the title page but hide its visible page number.
- Keep body text black. Red is allowed only for short unknown-data placeholders.
- Keep source listings monospaced, left-aligned, without syntax colors or bold code unless explicitly requested.

## Verification

Before completion, check:

- every requested output exists and is nonzero;
- required sections, credentials, citations, figures, tables, and placeholders are present;
- no corrupted text such as `????`;
- formatting authority was applied;
- cover/template roles were respected;
- no unexpected blank pages, colors, bold code, or decorative styling;
- all requested outputs came from the same source unless divergence was explicitly required.

