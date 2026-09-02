---
id: Q0043
normalized_question: 项目采用单 Agent 还是多 Agent 架构？为什么？
legacy_id: Q0052
area: Multi-Agent
knowledge_point: multi-agent-collaboration
tags:
  - Multi-Agent
  - Collaboration
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 项目采用单 Agent 还是多 Agent 架构？为什么？

## 原题原文

> 单 Agent 还是多 Agent 架构？

## 答案

### 面试直答

当前 Dynamic Planner 更准确地说是**单 Orchestrator 下的多角色/多 Executor 架构**，不是多个长期自治 Agent。Planner 拆分旅行子目标，Executor 可并行调用不同旅行技能，Judge 验收，Summary 统一表达。选择它是因为业务需要多意图并行，但又要求低延迟和受控输出。

### 一、为什么不是完全自治多 Agent

完全自治 Agent 需要独立目标、长期状态和相互通信，会增加轮次、冲突和不可预测延迟。旅行查询的角色边界相对清楚，使用受控 DAG 已能获得并行收益。

> **核心小结：** 业务里“多角色调用”不等于“多个自治主体”。

### 二、为什么不只用单 ReAct Agent

单 ReAct 可以灵活探索，但酒店、景点等无依赖查询若串行执行会增加延迟。Planner 一次拆分后并行 Executor，Judge 只在信息不足时有限回路，更符合移动端 SLA。

> **核心小结：** 架构选择由任务可拆分性和延迟约束决定，而不是追求 Agent 数量。

### 三、代价

需要处理并发限流、部分失败、结果去重和 Planner 开销。若请求很简单，规则路由或单工具调用更快；系统应按意图选择路径。

> **核心小结：** 简单任务走简单路径，复杂多意图才进入编排链路。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 15
- 岗位与面试时间：AI Agent开发岗 ｜ 面试时间：2026 年 8 月 5 日
- 题目在小节内的位置：第 3 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
