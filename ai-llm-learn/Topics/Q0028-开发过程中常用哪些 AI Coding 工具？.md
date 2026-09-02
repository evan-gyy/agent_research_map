---
id: Q0028
normalized_question: 开发过程中常用哪些 AI Coding 工具？
legacy_id: Q0033
area: Tool / Protocol
knowledge_point: harness-coding-agent
tags:
  - Harness
  - Coding Agent
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 开发过程中常用哪些 AI Coding 工具？

## 原题原文

> 平时开发过程中主要使用哪些AI Coding工具？

## 答案

### 面试直答

AI Coding 工具可以分为补全型、对话编辑型和 Agent 型。实际开发中可按任务选择：IDE 补全适合局部代码；Codex、Claude Code 这类 Agent 适合跨文件检索、命令执行、测试和长任务；代码审查与安全工具负责提交后的确定性检查。

### 一、选型

| 场景 | 工具形态 | 关注点 |
|---|---|---|
| 写一个函数/补全样板 | IDE 补全 | 低延迟、局部上下文 |
| 理解代码/生成 Patch | 对话编辑 | Diff 可审查 |
| 跨模块改造/排障 | Coding Agent | 工具、沙箱、测试、恢复 |
| PR 审查 | Review Agent + 静态工具 | 证据、误报、权限 |

> **核心小结：** 工具选择取决于任务跨度和副作用，不是 Agent 化程度越高越好。

### 二、使用方法

先给目标、范围、不可修改项和验收命令；要求 Agent 读取项目规则，改后运行测试并展示 Diff。敏感仓库关注数据策略、网络访问和日志；关键改动仍由人审查。

> **核心小结：** 把 AI 工具当有权限边界的工程协作者，而不是自动粘贴代码的聊天框。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 09
- 岗位与面试时间：AI Agent开发岗 ｜ 面试时间：2026 年 8 月 13 日
- 题目在小节内的位置：第 2 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
