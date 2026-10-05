# Writing Reports Skill

A reusable skill for Russian GOST-style student, laboratory, and course reports as verified PDF and editable DOCX artifacts. For paired GUAP delivery, the preferred route is a native editable Word master with a separately filled cover and PDF exported after field updating. The pinned LaTeX route remains available when explicitly needed.

## What the skill covers

- GOST 7.32–2017 defaults: A4, 30/15/20/20 mm margins, Times New Roman 14 pt, 1.5 spacing, 1.25 cm first-line indent, justified body text, and hidden title-page numbering;
- precedence for explicit instructions, institutional guidance, templates, examples, and defaults;
- separation of cover-only documents, body references, complete examples, and source data;
- real tables, captions, TOCs, section breaks, pagination, listings, colors, and layout verification;
- spreadsheet/source-data integrity and preservation of build inputs;
- complete GUAP-aligned report structure, reproducible execution stages with real evidence, and substantive task-by-task conclusions; see [content and evidence requirements](skills/writing-reports-pandoc-gost/references/report-content.md);
- factual student-report narrative without reader-directed instructions; unresolved inputs are clarified with the user before finalization, not left as questions or placeholders in the report;
- user-accessible editable application projects with launch instructions, verified Google Colab delivery when required, and a detailed `defense.md` for every report; see [submission artifacts](skills/writing-reports-pandoc-gost/references/submission-artifacts.md);
- XML or rendered inspection before claiming completion.

## Use

Load `skills/writing-reports-pandoc-gost/SKILL.md` in the target agent. The files in `examples/` are placeholder formats only; never commit real credentials or private report data.

Use `promt_template.md` for reusable assignment instructions. Fill credentials only in a private copy; the local `promt.md`, report fixtures, benchmark/SkillOpt work and generated caches are excluded from publication.

The repository integrations are available for Claude Code, Cursor, Gemini, and other skill loaders through the project guidance files and `.claude-plugin/` metadata.

## GUAP: editable Word master and PDF

The [tested Word-master route and three-way comparison](skills/writing-reports-pandoc-gost/references/word-master.md) selects DOCX → PDF for paired delivery. The [normative map and optional LaTeX profile](skills/writing-reports-pandoc-gost/references/guap-latex.md) scope the [university's linked standards](https://guap.ru/c/regdocs/stands/uch), including the right margin correction from 10 to 15 mm.

```bash
# Prepare a semantic body.docx without a cover/TOC and verified fields.json.
python3 skills/writing-reports-pandoc-gost/scripts/word_report.py \
  --body /path/to/body.docx --cover /path/to/cover-template.docx \
  --fields /path/to/fields.json --output /path/to/delivery/report.docx
/usr/bin/python3 skills/writing-reports-pandoc-gost/scripts/finalize_docx.py /path/to/delivery/report.docx
```

This route needs python-docx, docxcompose (tested 2.2.0), fontconfig/Times New Roman, LibreOffice and Python UNO. It preserves the institutional cover separately; `gost_docx.py` supplies the common body profile. The exported `report-word-layout.pdf` is the delivery PDF. Preserve inputs and inspect every page; compilation/conversion is not a compliance guarantee.

The comparison rendered the same content through native DOCX/PDF, Quarto 1.10.18 and tex2docx (default/direct). Word-master passed the selected checks; the Quarto configuration retained caption/TOC/numbering defects, while tex2docx lost title/bibliography content despite passing object counts. These are observed configurations, not claims that the libraries cannot be adapted.

For LaTeX-first work, retain `latex_report.py` and `latex_docx.py`; the latter now shares the Word body profile. XeLaTeX/TeX Live or Tectonic is needed only for this route.

## Repository layout

```text
skills/writing-reports-pandoc-gost/  # skill, references, scripts, LaTeX assets
examples/                          # placeholder input formats
promt_template.md                  # reusable assignment prompt without personal data
```

## Languages

English | [Русский](README.ru.md) | [中文](README.zh.md)
