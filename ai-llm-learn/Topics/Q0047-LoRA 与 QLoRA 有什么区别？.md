---
id: Q0047
normalized_question: LoRA 与 QLoRA 有什么区别？
legacy_id: Q0057
area: Training
knowledge_point: parameter-efficient-finetuning
tags:
  - LoRA
  - Fine-tuning
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# LoRA 与 QLoRA 有什么区别？

## 原题原文

> LoRA和QLoRA的区别？

## 答案

### 面试直答

LoRA 冻结原始权重，只训练低秩增量矩阵；QLoRA 在此基础上把冻结的基座权重量化到 4 bit，再用 LoRA 训练，从而进一步降低显存。**两者训练的 Adapter 思路相同，主要区别是基座权重的存储与计算精度。**

### 一、LoRA 原理

对原权重矩阵 $W_0in R^{d_{out}	imes d_{in}}$，不直接更新它，而是学习：

$$W=W_0+\Delta W,\qquad \Delta W=\frac{\alpha}{r}BA$$

其中 $Ain R^{r	imes d_{in}}$、$Bin R^{d_{out}	imes r}$，且 $r$ 远小于输入输出维度。训练只保存 A/B 的梯度和优化器状态。

> **核心小结：** LoRA 假设任务适配所需的权重变化可以用低秩矩阵表示。

### 二、QLoRA 增加了什么

| 维度 | LoRA | QLoRA |
|---|---|---|
| 冻结基座 | FP16/BF16 等 | 通常 4-bit NF4 |
| 可训练参数 | LoRA Adapter | LoRA Adapter |
| 显存 | 较低 | 更低 |
| 量化误差 | 无基座量化误差 | 可能存在 |
| 适用 | 资源较充足、追求稳定 | 单卡或显存紧张 |

经典 QLoRA 还使用 NF4、Double Quantization 和 Paged Optimizer 等技术；前向时量化权重会按计算需要反量化到计算 dtype，LoRA 参数仍以较高精度训练。

> **核心小结：** QLoRA 量化的是冻结基座，不是把需要学习的 LoRA 梯度也简单压成 4 bit。

### 三、工程取舍

QLoRA 能让大模型在更小显存上微调，但训练吞吐不一定更快，反量化有开销；量化误差对复杂任务可能有影响。选型要在相同数据、Rank、Context 和 Batch 下比较任务质量、峰值显存与训练时长。

> **核心小结：** QLoRA 主要优化“能不能放得下”，LoRA 更适合显存允许时追求更直接的训练路径。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 16
- 岗位与面试时间：AI Agent开发岗 ｜ 面试时间：2026 年 8 月 4 日
- 题目在小节内的位置：第 5 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
