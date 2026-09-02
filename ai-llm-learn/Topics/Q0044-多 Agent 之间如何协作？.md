---
id: Q0044
normalized_question: 多 Agent 之间如何协作？
legacy_id: Q0053
area: Multi-Agent
knowledge_point: multi-agent-collaboration
tags:
  - Multi-Agent
  - Collaboration
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 多 Agent 之间如何协作？

## 原题原文

> 多智能体怎么协作？

## 答案

### 面试直答

多 Agent 协作应通过结构化任务和 Artifact，而不是互相发送无限自然语言。上游输出任务结果、证据和状态；下游只接收完成当前工作所需的信息；Orchestrator 负责依赖、冲突、超时和最终验收。

### 一、协作协议

消息至少包含 task_id、parent_id、目标、状态、Artifact 引用、证据、错误类型和下一步建议。大型文件、日志放外部存储，只传路径和摘要。

> **核心小结：** 共享的是可验证的工作成果，不是所有思考轨迹。

### 二、协作模式

- Supervisor：中心 Agent 分配并汇总，最容易控制。
- Pipeline：研究→执行→验证，适合稳定流程。
- 并行专家：独立求解后投票或由 Judge 选择。
- Blackboard：围绕共享状态协作，适合动态任务。

> **核心小结：** 模式应匹配依赖结构；不是所有任务都需要 Agent互相对话。

### 三、冲突和失败

同一资源采用单写者或租约；每个任务带幂等键和 Deadline；失败区分可重试、需重规划和永久失败；最终由规则/测试/Judge 验收。

> **核心小结：** 协作质量取决于状态一致性和验收机制，而不是消息数量。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 15
- 岗位与面试时间：AI Agent开发岗 ｜ 面试时间：2026 年 8 月 5 日
- 题目在小节内的位置：第 4 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
