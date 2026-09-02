---
id: Q0073
normalized_question: 多轮、多会话场景下如何管理 Memory？
legacy_id: Q0090
area: Memory / Context
knowledge_point: memory-systems
tags:
  - Memory
  - Context
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 多轮、多会话场景下如何管理 Memory？

## 原题原文

> 多轮、多会话场景下 memory 如何处理？

## 答案

### 面试直答

多轮、多会话 Memory 要分清 Session、用户、项目和组织作用域。单轮 Context 保存当前轨迹；会话结束生成摘要和候选长期记忆；新会话按身份、权限与相关性检索，而不是直接拼接所有历史。

### 一、数据模型

每条 Memory 包含 subject、scope、content、source、timestamp、confidence、version 和 expiry。会话摘要与长期事实分库存储，避免摘要中的临时推测污染稳定记忆。

> **核心小结：** 作用域和来源比向量相似度更优先，否则容易串用户和串项目。

### 二、冲突与隐私

用户明确更正优先旧记录；时间敏感事实按版本失效；支持查看、删除和禁用记忆。召回后还要在 Prompt 中标注其来源和可能过期。

> **核心小结：** 跨会话 Memory 必须可治理，不能成为不可见、不可纠正的黑盒画像。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里AI Agent开发岗面经-01
- 面经小节：面经 03
- 岗位与面试时间：AI Agent 开发 ｜ 面试时间：2026 年 8 月 5 日
- 题目在小节内的位置：第 10 条
- 来源链接：https://www.nowcoder.com/discuss/923739430513299456
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
