---
id: Q0059
normalized_question: 上下文工程中如何使用 To-Do List 机制？
legacy_id: Q0070
area: Memory / Context
knowledge_point: context-token-compression
tags:
  - Context
  - Token
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 上下文工程中如何使用 To-Do List 机制？

## 原题原文

> 上下文工程经验：有没有做过To-Do List机制？

## 答案

### 面试直答

To-Do List 在 Context Engineering 中是一个外部化的任务状态表：把目标、步骤、状态、依赖和验证结果从长对话中提取出来，每轮只更新结构化状态。它降低遗忘和重复执行，但不能替代真实工具状态。

### 一、结构

每项包含 id、目标、pending/in_progress/done/blocked、依赖、证据和完成条件。模型开始动作前标记 in_progress，工具成功且验证通过后才标 done。

> **核心小结：** To-Do 的价值是让“还要做什么”稳定可见，并使进度可审计。

### 二、工程注意

- 列表由 Harness 持久化，不能只存在模型文本里。
- 限制粒度，避免每个微动作都成为任务。
- 压缩时保留未完成项和关键完成证据。
- 文件、测试和外部系统才是真实状态；列表与事实冲突时重新核验。

Codex 的 Plan/Goal 进度和 Coding Agent 的任务列表都体现类似思想。

> **核心小结：** To-Do 是控制面快照，不是环境事实的唯一来源。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 20
- 岗位与面试时间：AI Agent开发岗 ｜ 面试时间：2026 年 7 月 29 日
- 题目在小节内的位置：第 6 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
