# AI · LLM 学习库

一个由 Markdown 驱动、面向长期积累的 AI / LLM 系统化学习库。

这里把分散的技术问题整理成可检索、可关联、可持续补充的知识体系，覆盖语言模型、Agent、RAG、模型训练与推理、上下文与记忆、工具协议、评测和生产可靠性等主题。

> 当前收录 118 道正式问题、28 个受控知识点，并提供学习笔记、全文检索、分类统计和本机学习进度。

## 学习库能做什么

- **按问题学习**：每道题都有独立页面，可逐步补充核心回答、公式、代码和流程图。
- **按知识点组织**：问题通过受控知识点建立关联，自动统计出现频率和主题分布。
- **快速检索与筛选**：支持题号、标题、笔记全文搜索，以及分类、知识点和学习状态筛选。
- **记录个人进度**：收藏、最近浏览、学习中、待复习和已掌握状态保存在当前浏览器。
- **同时服务 Web 与 Obsidian**：Markdown 题库既可以直接在 Obsidian 中维护，也可以构建为静态网站。
- **静态、可审计、无后端**：不需要数据库或账号系统，可直接部署到 GitHub Pages。

## 内容范围

学习库聚焦 NLP、语言模型和 LLM 工程：

- Transformer、Attention、Token、训练、微调、对齐与推理优化
- Agent 架构、Planning、ReAct、Workflow、Harness 与多 Agent 协作
- Tool Use、Function Calling、MCP、参数 Schema 与工具可靠性
- RAG、Embedding、文档解析、混合检索、重排与检索评估
- Context、Memory、长上下文压缩与状态管理
- 评测体系、错误恢复、并发、稳定性与生产化设计

正式题库只收录有可追溯来源、且明确属于上述范围的问题。无法完成在线复核的内容会如实标记，推导题和自动扩展题不会混入正式编号。

## 工作方式

~~~text
可追溯的技术问题
        │
        ▼
Markdown 正式题库 ──────► Obsidian 本地知识库
        │
        ├──► 内容校验：编号、来源、知识点、公开字段
        │
        ▼
Astro 静态构建
        │
        ├──► 题库 / 详情 / 知识统计
        ├──► 搜索 / 筛选 / 公式 / Mermaid
        └──► GitHub Pages
                 │
                 ▼
          浏览器本机学习进度
~~~

正式 Markdown 是唯一内容源。网站在构建时读取题库，不复制第二份内容，也不会把私有采集字段直接发布到前端。

## 项目结构

~~~text
agent_research_map/
├── ai-llm-learn/
│   ├── Topics/                 # Q0001... 正式题库与学习笔记
│   ├── Archive/                # 非原题、非 NLP 等非正式归档
│   └── Templates/              # Obsidian 内容模板
├── web/
│   ├── src/                    # Astro 页面、内容解析与交互
│   ├── tests/                  # 数据与统计单元测试
│   ├── e2e/                    # Playwright 浏览器验收
│   └── scripts/                # 内容校验与公开产物审计
├── config/                     # 可选的扩展知识地图配置
├── data/                       # 可选的材料与离线分析数据
├── scripts/                    # Vault 与学习地图生成工具
└── .github/workflows/pages.yml # GitHub Pages 自动构建与发布
~~~

## 快速开始

### 浏览和维护 Markdown 题库

用 Obsidian 直接打开 **ai-llm-learn/**。正式题目位于 **ai-llm-learn/Topics/**，每个文件对应一道问题。

### 启动学习网站

需要 Node.js 22 或更高版本：

~~~bash
cd web
npm ci
npm run data:check
npm run dev
~~~

浏览器访问：

~~~text
http://localhost:4321/agent_research_map/
~~~

### 构建与验证

~~~bash
cd web
npm run data:check  # 检查正式题号、来源、知识点和公开字段
npm run check       # Astro / TypeScript 检查
npm test            # 数据解析与统计单元测试
npm run build       # 静态构建并审计最终公开产物
npm run test:e2e    # 浏览器端到端测试
~~~

首次运行端到端测试前需要安装 Chromium 测试运行时：

~~~bash
npx playwright install chromium
~~~

## 添加一道正式问题

1. 确认问题在原始网页或其他可验证来源中明确出现。
2. 在 **ai-llm-learn/Topics/** 新建下一个连续编号的 Markdown 文件。
3. 填写来源 URL、核验状态、knowledge_point 和 tags 等 frontmatter。
4. 在正文中补充学习笔记；暂时没有答案也可以保留为空。
5. 在 web 目录运行 npm run data:check，确认编号、来源和知识点均有效。

知识点使用受控目录，定义在 **web/src/data/knowledge-points.json**。需要新增知识点时，应先更新目录，再给题目引用，避免同义标签造成统计分裂。

## GitHub Pages

仓库已包含 GitHub Actions 工作流。推送到 master 后，工作流会依次完成：

~~~text
内容校验 → 类型检查 → 单元测试 → 静态构建 → 公开产物审计 → 浏览器测试 → Pages 部署
~~~

首次启用时，在仓库的 **Settings → Pages → Build and deployment** 中把 Source 设置为 **GitHub Actions**。项目站点路径为：

~~~text
https://evan-gyy.github.io/agent_research_map/
~~~

## 可选：扩展知识地图

仓库仍保留一套离线知识地图与材料分析工具，用于从更高层级查看主题、材料和个人知识缺口。它不是网站运行的依赖，可以按需使用：

~~~bash
python scripts/generate_vault.py
python scripts/market_analyzer.py
python scripts/market_analyzer.py --brief
~~~

这部分生成的 vault 和 output 是辅助视图；正式问题和学习笔记仍以 **ai-llm-learn/Topics/** 为准。

## 设计原则

1. **内容优先**：先沉淀可复核的问题和高质量笔记，再增加自动化。
2. **单一数据源**：Markdown 同时服务 Obsidian 和网站，不维护重复题库。
3. **来源可追溯**：正式问题必须能够回到明确来源，不把推测包装成事实。
4. **本地优先**：阅读、编辑和学习进度不依赖云端数据库。
5. **构建即审计**：编号、统计、字段白名单和公开定位文本都由自动检查守护。
