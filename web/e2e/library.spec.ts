import { expect, test } from "@playwright/test";
test("dashboard and question filtering work under the Pages base path", async ({ page }) => {
  await page.goto("/agent_research_map/"); await expect(page.getByRole("heading", { name: /把零散问题/ })).toBeVisible(); await expect(page.getByText("117", { exact: true }).first()).toBeVisible();
  await page.getByRole("link", { name: /浏览全部题目/ }).click(); await page.getByRole("searchbox").fill("Q0117"); await expect(page.locator("[data-result-count]")).toHaveText("1"); await expect(page.getByRole("heading", { name: "Flash Attention 的原理是什么？" })).toBeVisible();
});
test("desktop question rows stay compact with metadata aligned to the right", async ({ page }) => {
  await page.setViewportSize({ width: 1440, height: 1000 });
  await page.goto("/agent_research_map/questions/");
  const cards = page.locator("[data-question-card]");
  await expect(cards).toHaveCount(117);
  const layout = await cards.first().evaluate((card) => {
    const row = card.getBoundingClientRect();
    const main = card.querySelector(".question-card-main")!.getBoundingClientRect();
    const meta = card.querySelector(".question-card-meta")!.getBoundingClientRect();
    return { height: row.height, metaStartsAfterMain: meta.left >= main.right - 1 };
  });
  expect(layout.height).toBeLessThanOrEqual(64);
  expect(layout.metaStartsAfterMain).toBe(true);
});
test("area and knowledge point filters hide non-matching question rows", async ({ page }) => {
  await page.goto("/agent_research_map/questions/");
  const cards = page.locator("[data-question-card]");
  await page.getByLabel("Evaluation").check();
  await expect(page.locator("[data-result-count]")).toHaveText("7");
  await expect(cards.filter({ visible: true })).toHaveCount(7);
  await expect(cards.filter({ visible: true }).first()).toHaveAttribute("data-area", "Evaluation");
  await page.getByLabel("全部分类").check();
  await page.getByLabel("知识点").selectOption("evaluation-metrics-datasets");
  const expected = await page.locator('[data-question-card][data-point="evaluation-metrics-datasets"]').count();
  await expect(page.locator("[data-result-count]")).toHaveText(String(expected));
  await expect(cards.filter({ visible: true })).toHaveCount(expected);
});
test("local learning progress persists after refresh", async ({ page }) => {
  await page.goto("/agent_research_map/questions/q0008/"); await page.getByRole("button", { name: "已掌握" }).click(); await page.getByRole("button", { name: "收藏" }).click(); await page.reload(); await expect(page.getByRole("button", { name: "已掌握" })).toHaveClass(/active/); await expect(page.getByRole("button", { name: "收藏" })).toHaveText(/已收藏/);
});
test("detail page renders notes and neutral source information", async ({ page }) => {
  await page.goto("/agent_research_map/questions/q0015/"); await expect(page.getByRole("heading", { name: "核心回答" })).toBeVisible(); await expect(page.locator(".katex").first()).toBeVisible(); await expect(page.getByRole("link", { name: "查看原始链接" })).toHaveAttribute("href", new RegExp("^https://")); await expect(page.locator("body")).not.toContainText(/招聘|求职|面试|面经|岗位/);
});
test("mobile pages avoid horizontal overflow and expose the filter drawer", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/agent_research_map/questions/");
  await expect(page.getByRole("button", { name: "筛选与分类" })).toBeVisible();
  await page.getByRole("button", { name: "筛选与分类" }).click();
  await expect(page.getByRole("complementary")).toBeVisible();
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
  await page.goto("/agent_research_map/questions/q0015/");
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
});

test("agent atlas compares products and renders source-backed product details", async ({ page }) => {
  await page.goto("/agent_research_map/agents/");
  await expect(page.getByRole("heading", { name: "主流 Agent 案例" })).toBeVisible();
  await expect(page.locator(".agent-product-card")).toHaveCount(2);
  await page.getByLabel("选择知识点").selectOption("context-token-compression");
  await expect(page.locator("[data-agent-point]:visible")).toHaveCount(1);
  await expect(page.locator("[data-agent-point]:visible .agent-practice-card")).toHaveCount(2);
  await page.getByRole("link", { name: /查看完整案例/ }).first().click();
  await expect(page.getByRole("heading", { name: "Codex 案例" })).toBeVisible();
  await expect(page.locator(".agent-document .mermaid").first()).toBeVisible();
  await expect(page.getByRole("heading", { name: "十二、来源" })).toBeVisible();
});

test("question details link their knowledge point to product practices", async ({ page }) => {
  await page.goto("/agent_research_map/questions/q0003/");
  await expect(page.getByRole("heading", { name: "主流 Agent 怎么做" })).toBeVisible();
  await expect(page.locator(".agent-practice-mini")).toHaveCount(2);
  await page.getByRole("link", { name: "横向比较" }).click();
  await expect(page.getByLabel("选择知识点")).toHaveValue("context-token-compression");
  await expect(page.locator("[data-agent-point]:visible")).toHaveCount(1);
});

test("agent atlas and product details avoid mobile overflow", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/agent_research_map/agents/");
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
  await page.goto("/agent_research_map/agents/claude-code/");
  await expect(page.locator(".agent-document .mermaid").first()).toBeVisible();
  const overflow = await page.evaluate(() => ({
    fits: document.documentElement.scrollWidth <= window.innerWidth,
    offenders: [...document.querySelectorAll<HTMLElement>("body *")]
      .filter((element) => element.getBoundingClientRect().right > window.innerWidth + 1 && !element.closest(".agent-flow"))
      .slice(0, 8)
      .map((element) => element.tagName.toLowerCase() + "." + element.className),
  }));
  expect(overflow.fits, overflow.offenders.join(", ")).toBe(true);
});
