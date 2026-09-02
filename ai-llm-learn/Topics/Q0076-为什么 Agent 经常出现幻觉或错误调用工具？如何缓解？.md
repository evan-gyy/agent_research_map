---
id: Q0076
normalized_question: 为什么 Agent 经常出现幻觉或错误调用工具？如何缓解？
legacy_id: Q0093
area: Tool / Protocol
knowledge_point: tool-reliability
tags:
  - Tool Use
  - Reliability
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 为什么 Agent 经常出现幻觉或错误调用工具？如何缓解？

## 原题原文

> 为什么 Agent 经常出现幻觉或乱调工具？怎么缓解？

## 答案

### 面试直答

Agent 工具幻觉常来自工具描述相似、Schema 含糊、上下文过载、训练分布外问题和工具错误反馈不清。缓解要从工具路由、参数约束、执行校验、错误回灌和评测共同处理，不能只说“请勿幻觉”。

### 一、措施

- 只暴露当前需要的最小工具集。
- 描述写清何时用、何时不用和关键差异。
- 使用 JSON Schema、枚举和必填字段。
- 不存在的工具名直接拒绝并返回可用候选。
- 高风险参数由业务服务二次校验和用户确认。
- 工具失败返回结构化原因，避免模型误判成功。

> **核心小结：** 工具幻觉既是模型问题，也是工具设计和 Harness 反馈问题。

### 二、评估

使用相似工具、无工具、缺参数、注入攻击和错误结果样本，测误调用率、参数合法率、首次成功率和未授权调用率。

> **核心小结：** 要专门测试“不该调用”的负例，不能只测正常成功路径。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里AI Agent开发岗面经-01
- 面经小节：面经 04
- 岗位与面试时间：AI Agent 开发 ｜ 面试时间：2026 年 7 月 14 日
- 题目在小节内的位置：第 1 条
- 来源链接：https://www.nowcoder.com/discuss/923739430513299456
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
