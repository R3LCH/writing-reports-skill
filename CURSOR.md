# Using This Repo With Cursor

This repository includes a Cursor project rule so the GOST report skill applies automatically when you work here. For paired GUAP output, prefer an editable Word master with a separately filled cover and PDF export; see `skills/writing-reports-pandoc-gost/references/word-master.md`. The pinned LaTeX profile remains available when required.

## In This Repository

1. Open the folder in Cursor.
2. Cursor loads `.cursor/rules/writing-reports.mdc` with `alwaysApply: true`.
3. Use the examples in `examples/` as placeholder-only input formats.

## Use In Another Project

Copy `.cursor/rules/writing-reports.mdc` into the other project's `.cursor/rules/` directory. If that project already has report-specific rules, merge them instead of replacing local requirements.

## Skill Folder

The canonical reusable skill body is:

- `skills/writing-reports-pandoc-gost/SKILL.md`

Keep `CLAUDE.md`, `GEMINI.md`, `.cursor/rules/writing-reports.mdc`, and the GOST skill aligned when changing behavior.
