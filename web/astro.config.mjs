import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://evan-gyy.github.io",
  base: "/agent_research_map",
  trailingSlash: "always",
  output: "static",
  integrations: [sitemap()],
  vite: { build: { sourcemap: false } },
});
