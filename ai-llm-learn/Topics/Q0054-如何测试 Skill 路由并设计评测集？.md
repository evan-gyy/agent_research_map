---
id: Q0054
normalized_question: 如何测试 Skill 路由并设计评测集？
legacy_id: Q0065
area: Agent Application
knowledge_point: intent-routing
tags:
  - Intent
  - Routing
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 如何测试 Skill 路由并设计评测集？

## 原题原文

> skill路由测试你是怎么测试和设计测试集的

## 答案

### 面试直答

Skill 路由评测要同时测试“该调用时选对、不该调用时克制、参数和权限正确”。数据集覆盖单 Skill、多 Skill、相似 Skill、无 Skill、缺参数、冲突约束和对抗输入，并保存标准路由与预期结果。

### 一、指标

- Skill Top-1/Top-K 准确率和 Macro-F1。
- No-tool/Unknown 拒识率。
- 参数 Schema 合法率和必填字段完整率。
- 端到端任务成功率、错误调用成本和延迟。
- 高风险 Skill 未授权调用率必须接近零。

> **核心小结：** 路由正确不只看工具名，还要看是否该调用、参数和最终结果。

### 二、评测集

从真实日志分层抽样，补充相似描述困难负例和新版本回归；按 Query 而不是同模板随机切分，避免泄漏。每次修改 Skill 描述或路由模型都跑固定集和线上灰度。

> **核心小结：** 好评测集必须包含容易误路由和本应拒绝调用的样本。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 19
- 岗位与面试时间：AI Agent开发岗 ｜ 面试时间：2026 年 7 月 30 日
- 题目在小节内的位置：第 2 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
