---
id: Q0023
normalized_question: 如何选择 Embedding 模型？主要依据是什么？
legacy_id: Q0023
area: RAG
knowledge_point: embedding-vector-retrieval
tags:
  - Embedding
  - Vector Search
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 如何选择 Embedding 模型？主要依据是什么？

## 原题原文

> Embedding 模型怎么选择的 为什么

## 答案

### 面试直答

选择 Embedding 模型主要看目标语言与领域、检索任务、向量维度、最大长度、延迟成本和部署约束；最终用自己的 Query—Document 数据测 Recall@K、MRR/nDCG，而不是只看公开榜单。

### 一、筛选维度

- 中文、多语言、代码或专业领域覆盖。
- Query/Document 是否需要不同前缀或非对称编码。
- 长文本截断、向量维度和存储成本。
- 本地部署、吞吐、批处理与许可证。
- 是否支持归一化及与向量库距离度量兼容。

> **核心小结：** Embedding 模型要与数据分布和检索方式匹配，不是参数越大越好。

### 二、离线与线上验证

建立包含精确实体、语义改写、长尾和困难负例的数据集；比较稠密、BM25 和混合基线。线上再看任务成功、延迟和成本。更换模型需重建索引并进行双写或蓝绿切换。

> **核心小结：** 选型依据是自有数据上的检索增益与全链路成本。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 06
- 岗位与面试时间：AI Agent开发岗 ｜ 面试时间：2026 年 8 月 14 日
- 题目在小节内的位置：第 2 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
