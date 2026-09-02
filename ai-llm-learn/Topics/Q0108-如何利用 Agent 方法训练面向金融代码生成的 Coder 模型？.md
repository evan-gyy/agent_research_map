---
id: Q0108
normalized_question: 如何利用 Agent 方法训练面向金融代码生成的 Coder 模型？
legacy_id: Q0126
area: Agent Application
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

# 如何利用 Agent 方法训练面向金融代码生成的 Coder 模型？

## 原题原文

> 在现有大模型的基础上，如何通过 agent 的相关方法，训练一个 coder 模型，撰写金融领域相关模型的代码？

## 答案

### 面试直答

用 Agent 方法训练金融 Coder，不是让 Agent 自己随意改权重，而是用 Agent 生成和验证高质量训练轨迹：规划需求、检索金融规范、生成代码、运行测试/静态检查、根据错误修复，再把成功轨迹和失败对比转成 SFT、偏好或强化学习数据。

### 一、数据闭环

```mermaid
flowchart LR
 T[金融编码任务] --> P[Agent规划]
 P --> K[检索规范/API]
 K --> C[生成代码]
 C --> X[沙箱测试/风控检查]
 X -- 失败 --> C
 X -- 成功 --> D[轨迹清洗]
 D --> S[SFT/偏好/RL]
 S --> E[独立评测]
```

金融代码需要加入数值精度、时区、权限、审计和禁止真实交易等约束。测试环境使用脱敏数据和模拟接口，不能让训练 Agent 访问生产账户。

> **核心小结：** Agent 的价值是生成“带验证的过程数据”，沙箱和可执行测试负责质量闭环。

### 二、训练与评估

成功轨迹用于 SFT；同题好坏代码对用于 DPO；可验证单测、编译和安全扫描可作为 RL Reward。评估不仅看 Pass@k，还看金融规则正确率、安全违规率、修复轮次和 Token 成本。

> **核心小结：** 训练信号应尽量来自可执行验证，模型 Judge 只补充难以形式化的可读性和设计质量。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里大模型算法岗面经-02
- 面经小节：面经 04
- 岗位与面试时间：大模型算法 ｜ 面试时间：2026 年 4 月 15 日
- 题目在小节内的位置：第 6 条
- 来源链接：https://www.nowcoder.com/discuss/923309821460221952
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
