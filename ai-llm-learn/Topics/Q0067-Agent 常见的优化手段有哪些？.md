---
id: Q0067
normalized_question: Agent 常见的优化手段有哪些？
legacy_id: Q0084
area: Reliability / Production
knowledge_point: reliability-resilience
tags:
  - Reliability
  - Resilience
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# Agent 常见的优化手段有哪些？

## 原题原文

> Agent 优化有哪些常见手段？

## 答案

### 面试直答

Agent 常见优化分为模型与 Prompt、Context、规划、工具、运行时、评估六层。顺序应从可观测瓶颈出发：先修工具和数据硬错误，再优化 Context 与控制流，最后才考虑换模型或增加推理轮次。

### 一、优化地图

| 层次 | 常见手段 |
|---|---|
| Context | 检索、压缩、Tool Search、子 Agent 隔离 |
| Planning | 结构化任务、并行 DAG、有限重规划 |
| Tool | Schema、校验、幂等、缓存、批处理 |
| Runtime | 超时、背压、重试、熔断、恢复 |
| Model | 路由、蒸馏、Few-shot、推理预算 |
| Eval | 分层指标、回放、故障注入、灰度 |

> **核心小结：** 优化对象是端到端系统，不只是模型输出。

### 二、原则

每次只改变一个主要变量，在相同任务和预算下比较；关注 P95 和每成功任务成本；保留失败轨迹形成回归集。

> **核心小结：** 没有分层指标和对照实验，调优很容易变成不可归因的堆配置。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里AI Agent开发岗面经-01
- 面经小节：面经 03
- 岗位与面试时间：AI Agent 开发 ｜ 面试时间：2026 年 8 月 5 日
- 题目在小节内的位置：第 3 条
- 来源链接：https://www.nowcoder.com/discuss/923739430513299456
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
