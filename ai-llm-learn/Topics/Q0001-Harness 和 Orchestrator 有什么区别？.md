---
id: Q0001
normalized_question: Harness 和 Orchestrator 有什么区别？
legacy_id: Q0001
area: Tool / Protocol
knowledge_point: mcp-protocol
tags:
  - MCP
  - Protocol
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# Harness 和 Orchestrator 有什么区别？

## 原题原文

> 以前问“你们怎么调工具的”，现在问“Harness和orchestrator有什么区别”

## 答案

### 面试直答

Harness 是模型外的完整 Agent 运行环境，负责 Context、工具、状态、权限、执行、恢复和可观测；Orchestrator 是其中负责“任务怎么拆、由谁执行、何时汇总”的编排组件。**Harness 是大系统，Orchestrator 是控制任务流的一部分。**

### 一、边界

| 能力 | Harness | Orchestrator |
|---|---|---|
| 模型/上下文调用 | 是 | 使用但不一定实现 |
| 工具执行与沙箱 | 是 | 通常只调度 |
| 任务拆解/依赖 | 可包含 | 核心职责 |
| 权限/审批 | 是 | 遵守策略 |
| 会话恢复/压缩 | 是 | 可读取状态 |
| 多 Agent 分配 | 可支持 | 核心职责之一 |

> **核心小结：** Orchestrator 回答“下一步让谁做什么”，Harness 回答“整个 Agent 如何安全持续运行”。

### 二、实例

Dynamic Planner 的 Orchestrator 协调 Planner、Executor、Judge 和 Summary；其外层服务还包括 Memory、SSE、内容校验等 Harness 能力。Codex app-server 则是更通用的 Harness，提供 Thread/Turn/Item、工具与审批协议。

> **核心小结：** 不能把一个任务 DAG 调度器等同于完整 Agent Harness。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 01
- 岗位与面试时间：AI Agent 开发 ｜ 面试时间：2026 年 8 月 20 日
- 题目在小节内的位置：第 1 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
