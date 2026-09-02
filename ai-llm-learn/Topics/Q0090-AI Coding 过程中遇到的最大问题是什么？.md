---
id: Q0090
normalized_question: AI Coding 过程中遇到的最大问题是什么？
legacy_id: Q0107
area: Agent / Harness
knowledge_point: harness-coding-agent
tags:
  - Harness
  - Coding Agent
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# AI Coding 过程中遇到的最大问题是什么？

## 原题原文

> AI coding 过程中遇到的最大的问题是什么？

## 答案

### 面试直答

AI Coding 最大的问题通常不是“不会生成代码”，而是**长任务中的上下文与状态失真**：读了很多文件后忽略早期约束、修改基于过期版本、测试失败后重复尝试，最后局部代码合理但整体不满足需求。

### 一、典型表现

- 过度读取导致 Context Rot。
- 忘记用户补充要求或改动范围。
- Tool Result 截断后基于错误假设继续。
- 多 Agent 写同一文件产生语义冲突。
- 为通过单测过拟合，破坏其他行为。

> **核心小结：** Coding Agent 的难点是保持任务状态与仓库真实状态一致。

### 二、解决方式

用明确 Spec 和完成条件；任务状态外置为 Plan/To-Do；只读取必要上下文；改动使用 Worktree/Patch；每步以测试、类型和 Diff 为证据；检测无进展并重规划；压缩后重注入规则，必要时新开任务。

> **核心小结：** 可靠 AI Coding 依赖“规格—执行—验证—恢复”闭环，不是一次 Prompt 技巧。

### 三、如何衡量

统计一次通过率、回归率、无效工具调用、重复动作、人工修正量、P95 耗时和每成功任务成本。

> **核心小结：** 应衡量完整任务是否可合并，而不是模型生成了多少代码。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里大模型算法岗面经-02
- 面经小节：面经 01
- 岗位与面试时间：AI 应用研发 ｜ 面试时间：2026 年 4 月 22 日
- 题目在小节内的位置：第 4 条
- 来源链接：https://www.nowcoder.com/discuss/923309821460221952
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
