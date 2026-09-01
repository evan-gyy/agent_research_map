import fs from "node:fs";
import { getAllQuestions, getFrequencyRows, topicsDir } from "../src/lib/content";

const questions = await getAllQuestions();
const fileCount = fs.readdirSync(topicsDir).filter((name) => name.endsWith(".md")).length;
if (questions.length !== fileCount) throw new Error("题目文件数与解析结果不一致");
if (questions.length === 0) throw new Error("正式题库为空");

const ids = questions.map((question) => Number(question.id.slice(1)));
if (new Set(ids).size !== ids.length) throw new Error("存在重复题号");
const missing = [];
for (let id = Math.min(...ids); id <= Math.max(...ids); id += 1) {
  if (!ids.includes(id)) missing.push("Q" + String(id).padStart(4, "0"));
}
if (missing.length) throw new Error("题号不连续，缺少：" + missing.join(", "));

const frequencyTotal = getFrequencyRows(questions).reduce((sum, row) => sum + row.count, 0);
if (frequencyTotal !== questions.length) throw new Error("知识点频率发生重复或遗漏计数");
console.log("Content valid: " + questions.length + " questions, " + getFrequencyRows(questions).length + " knowledge points.");
