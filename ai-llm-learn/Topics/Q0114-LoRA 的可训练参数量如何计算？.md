---
id: Q0114
normalized_question: LoRA 的可训练参数量如何计算？
legacy_id: Q0132
area: Training
knowledge_point: parameter-efficient-finetuning
tags:
  - LoRA
  - Fine-tuning
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# LoRA 的可训练参数量如何计算？

## 原题原文

> LoRA 参数更新量的计算？

## 答案

### 面试直答

LoRA 将一个 $d_{out}	imes d_{in}$ 的权重更新替换为两个低秩矩阵：$Ain R^{r	imes d_{in}}$ 和 $Bin R^{d_{out}	imes r}$。因此该层可训练参数量是：

$$N_{LoRA}=r(d_{in}+d_{out})$$

而全量微调该层需要 $d_{in}d_{out}$ 个参数。若有 Bias 或额外模块可训练，再单独加上。

### 一、单层示例

假设线性层 $W$ 为 $4096	imes4096$，Rank $r=8$：

- 全量参数：$4096	imes4096=16,777,216$；
- LoRA 参数：$8	imes(4096+4096)=65,536$；
- 比例约为 $0.39\%$。

缩放系数 $\alpha/r$ 不增加可训练参数。Dropout 同样没有可训练参数。

> **核心小结：** LoRA 将乘法规模的权重更新变成 Rank 乘输入输出维度之和。

### 二、整个 Transformer 怎么算

对每个被注入的线性层求和：

$$N_{total}=\sum_{l\in target}r_l(d_{in,l}+d_{out,l})$$

例如只给 Attention 的 $W_Q$、$W_V$ 加 LoRA，就只计算这两类矩阵乘层数；如果 Q/K/V/O 和 MLP 都注入，参数会明显增加。GQA/MQA 中 K/V 投影输出维度可能小于 Q，不能统一假设都是 $d_{model}	imes d_{model}$。

> **核心小结：** 总参数量取决于目标模块、每层实际形状、Rank 和层数，不能只用一个公式乘“四个投影”。

### 三、参数量不等于全部显存

训练显存还包括 LoRA 梯度、优化器状态、激活和冻结基座权重。QLoRA 主要通过量化冻结基座降低显存，但 LoRA 可训练参数公式本身不变。

> **核心小结：** LoRA 参数少能降低梯度和优化器开销，峰值显存仍可能被激活或基座权重主导。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里大模型算法岗面经-02
- 面经小节：面经 06
- 岗位与面试时间：大模型算法 ｜ 面试时间：2026 年 4 月 12 日
- 题目在小节内的位置：第 1 条
- 来源链接：https://www.nowcoder.com/discuss/923309821460221952
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
