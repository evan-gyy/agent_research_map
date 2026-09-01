# ============================================================
# Agent Career Research OS — Market Data Schema v2.0
# ============================================================
# JD 和面经的结构化格式。
# 所有 topic_id 必须存在于 knowledge_map.yaml 中。
# 这样市场数据、个人能力、种子材料三者通过 Topic ID 连接。
# ============================================================

# ---- JD 示例 ----
# 存放路径: data/market/jd/YYYY-MM-DD-<source>-<id>.yaml

# jds:
#   - id: bytedance_agent_20260828
#     source: nowcoder          # nowcoder | boss | linkedin | manual
#     url: "https://..."
#     company: 字节跳动
#     title: AI Agent 工程师
#     date: 2026-08-28
#     skills:
#       - topic_id: agent_loop        # 必须匹配 knowledge_map.yaml 中的 topic id
#         mentioned_as: "Agent Loop"  # JD 原文怎么说的
#       - topic_id: context_management
#         mentioned_as: "Context 管理"
#     experience:
#       - "Agent 应用开发经验"
#       - "生产环境部署"
#     bonus:
#       - topic_id: mcp
#         mentioned_as: "MCP"
#     responsibilities:
#       - "Agent workflow 设计"
#       - "Agent 性能优化"
#     raw_text: |      # 原始 JD 文本（可选，用于回溯）
#       ...
