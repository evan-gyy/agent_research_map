import fs from "node:fs";
import path from "node:path";
import matter from "gray-matter";
import { unified } from "unified";
import remarkParse from "remark-parse";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import remarkRehype from "remark-rehype";
import rehypeKatex from "rehype-katex";
import rehypeStringify from "rehype-stringify";
import agentProductsJson from "../data/agent-products.json";
import knowledgePointsJson from "../data/knowledge-points.json";

export interface QuestionRecord {
  id: string;
  title: string;
  area: string;
  knowledgePoint: string;
  tags: string[];
  answerHtml: string | null;
  verificationLabel: "已核验" | "待复核";
  collectedAt: string;
  sourceUrl: string;
}

export interface KnowledgePoint {
  slug: string;
  label: string;
  tags: string[];
}

export interface FrequencyRow extends KnowledgePoint {
  count: number;
  highFrequency: boolean;
}

export interface AgentPractice {
  point: string;
  title: string;
  summary: string;
  section: string;
}

export interface AgentProduct {
  slug: string;
  name: string;
  vendor: string;
  tagline: string;
  evidence: string;
  flow: string[];
  practices: AgentPractice[];
  contentHtml: string;
}

const webRoot = path.resolve(process.cwd());
export const topicsDir = path.resolve(webRoot, "../ai-llm-learn/Topics");
export const agentProductsDir = path.resolve(webRoot, "../ai-llm-learn/Agent实现拆解");
export const knowledgePoints: KnowledgePoint[] = Object.entries(knowledgePointsJson).map(
  ([slug, value]) => ({ slug, label: value.label, tags: value.tags }),
);
const knownPoints = new Set(knowledgePoints.map((item) => item.slug));

function neutralize(markdown: string): string {
  return markdown
    .replaceAll("原题原文", "题目原文")
    .replaceAll("面试直答", "核心回答")
    .replaceAll("常见追问", "延伸思考")
    .replaceAll("面试时", "作答时");
}

async function renderMarkdown(markdown: string): Promise<string> {
  const result = await unified()
    .use(remarkParse)
    .use(remarkGfm)
    .use(remarkMath)
    .use(remarkRehype)
    .use(rehypeKatex)
    .use(rehypeStringify)
    .process(neutralize(markdown));
  return String(result);
}

let agentProductsPromise: Promise<AgentProduct[]> | undefined;
export function getAgentProducts(): Promise<AgentProduct[]> {
  agentProductsPromise ??= Promise.all(agentProductsJson.map(async (entry) => {
    const missing = entry.practices.filter((practice) => !knownPoints.has(practice.point));
    if (missing.length) {
      throw new Error(entry.name + " 包含未知知识点: " + missing.map((item) => item.point).join(", "));
    }
    const sourcePath = path.join(agentProductsDir, entry.sourceFile);
    if (!fs.existsSync(sourcePath)) throw new Error(entry.name + " 缺少拆解文档: " + entry.sourceFile);
    const markdown = fs.readFileSync(sourcePath, "utf8").replace(/^#\s+.+\r?\n+/, "");
    return { ...entry, contentHtml: await renderMarkdown(markdown) } as AgentProduct;
  }));
  return agentProductsPromise;
}

export async function getAgentPracticesForPoint(point: string) {
  const products = await getAgentProducts();
  return products.flatMap((product) => product.practices
    .filter((practice) => practice.point === point)
    .map((practice) => ({ product, practice })));
}

function extractSection(content: string, start: string, end: string): string {
  const startIndex = content.indexOf(start);
  const endIndex = content.indexOf(end, startIndex + start.length);
  if (startIndex < 0 || endIndex < 0) return "";
  return content.slice(startIndex + start.length, endIndex).trim();
}

export async function parseQuestionFile(filePath: string): Promise<QuestionRecord> {
  const raw = fs.readFileSync(filePath, "utf8");
  const { data, content } = matter(raw);
  const fileName = path.basename(filePath);
  const fileId = fileName.match(/^(Q\d{4})-/)?.[1];
  const title = content.match(/^#\s+(.+)$/m)?.[1]?.trim();
  const sourceUrl = content.match(/^- 来源链接：\s*(https?:\/\/\S+)$/m)?.[1];
  const errors: string[] = [];

  if (!fileId) errors.push("文件名必须以 Q0001- 形式开头");
  if (!data.id || data.id !== fileId) errors.push("frontmatter id 与文件名题号不一致");
  if (!title) errors.push("缺少一级标题");
  if (!data.area) errors.push("缺少 area");
  if (!data.knowledge_point || !knownPoints.has(data.knowledge_point)) errors.push("knowledge_point 不在受控目录中");
  if (!Array.isArray(data.tags)) errors.push("tags 必须为数组");
  if (!data.collected_at) errors.push("缺少 collected_at");
  if (!sourceUrl) errors.push("缺少可追溯的来源链接");
  if (!data.verification) errors.push("缺少 verification");
  if (errors.length) throw new Error(fileName + ": " + errors.join("；"));

  const answerMarkdown = extractSection(content, "## 答案", "## 问题来源")
    .replace(/<!--[^]*?-->/g, "")
    .trim();
  const verificationLabel = String(data.verification).toLowerCase().includes("verified")
    ? "已核验"
    : "待复核";

  return {
    id: String(data.id),
    title: title!,
    area: String(data.area),
    knowledgePoint: String(data.knowledge_point),
    tags: data.tags.map(String),
    answerHtml: answerMarkdown ? await renderMarkdown(answerMarkdown) : null,
    verificationLabel,
    collectedAt: data.collected_at instanceof Date
      ? data.collected_at.toISOString().slice(0, 10)
      : String(data.collected_at).slice(0, 10),
    sourceUrl: sourceUrl!,
  };
}

let questionsPromise: Promise<QuestionRecord[]> | undefined;
export function getAllQuestions(): Promise<QuestionRecord[]> {
  questionsPromise ??= Promise.all(
    fs.readdirSync(topicsDir)
      .filter((name) => name.endsWith(".md"))
      .map((name) => parseQuestionFile(path.join(topicsDir, name))),
  ).then((items) => items.sort((a, b) => a.id.localeCompare(b.id, "zh-CN")));
  return questionsPromise;
}

export function getFrequencyRows(questions: QuestionRecord[]): FrequencyRow[] {
  const counts = new Map<string, number>();
  for (const question of questions) counts.set(question.knowledgePoint, (counts.get(question.knowledgePoint) ?? 0) + 1);
  const rows = knowledgePoints
    .map((point) => ({ ...point, count: counts.get(point.slug) ?? 0, highFrequency: false }))
    .filter((point) => point.count > 0)
    .sort((a, b) => b.count - a.count || a.label.localeCompare(b.label, "zh-CN"));
  const cutoff = Math.ceil(rows.length * 0.25);
  rows.forEach((row, index) => { row.highFrequency = index < cutoff && row.count >= 3; });
  return rows;
}

export function getAreaRows(questions: QuestionRecord[]) {
  const counts = new Map<string, number>();
  for (const question of questions) counts.set(question.area, (counts.get(question.area) ?? 0) + 1);
  return [...counts.entries()]
    .map(([area, count]) => ({ area, count, share: count / questions.length }))
    .sort((a, b) => b.count - a.count || a.area.localeCompare(b.area));
}

export function getKnowledgePointLabel(slug: string): string {
  return knowledgePoints.find((item) => item.slug === slug)?.label ?? slug;
}

export function stripHtml(value: string | null): string {
  return (value ?? "").replace(/<[^>]*>/g, " ").replace(/\s+/g, " ").trim();
}
