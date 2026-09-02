---
id: Q0061
normalized_question: Redis 在 AI Agent 系统中有哪些应用场景？
legacy_id: Q0073
area: Agent / Harness
knowledge_point: system-performance-concurrency
tags:
  - Concurrency
  - Performance
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# Redis 在 AI Agent 系统中有哪些应用场景？

## 原题原文

> Redis 在 AI Agent 系统中可能有哪些应用场景？

## 答案

### 面试直答

Redis 在 Agent 系统中常用于短期状态、缓存、分布式限流、幂等键、任务进度、轻量队列和锁。它适合低延迟临时数据，不应默认承担不可丢失的长期 Transcript 或唯一业务真值。

### 一、应用

- 缓存模型/Embedding/工具结果。
- Session 和流式事件游标。
- Token Bucket 限流、并发信号量。
- request_id 幂等和去重。
- 带 TTL 的任务锁与进度。
- Pub/Sub 通知，但重要消息用 Streams/持久队列。

> **核心小结：** Redis 适合快状态和协调，不适合未经持久化设计的核心事实。

### 二、风险

锁要有 TTL 和所有者 Token；缓存 Key 包含模型、Prompt、权限和数据版本；防热点与大 Key；内存淘汰不能导致重复副作用。

> **核心小结：** Redis 的速度优势建立在明确一致性、过期和降级语义上。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 21
- 岗位与面试时间：AI Agent开发岗 ｜ 面试时间：2026 年 7 月 29 日
- 题目在小节内的位置：第 5 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
