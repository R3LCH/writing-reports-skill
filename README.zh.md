# 报告写作技能

把混乱的报告要求变成可验证、可交付的 Pandoc 输出。

Writing Reports Skills 为 Claude Code、Cursor、Gemini、Codex 风格 Agent 以及其他技能加载器提供一套可重复的报告生成流程。它不是让 Agent 临时猜测 DOCX/PDF 格式，而是让 Agent 先识别素材角色，保留语义化 Markdown 源文件，正确调用 Pandoc，并在完成前验证生成结果。

语言：[English](README.md) | [Русский](README.ru.md) | 中文

## 为什么使用它

报告生成失败通常不是 Pandoc 本身的问题。真正的问题往往是：模板角色不清楚、Agent 编造凭据信息、把仅封面的 DOCX 当作正文 `--reference-doc`、页码错误、文本乱码，或者在没有检查输出的情况下宣布完成。

这些技能就是为了解决这些问题。它们让 Agent 在关键节点放慢速度：询问缺失数据，区分文件用途，保留可复现源文件，执行转换，并检查最终产物。

## 你会得到什么

- **可靠的 Pandoc 工作流**，支持 DOCX、PDF、HTML 和 Markdown。
- **清晰的模板规则**，区分仅封面文件、正文样式 reference DOCX、完整示例、CSL、CSS、参考文献和源素材。
- **可复现的源文件**，使用 Markdown/YAML，而不是一次性的手工 DOCX 修改。
- **更安全的凭据处理**，不会编造学生、教师、客户或机构信息。
- **正确的“封面 + 正文”流程**，避免把仅封面的 DOCX 错用为 `--reference-doc`。
- **完成前验证**，检查文件、必要章节、引用、页面布局、占位符、乱码、空白页、颜色和源码清单格式。
- **俄语 GOST 风格支持**，适用于学生报告、实验报告、课程报告、GUAP 风格 DOCX/PDF、标题页、页码、页边距和源码清单。

## 适合场景

当你希望 AI Agent 处理以下任务时，适合使用本仓库：

- 实验报告、课程报告、学生报告和毕业设计类文档；
- 从 Markdown 生成的技术报告；
- 必须遵循 reference 文档或学校规范的 DOCX/PDF；
- 包含标题页、凭据信息、表格、图片、引用和代码清单的报告；
- 在 Claude Code、Cursor、Gemini 和 Codex-like 工作流中重复生产报告。

## 快速开始

### Claude Code Plugin

当 marketplace 可用后，从 Claude Code marketplace 安装插件：

```bash
claude plugin install writing-reports-skills@writing-reports-marketplace
```

如果不安装插件，可以将 `CLAUDE.md` 复制或合并到目标项目。

### Cursor

用 Cursor 打开本仓库。项目规则 `.cursor/rules/writing-reports.mdc` 已设置为 `alwaysApply: true`。

在其他项目中使用时，将 `.cursor/rules/writing-reports.mdc` 复制到该项目的 `.cursor/rules/` 目录。

### Gemini

将 `GEMINI.md` 复制或合并到 Gemini CLI 项目，或者将本仓库作为两个 `skills/` 文件夹的来源。

### Codex 和其他技能加载器

将 `skills/` 下的技能文件夹复制到工具的技能目录；如果工具支持从仓库加载技能，也可以直接引用本仓库。

## 包含的技能

- `writing-reports-pandoc` - 通用报告创建、格式化、转换和更新流程，支持 Pandoc、DOCX、PDF、HTML、Markdown、reference 文档、封面页、引用和模板。
- `writing-reports-pandoc-gost` - 严格的俄语 GOST 风格流程，适用于学生报告、实验报告、课程报告、GUAP 风格 DOCX/PDF、标题页、页码、页边距和纯文本源码清单。

## Agent 请求示例

```text
Use writing-reports-pandoc to create a DOCX and PDF report from report.md, reference.docx, and credentials.yaml. Preserve the Markdown source and verify the outputs.
```

```text
Use writing-reports-pandoc-gost to prepare a GOST-style lab report with a title page, page numbers, Times New Roman 14, 1.5 spacing, and plain code listings.
```

```text
Classify the files in this report folder, identify which DOCX is cover-only and which can be used as the body reference, then generate the final report.
```

## 仓库结构

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

## 示例文件

- `examples/credentials.example.yaml` - 带占位符的报告凭据信息示例。
- `examples/first-page.example.md` - 标题页源文件示例。
- `examples/report.example.md` - 语义化 Markdown 报告源文件示例。

不要提交真实的学生、教师、客户、机构或 API 凭据。只应在私有工作副本中替换占位符。
