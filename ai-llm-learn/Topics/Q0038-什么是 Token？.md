---
id: Q0038
normalized_question: 什么是 Token？
legacy_id: Q0047
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

# 什么是 Token？

## 原题原文

> 什么是token

## 答案

### 面试直答

Token 是模型处理文本的基本离散单元，不等同于字或单词。Tokenizer 将文本切成 Token ID，模型在这些 ID 上做 Embedding、Attention 和下一个 Token 预测；Context Window、计费和生成长度都按 Token 计算。

### 一、为什么不是按字

常见 BPE/Unigram 会把高频片段合并，英文词可能一个或多个 Token，中文字符和罕见符号也可能拆分。代码、JSON、空格和不同语言的 Token 密度不同。

> **核心小结：** Token 数取决于具体模型的 Tokenizer，不能用字符数精确代替。

### 二、工程意义

输入 Token 包括 System Prompt、历史消息、工具 Schema、检索证据和工具结果；还要为模型输出预留预算。成本近似为输入与输出 Token 分别乘单价，延迟也受 Context 长度影响。

> **核心小结：** Context 管理是在固定 Token 预算中安排规则、任务、证据和输出空间。

### 常见追问

- **一个中文字符等于一个 Token 吗？** 不保证，应使用目标模型 Tokenizer 实测。
- **窗口大就能全部塞入吗？** 能放下不代表模型能有效关注，成本和 Context Rot 仍存在。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 14
- 岗位与面试时间：AI Agent开发岗 ｜ 面试时间：2026 年 8 月 5 日
- 题目在小节内的位置：第 1 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
