---
id: Q0084
normalized_question: 多 Agent 协作有哪些常见模式？
legacy_id: Q0101
area: Multi-Agent
knowledge_point: multi-agent-collaboration
tags:
  - Multi-Agent
  - Collaboration
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 多 Agent 协作有哪些常见模式？

## 原题原文

> 多 Agent 协作常见模式有哪些？

## 答案

### 面试直答

常见多 Agent 模式包括 Supervisor、Pipeline、并行专家/投票、Planner-Executor-Judge、Blackboard 以及去中心化协商。生产中最常用的是中心化编排，因为任务状态、权限和预算更容易控制。

### 一、模式对比

| 模式 | 适合场景 | 主要代价 |
|---|---|---|
| Supervisor | 动态分工和统一汇总 | 中心瓶颈 |
| Pipeline | 稳定阶段流程 | 上游错误传播 |
| 并行专家 | 多方案、研究和验证 | 成本高、需仲裁 |
| Planner-Executor-Judge | 可拆分复杂任务 | 多模型轮次 |
| Blackboard | 动态共享问题空间 | 状态一致性复杂 |
| 去中心化协商 | 角色自治 | 通信爆炸、难审计 |

> **核心小结：** 模式差异本质是控制权、共享状态和通信拓扑不同。

### 二、选型

先看任务是否能拆分、子任务是否独立、是否有强 SLA 和写冲突。低延迟业务倾向中心 Planner + 并行 Executor；开放研究可用并行专家；固定流程优先 Workflow。

> **核心小结：** 能用简单 Workflow 解决时，不要为了“多 Agent”增加协作层。

### 三、共同保护

所有模式都需要任务 ID、依赖、最小权限、预算、超时、幂等、Artifact 引用和最终验收。没有这些，多 Agent 只是多个不受控的对话。

> **核心小结：** 协作模式决定组织形式，Harness 决定系统能否稳定运行。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里AI Agent开发岗面经-01
- 面经小节：面经 04
- 岗位与面试时间：AI Agent 开发 ｜ 面试时间：2026 年 7 月 14 日
- 题目在小节内的位置：第 9 条
- 来源链接：https://www.nowcoder.com/discuss/923739430513299456
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
