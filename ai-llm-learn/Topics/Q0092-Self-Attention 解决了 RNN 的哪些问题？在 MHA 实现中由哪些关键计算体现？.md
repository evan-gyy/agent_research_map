---
id: Q0092
normalized_question: Self-Attention 解决了 RNN 的哪些问题？在 MHA 实现中由哪些关键计算体现？
legacy_id: Q0110
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

# Self-Attention 解决了 RNN 的哪些问题？在 MHA 实现中由哪些关键计算体现？

## 原题原文

> Self-Attention 解决了什么问题，手撕 MHA 中哪几行代码解决了 RNN 的问题？

## 答案

### 面试直答

Self-Attention 解决了 RNN 的两个核心问题：序列计算难并行、长距离信息要逐步传播。Attention 让任意两个 Token 在一层内直接交互，训练时所有位置可用矩阵乘法并行；代价是标准 Attention 对序列长度的时间和显存复杂度为 $O(n^2)$。

### 一、关键计算

MHA 先得到多个 Head 的 Q/K/V：

$$head_i=softmax(rac{Q_iK_i^T}{sqrt{d_k}})V_i$$

$$MHA=Concat(head_1,...,head_h)W_O$$

$QK^T$ 一次产生所有位置两两关系，体现并行和直接长程依赖；多个 Head 在不同子空间建模不同关系。

> **核心小结：** RNN 沿时间步传递状态，Attention 用全局关系矩阵一次连接所有位置。

### 二、取舍

RNN 推理状态小、天然适合流式；Transformer 训练并行度高，但长序列 Attention 矩阵昂贵，自回归推理还需 KV Cache。Flash Attention 优化 IO，稀疏/线性 Attention 优化复杂度，GQA/MQA 优化 Cache。

> **核心小结：** Self-Attention 消除了训练的时间步依赖，但没有消除长序列的资源瓶颈。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里大模型算法岗面经-02
- 面经小节：面经 02
- 岗位与面试时间：LLM 应用算法 ｜ 面试时间：2026 年 4 月 20 日
- 题目在小节内的位置：第 2 条
- 来源链接：https://www.nowcoder.com/discuss/923309821460221952
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
