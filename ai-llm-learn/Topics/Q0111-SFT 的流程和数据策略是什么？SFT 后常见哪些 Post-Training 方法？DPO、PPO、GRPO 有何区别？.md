---
id: Q0111
normalized_question: SFT 的流程和数据策略是什么？SFT 后常见哪些 Post-Training 方法？DPO、PPO、GRPO 有何区别？
legacy_id: Q0129
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

# SFT 的流程和数据策略是什么？SFT 后常见哪些 Post-Training 方法？DPO、PPO、GRPO 有何区别？

## 原题原文

> SFT 的核心流程以及数据构建策略，SFT 之后常见的 Post-Training 有哪些？DPO 和 PPO 区别？GRPO 有没有用过？

## 答案

### 面试直答

SFT 用高质量“输入—目标输出”教模型遵循任务；之后常见 Post-Training 包括偏好优化 DPO、基于价值/奖励的 PPO，以及组内相对奖励的 GRPO。三者核心差别是：DPO 直接学偏好对，PPO 使用 Reward Model 和 Critic 做在线策略更新，GRPO 用同题多样本的组内相对优势减少对 Critic 的依赖。

### 一、SFT 流程

数据采集→清洗去重→格式统一→质量筛选→训练/验证按来源隔离→因果语言模型 CE 训练→能力和安全回归。数据要覆盖正常、边界、拒答和工具失败，避免只训练理想答案。

> **核心小结：** SFT 决定基础行为分布，数据质量、覆盖和切分比盲目扩大数量更重要。

### 二、三种方法

| 方法 | 数据/信号 | 优点 | 代价 |
|---|---|---|---|
| DPO | chosen/rejected 偏好对 | 简单稳定、无需在线 Rollout | 受离线偏好覆盖限制 |
| PPO | Reward + Critic + 在线采样 | 可直接优化序列级目标 | 系统复杂、显存和训练成本高 |
| GRPO | 同 Prompt 多输出的相对 Reward | 可省独立 Critic | 需要多样本采样和可靠 Reward |

> **核心小结：** 没有通用最优算法；离线偏好充分可选 DPO，可验证任务和在线采样条件好时考虑 PPO/GRPO。

### 三、工程保护

监控 KL 防止策略偏离基座，使用独立安全集和隐藏测试检查 Reward Hacking；不同方法在相同采样与计算预算下比较。

> **核心小结：** Post-Training 的难点常在 Reward、数据和评估，而不只是优化器公式。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里大模型算法岗面经-02
- 面经小节：面经 05
- 岗位与面试时间：大模型算法 ｜ 面试时间：2026 年 4 月 13 日
- 题目在小节内的位置：第 3 条
- 来源链接：https://www.nowcoder.com/discuss/923309821460221952
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
