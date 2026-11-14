/**
 * Exporta docs/informe.md a PDF (A4) usando el Chrome instalado en el sistema.
 *
 * Uso (desde la raíz del repo):
 *     node scripts/export-pdf.mjs
 */

import { existsSync } from "node:fs";
import { mkdir, readFile, rm, writeFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

import MarkdownIt from "markdown-it";
import puppeteer from "puppeteer-core";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const SOURCE = join(ROOT, "docs", "informe.md");
const TEMP_HTML = join(ROOT, "docs", ".informe-export.html");
const OUTPUT = join(ROOT, "docs", "informe.pdf");

const CHROME_CANDIDATES = [
  "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
  "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
];

const STYLES = `
  :root { color-scheme: light; }
  body {
    font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.55;
    color: #1f2328;
    margin: 0;
  }
  h1, h2, h3, h4, h5, h6 {
    line-height: 1.25;
    margin: 1.4em 0 0.6em;
    page-break-after: avoid;
    break-after: avoid-page;
    page-break-inside: avoid;
    break-inside: avoid;
  }
  h1 {
    font-size: 20pt;
    border-bottom: 1px solid #d1d9e0;
    padding-bottom: 0.2em;
    page-break-before: always;
    break-before: page;
    margin-top: 0;
  }
  /* Evita página en blanco al inicio si el primer h1 abre el cuerpo. */
  h1:first-of-type { page-break-before: avoid; break-before: auto; }
  h2 { font-size: 16pt; border-bottom: 1px solid #d1d9e0; padding-bottom: 0.2em; }
  h3 { font-size: 13.5pt; }
  h4 { font-size: 12pt; }
  h5, h6 { font-size: 11pt; }
  p, li { orphans: 3; widows: 3; }
  a { color: #0969da; text-decoration: none; word-break: break-word; }
  code, kbd, pre { font-family: "Cascadia Mono", Consolas, monospace; font-size: 9.5pt; }
  code { background: #f0f1f3; padding: 0.15em 0.35em; border-radius: 4px; }
  pre {
    background: #f6f8fa;
    padding: 10px 12px;
    border-radius: 6px;
    overflow-wrap: break-word;
    white-space: pre-wrap;
    page-break-inside: avoid;
    break-inside: avoid;
  }
  pre code { background: none; padding: 0; }
  blockquote { margin: 1em 0; padding: 0 1em; color: #59636e; border-left: 4px solid #d1d9e0; }
  /* Los separadores del ensamblado no se imprimen: el corte lo marca la página. */
  hr { display: none; }
  /* Imágenes más compactas para evitar hojas casi vacías. */
  img {
    max-width: 100%;
    max-height: 130mm;
    height: auto;
    display: block;
    margin: 0.4em auto 0.8em;
    page-break-inside: avoid;
    break-inside: avoid;
  }
  img[src*="mobile"],
  img[src*="execution_sprint2_mobile"],
  img[src*="video-about"] {
    max-height: 105mm;
  }
  figure.exec-shot {
    margin: 0.5em 0 0.9em;
    page-break-inside: avoid;
    break-inside: avoid;
  }
  figure.exec-shot img {
    max-height: 105mm;
    margin: 0 auto 0.35em;
  }
  figure.exec-shot figcaption {
    font-size: 9.5pt;
    text-align: center;
    color: #424a53;
    margin: 0;
  }
  .page-break {
    break-before: page;
    page-break-before: always;
    height: 0;
    margin: 0;
    padding: 0;
    border: 0;
  }
  table {
    border-collapse: collapse;
    width: 100%;
    margin: 0.8em 0;
    font-size: 9.5pt;
    page-break-inside: auto;
    break-inside: auto;
  }
  table th, table td { border: 1px solid #d1d9e0; padding: 5px 8px; vertical-align: top; word-break: break-word; }
  table th { background: #f6f8fa; }
  tr, td, th { page-break-inside: avoid; break-inside: avoid; }
  thead { display: table-header-group; }
  tfoot { display: table-footer-group; }
  @page { size: A4; margin: 18mm 15mm 16mm 15mm; }
  /* Carátula sola en la primera página; el siguiente bloque empieza limpio. */
  .caratula {
    font-size: 10pt;
    line-height: 1.2;
    page-break-after: always;
    break-after: page;
  }
  .caratula img { max-height: 30mm; width: auto; margin: 0 auto 2mm; }
  .caratula p { margin: 2.2mm 0; }
  .caratula table { width: auto; margin: 2mm auto; font-size: 9.5pt; }
  .caratula table th, .caratula table td { padding: 2px 10px; }
`;

/** Evita que Markdown-it trate títulos como texto crudo tras bloques HTML. */
function normalizeMarkdown(markdown) {
  return markdown
    .replace(/<\/table>(\s*)(?=<a id=|#{1,6}\s)/g, "</table>\n\n")
    .replace(/^(<a id="[^"]+"><\/a>)[ \t]*\n(?=#{1,6}\s)/gm, "$1\n\n")
    .replace(/\n{4,}/g, "\n\n\n");
}

function findChrome() {
  const fromEnv = process.env.CHROME_PATH;
  if (fromEnv && existsSync(fromEnv)) return fromEnv;
  const found = CHROME_CANDIDATES.find((candidate) => existsSync(candidate));
  if (!found) {
    throw new Error(
      "No se encontró Chrome ni Edge. Define la variable de entorno CHROME_PATH con la ruta del ejecutable.",
    );
  }
  return found;
}

/** Junta título + captura para que no queden en páginas distintas. */
function wrapExecutionShots(html) {
  return html.replace(
    /<p>((?:Mobile|Web|IoT|Backend|Testing)[^<]*)<\/p>\s*<p><img ([^>]+)><\/p>/g,
    "<figure class=\"exec-shot\"><img $2><figcaption>$1</figcaption></figure>",
  );
}

async function main() {
  const markdown = normalizeMarkdown(await readFile(SOURCE, "utf8"));
  const md = new MarkdownIt({ html: true, linkify: true, breaks: false });
  const body = wrapExecutionShots(md.render(markdown));

  const html = `<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Informe del Trabajo Final — SafePlant</title>
<style>${STYLES}</style>
</head>
<body>
${body}
</body>
</html>
`;

  await mkdir(dirname(TEMP_HTML), { recursive: true });
  await writeFile(TEMP_HTML, html, "utf8");

  const browser = await puppeteer.launch({
    executablePath: findChrome(),
    headless: true,
    args: ["--allow-file-access-from-files", "--no-sandbox"],
  });

  try {
    const page = await browser.newPage();
    await page.goto(`file:///${TEMP_HTML.replace(/\\/g, "/")}`, {
      waitUntil: "networkidle0",
      timeout: 180000,
    });
    await page.pdf({
      path: OUTPUT,
      format: "A4",
      printBackground: true,
      displayHeaderFooter: true,
      headerTemplate: "<div></div>",
      footerTemplate:
        '<div style="width:100%;font-family:Segoe UI,Arial,sans-serif;font-size:8pt;color:#59636e;text-align:center;">' +
        '<span class="pageNumber"></span> / <span class="totalPages"></span></div>',
      margin: { top: "18mm", right: "15mm", bottom: "16mm", left: "15mm" },
      timeout: 300000,
    });
  } finally {
    await browser.close();
    if (!process.argv.includes("--keep-html")) {
      await rm(TEMP_HTML, { force: true });
    }
  }

  console.log(`PDF generado: ${OUTPUT}`);
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});
