---
id: Q0004
normalized_question: Agent 出现路径震荡时如何优化？
legacy_id: Q0004
area: Reliability / Production
knowledge_point: reliability-resilience
tags:
  - Reliability
  - Resilience
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# Agent 出现路径震荡时如何优化？

## 原题原文

> Agent 出现路径震荡如何优化？

## 答案

### 面试直答

路径震荡是 Agent 在相似动作之间反复切换却没有有效进展。优化要先可观测：记录状态、动作、工具结果和进展指标；再通过重复检测、显式计划、失败记忆、最大步数和重规划打断循环。

### 一、检测

对动作做规范化，比较工具名、关键参数、目标文件和结果哈希；连续重复、状态无变化或错误相同即触发震荡。不能只比较自然语言文本。

> **核心小结：** 路径震荡的本质是动作重复且环境状态没有改善。

### 二、处理

- 把目标和完成条件外置到 Plan/To-Do。
- 将失败原因结构化回灌，禁止原参数立即重试。
- 重复一次后尝试备选策略，达到阈值后重规划或人工。
- 缩小工具集合和检索范围。
- 设置步数、Token、时间和成本预算。

> **核心小结：** 重试必须改变条件，否则只是放大成本。

### 三、评估

观察重复动作率、无进展步数、平均恢复步数和成功任务成本，并用历史震荡轨迹做回归。

> **核心小结：** 优化目标是更快恢复有效进展，而不只是减少调用次数。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 01
- 岗位与面试时间：AI Agent 开发 ｜ 面试时间：2026 年 8 月 20 日
- 题目在小节内的位置：第 4 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
