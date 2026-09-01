#!/usr/bin/env python3
"""
Agent Career Research OS — Market Analyzer v2.0

把招聘市场数据（JD + 面经）和个人能力 profile 对齐到 knowledge_map.yaml 的 Topic 体系，
产出：
  1. Market Skill Map     — 各 topic 的市场热度（JD + 面经频次）
  2. Trend                — 近期 vs 历史的增长趋势（数据足够时）
  3. Knowledge Gap        — 市场需求 - 个人能力 = 缺口
  4. Reading Plan         — 缺口 → 种子材料推荐
  5. Interview Plan       — 缺口 → 面试题推荐
  6. Daily Brief          — 每日学习摘要

用法:
  python scripts/market_analyzer.py
  python scripts/market_analyzer.py --brief   # 只输出 Daily Brief
"""

import os
import sys
import yaml
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict, Counter

# ---- Paths ----
ROOT = Path(__file__).parent.parent
CONFIG_PATH = ROOT / "config" / "knowledge_map.yaml"
SEED_PATH = ROOT / "data" / "seed_materials.yaml"
JD_DIR = ROOT / "data" / "market" / "jd"
INTERVIEW_DIR = ROOT / "data" / "market" / "interviews"
PROFILE_PATH = ROOT / "data" / "personal" / "skill_profile.yaml"
QUESTIONS_PATH = ROOT / "data" / "interview_questions.yaml"
OUTPUT_DIR = ROOT / "output"


# ============================================================
# Data Loading
# ============================================================

def load_yaml(path):
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_all_yaml_in_dir(dir_path):
    """Load all .yaml files in a directory and merge their lists."""
    results = {"jds": [], "interviews": []}
    if not dir_path.exists():
        return results
    for f in sorted(dir_path.glob("*.yaml")):
        data = load_yaml(f)
        if "jds" in data:
            results["jds"].extend(data["jds"])
        if "interviews" in data:
            results["interviews"].extend(data["interviews"])
    return results


def build_topic_index(km):
    """Build flat topic_id → {domain, topic_info} index."""
    index = {}
    for dkey, dinfo in km.get("domains", {}).items():
        for topic in dinfo.get("topics", []):
            tid = topic.get("id", "")
            # Note: topic IDs can repeat across domains (e.g. context_management)
            # We key by (domain, topic_id) but also provide a flat lookup
            if tid not in index:
                index[tid] = []
            index[tid].append({
                "domain": dkey,
                "domain_name": dinfo.get("name", dkey),
                "domain_cn": dinfo.get("name_cn", ""),
                "topic": topic
            })
    return index


def build_material_index(seed):
    """Build topic_id → [materials] and material_id → material indexes."""
    by_topic = defaultdict(list)
    by_id = {}
    for mat in seed.get("materials", []):
        tid = mat.get("topic", "")
        by_topic[tid].append(mat)
        by_id[mat.get("id", "")] = mat
    return by_topic, by_id


# ============================================================
# Market Analysis
# ============================================================

def analyze_jds(jds):
    """Count topic frequency from JDs."""
    topic_counts = Counter()
    topic_companies = defaultdict(set)
    topic_jd_titles = defaultdict(list)

    for jd in jds:
        company = jd.get("company", "")
        title = jd.get("title", "")
        seen_in_this_jd = set()

        for skill in jd.get("skills", []):
            tid = skill.get("topic_id", "")
            if tid and tid not in seen_in_this_jd:
                topic_counts[tid] += 1
                topic_companies[tid].add(company)
                topic_jd_titles[tid].append(title)
                seen_in_this_jd.add(tid)

        for bonus in jd.get("bonus", []):
            tid = bonus.get("topic_id", "")
            if tid and tid not in seen_in_this_jd:
                topic_counts[tid] += 0.5  # bonus weight
                topic_companies[tid].add(company)
                topic_jd_titles[tid].append(title)
                seen_in_this_jd.add(tid)

    return {
        "counts": topic_counts,
        "companies": topic_companies,
        "jd_titles": topic_jd_titles,
        "total_jds": len(jds),
    }


def analyze_interviews(interviews):
    """Count topic frequency from interview questions."""
    topic_counts = Counter()
    topic_questions = defaultdict(list)
    topic_companies = defaultdict(set)
    question_list = []

    for iv in interviews:
        company = iv.get("company", "")
        for q in iv.get("questions", []):
            question_list.append({
                "text": q.get("text", ""),
                "company": company,
                "date": iv.get("date", ""),
                "difficulty": q.get("difficulty", 3),
                "topics": q.get("topics", []),
            })
            for tid in q.get("topics", []):
                topic_counts[tid] += 1
                topic_companies[tid].add(company)
                topic_questions[tid].append(q.get("text", ""))

    return {
        "counts": topic_counts,
        "questions": topic_questions,
        "companies": topic_companies,
        "total_interviews": len(interviews),
        "total_questions": len(question_list),
        "question_list": question_list,
    }


def compute_market_heat(jd_analysis, iv_analysis):
    """Combine JD and interview frequencies into a heat score."""
    all_topics = set(jd_analysis["counts"].keys()) | set(iv_analysis["counts"].keys())
    heat = {}
    for tid in all_topics:
        jd_score = jd_analysis["counts"].get(tid, 0)
        iv_score = iv_analysis["counts"].get(tid, 0)
        companies = jd_analysis["companies"].get(tid, set()) | iv_analysis["companies"].get(tid, set())
        heat[tid] = {
            "jd_count": jd_score,
            "interview_count": iv_score,
            "total": jd_score + iv_score,
            "companies": sorted(companies),
            "company_count": len(companies),
        }
    return heat


# ============================================================
# Gap Analysis
# ============================================================

def compute_gap(heat, profile, topic_index):
    """Compute knowledge gap = market_demand - personal_skill."""
    skills = {s["topic_id"]: s for s in profile.get("skills", [])}

    gaps = []
    for tid, heat_info in heat.items():
        personal = skills.get(tid, {})
        level = personal.get("level", 1)
        interest = personal.get("interest", 3)

        # Gap score: high market heat + low personal level + high interest
        demand = heat_info["total"]
        gap_score = demand * (5 - level) * (interest / 5.0)

        gaps.append({
            "topic_id": tid,
            "domain": topic_index.get(tid, [{}])[0].get("domain_name", "") if tid in topic_index else "?",
            "topic_name": topic_index.get(tid, [{}])[0].get("topic", {}).get("name", tid) if tid in topic_index else tid,
            "topic_cn": topic_index.get(tid, [{}])[0].get("topic", {}).get("name_cn", "") if tid in topic_index else "",
            "market_heat": demand,
            "jd_count": heat_info["jd_count"],
            "interview_count": heat_info["interview_count"],
            "company_count": heat_info["company_count"],
            "personal_level": level,
            "interest": interest,
            "gap_score": round(gap_score, 2),
            "priority": "🔴" if gap_score > 10 else ("🟠" if gap_score > 5 else "🟡"),
        })

    gaps.sort(key=lambda x: -x["gap_score"])
    return gaps


# ============================================================
# Recommendation Engine
# ============================================================

def recommend_materials(gaps, materials_by_topic, max_per_gap=3):
    """For each gap, recommend seed materials."""
    recommendations = []
    for gap in gaps:
        tid = gap["topic_id"]
        mats = materials_by_topic.get(tid, [])
        # Sort by importance
        mats_sorted = sorted(mats, key=lambda m: -m.get("importance", 0))

        recommended = []
        for mat in mats_sorted[:max_per_gap]:
            recommended.append({
                "id": mat.get("id", ""),
                "title": mat.get("title", ""),
                "importance": mat.get("importance", 0),
                "type": mat.get("type", ""),
                "why_read": mat.get("why_read", ""),
                "url": mat.get("source", {}).get("url", ""),
            })

        recommendations.append({
            "topic_id": tid,
            "topic_name": gap["topic_name"],
            "topic_cn": gap["topic_cn"],
            "priority": gap["priority"],
            "gap_score": gap["gap_score"],
            "personal_level": gap["personal_level"],
            "market_heat": gap["market_heat"],
            "materials": recommended,
        })
    return recommendations


def recommend_interview_questions(gaps, questions_data, max_per_gap=3):
    """For each gap, recommend interview questions."""
    all_questions = questions_data.get("questions", [])
    # Build topic → questions index
    topic_questions = defaultdict(list)
    for q in all_questions:
        for tid in q.get("topics", []):
            topic_questions[tid].append(q)

    recommendations = []
    for gap in gaps[:10]:  # Top 10 gaps
        tid = gap["topic_id"]
        qs = topic_questions.get(tid, [])
        qs_sorted = sorted(qs, key=lambda q: -q.get("difficulty", 3))

        recommended = []
        for q in qs_sorted[:max_per_gap]:
            recommended.append({
                "id": q.get("id", ""),
                "text": q.get("text", ""),
                "difficulty": q.get("difficulty", 3),
                "companies": q.get("companies", []),
                "answer_keys": q.get("answer_keys", []),
                "related_materials": q.get("related_materials", []),
            })

        recommendations.append({
            "topic_id": tid,
            "topic_name": gap["topic_name"],
            "priority": gap["priority"],
            "questions": recommended,
        })
    return recommendations


# ============================================================
# Daily Brief
# ============================================================

def generate_daily_brief(gaps, material_recs, question_recs, jd_analysis, iv_analysis, topic_index):
    """Generate a Daily Brief markdown."""
    today = datetime.now().strftime("%Y-%m-%d")
    lines = [
        f"# Agent Daily Brief — {today}",
        "",
        f"📊 数据: {jd_analysis['total_jds']} JDs | {iv_analysis['total_interviews']} 面经 | {iv_analysis['total_questions']} 面试题",
        "",
        "## 🔥 市场热度 Top 10",
        "",
        "| # | Topic | JD | 面经 | 公司数 | 热度 |",
        "|---|-------|----|------|--------|------|",
    ]

    top_topics = sorted(gaps, key=lambda x: -x["market_heat"])[:10]
    for i, g in enumerate(top_topics, 1):
        name = g["topic_cn"] or g["topic_name"]
        lines.append(f"| {i} | {name} | {g['jd_count']:.0f} | {g['interview_count']} | {g['company_count']} | {g['market_heat']:.1f} |")

    lines.extend(["", "## 📌 你最大的能力缺口 Top 5", ""])
    for i, g in enumerate(gaps[:5], 1):
        name = g["topic_cn"] or g["topic_name"]
        lines.append(f"{i}. {g['priority']} **{name}** — 市场 {g['market_heat']:.0f} | 你的水平 {g['personal_level']}/5 | Gap Score {g['gap_score']}")

    lines.extend(["", "## 📚 今日阅读推荐", ""])
    for rec in material_recs[:5]:
        if not rec["materials"]:
            continue
        name = rec["topic_cn"] or rec["topic_name"]
        lines.append(f"### {rec['priority']} {name} (你的水平 {rec['personal_level']}/5)")
        lines.append("")
        for mat in rec["materials"]:
            stars = "⭐" * mat["importance"]
            url_part = f" [link]({mat['url']})" if mat["url"] else ""
            lines.append(f"- {stars} **{mat['title']}** ({mat['type']}){url_part}")
            lines.append(f"  - {mat['why_read']}")
        lines.append("")

    lines.extend(["## 🎯 今日面试题", ""])
    for rec in question_recs[:5]:
        if not rec["questions"]:
            continue
        name = rec["topic_name"]
        lines.append(f"### {rec['priority']} {name}")
        lines.append("")
        for q in rec["questions"]:
            companies = ", ".join(q["companies"]) if q["companies"] else ""
            lines.append(f"- **{q['text']}** ({companies})")
            for ak in q["answer_keys"][:2]:
                lines.append(f"  - {ak}")
        lines.append("")

    lines.extend([
        "## 💻 今日实践建议",
        "",
        "> 挑一个你的 🔴 缺口，设计一个最小实现或写一段分析。",
        "",
        "---",
        f"*Generated by Agent Career Research OS — {today}*",
    ])

    return "\n".join(lines)


# ============================================================
# Full Report
# ============================================================

def generate_full_report(heat, gaps, material_recs, question_recs, jd_analysis, iv_analysis, topic_index):
    """Generate a comprehensive analysis report."""
    today = datetime.now().strftime("%Y-%m-%d")
    lines = [
        f"# Agent Career Research OS — Market Analysis Report",
        f"",
        f"Generated: {today}",
        f"",
        f"## Overview",
        f"",
        f"- JDs analyzed: {jd_analysis['total_jds']}",
        f"- Interviews analyzed: {iv_analysis['total_interviews']}",
        f"- Interview questions: {iv_analysis['total_questions']}",
        f"- Unique topics with market signal: {len(heat)}",
        f"- Knowledge gaps identified: {len([g for g in gaps if g['gap_score'] > 0])}",
        f"",
        f"## Market Skill Map — 完整热度表",
        f"",
        f"| Topic | Domain | JD | 面经 | 公司 | 热度 |",
        f"|-------|--------|----|------|------|------|",
    ]

    # Sort by heat
    sorted_heat = sorted(heat.items(), key=lambda x: -x[1]["total"])
    for tid, info in sorted_heat:
        topic_entries = topic_index.get(tid, [{}])
        tname = topic_entries[0].get("topic", {}).get("name", tid) if topic_entries else tid
        tcn = topic_entries[0].get("topic", {}).get("name_cn", "") if topic_entries else ""
        dname = topic_entries[0].get("domain_name", "") if topic_entries else ""
        display = f"{tcn} ({tname})" if tcn else tname
        companies = ", ".join(info["companies"][:3])
        if len(info["companies"]) > 3:
            companies += "..."
        lines.append(f"| {display} | {dname} | {info['jd_count']:.1f} | {info['interview_count']} | {companies} | {info['total']:.1f} |")

    lines.extend(["", "## Knowledge Gap Analysis — 能力缺口", ""])
    lines.append("| Priority | Topic | Domain | 市场 | 你的水平 | Gap Score |")
    lines.append("|----------|-------|--------|------|----------|-----------|")
    for g in gaps:
        if g["gap_score"] <= 0:
            continue
        name = g["topic_cn"] or g["topic_name"]
        lines.append(f"| {g['priority']} | {name} | {g['domain']} | {g['market_heat']:.1f} | {g['personal_level']}/5 | {g['gap_score']} |")

    lines.extend(["", "## Reading Plan — 阅读计划", ""])
    for rec in material_recs:
        if not rec["materials"]:
            continue
        name = rec["topic_cn"] or rec["topic_name"]
        lines.append(f"### {rec['priority']} {name}")
        lines.append(f"- Market heat: {rec['market_heat']:.1f} | Your level: {rec['personal_level']}/5 | Gap: {rec['gap_score']}")
        lines.append("")
        for mat in rec["materials"]:
            stars = "⭐" * mat["importance"]
            url_part = f" [link]({mat['url']})" if mat["url"] else ""
            lines.append(f"- {stars} **{mat['title']}** ({mat['type']}){url_part}")
            lines.append(f"  - {mat['why_read']}")
        lines.append("")

    lines.extend(["", "## Interview Question Bank — 面试题推荐", ""])
    for rec in question_recs:
        if not rec["questions"]:
            continue
        lines.append(f"### {rec['priority']} {rec['topic_name']}")
        lines.append("")
        for q in rec["questions"]:
            companies = ", ".join(q["companies"]) if q["companies"] else ""
            lines.append(f"- **{q['text']}** ({companies})")
            lines.append(f"  - Difficulty: {'🔥' * q['difficulty']}")
            lines.append(f"  - Answer keys:")
            for ak in q["answer_keys"]:
                lines.append(f"    - {ak}")
            if q["related_materials"]:
                lines.append(f"  - Related materials: {', '.join(q['related_materials'])}")
            lines.append("")

    lines.extend(["", "---", f"*Generated by Agent Career Research OS — {today}*"])
    return "\n".join(lines)


# ============================================================
# Main
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Agent Career Research OS — Market Analyzer")
    parser.add_argument("--brief", action="store_true", help="Only output Daily Brief")
    parser.add_argument("--output", type=str, default=None, help="Output directory")
    args = parser.parse_args()

    print("=" * 60)
    print("Agent Career Research OS — Market Analyzer v2.0")
    print("=" * 60)

    # Load all data
    km = load_yaml(CONFIG_PATH)
    seed = load_yaml(SEED_PATH)
    profile = load_yaml(PROFILE_PATH)
    questions = load_yaml(QUESTIONS_PATH)

    market_data = load_all_yaml_in_dir(JD_DIR)
    # Also load interviews from the interviews dir
    iv_market_data = load_all_yaml_in_dir(INTERVIEW_DIR)
    market_data["interviews"].extend(iv_market_data["interviews"])

    topic_index = build_topic_index(km)
    materials_by_topic, materials_by_id = build_material_index(seed)

    # Analyze
    jd_analysis = analyze_jds(market_data["jds"])
    iv_analysis = analyze_interviews(market_data["interviews"])
    heat = compute_market_heat(jd_analysis, iv_analysis)
    gaps = compute_gap(heat, profile, topic_index)
    material_recs = recommend_materials(gaps, materials_by_topic)
    question_recs = recommend_interview_questions(gaps, questions)

    # Generate outputs
    out_dir = Path(args.output) if args.output else OUTPUT_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.brief:
        brief = generate_daily_brief(gaps, material_recs, question_recs, jd_analysis, iv_analysis, topic_index)
        brief_path = out_dir / "daily_brief.md"
        brief_path.write_text(brief, encoding="utf-8")
        print(f"\nDaily Brief → {brief_path}")
        print("\n" + "=" * 50)
        print(brief)
    else:
        report = generate_full_report(heat, gaps, material_recs, question_recs, jd_analysis, iv_analysis, topic_index)
        report_path = out_dir / "market_analysis.md"
        report_path.write_text(report, encoding="utf-8")
        print(f"\nFull Report → {report_path}")

        brief = generate_daily_brief(gaps, material_recs, question_recs, jd_analysis, iv_analysis, topic_index)
        brief_path = out_dir / "daily_brief.md"
        brief_path.write_text(brief, encoding="utf-8")
        print(f"Daily Brief → {brief_path}")

        # Also dump raw analysis as YAML for programmatic use
        analysis_data = {
            "generated": datetime.now().isoformat(),
            "stats": {
                "total_jds": jd_analysis["total_jds"],
                "total_interviews": iv_analysis["total_interviews"],
                "total_questions": iv_analysis["total_questions"],
                "total_topics_with_signal": len(heat),
            },
            "market_heat": {tid: {**v, "companies": v["companies"]} for tid, v in heat.items()},
            "knowledge_gaps": [{k: v for k, v in g.items() if k != "companies"} for g in gaps],
        }
        analysis_path = out_dir / "analysis.json"
        import json
        analysis_path.write_text(json.dumps(analysis_data, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        print(f"Raw analysis → {analysis_path}")

    print(f"\nDone. {jd_analysis['total_jds']} JDs, {iv_analysis['total_interviews']} interviews, {len(heat)} topics.")


if __name__ == "__main__":
    main()
