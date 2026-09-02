---
id: Q0089
normalized_question: 你使用过哪些 Agent 产品？其中哪些设计令人印象深刻？
legacy_id: Q0106
area: Agent Application
knowledge_point: agent-architecture-core
tags:
  - Agent
  - Architecture
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 你使用过哪些 Agent 产品？其中哪些设计令人印象深刻？

## 原题原文

> 有没有用过市面上一些 agent 产品，印象最深刻的设计有哪些？

## 答案

### 面试直答

如果按当前项目材料回答，我重点关注三类 Agent：**Codex 代表开放式 Coding Agent Harness，Claude Code 代表成熟的工具循环与 Context/Hook 体系，Dynamic Planner 代表低延迟旅行业务 Agent。** 它们最有价值的差异不是模型品牌，而是如何在不同约束下分配控制权。

### 一、三个系统的亮点

| 系统 | 令人印象深刻的设计 | 解决的问题 |
|---|---|---|
| Codex | Thread/Turn/Item 协议、沙箱审批、Resume/Fork、app-server | 将 Agent Loop 嵌入不同产品并可观测运行 |
| Claude Code | 多级压缩、Tool Search、Hooks、独立子 Agent Context | 长任务上下文和企业控制 |
| Dynamic Planner | Planner + 并行 Executor + Judge + Summary | 旅行多意图下兼顾低延迟与结果充分性 |

Codex 把命令、文件修改和工具调用做成结构化事件，宿主应用可以展示进度并响应审批；Claude Code 不只在窗口满时摘要，还通过微压缩、规则重注入、工具延迟加载和子 Agent 隔离共同管理 Context。

> **核心小结：** 成熟 Agent 的差距往往来自 Harness：状态、工具、权限、Context 和可观测性，而不仅是模型推理能力。

### 二、为什么不能直接照搬

Coding Agent 可以接受更长时间探索，并通过测试验证；移动端旅行 Agent 更强调首屏耗时和稳定结构，不能照搬开放式多轮 ReAct。Dynamic Planner 先规划一次并行调用技能，更适合子目标相对稳定的业务，但灵活性不如 Coding Agent。

> **核心小结：** 好设计必须与任务开放度、延迟、风险和验证方式匹配。

### 三、表达建议

回答“使用过哪些产品”时，应只说真实使用深度：日常使用、源码研究和仅体验要分开。每个产品给一个具体任务和一个不足，例如 Codex 的长任务控制强但开放探索成本波动；Claude Code 的扩展面丰富但 Context 与权限配置更复杂；业务 Agent 延迟稳定但泛化范围更窄。

> **核心小结：** 用“任务—机制—收益—代价”讲体验，比罗列产品名称更可信。

### 延伸阅读

- [Codex 模块地图](<../Agent实现拆解/Codex.md>)
- [Claude Code 模块地图](<../Agent实现拆解/Claude Code.md>)

### 常见追问

- **你最想借鉴什么？** 我会优先借鉴结构化事件、子任务 Context 隔离和分层评估，而不是直接复制 UI。
- **哪个 Agent 最好？** 没有脱离场景的最好；Coding、低延迟查询和高风险业务需要不同控制结构。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里大模型算法岗面经-02
- 面经小节：面经 01
- 岗位与面试时间：AI 应用研发 ｜ 面试时间：2026 年 4 月 22 日
- 题目在小节内的位置：第 3 条
- 来源链接：https://www.nowcoder.com/discuss/923309821460221952
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
