---
name: interview-original-question-collector
description: Collect verified NLP and language-model interview questions from webpages into a traceable local question bank. Use when gathering, refreshing, filtering, indexing, or auditing original interview questions; exclude inferred questions and non-NLP modalities.
---

# 原题采集

目标：只把网页公开正文中明确出现的 NLP、语言模型、Agent、RAG 或 LLM 工程原题加入正式题库。本项目默认题库为 `ai-llm-learn/`。

## 流程

1. 实际打开来源网页；不能访问时停止入库并标记待复核，不得沿用旧记录冒充本轮核验。
2. 定位帖子正文，隔离推荐流、评论、热榜和侧栏；按“页面 → 面经小节 → 岗位/日期 → 原题位置”提取。
3. 保存公开正文逐条快照。遇到登录、订阅或付费边界，只采集公开内容，不绕过限制。
4. 筛选正式原题，去重后按网页顺序连续编号；题卡保留原题原文、URL、页面标题、小节、岗位/日期、位置和核验日期。
5. 更新公司索引、主题索引、网页台账和下一编号。范围外或不合格条目保留到明确归档，并写明原因。
6. 校验编号连续、原题唯一、字段齐全、索引无断链，并核对“公开条目 = 入库 + 未入库”。

## 入库规则

- 必须是网页中明确出现的原题或面试指令；不得从岗位方向、答案、上下文或相邻问题推导、改写或扩展。
- 卡内“原题原文”保持页面原句；只允许为文件名做操作系统安全化。
- 保留：NLP、语言模型、Agent/Harness、RAG、Memory/Context、Tool/MCP、LLM 训练、推理与工程。
- 保留与语言模型直接相关的 Transformer、Attention、MHA/GQA/MQA/MLA、LoRA、SFT、DPO 等基础题。
- 排除：多模态、计算机视觉、ASR/语音、会议转写、音视频模型及相关业务场景。判断有歧义时结合面经小节和前后题目，不只看关键词。
- 排除答案文本、作者叙述、无法独立理解的残句及超出题库范围的通用题；在快照中记录未入库原因。
- 网页所标公司属于来源声明；除非有独立证据，不表述为已证实该公司真实提问。
