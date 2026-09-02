---
id: Q0021
normalized_question: 如何判断 Agent 是否能够在生产环境稳定运行？
legacy_id: Q0021
area: Reliability / Production
knowledge_point: reliability-resilience
tags:
  - Reliability
  - Resilience
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 如何判断 Agent 是否能够在生产环境稳定运行？

## 原题原文

> "你们Agent目前在生产环境稳定运行了吗？

## 答案

### 面试直答

判断 Agent 能否生产稳定运行，要同时看结果、过程、效率、可靠性和安全，并经过离线回放、故障注入、灰度和长期线上监控。平均准确率高不等于可生产，P95/P99 长尾和高风险失败更关键。

### 一、准入指标

- 任务成功、事实正确、引用/工具结果一致。
- 工具成功率、错误参数率、循环率和恢复率。
- P50/P95/P99 延迟、成本和并发容量。
- 超时、崩溃、重复副作用和降级成功率。
- 越权调用、敏感信息泄漏和 Prompt Injection 成功率。

> **核心小结：** 生产准入是多维 SLO，不是单一模型分数。

### 二、验证阶段

固定测试集→历史日志回放→依赖超时/限流故障注入→影子流量→小比例灰度→扩大。关键动作保留人工审批和 Kill Switch。

> **核心小结：** 稳定性必须在真实依赖故障和流量长尾下验证。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 05
- 岗位与面试时间：AI Agent开发岗 ｜ 面试时间：2026 年 8 月 16 日
- 题目在小节内的位置：第 4 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
