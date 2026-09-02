---
id: Q0091
normalized_question: Claude Code 的 Memory 机制如何实现？
legacy_id: Q0109
area: Memory / Context
knowledge_point: memory-systems
tags:
  - Memory
  - Context
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# Claude Code 的 Memory 机制如何实现？

## 原题原文

> Claude Code 的 memory 怎么实现的？

## 答案

### 面试直答

Claude Code 的 Memory 不是单一向量库。官方机制至少包括项目指令文件、会话 Transcript、自动记忆与压缩后重注入：稳定规则放在 `CLAUDE.md`，长会话通过 Compact 生成摘要，恢复时重新加载规则和相关 Memory；子 Agent 默认使用独立 Context。

### 一、层次

- `CLAUDE.md`：用户或项目明确维护的长期规则与约定。
- Session Transcript：支持 Resume/Continue/Fork 的完整执行记录。
- Compaction Summary：窗口满时保留目标、决策、文件、错误和下一步。
- Auto Memory：保存跨会话可复用信息，但应受作用域和用户控制。

> **核心小结：** Claude Code 将稳定规则、完整历史、压缩状态和长期记忆分开处理。

### 二、为什么这样做

`CLAUDE.md` 可在压缩后确定性重载，比只依赖摘要可靠；Transcript 用于恢复与审计；子 Agent 独立窗口减少主线程污染。具体当前实现以 Anthropic 官方文档为准，本地历史源码快照只能辅助理解调用链。

> **核心小结：** Memory 的工程价值来自分层和恢复语义，而不是“模型永远记得所有聊天”。

### 延伸阅读

- [Claude Code 模块地图](<../Agent实现拆解/Claude Code.md>)

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里大模型算法岗面经-02
- 面经小节：面经 02
- 岗位与面试时间：LLM 应用算法 ｜ 面试时间：2026 年 4 月 20 日
- 题目在小节内的位置：第 1 条
- 来源链接：https://www.nowcoder.com/discuss/923309821460221952
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
