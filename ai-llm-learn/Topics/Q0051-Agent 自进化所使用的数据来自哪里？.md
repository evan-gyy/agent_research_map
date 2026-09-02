---
id: Q0051
normalized_question: Agent 自进化所使用的数据来自哪里？
legacy_id: Q0061
area: Agent / Harness
knowledge_point: agent-self-evolution
tags:
  - Self-Evolution
  - Agent
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# Agent 自进化所使用的数据来自哪里？

## 原题原文

> 用于做agent自进化的数据从哪来的？

## 答案

### 面试直答

Agent 自进化数据主要来自真实任务轨迹、失败与人工纠正、离线仿真、评测集和工具执行反馈。数据必须脱敏、去重、标注来源，并防止把模型自己的错误输出未经验证地循环训练。

### 一、数据来源

- 成功轨迹：目标、动作、工具结果和验证证据。
- 失败轨迹：超时、错误工具、路径震荡和用户纠正。
- 人工示范：高风险或复杂任务的标准处理。
- 可执行反馈：测试、编译、SQL 执行和规则校验。
- 合成任务：补足长尾，但需真实分布校准。

> **核心小结：** 失败和纠正往往比最终成功文本更能提供改进信号。

### 二、数据治理

按用户和项目授权采集，删除凭据与个人信息；按时间和任务切分训练/测试，避免同一轨迹泄漏；保留模型、Prompt、工具版本和结果证据。只有通过外部验证的轨迹进入训练或 Skill 候选库。

> **核心小结：** 自进化数据首先是数据治理问题，其次才是训练或 Prompt 优化问题。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 18
- 岗位与面试时间：AI Agent开发岗 ｜ 面试时间：2026 年 7 月 31 日
- 题目在小节内的位置：第 3 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
