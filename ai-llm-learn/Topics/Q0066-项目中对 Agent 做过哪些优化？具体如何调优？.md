---
id: Q0066
normalized_question: 项目中对 Agent 做过哪些优化？具体如何调优？
legacy_id: Q0083
area: Reliability / Production
knowledge_point: reliability-resilience
tags:
  - Reliability
  - Resilience
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 项目中对 Agent 做过哪些优化？具体如何调优？

## 原题原文

> 项目过程中针对 Agent 做过哪些优化？具体怎么调优？

## 答案

### 面试直答

项目优化应按瓶颈分层回答，而不是罗列 Prompt 技巧。以旅行 Agent 为例，可从规划、并行工具、Judge、Memory、SSE 和容错说明；具体收益数字必须来自真实压测和评测报告。

### 一、可确认的优化方向

- Planner 流式产生子目标，Executor 对独立旅行技能并行执行。
- Memory 在请求开始异步加载，与前置处理重叠。
- Judge 检查必需信息，避免无边界探索。
- Summary 与内容校验分离，SSE 降低感知等待。
- 工具超时、部分失败和重规划设置总体预算。

> **核心小结：** 优化围绕减少串行模型轮次、提高工具并发和控制回路长度。

### 二、如何证明

逐项做消融：串行 vs 并行、无 Judge vs 有 Judge、同步 vs 异步 Memory；在同一 Query 集比较任务成功率、P95 延迟、工具调用数和成本。没有真实结果时明确说需要补压测数据。

> **核心小结：** 优化结论必须有基线、单变量和预算一致的对照。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里AI Agent开发岗面经-01
- 面经小节：面经 03
- 岗位与面试时间：AI Agent 开发 ｜ 面试时间：2026 年 8 月 5 日
- 题目在小节内的位置：第 2 条
- 来源链接：https://www.nowcoder.com/discuss/923739430513299456
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
