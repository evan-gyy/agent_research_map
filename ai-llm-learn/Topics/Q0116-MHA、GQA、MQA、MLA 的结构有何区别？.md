---
id: Q0116
normalized_question: MHA、GQA、MQA、MLA 的结构有何区别？
legacy_id: Q0134
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

# MHA、GQA、MQA、MLA 的结构有何区别？

## 原题原文

> MHA、GQA、MQA、MLA 的结构？

## 答案

### 面试直答

MHA、GQA、MQA、MLA 的主要差别在 K/V 如何共享与压缩。MHA 每个 Query Head 有独立 K/V，质量强但 KV Cache 最大；MQA 所有 Query Head 共享一组 K/V，最省 Cache；GQA 让若干 Query Head 共享一组 K/V，在质量和效率间折中；MLA 将 K/V 表示压缩到低维潜变量，推理时从潜表示恢复所需成分。

### 一、结构对比

| 结构 | Query Heads | KV Heads/表示 | KV Cache | 特点 |
|---|---:|---|---|---|
| MHA | $h$ | $h$ 组 | 最大 | 表达充分 |
| GQA | $h$ | $g<h$ 组 | 较小 | 常用折中 |
| MQA | $h$ | 1 组 | 最小 | 吞吐高，可能损失质量 |
| MLA | 多头 | 低秩潜表示 | 显著压缩 | 结构更复杂 |

KV Cache 大致与层数、序列长度、KV Head 数和 Head Dim 成正比，因此减少 KV Head 或压缩潜表示能直接降低显存与带宽。

> **核心小结：** 四者主要是在保持多 Query 表达能力的同时，减少历史 K/V 的存储和读取。

### 二、工程选型

长上下文和高并发服务更关注 Cache，常用 GQA/MQA/MLA；追求最强质量且资源充足可用 MHA。MLA 的收益依赖配套训练和推理 Kernel，不能只在已有 MHA 权重上无成本替换。

> **核心小结：** 结构选型要同时看模型质量、KV Cache、内存带宽和推理框架支持。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里大模型算法岗面经-02
- 面经小节：面经 06
- 岗位与面试时间：大模型算法 ｜ 面试时间：2026 年 4 月 12 日
- 题目在小节内的位置：第 3 条
- 来源链接：https://www.nowcoder.com/discuss/923309821460221952
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
