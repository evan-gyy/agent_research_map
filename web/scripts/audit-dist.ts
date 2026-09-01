import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const webRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const dist = path.join(webRoot, "dist");
const forbiddenVisible = ["招聘", "求职", "面试", "面经", "岗位"];
const forbiddenFields = ["company", "source_track", "legacy_id", "页面标题", "面经小节"];
const files: string[] = [];
function walk(dir: string) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full);
    else if (/\.(html|json|js|xml)$/.test(entry.name)) files.push(full);
  }
}
walk(dist);
const errors: string[] = [];
for (const file of files) {
  const content = fs.readFileSync(file, "utf8");
  const withoutScripts = file.endsWith(".html")
    ? content.replace(/<script[^>]*>[\s\S]*?<\/script>/gi, "").replace(/<style[^>]*>[\s\S]*?<\/style>/gi, "")
    : content;
  const words = file.endsWith(".js") ? forbiddenVisible : [...forbiddenVisible, ...forbiddenFields];
  for (const word of words) {
    if (withoutScripts.includes(word)) errors.push(path.relative(dist, file) + " 包含禁用内容：" + word);
  }
}
if (errors.length) throw new Error(errors.slice(0, 20).join("\n"));
console.log("Dist audit passed: " + files.length + " public files checked.");
