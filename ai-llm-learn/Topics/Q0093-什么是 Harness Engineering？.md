---
id: Q0093
normalized_question: 什么是 Harness Engineering？
legacy_id: Q0111
area: Agent / Harness
knowledge_point: harness-coding-agent
tags:
  - Harness
  - Coding Agent
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 什么是 Harness Engineering？

## 原题原文

> Harness Engineering？

## 答案

### 面试直答

Harness Engineering 是设计和优化模型外的 Agent 运行系统：Context 组装、Agent Loop、工具、状态、权限、沙箱、记忆、压缩、恢复、可观测和评估。它关注的是让模型在真实环境中稳定完成任务，而不只是优化 Prompt。

### 一、核心模块

- 上下文：规则、历史、检索证据和工具描述。
- 控制：计划、循环、预算和终止。
- 执行：工具路由、Schema、沙箱和审批。
- 状态：Thread/Turn、Memory、Checkpoint 和 Resume。
- 质量：测试、Judge、日志、评测集和灰度。

> **核心小结：** 模型决定能力上限，Harness 决定能力能否稳定转化为产品结果。

### 二、为什么重要

同一模型在不同 Harness 下会因保留推理、压缩、工具反馈和权限策略产生显著差异。Coding Agent、旅行 Agent 和客服 Agent 的业务界面与工具不同，但都需要上述运行能力。

> **核心小结：** Harness Engineering 是 Agent 时代的系统工程，不是一个更长的 System Prompt。

### 延伸阅读

- [Codex 模块地图](<../Agent实现拆解/Codex.md>)
- [Claude Code 模块地图](<../Agent实现拆解/Claude Code.md>)

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里大模型算法岗面经-02
- 面经小节：面经 02
- 岗位与面试时间：LLM 应用算法 ｜ 面试时间：2026 年 4 月 20 日
- 题目在小节内的位置：第 3 条
- 来源链接：https://www.nowcoder.com/discuss/923309821460221952
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
