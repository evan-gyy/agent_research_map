import assert from "node:assert/strict";
import test from "node:test";
import { getAllQuestions, getAreaRows, getFrequencyRows } from "../src/lib/content";

test("formal questions parse into a public whitelist", async () => {
  const questions = await getAllQuestions();
  assert.equal(questions.length, 118);
  assert.deepEqual(Object.keys(questions[0]).sort(), [
    "answerHtml", "area", "collectedAt", "id", "knowledgePoint", "sourceUrl", "tags", "title", "verificationLabel",
  ].sort());
  assert.equal(questions[0].id, "Q0001");
  assert.equal(questions.at(-1)?.id, "Q0118");
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
