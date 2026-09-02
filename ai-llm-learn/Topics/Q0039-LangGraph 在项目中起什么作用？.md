---
id: Q0039
normalized_question: LangGraph 在项目中起什么作用？
legacy_id: Q0048
area: Agent / Harness
knowledge_point: workflow-state-orchestration
tags:
  - Workflow
  - State
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# LangGraph 在项目中起什么作用？

## 原题原文

> 项目中LangGraph有什么作用?

## 答案

### 面试直答

LangGraph 在项目中用于把 Agent 编排表示成有状态图：节点执行模型或工具，边决定固定或条件路由，State 在节点间传递，并可通过 Checkpointer 支持暂停、恢复和 Human-in-the-loop。它适合复杂、长运行、需要可恢复的 Workflow。

### 一、核心抽象

StateGraph 定义共享 State；Node 接收 State 返回增量更新；Edge/Conditional Edge 决定下一节点；Reducer 处理并行更新；Checkpointer 按 Thread 保存执行状态。

> **核心小结：** LangGraph 的价值是显式状态与控制流，不是替模型自动规划。

### 二、边界

简单单轮 Tool Calling 不必引入图框架；图过细会增加维护和序列化成本。业务规则、权限和工具实现仍需自己设计。

> **核心小结：** LangGraph 提供运行时骨架，但不会替代领域建模和评测。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 14
- 岗位与面试时间：AI Agent开发岗 ｜ 面试时间：2026 年 8 月 5 日
- 题目在小节内的位置：第 2 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
