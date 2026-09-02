import assert from "node:assert/strict";
import test from "node:test";
import { getAgentPracticesForPoint, getAgentProducts, getAllQuestions, getAreaRows, getFrequencyRows, knowledgePoints } from "../src/lib/content";

test("formal questions parse into a public whitelist", async () => {
  const questions = await getAllQuestions();
  assert.equal(questions.length, 117);
  assert.deepEqual(Object.keys(questions[0]).sort(), [
    "answerHtml", "area", "collectedAt", "id", "knowledgePoint", "sourceUrl", "tags", "title", "verificationLabel",
  ].sort());
  assert.equal(questions[0].id, "Q0001");
  assert.equal(questions.at(-1)?.id, "Q0117");
});

test("frequency counts each question exactly once", async () => {
  const questions = await getAllQuestions();
  const rows = getFrequencyRows(questions);
  assert.equal(rows.reduce((sum, row) => sum + row.count, 0), questions.length);
  assert.ok(rows.filter((row) => row.highFrequency).every((row) => row.count >= 3));
});

test("area statistics cover the full bank", async () => {
  const questions = await getAllQuestions();
  assert.equal(getAreaRows(questions).reduce((sum, row) => sum + row.count, 0), questions.length);
});

test("agent product documents and knowledge-point mappings are valid", async () => {
  const products = await getAgentProducts();
  const knownPoints = new Set(knowledgePoints.map((point) => point.slug));
  assert.deepEqual(products.map((product) => product.slug), ["codex", "claude-code"]);
  assert.ok(products.every((product) => product.contentHtml.includes("<h2")));
  assert.ok(products.every((product) => product.practices.length >= 10));
  assert.ok(products.flatMap((product) => product.practices).every((practice) => knownPoints.has(practice.point)));
  assert.equal((await getAgentPracticesForPoint("context-token-compression")).length, 2);
});
