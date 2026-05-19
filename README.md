# Writing Reports Skills

Turn messy report requirements into verified Pandoc outputs your agent can actually ship.

Writing Reports Skills gives Claude Code, Cursor, Gemini, Codex-style agents, and other skill loaders a repeatable workflow for producing academic, technical, and institutional reports. Instead of asking an agent to improvise DOCX/PDF formatting from memory, this repository teaches it to classify assets, preserve semantic Markdown sources, use Pandoc correctly, and verify the final files before calling the job done.

Languages: English | [Русский](README.ru.md) | [中文](README.zh.md)

## Why Use This

Most report-generation failures are not caused by Pandoc. They come from unclear template roles, invented credentials, cover pages used as body references, broken page numbering, corrupted text, and agents declaring success without checking the output.

These skills are built to prevent that. They make the agent slow down at the right points, ask for missing data, keep the report source reproducible, and inspect generated artifacts before completion.

## What You Get

- **Reliable Pandoc workflow** for DOCX, PDF, HTML, and Markdown reports.
- **Template discipline** that separates cover-only documents, body-style references, full examples, CSL files, CSS files, bibliographies, and source assets.
- **Reproducible source files** using semantic Markdown and YAML frontmatter instead of one-off document edits.
- **Safer credentials handling** with explicit placeholders and no invented student, teacher, client, or institution data.
- **DOCX cover + body handling** without accidentally using a title page as `--reference-doc`.
- **Verification gates** for generated files, required sections, citations, page layout, placeholders, text corruption, unexpected blank pages, colors, and code-listing formatting.
- **GOST-style report support** for Russian student reports, lab reports, course reports, GUAP-style outputs, title pages, page numbering, margins, and source listings.

## Best Fit

Use this repository when you want an AI coding agent to help with:

- lab reports, course reports, student reports, and diploma-style documents;
- technical reports generated from Markdown;
- DOCX/PDF deliverables that must follow a reference document or institution rules;
- reports with title pages, credentials, tables, figures, citations, and code listings;
- repeatable report production across Claude Code, Cursor, Gemini, and Codex-like workflows.

## Quick Start

### Claude Code Plugin

Install from the Claude Code marketplace after the marketplace is available:

```bash
claude plugin install writing-reports-skills@writing-reports-marketplace
```

For per-project use without plugin installation, copy or merge `CLAUDE.md` into the target project.

### Cursor

Open this repository in Cursor. The project rule at `.cursor/rules/writing-reports.mdc` is committed with `alwaysApply: true`.

For another project, copy `.cursor/rules/writing-reports.mdc` into that project's `.cursor/rules/` directory.

### Gemini

Copy or merge `GEMINI.md` into a Gemini CLI project, or keep this repository available as the source of the two `skills/` folders.

### Codex And Other Skill Loaders

Copy the folders under `skills/` into your tool's skills directory, or reference this repository directly if your tool supports repository-backed skills.

## Included Skills

- `writing-reports-pandoc` - general report creation, formatting, conversion, and update workflow for Pandoc, DOCX, PDF, HTML, Markdown, reference documents, cover pages, citations, and templates.
- `writing-reports-pandoc-gost` - strict Russian GOST-style workflow for student reports, lab reports, course reports, GUAP-style DOCX/PDF outputs, title pages, page numbering, margins, and plain source listings.

## Example Agent Requests

```text
Use writing-reports-pandoc to create a DOCX and PDF report from report.md, reference.docx, and credentials.yaml. Preserve the Markdown source and verify the outputs.
```

```text
Use writing-reports-pandoc-gost to prepare a GOST-style lab report with a title page, page numbers, Times New Roman 14, 1.5 spacing, and plain code listings.
```

```text
Classify the files in this report folder, identify which DOCX is cover-only and which can be used as the body reference, then generate the final report.
```

## Repository Layout

```text
.claude-plugin/plugin.json
.claude-plugin/marketplace.json
.cursor/rules/writing-reports.mdc
CLAUDE.md
CURSOR.md
GEMINI.md
examples/
skills/
  writing-reports-pandoc/
    SKILL.md
    agents/openai.yaml
  writing-reports-pandoc-gost/
    SKILL.md
    agents/openai.yaml
```

## Examples

- `examples/credentials.example.yaml` - placeholder credentials for reports.
- `examples/first-page.example.md` - title-page source example.
- `examples/report.example.md` - semantic Markdown report source example.

Do not commit real student, teacher, client, institution, or API credentials. Replace placeholders only in private working copies.
