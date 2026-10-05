# 📝 报告写作技能

**生成经过验证的 PDF 和可编辑 DOCX 报告；GUAP 双格式交付优先使用 Word 主文档，再导出 PDF。**

Writing Reports Skill 帮助 Agent 分类素材、保留源文件、应用大学规范并验证最终文档。优先生成可编辑 Word 正文、单独填写封面、更新目录后导出 PDF；明确需要 LaTeX 时仍可使用固定版本的 latex-g7-32。不会从 PDF 反向转换 DOCX。

🌐 语言：[English](README.md) | [Русский](README.ru.md) | 中文

## 🚀 为什么使用它

报告生成失败通常不是 Pandoc 本身的问题。真正的问题往往是：模板角色不清楚、Agent 编造凭据信息、把仅封面的 DOCX 当作正文 `--reference-doc`、页码错误、文本乱码，或者在没有检查文件的情况下宣布完成。

这些技能为 Agent 提供接近 production 的报告流程：询问缺失输入，分类素材，保留可复现源文件，执行转换，并检查最终产物。

## ✨ 你会得到什么

- **可编辑 DOCX 及其最终排版的 PDF**；Pandoc 和 Quarto 是可选工具。参见 [Word 主文档流程与三种路线的实际比较](skills/writing-reports-pandoc-gost/references/word-master.md)。
- 🗂️ **清晰的模板规则**，区分仅封面文件、正文样式 reference DOCX、完整示例、CSL、CSS、参考文献和源素材。
- 🔁 **可复现的报告源文件**，使用语义化 Markdown 和 YAML frontmatter。
- 🌐 **从 URL 获取格式规范**，支持官方网页和 PDF：抓取、提取、保存来源证据并应用规则。
- 🔒 **更安全的凭据处理**，不会编造学生、教师、客户或机构信息。
- 📄 **正确的“封面 + 正文”流程**，避免把仅封面的 DOCX 错用为 `--reference-doc`。
- ✅ **完成前验证**，检查文件、必要章节、引用、页面布局、占位符、乱码、空白页、颜色和源码清单格式。
- 📐 **俄语 GOST 风格支持**，适用于学生报告、实验报告、课程报告、标题页、页码、页边距和源码清单。

## 🎯 适合场景

当你希望 AI Agent 处理以下任务时，适合使用本仓库：

- 实验报告、课程报告、学生报告和毕业设计类文档；
- 从 Markdown 生成的技术报告；
- 必须遵循 reference 文档、上传的规范文件或官方规范 URL 的 DOCX/PDF；
- 包含标题页、凭据信息、表格、图片、引用和代码清单的报告；
- 在 Claude Code、Cursor、Gemini 和 Codex-like 工作流中重复生产报告。

## ⚡ 快速开始

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

## 🧩 包含的技能

- `writing-reports-pandoc-gost` - 严格的俄语 GOST 风格流程，适用于学生报告、实验报告、课程报告、DOCX/PDF、标题页、页码、页边距和纯文本源码清单。

## 💬 Agent 请求示例

```text
```

```text
Use writing-reports-pandoc-gost to prepare a GOST-style lab report with a title page, page numbers, Times New Roman 14, 1.5 spacing, and plain code listings.
```

```text
Classify the files in this report folder, identify which DOCX is cover-only and which can be used as the body reference, then generate the final report.
```

```text
```

## 🌐 从 URL 获取格式规范

你可以给 Agent 一个官方格式规范 URL，而不需要手动列出所有规则。技能会要求 Agent：

1. 使用可用的 web/browser 工具抓取 URL；
2. 提取可执行规则，例如页边距、字体、行距、标题页、页码、引用、必要章节和输出格式；
3. 保存 URL、获取日期、页面/文档标题、内容类型和提取出的规则；
4. 如果 URL 被阻止、需要登录或无法访问，则要求你粘贴文本或上传源文件；
5. 先应用提取出的规则，再使用默认值。

这样，来自 URL 的格式要求是可审计的，而不是隐藏在 Agent 的记忆里。

## 🗃️ 仓库结构

```text
.claude-plugin/plugin.json
.claude-plugin/marketplace.json
.cursor/rules/writing-reports.mdc
CLAUDE.md
CURSOR.md
GEMINI.md
examples/
skills/
  writing-reports-pandoc-gost/
    SKILL.md
    agents/openai.yaml
```

## 🧪 示例文件

- `examples/credentials.example.yaml` - 带占位符的报告凭据信息示例。
- `examples/first-page.example.md` - 标题页源文件示例。
- `examples/report.example.md` - 语义化 Markdown 报告源文件示例。

可以把示例文件作为安全起点：将它们复制到私有报告工作区，在那里替换真实数据，然后让 Agent 基于这些文件生成报告。不要把真实凭据保存到本仓库。

不要提交真实的学生、教师、客户、机构或 API 凭据。只应在私有工作副本中替换占位符。
