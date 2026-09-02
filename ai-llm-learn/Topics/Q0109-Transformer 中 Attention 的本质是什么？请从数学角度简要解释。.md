---
id: Q0109
normalized_question: Transformer 中 Attention 的本质是什么？请从数学角度简要解释。
legacy_id: Q0127
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

# Transformer 中 Attention 的本质是什么？请从数学角度简要解释。

## 原题原文

> Transformer 中 Attention 的本质是什么？从数学角度简要解释一下。

## 答案

### 面试直答

Attention 的本质是**基于内容的可微检索**：Query 表示当前需要什么，Key 表示候选如何被匹配，Value 表示候选携带的信息；Softmax 将相似度转成归一化权重，再对 Value 做加权汇总。

### 一、数学表达

$$A=softmax(rac{QK^T}{sqrt{d_k}}),qquad O=AV$$

$A_{ij}$ 表示位置 $i$ 从位置 $j$ 读取信息的比例。缩放避免高维点积方差过大；Mask 将未来位置或 Padding 的 Logit 设为负无穷。

> **核心小结：** Attention 先计算“从哪里读”，再计算“读到什么”。

### 二、多头与复杂度

多头将表示投影到多个子空间，分别学习不同关系，拼接后再投影。标准 Self-Attention 构造 $n	imes n$ 权重矩阵，时间和显存随序列长度平方增长；自回归推理用 KV Cache 避免重复计算历史 K/V。

> **核心小结：** 多头增加关系表达，KV Cache 减少重复计算，但长 Context 仍带来 Cache 和注意力成本。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里大模型算法岗面经-02
- 面经小节：面经 05
- 岗位与面试时间：大模型算法 ｜ 面试时间：2026 年 4 月 13 日
- 题目在小节内的位置：第 1 条
- 来源链接：https://www.nowcoder.com/discuss/923309821460221952
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
