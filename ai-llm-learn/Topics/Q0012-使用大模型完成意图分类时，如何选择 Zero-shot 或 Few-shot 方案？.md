---
id: Q0012
normalized_question: 使用大模型完成意图分类时，如何选择 Zero-shot 或 Few-shot 方案？
legacy_id: Q0012
area: Agent Application
knowledge_point: intent-routing
tags:
  - Intent
  - Routing
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 使用大模型完成意图分类时，如何选择 Zero-shot 或 Few-shot 方案？

## 原题原文

> 如果使用大模型完成意图分类，如何选择Zero-shot、Few-shot方案？

## 答案

### 面试直答

Zero-shot 适合标签语义清晰、样本少或快速冷启动；Few-shot 适合类别边界微妙、格式固定和有代表性示例。选择应通过同一评测集比较 Macro-F1、稳定性、Token、延迟，而不是默认示例越多越好。

### 一、判断条件

Zero-shot 先写清标签定义、正反边界和 unknown；若混淆矩阵显示相似意图持续误判，再加入覆盖边界的 Few-shot。示例应多样、短且无冲突，避免泄漏答案模板。

> **核心小结：** Few-shot 用来修正决策边界，不是堆历史样本。

### 二、生产策略

稳定高频类可蒸馏成小分类器；大模型处理低置信和新意图。动态选示例时只取同领域近邻，并防 Prompt Injection。标签变化后重跑回归集。

> **核心小结：** 最佳方案通常是 Zero-shot 冷启动、错误驱动补 Few-shot、成熟后轻量化。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 02
- 岗位与面试时间：AI Agent开发岗 ｜ 面试时间：2026 年 8 月 20 日
- 题目在小节内的位置：第 5 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
