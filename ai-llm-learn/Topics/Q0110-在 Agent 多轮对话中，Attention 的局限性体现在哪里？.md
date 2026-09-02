---
id: Q0110
normalized_question: 在 Agent 多轮对话中，Attention 的局限性体现在哪里？
legacy_id: Q0128
area: Model / Inference
knowledge_point: transformer-attention
tags:
  - Transformer
  - Attention
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 在 Agent 多轮对话中，Attention 的局限性体现在哪里？

## 原题原文

> 在 Agent 多轮对话任务中，Attention 的局限性体现在哪里？

## 答案

### 面试直答

在 Agent 多轮对话中，Attention 的局限不仅是窗口上限：历史越长，计算和 KV Cache 成本越高，关键信息越容易被日志与工具输出稀释；模型还可能过度关注近期消息、忽略早期约束，或在压缩后丢失细节。

### 一、典型问题

- 标准 Attention 长度复杂度高，长会话增加延迟和显存。
- “能放进窗口”不等于“能可靠使用”，会出现 Lost-in-the-Middle。
- 大量工具 Schema、文件和日志造成 Context Pollution。
- 多轮指令可能冲突，模型难判断哪条仍有效。
- 摘要是有损的，多次压缩会累积误差。

> **核心小结：** 大窗口缓解容量问题，但不能自动解决注意力分配和信息治理。

### 二、Harness 层解决

使用稳定规则重注入、近期消息原文、结构化 Checkpoint、按需检索和子 Agent 隔离；旧 Tool Result先局部清理，必要时再全局压缩。Codex 与 Claude Code 都使用压缩和独立子任务降低主 Context 噪声。

> **核心小结：** Agent 的长程可靠性更多依赖 Context Engineering，而不是期待 Attention 自动记住全部历史。

### 三、评估

构造早期约束、跨轮指代、长日志干扰和多次压缩用例，测约束保持率、事实召回、恢复成功率、延迟和成本。

> **核心小结：** 长上下文能力要用任务保持率验证，不能只看最大 Token 数。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里大模型算法岗面经-02
- 面经小节：面经 05
- 岗位与面试时间：大模型算法 ｜ 面试时间：2026 年 4 月 13 日
- 题目在小节内的位置：第 2 条
- 来源链接：https://www.nowcoder.com/discuss/923309821460221952
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
