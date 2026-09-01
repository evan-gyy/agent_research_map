# AI · LLM 学习库网站

这是一个由 ../ai-llm-learn/Topics 下 Markdown 构建的纯静态 Astro 网站。正式 Markdown 题库是唯一内容源；网站只发布白名单字段，不复制第二份题库，也不使用数据库或后端 API。

## 本地使用

    npm ci
    npm run data:check
    npm run dev

本地地址为 http://localhost:4321/agent_research_map/ 。学习状态、收藏和最近浏览只写入浏览器 localStorage。

新增正式题目时，在 Markdown frontmatter 中填写受控的 knowledge_point 与 tags。知识点目录位于 src/data/knowledge-points.json；构建会拒绝题号不连续、来源链接缺失、知识点未知或重复计数的内容。

## 验证与构建

    npm run check
    npm test
    npm run build
    npm run test:e2e

npm run build 会生成 dist，并审计最终公开文件，阻止求职定位文本与私有来源字段进入网站。端到端测试需要先执行 npx playwright install chromium。

## GitHub Pages

.github/workflows/pages.yml 在 master 分支的题库或网站文件变更后自动校验、构建、浏览器测试并部署。仓库首次启用时，在 GitHub 的 Settings → Pages → Build and deployment 中把 Source 设为 GitHub Actions。站点路径按项目 Pages 配置为 /agent_research_map/。
