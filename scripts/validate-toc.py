from pathlib import Path
import re

front = Path("docs/00-student-outcome.md").read_text(encoding="utf-8")
informe = Path("docs/informe.md").read_text(encoding="utf-8")
toc = front.split("<!-- TOC:start -->")[1].split("<!-- TOC:end -->")[0]
links = re.findall(r"\]\(informe\.md#([^)]+)\)", toc)
anchors = set(re.findall(r'<a id="([^"]+)"></a>', informe))
missing = [a for a in links if a not in anchors]
print(f"TOC links: {len(links)}")
print(f"Anchors in informe: {len(anchors)}")
print(f"Missing: {len(missing)}")
for a in missing[:20]:
    print("  -", a)
