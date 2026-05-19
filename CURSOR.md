# Using This Repo With Cursor

This repository includes a Cursor project rule so the Pandoc report skills apply automatically when you work here.

## In This Repository

1. Open the folder in Cursor.
2. Cursor loads `.cursor/rules/writing-reports.mdc` with `alwaysApply: true`.
3. Use the examples in `examples/` as placeholder-only input formats.

## Use In Another Project

Copy `.cursor/rules/writing-reports.mdc` into the other project's `.cursor/rules/` directory. If that project already has report-specific rules, merge them instead of replacing local requirements.

## Skill Folders

The canonical skill bodies live in:

- `skills/writing-reports-pandoc/SKILL.md`
- `skills/writing-reports-pandoc-gost/SKILL.md`

Keep `CLAUDE.md`, `GEMINI.md`, `.cursor/rules/writing-reports.mdc`, and both skill files aligned when changing behavior.

