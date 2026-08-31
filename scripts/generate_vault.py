#!/usr/bin/env python3
"""
Agent Research OS — Vault Generator v1.1
从 knowledge_map.yaml + seed_materials.yaml 生成 Obsidian Vault。

输出结构：
  vault/
    00-Foundations/
      00-Foundations.md          ← 领域首页（文件名带领域名，graph 里可区分）
      concepts/
        Chain-of-Thought.md      ← 概念页
        ...
      materials/
        Chain-of-Thought-Prompting-….md  ← 论文/系统页
        ...
    01-Agent-Paradigms/
      ...
    ...
    _index.md                     ← 总览
    Knowledge-Map.md              ← 完整知识树

用法:
  python scripts/generate_vault.py
"""

import os
import sys
import re
import yaml
import json
from pathlib import Path

# ---- Paths ----
ROOT = Path(__file__).parent.parent
CONFIG_PATH = ROOT / "config" / "knowledge_map.yaml"
SEED_PATH = ROOT / "data" / "seed_materials.yaml"
VAULT_PATH = ROOT / "vault"

DOMAIN_NUM = {
    "foundations": "00",
    "agent_paradigms": "01",
    "planning_reasoning": "02",
    "tool_use": "03",
    "memory_context": "04",
    "multi_agent": "05",
    "agent_training": "06",
    "agent_evaluation": "07",
    "agent_systems": "08",
    "agent_harness": "09",
}


def slugify(text):
    text = re.sub(r"[^\w\u4e00-\u9fff\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def format_list(items):
    if not items:
        return "[]"
    return "[" + ", ".join(f'"{i}"' for i in items) + "]"


# ============================================================
# Note generators
# ============================================================

def generate_material_note(mat, domain_key, topic_info, concept_slug):
    """Generate a single material (paper/system/benchmark) note."""
    title = mat.get("title", "")
    slug = slugify(title) if title else mat.get("id", "untitled")

    fm = f"""---
type: {mat.get("type", "paper")}
title: "{title}"
authors: {format_list(mat.get("authors", []))}
year: {mat.get("year", "")}

domain: {domain_key}
topic: {mat.get("topic", "")}
role: {format_list(mat.get("role", []))}
status: {mat.get("status", "unread")}
importance: {mat.get("importance", 3)}
difficulty:
canonical: {str(mat.get("canonical", False)).lower()}

source:
  type: {mat.get("source", {}).get("type", "")}
  url: {mat.get("source", {}).get("url", "")}

why_read: {mat.get("why_read", "")}
prerequisite: {format_list(mat.get("prerequisite", []))}
followup: {format_list(mat.get("followup", []))}
unlocks: []

related_concepts:
  - "[[{concept_slug}]]"
related_papers: []

last_reviewed: 2026-08-31
tags:
  - material
  - {mat.get("type", "paper")}
  - {domain_key}
  - {mat.get("topic", "")}
---

# {title}

## 一句话

{mat.get("why_read", "")}

## 解决什么问题

## 为什么重要

## 核心方法

## Architecture / 设计

## 实验 / 效果

## 主要结论

## 局限

## 与其他工作的关系

- 所属概念: [[{concept_slug}]]
- 前置: {format_list(mat.get("prerequisite", []))}
- 后续: {format_list(mat.get("followup", []))}

## 我的理解

## 值得记住的东西
"""
    return slug, fm


def generate_concept_note(topic, domain_key, domain_info, materials_for_topic):
    """Generate a concept note for a topic, with links to its materials."""
    name = topic.get("name", "")
    slug = slugify(name)
    desc = topic.get("description", "")
    name_cn = topic.get("name_cn", "")

    # Build canonical papers list with actual links
    mat_links = []
    for m in materials_for_topic:
        m_title = m.get("title", "")
        m_slug = slugify(m_title)
        m_imp = m.get("importance", 0)
        stars = "\u2b50" * m_imp
        mat_links.append(f"- {stars} [[{m_slug}]]")

    mat_section = "\n".join(mat_links) if mat_links else "<!-- 暂无，待填充 -->"

    fm = f"""---
type: concept
title: "{name}"
domain: {domain_key}
topic: {topic.get("id", "")}
tags:
  - concept
  - {domain_key}
  - {topic.get("id", "")}
---

# {name}

> {desc}

## Definition

{desc}

## Evolution

<!-- 这个概念从什么演变来？又通向什么？ -->

## Key Questions

-
-

## Canonical Papers

{mat_section}

## Related Concepts

- [[]]

## My Understanding
"""
    return slug, fm


def generate_domain_index(domain_key, domain_info, materials, topics, concept_slugs):
    """Generate a domain index page."""
    name = domain_info.get("name", domain_key)
    name_cn = domain_info.get("name_cn", "")
    desc = domain_info.get("description", "")
    target = domain_info.get("target_papers", 0)

    num = DOMAIN_NUM.get(domain_key, "??")
    actual_count = len(materials)
    index_slug = f"{num}-{slugify(name)}"

    lines = [
        "---",
        f"type: domain_index",
        f'domain: {domain_key}',
        f'tags:',
        f'  - domain',
        f'  - {domain_key}',
        "---",
        "",
        f"# {num}. {name} — {name_cn}",
        "",
        f"> {desc}",
        "",
        f"**目标篇数**: {target} | **当前篇数**: {actual_count}",
        "",
        "## Topics (概念)",
        "",
    ]

    for t in topics:
        t_slug = slugify(t.get("name", ""))
        lines.append(f"- [[{t_slug}]] — {t.get('name_cn', '')}: {t.get('description', '')}")

    lines.extend(["", "## Materials (材料)", ""])

    for imp in [5, 4, 3, 2, 1]:
        mats = [m for m in materials if m.get("importance") == imp]
        if mats:
            _stars = chr(0x2b50) * imp
            lines.append(f"### {_stars} Importance {imp}")
            lines.append("")
            for m in mats:
                title = m.get("title", "")
                role = "/".join(m.get("role", []))
                year = m.get("year", "")
                lines.append(f"- [[{slugify(title)}]] ({year}) — {role}")
            lines.append("")

    return index_slug, "\n".join(lines)


def generate_master_index(km, materials_by_domain, topics_by_domain, domain_index_slugs):
    lines = [
        "---",
        "type: master_index",
        "tags:",
        "  - root",
        "---",
        "",
        "# Agent Research OS — Knowledge Map v1.0",
        "",
        "> 一个能自动构建和维护 Agent 领域知识地图的 Research Agent",
        "",
        "## 一级领域",
        "",
    ]

    for dkey, dinfo in km.get("domains", {}).items():
        num = DOMAIN_NUM.get(dkey, "??")
        name = dinfo.get("name", dkey)
        name_cn = dinfo.get("name_cn", "")
        desc = dinfo.get("description", "")
        mat_count = len(materials_by_domain.get(dkey, []))
        topic_count = len(topics_by_domain.get(dkey, []))
        idx_slug = domain_index_slugs.get(dkey, f"{num}-{slugify(name)}")
        lines.append(f"### {num}. [[{idx_slug}|{name}]] — {name_cn}")
        lines.append(f"> {desc}")
        lines.append(f"> Topics: {topic_count} | Materials: {mat_count}")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## 核心 Ontology",
        "",
        "```",
        "                   AGENT",
        "                     |",
        "       +-------------+-------------+",
        "       |             |             |",
        "   Reasoning      Planning       Tool",
        "       |             |             |",
        "       +-------------+-------------+",
        "                     |",
        "                   Memory",
        "                     |",
        "                  Context",
        "                     |",
        "                Agent Loop",
        "                     |",
        "          +----------+----------+",
        "          |          |          |",
        "       Session     Runtime    Sandbox",
        "          |          |          |",
        "          +----------+----------+",
        "                     |",
        "                  Harness",
        "                     |",
        "                Evaluation",
        "                     |",
        "              Self Improvement",
        "```",
        "",
        "---",
        "",
        "## 学习路线 (Curriculum)",
        "",
        "```",
        "Level 1: LLM Reasoning -> CoT -> Tool Use",
        "Level 2: ReAct -> Planning -> Reflection -> Memory",
        "Level 3: Agent Loop -> Multi-Agent -> RAG Agent -> Coding Agent",
        "Level 4: Agent Runtime -> Harness -> Context Engineering -> Evaluation",
        "Level 5: Agentic RL -> Harness Optimization -> Self-improving Agent",
        "```",
        "",
        "---",
        "",
        "## 统计",
        "",
    ])

    total_mats = sum(len(v) for v in materials_by_domain.values())
    total_topics = sum(len(v) for v in topics_by_domain.values())
    lines.append(f"- 一级领域: 10")
    lines.append(f"- Topics: {total_topics}")
    lines.append(f"- Materials: {total_mats}")

    all_mats = []
    for v in materials_by_domain.values():
        all_mats.extend(v)

    for imp in [5, 4, 3, 2, 1]:
        count = sum(1 for m in all_mats if m.get("importance") == imp)
        if count > 0:
            stars = "\u2b50" * imp
            lines.append(f"- {stars} Importance {imp}: {count}")

    lines.append("")
    lines.append("### 按类型")
    types = {}
    for m in all_mats:
        t = m.get("type", "unknown")
        types[t] = types.get(t, 0) + 1
    for t, c in sorted(types.items(), key=lambda x: -x[1]):
        lines.append(f"- {t}: {c}")

    lines.append("")
    lines.append("### 按状态")
    statuses = {}
    for m in all_mats:
        s = m.get("status", "unread")
        statuses[s] = statuses.get(s, 0) + 1
    for s, c in statuses.items():
        lines.append(f"- {s}: {c}")

    return "\n".join(lines)


def generate_knowledge_map_md(km, materials_by_domain, topics_by_domain):
    lines = [
        "---",
        "type: knowledge_map",
        "tags:",
        "  - root",
        "---",
        "",
        "# Knowledge Map — 完整知识树",
        "",
    ]

    for dkey, dinfo in km.get("domains", {}).items():
        num = DOMAIN_NUM.get(dkey, "??")
        name = dinfo.get("name", dkey)
        name_cn = dinfo.get("name_cn", "")
        lines.append(f"## {num}. {name} — {name_cn}")
        lines.append("")
        lines.append(f"> {dinfo.get('description', '')}")
        lines.append("")

        topics = topics_by_domain.get(dkey, [])
        for t in topics:
            tname = t.get("name", "")
            tdesc = t.get("description", "")
            lines.append(f"- **{tname}**: {tdesc}")

            mats = [m for m in materials_by_domain.get(dkey, []) if m.get("topic") == t.get("id")]
            for m in mats:
                imp = m.get("importance", 0)
                stars = "\u2b50" * imp
                title = m.get("title", "")
                role = "/".join(m.get("role", []))
                year = m.get("year", "")
                lines.append(f"  - {stars} [[{slugify(title)}]] ({year}) — {role}")

        lines.append("")

    return "\n".join(lines)


# ============================================================
# Obsidian config — graph colors by type
# ============================================================

def generate_obsidian_graph_config():
    """Generate .obsidian/graph.json with color rules by tag."""
    config = {
        "collapse-filter": False,
        "search": "",
        "showTags": True,
        "showAttachments": False,
        "hideUnresolved": True,
        "showOrphans": True,
        "collapse-color-groups": True,
        "colorGroups": [
            {
                "query": "tag:domain",
                "color": {"a": 1, "rgb": 1666687}
            },
            {
                "query": "tag:concept",
                "color": {"a": 1, "rgb": 14745471}
            },
            {
                "query": "tag:material",
                "color": {"a": 1, "rgb": 9408399}
            },
        ],
        "collapse-display": False,
        "showArrow": True,
        "textFadeMultiplier": 0,
        "nodeSizeMultiplier": 1.0,
        "lineSizeMultiplier": 1.0,
    }
    return config


def generate_obsidian_app_config():
    """Generate .obsidian/app.json."""
    return {
        "alwaysUpdateLinks": True,
        "newFileLocation": "current",
        "useMarkdownLinks": False,
    }


# ============================================================
# Main
# ============================================================

def main():
    print("=" * 60)
    print("Agent Research OS — Vault Generator v1.1")
    print("=" * 60)

    km = load_yaml(CONFIG_PATH)
    seed = load_yaml(SEED_PATH)

    domains = km.get("domains", {})
    materials = seed.get("materials", [])

    # Group materials by domain
    materials_by_domain = {}
    for m in materials:
        d = m.get("domain", "")
        if d not in materials_by_domain:
            materials_by_domain[d] = []
        materials_by_domain[d].append(m)

    # Group topics by domain
    topics_by_domain = {}
    for dkey, dinfo in domains.items():
        topics_by_domain[dkey] = dinfo.get("topics", [])

    # Clean vault
    if VAULT_PATH.exists():
        import shutil
        shutil.rmtree(VAULT_PATH)
    VAULT_PATH.mkdir(parents=True, exist_ok=True)

    # Track domain index slugs for master index links
    domain_index_slugs = {}

    # Generate domain folders + notes
    for dkey, dinfo in domains.items():
        num = DOMAIN_NUM.get(dkey, "??")
        name = dinfo.get("name", dkey)
        folder_name = f"{num}-{slugify(name)}"
        domain_dir = VAULT_PATH / folder_name
        concepts_dir = domain_dir / "concepts"
        materials_dir = domain_dir / "materials"
        concepts_dir.mkdir(parents=True, exist_ok=True)
        materials_dir.mkdir(parents=True, exist_ok=True)

        domain_topics = topics_by_domain.get(dkey, [])
        domain_mats = materials_by_domain.get(dkey, [])

        # Build topic_id -> concept_slug map
        topic_slug_map = {}
        for t in domain_topics:
            topic_slug_map[t.get("id", "")] = slugify(t.get("name", ""))

        # Domain index
        idx_slug, index_content = generate_domain_index(
            dkey, dinfo, domain_mats, domain_topics, topic_slug_map
        )
        domain_index_slugs[dkey] = idx_slug
        (domain_dir / f"{idx_slug}.md").write_text(index_content, encoding="utf-8")

        # Concept notes
        for topic in domain_topics:
            tid = topic.get("id", "")
            topic_mats = [m for m in domain_mats if m.get("topic") == tid]
            slug, content = generate_concept_note(topic, dkey, dinfo, topic_mats)
            (concepts_dir / f"{slug}.md").write_text(content, encoding="utf-8")

        # Material notes
        for mat in domain_mats:
            tid = mat.get("topic", "")
            concept_slug = topic_slug_map.get(tid, slugify(tid))
            slug, content = generate_material_note(mat, dkey, None, concept_slug)
            (materials_dir / f"{slug}.md").write_text(content, encoding="utf-8")

        print(f"  {folder_name}/ — {len(domain_topics)} concepts, {len(domain_mats)} materials")

    # Master index
    master = generate_master_index(km, materials_by_domain, topics_by_domain, domain_index_slugs)
    (VAULT_PATH / "_index.md").write_text(master, encoding="utf-8")

    # Knowledge map
    km_md = generate_knowledge_map_md(km, materials_by_domain, topics_by_domain)
    (VAULT_PATH / "Knowledge-Map.md").write_text(km_md, encoding="utf-8")

    # Obsidian config
    obsidian_dir = VAULT_PATH / ".obsidian"
    obsidian_dir.mkdir(exist_ok=True)

    graph_config = generate_obsidian_graph_config()
    (obsidian_dir / "graph.json").write_text(
        json.dumps(graph_config, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    app_config = generate_obsidian_app_config()
    (obsidian_dir / "app.json").write_text(
        json.dumps(app_config, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # Stats
    total_mats = len(materials)
    total_topics = sum(len(v) for v in topics_by_domain.values())

    print()
    print(f"  Vault generated: {VAULT_PATH}")
    print(f"   Domains: 10 | Topics: {total_topics} | Materials: {total_mats}")
    print(f"   Structure: each domain has concepts/ + materials/ subfolders")
    print(f"   Graph: color-coded by type (domain=green, concept=orange, material=purple)")
    print()
    print("Next steps:")
    print("  1. Open vault/ in Obsidian (as a vault)")
    print("  2. Start from _index.md")
    print("  3. Press Ctrl+G for graph view (colors auto-configured)")


if __name__ == "__main__":
    main()
