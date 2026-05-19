# 📝 Writing Reports Skills

**Turn rough requirements, templates, and credentials into verified Pandoc reports your AI agent can deliver.**

Writing Reports Skills gives Claude Code, Cursor, Gemini, Codex-style agents, and other skill loaders a repeatable workflow for producing academic, technical, and institutional reports. It helps the agent classify report assets, preserve semantic Markdown sources, use Pandoc correctly, and verify DOCX/PDF/HTML/Markdown outputs before declaring the work complete.

🌐 Languages: English | [Русский](README.ru.md) | [中文](README.zh.md)

## 🚀 Why Use It

Most report-generation failures are not Pandoc failures. They come from unclear template roles, invented credentials, cover pages used as body references, broken page numbering, corrupted text, and agents saying "done" without checking the actual file.

These skills give the agent a production-minded report workflow: clarify missing inputs, classify assets, keep a reproducible source, convert with Pandoc, and verify the final artifacts.

## ✨ What You Get

- 🧱 **Reliable Pandoc pipeline** for DOCX, PDF, HTML, and Markdown.
- 🗂️ **Template discipline** for cover-only documents, body-style references, full examples, CSL files, CSS files, bibliographies, and source assets.
- 🔁 **Reproducible reports** built from semantic Markdown and YAML frontmatter.
- 🌐 **URL-based guideline intake** for official web pages and PDFs: fetch, extract, preserve source evidence, and apply the rules.
- 🔒 **Safer credential handling** with explicit placeholders and no invented student, teacher, client, or institution data.
- 📄 **Correct cover + body workflows** without using a title page as `--reference-doc`.
- ✅ **Verification gates** for files, required sections, citations, page layout, placeholders, text corruption, blank pages, colors, and code-listing formatting.
- 📐 **GOST-style support** for Russian student reports, lab reports, course reports, title pages, page numbering, margins, and source listings.

## 🎯 Best Fit

Use this repository when you want an AI coding agent to help with:

- lab reports, course reports, student reports, and diploma-style documents;
- technical reports generated from Markdown;
- DOCX/PDF deliverables that must follow a reference document, uploaded guideline, or official guideline URL;
- reports with title pages, credentials, tables, figures, citations, and code listings;
- repeatable report production across Claude Code, Cursor, Gemini, and Codex-like workflows.

## ⚡ Quick Start

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

## 🧩 Included Skills

- `writing-reports-pandoc` - general report creation, formatting, conversion, and update workflow for Pandoc, DOCX, PDF, HTML, Markdown, reference documents, cover pages, citations, and templates.
- `writing-reports-pandoc-gost` - strict Russian GOST-style workflow for student reports, lab reports, course reports, DOCX/PDF outputs, title pages, page numbering, margins, and plain source listings.

## 💬 Example Agent Requests

```text
Use writing-reports-pandoc to create a DOCX and PDF report from report.md, reference.docx, and credentials.yaml. Preserve the Markdown source and verify the outputs.
```

```text
Use writing-reports-pandoc-gost to prepare a GOST-style lab report with a title page, page numbers, Times New Roman 14, 1.5 spacing, and plain code listings.
```

```text
Classify the files in this report folder, identify which DOCX is cover-only and which can be used as the body reference, then generate the final report.
```

```text
Use writing-reports-pandoc to fetch the formatting guidelines from this official URL, preserve the extracted rules in report-guidelines.md, then generate DOCX and PDF outputs from report.md.
```

## 🌐 Guidelines From URLs

You can give the agent an official style-guide URL instead of manually pasting every formatting rule. The skills instruct the agent to:

1. fetch the URL with available web/browser tools;
2. extract actionable rules such as margins, fonts, spacing, title-page rules, page numbering, citations, required sections, and output formats;
3. preserve the URL, retrieval date, page/document title, content type, and extracted rules;
4. ask you to paste or upload the guideline source if the URL is blocked, private, or requires authentication;
5. apply the extracted rules before using defaults.

This makes URL-based guidelines auditable instead of hidden in the agent's memory.

## 🗃️ Repository Layout

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

## 🧪 Examples

- `examples/credentials.example.yaml` - placeholder credentials for reports.
- `examples/first-page.example.md` - title-page source example.
- `examples/report.example.md` - semantic Markdown report source example.

Use the examples as safe starting inputs: copy them into a private report workspace, replace placeholders with real data there, then ask the agent to build from those files. Keep real credentials out of this repository.

Do not commit real student, teacher, client, institution, or API credentials. Replace placeholders only in private working copies.
