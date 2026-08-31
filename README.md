# Agent Research OS

一个能自动构建和维护 Agent 领域知识地图的 Research Agent。

不是"AI 论文收藏夹"，而是一套以**概念为中心**的知识网络——论文、系统、基准、框架都挂在知识树的节点上，树的结构由人定义，材料由 Agent 填充。

## 项目结构

```
agent_research_map/
├── config/
│   └── knowledge_map.yaml      # 知识树定义（10 个一级领域，60 个 Topic）
├── data/
│   └── seed_materials.yaml     # 人工筛选的经典种子材料（49 篇）
├── templates/
│   ├── paper.md                # 材料笔记模板
│   └── concept.md              # 概念笔记模板
├── scripts/
│   └── generate_vault.py       # 从 YAML 生成 Obsidian Vault
├── vault/                      # 生成的 Obsidian Vault（gitignore）
└── docs/
    └── history.txt              # 设计对话记录
```

## v1 范围（已完成）

**M1: 建立经典知识地图**

- [x] 10 个一级领域的知识树定义
- [x] 60 个 Topic 的分类体系
- [x] 49 篇人工筛选的经典种子材料
- [x] Obsidian Vault 生成器
- [x] 每篇材料的统一 Schema（frontmatter + 正文模板）

### 知识树（10 个一级领域）

```
00. Foundations         — 为什么 LLM 能做 Agent
01. Agent Paradigms     — Agent 是怎么工作的（ReAct/Plan-Execute/Reflection）
02. Planning & Reasoning — 任务分解、搜索、验证
03. Tool Use            — 工具调用、学习、创建、协议
04. Memory & Context    — 上下文管理、短期/长期记忆
05. Multi-Agent         — 协作、辩论、角色分工
06. Agent Training      — SFT、RL、RLVR、Agentic RL
07. Agent Evaluation    — 通用/Web/Coding 基准
08. Agent Systems       — Coding/Web/Research Agent
09. Agent Harness       — Context/Session/Loop/Runtime/Sandbox
```

### 材料分布

| 重要性 | 数量 | 阅读策略 |
|--------|------|----------|
| ★★★★★ | 13 | 必须真正读完 |
| ★★★★  | 19 | 看论文 + 总结 + 实验 |
| ★★★   | 15 | 知道解决什么问题即可 |
| ★★    | 2  | 补充 |

| 类型 | 数量 |
|------|------|
| paper | 32 |
| system | 7 |
| benchmark | 4 |
| survey | 3 |
| protocol | 1 |
| framework | 1 |
| blog | 1 |

## 使用方法

```bash
# 生成/刷新 Obsidian Vault
python scripts/generate_vault.py

# Windows 下如果遇到编码错误：
$env:PYTHONIOENCODING="utf-8"; python scripts/generate_vault.py
```

然后用 Obsidian 打开 `vault/` 文件夹作为 Vault，从 `_index.md` 开始浏览。

## 后续路线（v2+）

**M2: Reading Agent**
- 从 49 篇经典材料自动生成前置依赖图
- 基于依赖图排序出学习路线
- 跟踪阅读进度，推荐下一篇该读什么

**M3: 每日论文 Feed**
- 自动搜索 arXiv / Semantic Scholar 新论文
- 映射到知识树节点
- 判断是否改变现有认知
- 值得读的加入 Daily Reading

**M4: 搜索 Agent（自动填充知识树）**
- Discovery → Classifier → Ranker → Gap Detector 四阶段 workflow
- 每个节点自动找候选论文，人工 Review 后确认
- Coverage + Canonicality 双维度保证

## 设计原则

1. **知识树由人定义**，不由 LLM 自动生成 tags
2. **论文挂在概念下**，分类第一层是问题/概念不是论文
3. **不限于论文**——Paper、System、GitHub、Blog、Benchmark 都是一等公民
4. **人机共创**——Agent 负责搜索/分类/排序，人负责 Review 和体系设计
5. **经典性可变**——`canonical` 是可重新评估的标签，不是永久标签
