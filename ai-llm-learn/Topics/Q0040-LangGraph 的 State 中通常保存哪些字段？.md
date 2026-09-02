---
id: Q0040
normalized_question: LangGraph 的 State 中通常保存哪些字段？
legacy_id: Q0049
area: Agent / Harness
knowledge_point: workflow-state-orchestration
tags:
  - Workflow
  - State
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# LangGraph 的 State 中通常保存哪些字段？

## 原题原文

> LangGraph中的state保存了哪些字段?

## 答案

### 面试直答

LangGraph State 应保存节点间真正需要共享、可序列化和可恢复的信息，例如消息、用户请求、计划、任务状态、工具结果引用、错误、重试次数和最终输出；不要塞数据库连接、大文件正文或不可序列化客户端。

### 一、字段示例

- messages：对话或模型消息，配合 Reducer 追加。
- request/user_context：规范化请求和权限作用域。
- plan/tasks：子任务、依赖和状态。
- evidence_refs：工具结果 ID/路径，不一定存全文。
- error/retry_count/deadline：可靠性控制。
- final_answer：最终结构化输出。

> **核心小结：** State 是可恢复的控制面数据，不是进程内所有对象的垃圾箱。

### 二、设计原则

字段用 TypedDict/Pydantic 明确定义；并行写同一字段配置 Reducer；大对象外置；记录 Schema Version；区分持久业务事实与临时派生值。

> **核心小结：** State 越小、边界越清晰，Checkpoint、并行合并和回放越可靠。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 14
- 岗位与面试时间：AI Agent开发岗 ｜ 面试时间：2026 年 8 月 5 日
- 题目在小节内的位置：第 3 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
