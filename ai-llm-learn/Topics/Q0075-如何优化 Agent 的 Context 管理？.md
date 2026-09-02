---
id: Q0075
normalized_question: 如何优化 Agent 的 Context 管理？
legacy_id: Q0092
area: Memory / Context
knowledge_point: context-token-compression
tags:
  - Context
  - Token
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 如何优化 Agent 的 Context 管理？

## 原题原文

> 上下文处理相关的场景题：如何优化 context 管理？

## 答案

### 面试直答

Agent Context 优化要同时做预算、筛选、压缩、检索、隔离和缓存：稳定规则重注入，近期任务状态保原文，旧历史结构化摘要，大资料按需检索，独立探索交给子 Agent，工具 Schema 延迟加载。

### 一、优化顺序

先测 Token 构成，再处理最大项：工具输出过大先截断/落盘，Schema 过多先路由，历史过长再压缩，知识文档用 RAG。不要一开始就粗暴滑窗。

> **核心小结：** Context 优化应针对实际 Token 热点，而不是统一删除旧消息。

### 二、质量保护

压缩摘要保留目标、约束、决策、文件、错误和下一步；原始 Transcript 可回查；用续接成功率、关键信息保留率、输入 Token、P95 延迟和任务成功率评估。经历多次压缩或目标变化时新开会话。

> **核心小结：** 优化目标是在更少 Token 下保持任务成功，而不只是减少计费。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里AI Agent开发岗面经-01
- 面经小节：面经 03
- 岗位与面试时间：AI Agent 开发 ｜ 面试时间：2026 年 8 月 5 日
- 题目在小节内的位置：第 12 条
- 来源链接：https://www.nowcoder.com/discuss/923739430513299456
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
