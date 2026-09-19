import { createServer } from "node:http";
import { existsSync, readFileSync, unlinkSync, writeFileSync } from "node:fs";
import { dirname, extname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const markdownItId = process.env.MARKDOWN_IT_DIR
  ? join(process.env.MARKDOWN_IT_DIR, "markdown-it")
  : "markdown-it";
const MarkdownIt = require(markdownItId);
const puppeteer = require(join(process.env.MARKDOWN_IT_DIR || "", "puppeteer-core"));

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const docs = join(root, "docs");
const mdPath = join(docs, "informe.md");
const htmlPath = join(docs, "_informe-export.html");
const pdfPath = join(docs, "informe.pdf");
const chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const mime = {
  ".html": "text/html; charset=utf-8",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".gif": "image/gif",
  ".svg": "image/svg+xml",
  ".webp": "image/webp",
};

const md = new MarkdownIt({ html: true, linkify: true, breaks: false });

const toWebAsset = (src) => {
  const decoded = decodeURIComponent(src).replace(/\\/g, "/");
  const idx = decoded.indexOf("assets/");
  if (idx >= 0) return "/" + decoded.slice(idx);
  return src;
};

let source = readFileSync(mdPath, "utf8");
source = source.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, (_, alt, src) => {
  const safeAlt = alt.replace(/"/g, "&quot;");
  return `<img src="${toWebAsset(src)}" alt="${safeAlt}">`;
});
source = source.replace(/src="((?:\.\.\/)?assets\/[^"]+)"/g, (_, src) => `src="${toWebAsset(src)}"`);

const body = md.render(source);
const html = `<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Informe SafePlant — Macallys</title>
  <style>
    @page { size: A4; margin: 14mm 12mm 16mm 12mm; }
    body { font-family: "Segoe UI", Arial, sans-serif; font-size: 11pt; line-height: 1.45; color: #111; }
    h1 { font-size: 20pt; page-break-before: always; margin-top: 0; }
    h1:first-of-type { page-break-before: avoid; }
    h2 { font-size: 15pt; margin-top: 1.4em; }
    h3, h4 { font-size: 13pt; }
    img { max-width: 100%; height: auto; display: block; margin: 12px auto; page-break-inside: avoid; }
    table { border-collapse: collapse; width: 100%; margin: 10px 0; font-size: 9.5pt; }
    th, td { border: 1px solid #bbb; padding: 5px 7px; vertical-align: top; }
    th { background: #f3f3f3; }
    pre, code { white-space: pre-wrap; word-break: break-word; font-size: 9pt; }
    blockquote { border-left: 3px solid #ccc; margin-left: 0; padding-left: 12px; color: #333; }
  </style>
</head>
<body>
${body}
</body>
</html>`;

writeFileSync(htmlPath, html, "utf8");

const server = createServer((req, res) => {
  const urlPath = decodeURIComponent((req.url || "/").split("?")[0]);
  const file = resolve(root, urlPath.replace(/^\/+/, ""));
  if (!file.startsWith(root) || !existsSync(file)) {
    res.writeHead(404);
    res.end();
    return;
  }
  const type = mime[extname(file).toLowerCase()] || "application/octet-stream";
  res.writeHead(200, { "Content-Type": type });
  res.end(readFileSync(file));
});

await new Promise((resolveListen) => server.listen(0, "127.0.0.1", resolveListen));
const { port } = server.address();
const url = `http://127.0.0.1:${port}/docs/_informe-export.html`;

const browser = await puppeteer.launch({
  executablePath: chrome,
  headless: true,
  args: ["--disable-gpu", "--no-first-run"],
});

try {
  const page = await browser.newPage();
  await page.goto(url, { waitUntil: "networkidle0", timeout: 180000 });
  await page.pdf({
    path: pdfPath,
    format: "A4",
    printBackground: true,
    displayHeaderFooter: false,
    margin: { top: "14mm", bottom: "16mm", left: "12mm", right: "12mm" },
  });
} finally {
  await browser.close();
  server.close();
  try {
    unlinkSync(htmlPath);
  } catch {
    /* ignore */
  }
}

console.log(`PDF escrito: ${pdfPath}`);
