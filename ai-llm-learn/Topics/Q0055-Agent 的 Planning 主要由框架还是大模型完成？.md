---
id: Q0055
normalized_question: Agent 的 Planning 主要由框架还是大模型完成？
legacy_id: Q0066
area: Agent / Harness
knowledge_point: planning-task-decomposition
tags:
  - Planning
  - Task Decomposition
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# Agent 的 Planning 主要由框架还是大模型完成？

## 原题原文

> 你觉得planning规划这一块是agent框架做的还是大模型做的？

## 答案

### 面试直答

Planning 通常由**大模型生成语义计划，框架或 Harness 负责约束、保存、调度、验证和重规划**。大模型擅长理解开放目标和拆分语义任务；框架擅长依赖、状态、预算、权限和确定性执行。固定业务也可以完全由规则或 DAG 规划。

### 一、职责分工

| 大模型 | 框架/Harness |
|---|---|
| 理解目标和隐含约束 | 定义计划 Schema |
| 提出子任务和候选路径 | 校验依赖与允许工具 |
| 根据观察调整计划 | 并发调度、状态持久化 |
| 判断证据是否充分 | 最大步数、Deadline、审批 |

> **核心小结：** 模型决定计划内容，框架决定计划是否可执行、如何运行以及何时停止。

### 二、三种实现

- 固定 Workflow：代码规划，延迟低、可预测。
- LLM Planner + DAG Executor：先生成结构化任务，再受控并行。
- ReAct：每步根据工具反馈动态决定，灵活但轮数不稳定。

Dynamic Planner 属于第二类：Planner 生成旅行子目标，Orchestrator 调度 Executor，Judge 决定是否有限重规划。

> **核心小结：** Planning 应根据任务不确定性选择，不是所有请求都需要一次大模型规划调用。

### 常见追问

- **框架会自己规划吗？** 框架可提供节点、状态和调度原语，但语义拆解通常来自模型或业务规则。
- **为什么不让模型直接执行计划？** 权限、并发和副作用需要确定性控制。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 20
- 岗位与面试时间：AI Agent开发岗 ｜ 面试时间：2026 年 7 月 29 日
- 题目在小节内的位置：第 1 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
