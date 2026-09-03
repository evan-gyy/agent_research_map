#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";

const args = process.argv.slice(2);
const strict = args.includes("--strict");
const target = args.find((arg) => !arg.startsWith("--"));
if (!target) {
  console.error("Usage: node validate_agent_research.mjs <markdown-file> [--strict]");
  process.exit(2);
}

const file = path.resolve(target);
if (!fs.existsSync(file)) {
  console.error("File not found: " + file);
  process.exit(2);
}

const text = fs.readFileSync(file, "utf8");
const errors = [];
const warnings = [];
const requirePattern = (name, pattern) => {
  if (!pattern.test(text)) errors.push("Missing " + name);
};
const count = (pattern) => Array.from(text.matchAll(pattern)).length;

requirePattern("verification date", /核验日期|验证日期|verified on/i);
requirePattern("evidence boundary", /证据边界|证据等级|事实边界|evidence/i);
requirePattern("module map", /模块地图|模块总览|核心模块|module map/i);
requirePattern("end-to-end flow", /端到端|完整流程|主链路|end-to-end/i);
requirePattern("context analysis", /Context|上下文/);
requirePattern("tool analysis", /Tool|工具/);
requirePattern("failure or boundary path", /失败|错误|异常|取消|中断|边界/);
requirePattern("source reading route", /源码阅读路线|阅读顺序|source.*route/i);
requirePattern("sources section", /^##+ .*来源|^##+ Sources/im);
requirePattern("transferable lessons", /可迁移|工程经验|设计启示|transferable/i);

const mermaidCount = count(/```mermaid[\s\S]*?```/g);
const codeCount = count(/```(?:ts|tsx|js|jsx|rust|rs|py|python|json|yaml|yml|text|bash|sh)[\s\S]*?```/g);
const tableCount = count(/^\|.+\|\r?\n\|(?:[-: ]+\|)+$/gm);
const evidenceLabels = [
  "官方文档确认",
  "官方公开源码确认",
  "可复现实验确认",
  "非官方历史快照观察",
  "概念映射",
  "工程建议",
  "待核验",
].filter((label) => text.includes(label));

if (mermaidCount < 2) errors.push("Need at least 2 Mermaid diagrams; got " + mermaidCount);
if (codeCount < 1) errors.push("No source or pseudocode block found");
if (tableCount < 1) warnings.push("No Markdown table detected");
if (evidenceLabels.length < 2) errors.push("Fewer than 2 evidence labels used");

if (strict) {
  if (mermaidCount < 4) errors.push("Strict mode needs at least 4 Mermaid diagrams; got " + mermaidCount);
  if (codeCount < 3) errors.push("Strict mode needs at least 3 code/pseudocode blocks; got " + codeCount);
  requirePattern("complete example", /完整.*示例|运行示例|示例：|walkthrough/i);
  requirePattern("tradeoff discussion", /取舍|代价|trade-?off/i);
  requirePattern("commit or version", /commit|版本|version/i);
}

const fenceCount = count(/^```/gm);
if (fenceCount % 2 !== 0) errors.push("Unbalanced Markdown fences: " + fenceCount);

for (const warning of warnings) console.warn("WARN: " + warning);
if (errors.length) {
  for (const error of errors) console.error("ERROR: " + error);
  process.exit(1);
}

console.log([
  "Agent research validation passed: " + path.basename(file),
  "mermaid=" + mermaidCount,
  "code=" + codeCount,
  "evidenceLabels=" + evidenceLabels.length,
  "strict=" + strict,
].join("; "));
