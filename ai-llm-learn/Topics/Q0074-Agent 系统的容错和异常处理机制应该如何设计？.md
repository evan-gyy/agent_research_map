---
id: Q0074
normalized_question: Agent 系统的容错和异常处理机制应该如何设计？
legacy_id: Q0091
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

# Agent 系统的容错和异常处理机制应该如何设计？

## 原题原文

> 如果系统出现异常，整体的容错和异常处理机制怎么设计？

## 答案

### 面试直答

Agent 容错要按错误类型设计：模型错误、工具参数错误、依赖超时、部分结果、状态冲突和用户中断分别处理。统一重试会造成重复副作用和重试风暴，应使用超时、幂等、退避、熔断、降级、Checkpoint 和人工接管。

### 一、错误策略

| 错误 | 处理 |
|---|---|
| 参数不合法 | Schema 错误回灌，有限修复 |
| 临时网络失败 | 指数退避 + 抖动 |
| 限流 | 尊重 Retry-After，队列削峰 |
| 写操作不确定 | 幂等键/查询真实状态，禁止盲重试 |
| 部分成功 | 保存成功节点，只补失败节点 |
| 预算耗尽 | 降级回答或人工接管 |

> **核心小结：** 重试依据错误可恢复性和副作用，而不是见错就重试。

### 二、状态与恢复

持久化 Thread、任务节点和 Tool Call ID；Checkpoint 记录已完成副作用；进程重启后先对账再继续。提供 Kill Switch 和审计日志。

> **核心小结：** 可恢复性来自持久状态与幂等执行，不是模型重新回忆一遍。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里AI Agent开发岗面经-01
- 面经小节：面经 03
- 岗位与面试时间：AI Agent 开发 ｜ 面试时间：2026 年 8 月 5 日
- 题目在小节内的位置：第 11 条
- 来源链接：https://www.nowcoder.com/discuss/923739430513299456
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
