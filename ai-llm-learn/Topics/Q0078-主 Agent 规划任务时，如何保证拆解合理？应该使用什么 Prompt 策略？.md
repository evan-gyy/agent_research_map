---
id: Q0078
normalized_question: 主 Agent 规划任务时，如何保证拆解合理？应该使用什么 Prompt 策略？
legacy_id: Q0095
area: Agent / Harness
knowledge_point: planning-task-decomposition
tags:
  - Planning
  - Task Decomposition
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# 主 Agent 规划任务时，如何保证拆解合理？应该使用什么 Prompt 策略？

## 原题原文

> 主 Agent 做任务规划时，怎么保证拆解步骤合理？用的哪种 Prompt 策略？

## 答案

### 面试直答

保证主 Agent 拆解合理，不能只靠一句“请逐步思考”。应给 Planner 结构化目标、约束、可用能力和输出 Schema，再由代码校验依赖、覆盖、冲突和预算；执行中根据真实结果有限重规划。

### 一、好的计划结构

每个子任务包含 id、goal、dependencies、allowed_tools、inputs、expected_output、success_criteria、priority 和 budget。Planner 还要输出全局完成条件和不应执行的范围。

> **核心小结：** 合理计划必须可调度、可验证，而不只是自然语言步骤看起来顺畅。

### 二、Prompt 策略

使用任务分解 Prompt：先复述目标和硬约束，再识别独立子目标与依赖，优先并行无依赖任务，最后以 JSON Schema 输出。提供少量覆盖“多意图、缺信息、工具不可用”的示例，比堆通用 CoT 更有效。

```text
目标与完成标准 → 约束/未知项 → 子任务及依赖
→ 工具与输入 → 预期证据 → 失败/回退 → 结构化计划
```

> **核心小结：** Prompt 负责引导语义拆解，Schema 和 Validator 负责阻止不可执行计划。

### 三、验证和重规划

代码检测环依赖、重复任务、未覆盖约束、写冲突和超预算；Judge 检查结果是否满足 must 信息。重规划只针对失败或缺失节点，并限制次数和总 Deadline。

Dynamic Planner 的 Planner、并行 Executor 和 Judge 就是这种受控方案，但其效果仍需与单轮或固定 Workflow 在同一预算下比较。

> **核心小结：** 规划质量来自 Prompt、结构校验、执行反馈和有限重规划的组合。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里AI Agent开发岗面经-01
- 面经小节：面经 04
- 岗位与面试时间：AI Agent 开发 ｜ 面试时间：2026 年 7 月 14 日
- 题目在小节内的位置：第 3 条
- 来源链接：https://www.nowcoder.com/discuss/923739430513299456
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
