---
id: Q0080
normalized_question: ReAct 范式是什么？有哪些优缺点？
legacy_id: Q0097
area: Agent / Harness
knowledge_point: react-agent-loop
tags:
  - ReAct
  - Agent Loop
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# ReAct 范式是什么？有哪些优缺点？

## 原题原文

> 项目一中使用了 ReAct，ReAct 范式是什么？有什么优缺点？

## 答案

### 面试直答

ReAct 范式让模型在每次观察后重新决策，优点是适应未知环境、可利用工具反馈纠错；缺点是调用次数不可预测、成本和延迟高、易震荡，并扩大提示注入与越权风险。

### 一、适用场景

适合排障、开放研究、网页或代码探索；不适合固定查询、严格低延迟和高风险写操作。业务主链路可以一次 Planner 并行工具，失败分支再进入有限 ReAct。

> **核心小结：** 中间结果会显著改变下一步时，ReAct 才真正有价值。

### 二、优化

- 工具 Schema 和权限前置校验。
- 最大步数、Token、成本和 Deadline。
- 记录状态与重复动作，触发重规划或终止。
- 工具结果摘要但保留关键证据。
- 将成熟高频路径固化为 Workflow。

> **核心小结：** 生产 ReAct 必须是有预算、有状态、有权限边界的受控循环。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里AI Agent开发岗面经-01
- 面经小节：面经 04
- 岗位与面试时间：AI Agent 开发 ｜ 面试时间：2026 年 7 月 14 日
- 题目在小节内的位置：第 5 条
- 来源链接：https://www.nowcoder.com/discuss/923739430513299456
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
