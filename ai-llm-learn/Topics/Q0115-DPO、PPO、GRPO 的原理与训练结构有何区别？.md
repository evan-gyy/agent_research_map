---
id: Q0115
normalized_question: DPO、PPO、GRPO 的原理与训练结构有何区别？
legacy_id: Q0133
area: Training
knowledge_point: alignment-training-distillation
tags:
  - Post-Training
  - Distillation
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# DPO、PPO、GRPO 的原理与训练结构有何区别？

## 原题原文

> DPO、PPO、GRPO 的结构？

## 答案

### 面试直答

DPO、PPO、GRPO 都用于让模型偏向更好的回答，但训练结构不同：DPO 是离线偏好分类式目标；PPO 是 Actor-Critic 在线强化学习；GRPO 通过同一问题的一组回答计算相对优势，通常不训练独立 Critic。

### 一、核心原理

DPO 直接提高 chosen 相对 rejected 的对数概率差，并用参考模型限制漂移：

$$L_{DPO}=-logsigma(eta[(logpi_	heta(y^+|x)-logpi_{ref}(y^+|x))-(logpi_	heta(y^-|x)-logpi_{ref}(y^-|x))])$$

PPO 用 Reward Model 得到回报、Critic 估计优势，再用 Clip 限制策略更新。GRPO 对同一 Prompt 采样一组答案，将每个 Reward 相对组均值标准化作为优势，再加 KL 约束。

> **核心小结：** DPO 比较成对偏好，PPO 依赖价值估计，GRPO 依赖组内相对比较。

### 二、结构对比

| 方法 | 需要在线 Rollout | Reward Model | Critic | 主要风险 |
|---|---|---|---|---|
| DPO | 否 | 偏好数据隐式提供 | 否 | 数据分布固定 |
| PPO | 是 | 通常需要 | 是 | 训练不稳定、成本高 |
| GRPO | 是 | 规则或模型 Reward | 通常不需要 | 多采样成本、组内偏差 |

> **核心小结：** GRPO 省的是 Critic，不是采样和 Reward；DPO 省在线 RL，但不能探索数据外行为。

### 三、选型

对话偏好数据成熟、资源有限时选 DPO；复杂不可执行偏好且基础设施完整可用 PPO；数学、代码等可验证任务适合 GRPO，但必须防止模型利用 Reward 漏洞。

> **核心小结：** 选型依据是反馈形式、可验证性和计算预算，不应只看算法热度。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里大模型算法岗面经-02
- 面经小节：面经 06
- 岗位与面试时间：大模型算法 ｜ 面试时间：2026 年 4 月 12 日
- 题目在小节内的位置：第 2 条
- 来源链接：https://www.nowcoder.com/discuss/923309821460221952
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
