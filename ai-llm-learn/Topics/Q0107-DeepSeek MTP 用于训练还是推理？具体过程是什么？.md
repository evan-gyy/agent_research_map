---
id: Q0107
normalized_question: DeepSeek MTP 用于训练还是推理？具体过程是什么？
legacy_id: Q0125
area: Model / Inference
knowledge_point: inference-optimization
tags:
  - Inference
  - Optimization
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# DeepSeek MTP 用于训练还是推理？具体过程是什么？

## 原题原文

> DeepSeek-MTP 是用在训练阶段还是推理阶段的，具体过程是怎样的？

## 答案

### 面试直答

DeepSeek-V3 的 MTP（Multi-Token Prediction）**首先是预训练阶段的辅助训练目标**：在每个位置除预测下一个 Token，还用顺序的 MTP 模块预测后续多个 Token，以增加训练信号和规划能力。训练完成后，MTP 模块可以丢弃；也可以在推理时保留，用作 Speculative Decoding 的 Draft 预测来加速。所以它不是纯训练或纯推理二选一。

### 一、训练过程

主模型先得到当前位置的隐藏状态。第 $k$ 个 MTP 模块结合前一模块状态与第 $k$ 个未来 Token 的 Embedding，经过投影和 Transformer Block，预测再后一个 Token。多个深度的交叉熵损失按权重加入主 Next-Token Loss：

$$L=L_{NTP}+\lambda\sum_{k=1}^{D}L_{MTP}^{(k)}$$

其中 $D$ 是预测深度。各 MTP 模块顺序预测，Embedding 和输出 Head 可与主模型共享；训练时辅助损失的权重可以随训练阶段调整。

> **核心小结：** MTP 在预训练中让每个位置提供多个未来 Token 的监督，但主模型的标准下一个 Token 目标仍然存在。

### 二、推理时怎么用

```mermaid
flowchart LR
 H[主模型当前状态] --> D1[MTP1 提议 token t+1]
 D1 --> D2[MTP2 提议 token t+2]
 D2 --> V[主模型并行验证候选]
 V --> A[接受正确前缀]
 A --> N[继续解码]
```

若部署保留 MTP 模块，它们可以一次提议多个未来 Token，再由主模型验证；接受率高时减少串行解码步数。这属于 Speculative Decoding 思路，最终分布由验证保证。若系统未实现相应 Kernel 或接受率低，额外 Draft/验证成本可能抵消收益，因此部署也可以只使用训练后的主模型。

> **核心小结：** MTP 的质量增益来自训练目标，推理加速取决于是否部署并有效利用 MTP Draft Head。

### 三、与一次输出多个 Token 的区别

MTP 训练不是让标准自回归模型不经验证地同时吐出多个 Token；它构造多个未来预测头增加监督。推理阶段也需要验证候选，不能把所有预测直接视为最终输出。

> **核心小结：** “预测多个”不等于“无条件接受多个”，训练辅助头和推理解码协议是两件事。

### 来源

- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)
- [DeepSeek-V3 GitHub](https://github.com/deepseek-ai/DeepSeek-V3)

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里大模型算法岗面经-02
- 面经小节：面经 04
- 岗位与面试时间：大模型算法 ｜ 面试时间：2026 年 4 月 15 日
- 题目在小节内的位置：第 5 条
- 来源链接：https://www.nowcoder.com/discuss/923309821460221952
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
