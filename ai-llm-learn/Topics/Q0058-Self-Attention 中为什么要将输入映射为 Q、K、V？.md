---
id: Q0058
normalized_question: Self-Attention 中为什么要将输入映射为 Q、K、V？
legacy_id: Q0069
area: Model / Inference
knowledge_point: transformer-attention
tags:
  - Transformer
  - Attention
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# Self-Attention 中为什么要将输入映射为 Q、K、V？

## 原题原文

> Self-attention机制：QKV为什么要这么分？

## 答案

### 面试直答

Self-Attention 把同一输入映射成 Q、K、V，是为了把“我要找什么”“每个位置提供什么匹配键”“真正聚合什么内容”三个角色解耦。Q 与 K 决定权重，权重再对 V 加权求和。

### 一、计算

$$Q=XW_Q,quad K=XW_K,quad V=XW_V$$

$$Attention(Q,K,V)=softmax(rac{QK^T}{sqrt{d_k}})V$$

位置 $i$ 的 Query 与所有 Key 点积，得到它对各位置的关注度；Value 是被聚合的信息。除以 $sqrt{d_k}$ 防止维度大时点积过大导致 Softmax 饱和。

> **核心小结：** Q/K 负责寻址，V 负责传递内容，独立投影让模型学习不同的匹配与表示空间。

### 二、为什么不用同一个向量

如果直接用 $X$ 同时匹配和聚合，会限制表达能力。不同 Head 还能学习语法依赖、实体关系和位置模式。Cross-Attention 中 Q 来自 Decoder，K/V 来自 Encoder，更能体现三者角色差异。

> **核心小结：** QKV 设计既提升表示能力，也使 Self-Attention 与 Cross-Attention 使用统一计算形式。

### 常见追问

- **Q、K、V 一定不同吗？** 输入来源在 Self-Attention 中相同，但投影矩阵不同。
- **为什么 K 和 V 常共享更少的 Head？** GQA/MQA 通过共享 K/V 降低 KV Cache。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 20
- 岗位与面试时间：AI Agent开发岗 ｜ 面试时间：2026 年 7 月 29 日
- 题目在小节内的位置：第 4 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
