import { defineConfig, devices } from "@playwright/test";
export default defineConfig({
  testDir: "./e2e", fullyParallel: true, retries: process.env.CI ? 2 : 0, reporter: process.env.CI ? "github" : "list",
  use: { baseURL: "http://127.0.0.1:4323/agent_research_map", trace: "on-first-retry" },
  webServer: { command: "node scripts/serve-dist.mjs", url: "http://127.0.0.1:4323/agent_research_map/", reuseExistingServer: !process.env.CI },
  projects: [{ name: "chromium", use: { ...devices["Desktop Chrome"] } }],
});
