# Agent Career Research OS

不是"AI 论文收藏夹"，而是一套**以求职/能力要求为目标，自动构建个人 Agent 学习路线的 Research Agent**。

核心闭环：

```
          招聘市场
             │
      ┌──────┴──────┐
      ↓             ↓
     JD            面经
      │             │
      └──────┬──────┘
             ↓
       Skill / Topic Extractor
             ↓
      ┌───────────────┐
      │ Agent 能力地图 │  ← config/knowledge_map.yaml (60 个 Topic)
      └───────┬───────┘
              ↓
       Knowledge Gap     ← data/personal/skill_profile.yaml
              ↓
      Paper / Blog / GitHub  ← data/seed_materials.yaml (49 篇)
              ↓
        学习 & 面试          ← data/interview_questions.yaml
              ↓
       新 JD / 新面经
              ↺
```

## 项目结构

```
agent_research_map/
├── config/
│   └── knowledge_map.yaml          # 知识树（10 领域，60 Topic）— 系统骨架
├── data/
│   ├── seed_materials.yaml         # 49 篇经典种子材料
│   ├── interview_questions.yaml    # 面试题库（含 answer keys）
│   ├── market/
│   │   ├── jd/                     # 招聘信息（YAML，按 Topic 结构化）
│   │   ├── interviews/             # 面经（YAML，按 Topic 结构化）
│   │   └── SCHEMA.md               # 数据格式说明
│   └── personal/
│       └── skill_profile.yaml      # 个人能力自评（60 Topic × level/interest）
├── scripts/
│   ├── generate_vault.py           # v1: 生成 Obsidian Vault
│   └── market_analyzer.py          # v2: 市场分析 + 缺口 + 推荐
├── output/
│   ├── daily_brief.md              # 每日摘要
│   ├── market_analysis.md         # 完整分析报告
│   └── analysis.json               # 原始数据（供程序使用）
├── templates/
│   ├── paper.md
│   └── concept.md
├── vault/                          # 生成的 Obsidian Vault（gitignore）
└── docs/
    └── history.txt
```

## 快速开始

```bash
# v1: 生成 Obsidian 知识库
python scripts/generate_vault.py

# v2: 市场分析 + 缺口 + 每日推荐
python scripts/market_analyzer.py          # 完整报告
python scripts/market_analyzer.py --brief  # 只看每日摘要
```

## 设计原则

### 1. Topic ID 是整个系统的连接键

所有数据——JD、面经、种子材料、个人能力——都通过 `knowledge_map.yaml` 中定义的 Topic ID 连接。

```yaml
# knowledge_map.yaml 定义了 topic: agent_loop
# seed_materials.yaml 的材料挂在 topic: agent_loop 下
# jd/*.yaml 的 skill 指向 topic_id: agent_loop
# interviews/*.yaml 的 question 指向 topics: [agent_loop]
# skill_profile.yaml 评估 topic_id: agent_loop 的 level
# interview_questions.yaml 关联 topics: [agent_loop]
```

这意味着：**加一个 Topic 到 knowledge_map.yaml，整个系统自动知道它。**

### 2. 数据是 YAML，不是数据库

所有数据是纯 YAML 文件，git 跟踪，人可读可改。不需要数据库、不需要服务端。

### 3. 分析是确定性 Python，不是 LLM

`market_analyzer.py` 是纯 Python 统计：频次、缺口、排序。不调用任何 LLM API。
LLM 的角色在数据采集层（把原始 JD/面经文本结构化为 YAML），这是可选的离线步骤。

### 4. 渐进式自动化

```
v1 (已完成): 人工定义知识树 + 人工筛选种子材料
v2 (已完成): 人工结构化市场数据 + 自动分析缺口 + 自动推荐
v3 (下一步): LLM 辅助从原始 JD/面经文本提取 Topic（半自动）
v4 (未来):   自动抓取 + 全自动 Daily Brief
```

## v2 模块

### ① Market Intelligence

`data/market/jd/` 和 `data/market/interviews/` 存放结构化的 JD 和面经。
每个条目的 skill/question 都关联到 `knowledge_map.yaml` 的 Topic ID。

### ② Knowledge Map

`config/knowledge_map.yaml` 是系统骨架，10 个一级领域、60 个 Topic。
`data/seed_materials.yaml` 是 49 篇人工筛选的经典材料，挂在 Topic 下。

### ③ Research Agent（推荐引擎）

`market_analyzer.py` 的 `recommend_materials()` 函数：
对每个能力缺口，从种子材料中按 importance 排序推荐。

### ④ Interview Agent

`data/interview_questions.yaml` 是面试题库，每题关联 Topic + answer keys。
`market_analyzer.py` 的 `recommend_interview_questions()` 按缺口推荐。

## 输出示例

```
📌 你最大的能力缺口 Top 5

1. 🔴 Agent 可靠性 — 市场 4 | 你的水平 2/5 | Gap Score 13.5
2. 🔴 Harness 优化 — 市场 4 | 你的水平 2/5 | Gap Score 12.0
3. 🟠 错误恢复 — 市场 5 | 你的水平 3/5 | Gap Score 10.0
4. 🟠 评估（Harness） — 市场 3 | 你的水平 2/5 | Gap Score 9.0
5. 🟠 工具调用 — 市场 9 | 你的水平 4/5 | Gap Score 9.0
```

## 后续路线

**v3: LLM 辅助数据采集**
- 从原始 JD/面经文本自动提取 Topic（半自动，人工 review）
- 从 arXiv / Semantic Scholar 自动搜索新论文
- 判断新论文是否改变现有认知

**v4: 趋势分析**
- 按日期统计 Topic 频次变化
- 识别上升/下降趋势
- 自动生成 Daily Brief

## 使用方法

```bash
# 1. 生成 Obsidian Vault（知识库浏览）
python scripts/generate_vault.py

# 2. 运行市场分析
python scripts/market_analyzer.py --brief

# 3. 添加新 JD
# 在 data/market/jd/ 下创建 YAML，skills 的 topic_id 匹配 knowledge_map.yaml

# 4. 更新个人能力
# 编辑 data/personal/skill_profile.yaml

# 5. 重新分析
python scripts/market_analyzer.py
```
