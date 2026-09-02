---
id: Q0094
normalized_question: BIRD 数据集和 DB-BIRD Reward 模型分别是什么？
legacy_id: Q0112
area: Evaluation
knowledge_point: evaluation-metrics-datasets
tags:
  - Evaluation
  - Dataset
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# BIRD 数据集和 DB-BIRD Reward 模型分别是什么？

## 原题原文

> Bird 数据集和 DB-Bird reward 模型了解吗？

## 答案

### 面试直答

BIRD 是公开的 Text-to-SQL 基准；但我没有在 BIRD 官方资料或公开论文中找到正式名为“DB-BIRD Reward Model”的对象，不能把它当成已确认专名。回答时应先澄清提问者是否指 **BIRD 的 R-VES 指标、BIRD-Critic，还是泛指数据库任务的 Reward Model**，再分别说明。

### 一、BIRD 数据集

BIRD 全称 Big Bench for Large-scale Database Grounded Text-to-SQL Evaluation，关注真实数据库内容对 Text-to-SQL 的影响。官方公开信息包括：

- 超过 12,751 个 Question-SQL Pair；
- 95 个大型数据库，总规模约 33.4 GB；
- 覆盖 37 个以上专业领域；
- 特别考察外部知识、数据库脏值和 SQL 执行效率。

核心评测不是 SQL 字符串是否完全相同，而是执行后结果是否正确；效率可结合 VES/R-VES 等指标分析。

> **核心小结：** BIRD 测的是模型在大型、真实、带脏数据和领域知识的数据库上生成正确且有效率 SQL 的能力。

### 二、“DB-BIRD Reward Model”的名称歧义

截至本题核验，没有找到 BIRD 官方定义的同名模型。它可能是原始记录中的简称或混淆：

- **R-VES**：BIRD Mini-Dev 提出的 Reward-based Valid Efficiency Score，是评测指标，不是 Reward Model。
- **BIRD-Critic**：考察模型发现和修复数据库应用或 SQL 问题的 Benchmark，也不等同于名为 DB-BIRD 的 Reward Model。
- **数据库任务 Reward Model**：给候选 SQL、执行轨迹或答案打分的通用模型，可能用于候选排序或强化学习，但具体结构必须以提问者所指论文或项目为准。

> **核心小结：** 面对无法核验的专名，应先澄清对象，不能把通用 Reward Model 机制冒充成 BIRD 官方组件。

### 三、如果对方指数据库 Reward Model

可以继续回答：Reward 应优先使用可执行信号，例如 SQL 是否可运行、执行结果是否正确、是否越权、效率是否达标；模型评分只补充 Schema 对齐和语义质量。不同 SQL 可能等价，所以不能只比较文本。训练/测试还要按数据库切分，防止 Schema 泄漏，并用隐藏用例检查 Reward Hacking。

> **核心小结：** 数据库 Reward 最可靠的基础是安全沙箱中的真实执行，模型 Judge 只能作为辅助信号。

### 常见追问

- **为什么不能只用 Exact Match？** SQL 存在多种语义等价写法，执行正确性更接近真实目标。
- **R-VES 是什么？** 它是兼顾有效性与执行效率的 Reward-based 指标，不是训练 Reward Model 的专名。

### 核验来源

- [BIRD 官方网站](https://bird-bench.github.io/)

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里大模型算法岗面经-02
- 面经小节：面经 02
- 岗位与面试时间：LLM 应用算法 ｜ 面试时间：2026 年 4 月 20 日
- 题目在小节内的位置：第 4 条
- 来源链接：https://www.nowcoder.com/discuss/923309821460221952
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
