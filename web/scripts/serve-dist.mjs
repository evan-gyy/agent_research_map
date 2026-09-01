import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const webRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const dist = path.join(webRoot, "dist");
const prefix = "/agent_research_map";
const types = { ".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".css": "text/css; charset=utf-8", ".svg": "image/svg+xml", ".xml": "application/xml; charset=utf-8" };
const server = http.createServer((req, res) => {
  let pathname = decodeURIComponent(new URL(req.url ?? "/", "http://localhost").pathname);
  if (!pathname.startsWith(prefix)) { res.writeHead(404).end(); return; }
  pathname = pathname.slice(prefix.length) || "/";
  let file = path.join(dist, pathname);
  if (pathname.endsWith("/")) file = path.join(file, "index.html");
  if (!path.extname(file)) file = path.join(file, "index.html");
  const resolved = path.resolve(file);
  if (!resolved.startsWith(dist) || !fs.existsSync(resolved)) { res.writeHead(404).end(); return; }
  res.writeHead(200, { "Content-Type": types[path.extname(resolved)] ?? "application/octet-stream" });
  fs.createReadStream(resolved).pipe(res);
});
server.listen(4323, "127.0.0.1", () => console.log("Serving dist at http://127.0.0.1:4323"));
