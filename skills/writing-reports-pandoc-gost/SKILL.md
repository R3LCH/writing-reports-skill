---
name: writing-reports-pandoc-gost
description: Use when preparing Russian GOST-style student, laboratory, or course reports and strict DOCX/PDF outputs; prefers an editable Word master with PDF export for paired delivery and retains a GUAP LaTeX profile when required.
---

# Writing Russian GOST Reports

## Core rule

For paired GUAP DOCX/PDF delivery, prefer a native editable Word master with a separately filled institutional cover and PDF exported from the finalized DOCX. Read `references/word-master.md` for the tested route, commands, comparison and limits; read `references/guap-latex.md` for the normative map and the optional pinned LaTeX route. Optimize rendered artifacts, not the compiler. Correct formatting and identical content matter; independent LaTeX/Word pagination need not match. Never deliver a PDF renamed as DOCX or a rasterized Word document. Pandoc and Quarto are optional preparation tools, not compliance guarantees.

## Before building

Identify:

- requested output files and language;
- applicable formatting authority, in precedence order: explicit user instruction, official institutional guidance, supplied local standard/template, complete prior report, then defaults below;
- the role of every asset: cover-only, body-style reference, complete example, source data, or calculation workbook;
- required sections, tables, figures, listings, citations, and page-number behavior;
- credentials. Never invent them. Resolve missing required values with the user before final delivery; unknown-data placeholders are allowed only in an explicitly requested draft, not a finished report.

If guidance conflicts, surface the conflict and apply the higher-precedence source. Preserve the source URL/file, retrieval date when relevant, extracted actionable rules, unresolved ambiguities, and applied precedence in a local note or build manifest.

For GUAP, start from https://guap.ru/c/regdocs/docs/uch (student-work rules, official covers, templates and examples) and https://guap.ru/c/regdocs/stands/uch (standards and amendments); read the applicable linked documents. Read `references/report-content.md` before outlining or writing: it maps GUAP section rules, detailed execution evidence and comprehensive conclusions to their sources. Apply GOST 7.32–2017 report rules, GOST R 2.105–2019 for applicable ESKD documents, and GOST R 7.0.100–2018 bibliographic descriptions; do not impose dissertation rules, research-registration fields or ESKD frames on every laboratory report. Record exact clauses and local exceptions. Template defaults and old standard names never override the linked authority.

## Data and content integrity

Read source spreadsheets and documents rather than copying stale values. Distinguish sourced, calculated, and educationally supplied values. Preserve the calculation workbook when it is part of the assignment. Never invent factual content or credentials. Keep semantic source content beside the final artifact when the route supports it.

## Student-authored narrative and clarification

Write the report as an academically appropriate account of completed, understood work: explain what was done, why the method was chosen, what was obtained and how it was checked. Prefer factual past-tense/impersonal phrasing (“были заданы параметры”, “расчёт выполнен”, “полученное значение подтверждено”); use first person only when the assignment allows it. This is a style requirement, not permission to invent the student's participation, actions or understanding.

Do not address the reader with calls to action such as “сохрани”, “запиши”, “введите”, “нажмите”, “добавьте скриншот”, or “проверьте результат”. Do not turn the execution section into a tutorial or include agent/user correspondence, drafting notes or instructions to finish the work. Describe actual operations and their reasons instead. Source code/commands and clearly identified quotations may retain their original syntax; separately required user manuals remain separate from the report narrative. Practical recommendations must be impersonal, substantiated findings, not orders to the reader.

Do not use the em dash (Unicode U+2014) when writing report text. Use the literal ASCII hyphen `-` (U+002D) instead wherever dash punctuation is needed, including headings, paragraphs, captions, table text, conclusions and generated TOC entries. Prevent automatic typography or export substitutions from reintroducing em dashes. This is a punctuation rule, not a request to change mathematical minus signs or source-code operators; preserve original input files unchanged.

Resolve uncertainty about the assignment, variant, inputs, credentials, actual actions/results, required evidence or formatting before writing the affected final content. First inspect accessible assignment files and authoritative sources; if ambiguity remains, ask the user specific, grouped questions in chat and await answers before the dependent step or final delivery. Continue independent known work. Do not put questions, missing-data notices, guessed alternatives, “вероятно/предположительно” fillers or unresolved placeholders into the finished report.

Keep drafting uncertainty and missing access in chat/private working notes, not report prose. This does not permit concealing measured uncertainty, established methodological limits or observed negative results: those are factual scientific results and must be stated precisely when applicable. Never manufacture certainty or claim unverified work was completed.

## Complete, evidence-backed content

Default to a fully explained report, not a brief summary. Before writing, map every assignment item (including required control questions) to a section, actual action/calculation, result, evidence, verification and conclusion. Preserve this coverage map with the report inputs. Follow `references/report-content.md`; detailed evidence and comprehensive conclusions are this skill's user-requested policy, not an invented GOST requirement for screenshots at every click.

Use the applicable GUAP structure: official cover; contents; terms/abbreviations when needed; unnumbered ВВЕДЕНИЕ; numbered thematic main sections/subsections; unnumbered ЗАКЛЮЧЕНИЕ; СПИСОК ИСПОЛЬЗОВАННЫХ ИСТОЧНИКОВ; appendices when present. Determine the exact composition from the work type and assignment; for an actual research report check all mandatory GOST §4 elements and legitimate exceptions. State the goal, every task, input data and success criteria in the introduction. Do not replace substantive thematic sections with one undifferentiated narrative.

Explain each substantive execution stage: purpose; sourced inputs and relevant conditions; method and rationale; reproducible operations/formulas with substitutions, units and intermediate results; actual outcome; referenced evidence; correctness check; interpretation, limitations and stage conclusion. Cover every assigned variant/result. Be exhaustive about relevant work, not repetitive about trivial clicks or unrelated theory.

Support substantive results with real screenshots, native data tables, plots from actual data, execution output or other appropriate records. Capture evidence during execution, preserve originals and provenance, place it near the explanation, and explain what each object proves. Cite every figure/table/appendix with consistent numbering and readable captions. Never fabricate screenshots, measurements, successful runs or unseen application state; a schematic or rendered report page is not execution evidence. If required evidence is inaccessible, finish reachable work, ask the user for the missing access/input in chat and do not finalize the affected content or claim the task is complete.

Write a comprehensive ЗАКЛЮЧЕНИЕ: assess achievement of the goal; give a concrete, supported result for every task; interpret key values/behavior; evaluate checks, uncertainty and limitations; disclose unresolved/negative results; give justified practical recommendations. Include efficiency/novelty comparisons only when applicable and supported. Do not introduce new results there or substitute “skills acquired / all tasks completed” for substantive findings. Full means complete in meaning, not a page-count target.

## Editable application handoff, Colab and defense notes

Read `references/submission-artifacts.md` before executing work in an application, preparing a required Colab notebook or assembling the submission package. These are user-required deliverables, not GOST additions.

If computer use or a device application was used to perform the assignment, preserve the native editable project and all entered data, code, objects, settings and dependent assets. The user must be able to open the same work in the application, run it for demonstration and change the data. Check availability/access before execution; reopen the saved project and verify the actual launch and editability, not just a screenshot or transient session. Transfer isolated-environment work into a user-accessible persistent package. Tell the user the exact application, project path/link, launch steps and where to edit values; use a separate `RUN.md` when needed.

If the assignment requires Google Colab, prepare a complete valid `.ipynb` matching the task/template: all assignment items, theory/method explanations, executable code, actual outputs, tables/plots, real screenshots of results, correctness checks and a comprehensive analytical conclusion covering the whole work. Actually execute and save it in the user's Google Drive/Colab through an authorized user session; reopen the saved notebook in Colab and verify content, retained outputs/assets and user editing access. Include the actual verified Colab URL in the report body, `defense.md` and delivery message. A local `.ipynb`, invented URL or instruction to upload manually is not fulfillment. Resolve missing login/account/required sharing information with the user; never bypass authentication, request passwords in chat, upload under another identity or make private work public without authorization. Do not claim Colab execution from a local run or completion while upload/access is blocked.

For every report also deliver a fully populated `defense.md` beside the outputs (or the assignment's required Markdown filename). Explain the relevant theory exhaustively, what was done and why, tools and parameters, every significant formula's name/notation/variables/units/applicability and actual substitution, used functions' qualified names/call syntax/arguments/returns/behavior, and technical concepts with their meaning in this work. Include stage-by-stage explanations, checks and analytical results, answers to required control questions, sources and artifact links. Keep it consistent with the report, native project and notebook; it is a detailed preparation-for-submission/defense document, not a generic glossary or empty outline. Separate launch instructions from the report narrative.

## Default Russian GOST presentation

When no stricter rule applies, use A4; left/right/top/bottom margins 30/15/20/20 mm; Times New Roman 14 pt; 1.5 line spacing; first-line indent 1.25 cm; justified body text; black text; title page counted but without a visible number; and plain, left-aligned monospaced source listings without syntax colors or bold. The 15 mm right margin follows GOST 7.32–2017 §6.1.1; 14 pt is the selected student-report default, while this standard permits sizes ≥12 pt. Never silently substitute the required font.

## Layout and document structure

- Keep a cover-only document separate from body-style references. Do not use a cover-only file as a global style source.
- Put the cover in its own section with no visible footer/page number when required; start the body with a real next-page section break, avoiding accidental blank pages.
- For DOCX, use real Word tables with visible borders, readable widths, and the requested alignment. For LaTeX, use semantic tabular/longtable environments with equivalent readable geometry. Keep cover alignment tables separate from body-table cleanup.
- Put table captions above tables and left-aligned, and figure captions below figures and centered, unless the authority says otherwise. Center figure paragraphs when required.
- Use a real TOC field where possible. If field updating is unavailable, include visible result entries in the field, with black text, dot leaders, and a required page break after the TOC.
- For GUAP, number main sections/subsections with Arabic numerals (`1`, `1.1`), without a trailing dot; introduction/conclusion and other structural elements remain unnumbered. Follow the assignment's applicable structure, not arbitrary automatic numbering. Start each structural element and main section on a new page, not every subsection.
- In body table cells, remove accidental tabs, numbering, paragraph/style indents, cell margins, and before/after spacing when the target requires compact cells. Never apply those changes to cover layout tables.
- Remove unapproved colors and highlights. Unknown-data placeholders belong only in explicitly requested drafts; never retain them in a finished report. Red is allowed there only when the authority permits it.

## Route selection

For paired output, prepare a semantic body DOCX without its cover/TOC using native Word elements; Pandoc from prepared Markdown is optional. Assemble it with `scripts/word_report.py --body <body.docx> --cover <cover-template.docx> --fields <fields.json> --output <new-report.docx>`. The cover is filled separately, preserving its runs/layout; never apply body-table cleanup to it. Use verified string values; obtain missing final-report values from the user before assembly. The body must already contain consistent section/table/figure/appendix labels and resolved citations. Continued tables require explicit continuation captions at actual page boundaries, not just repeated headers.

Finalize with `scripts/finalize_docx.py <report.docx>` (LibreOffice/UNO), then inspect every page of the exported PDF and the DOCX's editable structure. Here `report-word-layout.pdf` is the delivery PDF itself. Keep the final DOCX and its exact PDF export together; record versions, inputs and checksums. See `references/word-master.md` for appendix titles, equation layout and unsupported cover cases.

When LaTeX PDF is explicitly required or preferable for a TeX-centred task, prepare a private project using `scripts/latex_report.py prepare <new-directory>`; it pins the upstream revision/submodule, retains the upstream license, and copies `assets/latex/guap-report.sty` and `report.tex`. Replace all demonstration content with verified assignment data. Keep corrections in the local overlay. Build with `scripts/latex_report.py build <directory>` (XeLaTeX) or `--engine <tectonic>`. Disable shell escape; use a real filesystem sandbox for untrusted input. Prewarm dependencies before offline runs.

For a LaTeX-first task also requesting Word, export shared source semantics using `scripts/latex_docx.py <directory>` with Pandoc/python-docx, then run `scripts/finalize_docx.py <directory>/build/report.docx` to update fields and render Word separately. The exporter shares the Word profile with the primary route; it does not reproduce arbitrary TeX layout or a supplied Word cover. If a construct cannot be exported faithfully, build it natively from the same data; never omit it, flatten the document, or hide warnings. Preserve editable tables/OMML and verify numbering/citations. Final LaTeX PDF and DOCX may have different page breaks, not different content. `tex2docx` counts alone do not prove title/bibliography/appendix fidelity.

## Verification gate

Before delivery, verify the actual output:

- every requested file exists and is nonzero;
- required sections, verified content, credentials, tables, figures, captions and citations are present; no unresolved placeholders, questions or drafting uncertainty remain in the finished report;
- every assignment item has a detailed execution account, actual result, appropriate evidence and correctness assessment; missing required evidence is raised with the user in chat before finalization, never fabricated;
- introduction tasks and conclusion findings correspond one-to-one; conclusions are substantive and supported by the main body, with limitations and unresolved tasks explicit;
- all applicable GUAP structural elements and section numbering are present; every figure/table/appendix is referenced and explained, evidence is readable and matches retained originals;
- the complete `defense.md` explains the actual work, relevant theory, formulas, function syntax/behavior and technical concepts, with consistent results and working artifact links;
- for application-based work, the user-accessible native project retains all necessary data/settings/assets, reopens and runs, permits editing, and has exact launch/edit instructions communicated to the user;
- when Colab is required, the complete notebook is actually executed and saved under the authorized user's account, reopens in Colab with outputs/screenshots/assets and editing access, and its real verified link is present in the report and handoff materials;
- prose describes completed, understood work without reader-directed imperatives, tutorial instructions, agent commentary or unsupported certainty; practical recommendations are substantiated and impersonal;
- no corrupted text such as `????`;
- report text in the source and final DOCX/PDF contains no em dashes (U+2014); dash punctuation uses ASCII `-` (U+002D), including generated fields and captions after updating/exporting;
- margins, font, spacing, indentation, alignment, section breaks, and page numbering match the authority;
- no accidental blank page after the cover or TOC;
- DOCX body tables are native editable tables; LaTeX tables are readable, with visible borders where required, no clipping, and verified continued headers/captions when spanning pages;
- listings are left-aligned, monospaced, plain, and not bold unless required;
- colors/highlights are limited to explicitly permitted uses;
- the source data and final artifact correspond;
- for the LaTeX route, compilation converged, with no unresolved references, missing glyphs or overfull boxes; PDF fonts are embedded and page size is A4;
- DOCX TOC/PAGE fields have been updated and saved; equations, tables and source content remain editable;
- every page of the final PDF was inspected for overflow, blank pages, misplaced captions, numbering and source-content agreement; for independent LaTeX/DOCX outputs inspect both PDFs. In the Word-master route the exported PDF is already the DOCX render. If visual rendering is unavailable, structural inspection is a limited fallback, not proof of perfect layout.

Report verification blockers and exact limitations to the user in chat, not as drafting notes inside the report. Do not claim completion or deliver a supposedly finished report while required clarifications/evidence remain unresolved.
