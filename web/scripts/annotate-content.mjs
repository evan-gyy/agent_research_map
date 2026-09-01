import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const webRoot = path.resolve(here, "..");
const topicsDir = path.resolve(webRoot, "../ai-llm-learn/Topics");
const catalog = JSON.parse(fs.readFileSync(path.join(webRoot, "src/data/knowledge-points.json"), "utf8"));

const groups = {
  "agent-architecture-core": [8, 10, 30, 42, 64, 66, 88, 90],
  "react-agent-loop": [2, 19, 31, 35, 49, 81],
  "planning-task-decomposition": [56, 79],
  "workflow-state-orchestration": [18, 39, 40, 45, 48, 99],
  "agent-framework-langgraph": [41, 71],
  "harness-coding-agent": [26, 28, 29, 91, 94],
  "agent-self-evolution": [50, 51, 52],
  "intent-routing": [11, 12, 55, 72],
  "multi-agent-collaboration": [7, 20, 34, 43, 44, 80, 85],
  "context-token-compression": [3, 6, 25, 38, 60, 76],
  "memory-systems": [5, 9, 57, 73, 74, 92],
  "tool-design": [32],
  "parameter-schema": [33],
  "function-calling": [82, 83],
  "mcp-protocol": [1, 24, 58],
  "tool-reliability": [14, 77, 84],
  "rag-architecture": [13, 46, 63, 87, 101, 102, 113, 114],
  "document-parsing-chunking": [16, 27, 105],
  "embedding-vector-retrieval": [23, 69, 70],
  "hybrid-retrieval-reranking": [15, 17, 96],
  "rag-evaluation-hallucination": [36, 65],
  "transformer-attention": [59, 93, 110, 111, 117, 118],
  "inference-optimization": [106, 108],
  "parameter-efficient-finetuning": [47, 115],
  "alignment-training-distillation": [98, 104, 107, 109, 112, 116],
  "system-performance-concurrency": [37, 61, 62, 86],
  "reliability-resilience": [4, 21, 53, 67, 68, 75],
  "evaluation-metrics-datasets": [22, 54, 78, 89, 95, 97, 100, 103],
};

const assignment = new Map();
for (const [point, ids] of Object.entries(groups)) {
  if (!catalog[point]) throw new Error("Unknown knowledge point: " + point);
  for (const n of ids) {
    const id = "Q" + String(n).padStart(4, "0");
    if (assignment.has(id)) throw new Error("Duplicate assignment: " + id);
    assignment.set(id, point);
  }
}

const files = fs.readdirSync(topicsDir).filter((name) => name.endsWith(".md"));
for (const file of files) {
  const id = file.match(/^(Q\d{4})-/)?.[1];
  if (!id || !assignment.has(id)) throw new Error("Missing assignment: " + file);
  const fullPath = path.join(topicsDir, file);
  let raw = fs.readFileSync(fullPath, "utf8");
  if (/^knowledge_point:/m.test(raw)) continue;
  const point = assignment.get(id);
  const tags = catalog[point].tags.map((tag) => "  - " + tag).join("\n");
  raw = raw.replace(/^(area:.*)$/m, "$1\nknowledge_point: " + point + "\ntags:\n" + tags);
  fs.writeFileSync(fullPath, raw, "utf8");
}

if (files.length !== assignment.size) {
  throw new Error("File/assignment mismatch: " + files.length + "/" + assignment.size);
}
console.log("Annotated " + files.length + " formal questions.");
