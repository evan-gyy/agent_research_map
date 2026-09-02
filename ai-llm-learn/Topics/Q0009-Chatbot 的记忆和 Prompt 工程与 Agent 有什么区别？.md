---
id: Q0009
normalized_question: Chatbot 的记忆和 Prompt 工程与 Agent 有什么区别？
legacy_id: Q0009
area: Memory / Context
knowledge_point: memory-systems
tags:
  - Memory
  - Context
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# Chatbot 的记忆和 Prompt 工程与 Agent 有什么区别？

## 原题原文

> Chatbot也可以有记忆（存聊天历史）、也可以有Prompt工程？

## 答案

### 面试直答

Chatbot 记忆主要让对话连续、个性化；Prompt 工程主要设计当前调用的指令与示例；Agent 还必须记住任务状态、工具结果、计划和外部副作用。Agent Memory 因此更强调作用域、时效、来源和可执行状态。

### 一、区别

| 维度 | Chatbot Memory | Prompt 工程 | Agent Memory |
|---|---|---|---|
| 目标 | 连续交流 | 控制当前输出 | 跨步骤完成任务 |
| 内容 | 偏好、历史事实 | 指令、示例、格式 | 计划、证据、工具状态 |
| 风险 | 错误个性化 | 指令冲突 | 重复执行、越权、状态不一致 |

> **核心小结：** Prompt 是当前输入，Memory 是可复用信息；Agent Memory 还要对真实动作负责。

### 二、工程设计

区分用户长期偏好、会话摘要和任务状态；写入前验证，读取时按用户与项目隔离，所有事实带来源和时间。支付、文件写入等副作用不能只凭 Memory 判断，应查询真实系统。

> **核心小结：** Memory 帮助模型回忆，数据库和工具才是业务事实真值。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 02
- 岗位与面试时间：AI Agent开发岗 ｜ 面试时间：2026 年 8 月 20 日
- 题目在小节内的位置：第 2 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
