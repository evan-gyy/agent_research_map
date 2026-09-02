---
id: Q0097
normalized_question: Reward 应该如何设计？模型蒸馏通常使用哪些损失函数？
legacy_id: Q0115
area: Evaluation
knowledge_point: alignment-training-distillation
tags:
  - Post-Training
  - Distillation
company: 阿里巴巴
source_track: verified-web-original
evidence: verified-page-text
verification: online-verified
collected_at: 2026-09-01
status: draft
---

# Reward 应该如何设计？模型蒸馏通常使用哪些损失函数？

## 原题原文

> Reward 怎么设计的，蒸馏的损失函数？

## 答案

### 面试直答

Reward 设计要把业务目标拆成可验证信号，并防止模型钻空子；蒸馏则让学生模型同时学习教师的软分布、标准答案和必要的中间能力。常见总损失是任务损失与蒸馏损失的加权和，而不是只模仿教师最终文本。

### 一、Reward 设计

Reward 可以组合：结果正确、格式合法、过程约束、效率和安全惩罚。代码/SQL 任务优先用测试或执行结果等可验证 Reward，主观质量再用 Judge。各项要归一化，并用隐藏测试检查 Reward Hacking。

> **核心小结：** Reward 必须与真实目标一致、可审计，并覆盖正确性之外的安全和成本。

### 二、蒸馏损失

常见形式：

$$L=alpha L_{hard}+(1-alpha)T^2 KL(p_t^T|p_s^T)+eta L_{feature}$$

其中 $L_{hard}$ 是标准标签交叉熵，KL 让学生学习教师温度 $T$ 下的软概率，$L_{feature}$ 可对齐隐藏层或注意力。生成任务还可蒸馏教师生成的高质量轨迹，但要过滤错误和风格噪声。

> **核心小结：** 硬标签教“答案是什么”，软标签教类别或 Token 间相对关系，中间层损失教表示方式。

### 三、工程验证

在相同数据、推理预算下比较学生基线、仅 SFT、Logit 蒸馏和轨迹蒸馏；同时看准确率、校准、延迟和显存。Reward 模型也要单独测与人工偏好的一致率和分布外鲁棒性。

> **核心小结：** Reward 和蒸馏都需要独立评测，不能用训练目标本身证明成功。

## 问题来源

- 公司：阿里巴巴
- 页面标题：阿里面经-阿里大模型算法岗面经-02
- 面经小节：面经 02
- 岗位与面试时间：LLM 应用算法 ｜ 面试时间：2026 年 4 月 20 日
- 题目在小节内的位置：第 7 条
- 来源链接：https://www.nowcoder.com/discuss/923309821460221952
- 在线核验：2026-09-01 已在公开网页正文中逐条核验
- 证据级别：网页公开正文原文
