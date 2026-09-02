---
id: Q0006
normalized_question: 如何处理大量工具描述导致的 Prompt 过长问题？
legacy_id: Q0006
area: Tool / Protocol
knowledge_point: context-token-compression
tags:
  - Context
  - Token
company: 字节跳动
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 如何处理大量工具描述导致的 Prompt 过长问题？

## 原题原文

> 如何处理大量工具描述导致 Prompt 过长？

## 答案

### 面试直答

大量工具描述导致 Prompt 过长时，不应把所有完整 Schema 每轮都塞给模型。我会采用**工具分组路由、按需加载 Schema、压缩描述、子 Agent 隔离和缓存**，并用工具选择正确率与 Token/延迟共同评估。

### 一、分层加载

先只暴露工具名、用途和路由标签；模型或规则确定领域后，再加载相关工具的完整参数 Schema。Claude Code 的 MCP Tool Search 就体现这种按需发现思路。

> **核心小结：** 先选工具集合，再选具体工具，避免工具数量线性占满 Context。

### 二、工程方法

- 合并重复工具，描述聚焦“何时用/何时不用”。
- Schema 使用枚举和引用，删除冗长示例但保留约束。
- 按业务域、权限和当前状态预过滤。
- 独立子 Agent 只拿完成任务所需的最小工具集。
- 静态工具前缀保持稳定，提高 Prompt Cache 命中。

> **核心小结：** Token 优化不能牺牲参数约束，否则会以错误调用率偿还成本。

### 三、评估

构造相似工具、无可用工具和跨域任务，测 Top-1 选择率、参数合法率、无效调用率、输入 Token、P95 延迟和缓存命中率。

> **核心小结：** 最优方案是在相同工具正确率下减少 Context，而不是单纯缩短描述。

## 问题来源

- 公司：字节跳动
- 页面标题：字节面经-字节跳动AI Agent开发岗面经-01
- 面经小节：面经 01
- 岗位与面试时间：AI Agent 开发 ｜ 面试时间：2026 年 8 月 20 日
- 题目在小节内的位置：第 6 条
- 来源链接：https://www.nowcoder.com/discuss/922659050167226368
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
