---
id: Q0079
normalized_question: 子 Agent 之间如何传递上下文？
legacy_id: Q0096
area: Memory / Context
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

# 子 Agent 之间如何传递上下文？

## 原题原文

> 子 Agent 之间的上下文怎么传递？

## 答案

### 面试直答

子 Agent 之间传递上下文应遵循“最小充分”原则：通过 Orchestrator 传递任务目标、硬约束、输入 Artifact、关键证据和验收标准，而不是复制父会话全部历史。大内容保存在文件或对象存储中，通过 ID/路径引用。

### 一、上下文包

```text
Task: 要完成什么
Constraints: 权限、范围、Deadline
Inputs: 文件/数据/上游 Artifact
Decisions: 已确认的关键决策
Evidence: 来源与置信度
Output Contract: 返回格式和验收标准
```

> **核心小结：** 上下文传递的目标是让接收者独立完成任务，而不是复刻发送者的整个 Context。

### 二、传递方式

短信息用结构化消息；大日志和文档用引用；稳定规则从项目级配置重新加载；跨会话长期偏好从有权限的 Memory 召回。结果返回时附证据和 Artifact，而不是只给一句结论。

> **核心小结：** 控制面传元数据，数据面传 Artifact 引用，可以降低 Token 和串扰。

### 三、风险

摘要会丢细节，因此保留原始来源；不同 Agent 版本可能理解 Schema 不同，需要版本字段；用户和任务作用域必须隔离，防止跨租户泄漏。

> **核心小结：** 上下文压缩、可回溯性和权限隔离必须同时设计。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里AI Agent开发岗面经-01
- 面经小节：面经 04
- 岗位与面试时间：AI Agent 开发 ｜ 面试时间：2026 年 7 月 14 日
- 题目在小节内的位置：第 4 条
- 来源链接：https://www.nowcoder.com/discuss/923739430513299456
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
