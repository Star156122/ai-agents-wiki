#!/usr/bin/env python3
"""檢查 Wiki 與簡報（只用標準函式庫）。用法：python3 tools/check.py"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
errors, warnings = [], []

def err(msg): errors.append(msg)
def warn(msg): warnings.append(msg)

def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    data = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data

pages = sorted(p for p in WIKI.rglob("*.md") if p.name not in ("index.md", "log.md"))
source_ids = {p.name.split("-")[0] + "-" + p.name.split("-")[1]: p for p in (WIKI / "sources").glob("src-*.md")}

# 1 + 2：frontmatter、來源頁
for p in pages:
    rel = p.relative_to(WIKI)
    text = p.read_text(encoding="utf-8")
    fm = frontmatter(text)
    if fm is None:
        err(f"[frontmatter] {rel} 缺少 frontmatter"); continue
    for key in ("title", "type", "sources", "updated"):
        if key not in fm:
            err(f"[frontmatter] {rel} 缺少欄位 {key}")
    if fm.get("type") == "concept":
        ids = re.findall(r"src-\d+", fm.get("sources", ""))
        if not ids:
            err(f"[sources] {rel} 沒有列出任何來源")
        for sid in ids:
            if sid not in source_ids:
                err(f"[sources] {rel} 引用不存在的來源 {sid}")
        cited = set(re.findall(r"\[(src-\d+)\]", text))
        for sid in cited - set(ids):
            err(f"[sources] {rel} 內文標註 {sid}，但 frontmatter 未列出")
        if not cited:
            err(f"[sources] {rel} 內文沒有任何 [src-NN] 標註")
    if fm.get("type") == "source":
        if "**url**" not in text: err(f"[source] {rel} 缺少 url")
        if "**fetched**" not in text: err(f"[source] {rel} 缺少 fetched")
        quotes = re.findall(r"^>\s*\"(.+?)\"", text, re.M)
        if len(quotes) > 1:
            err(f"[quote] {rel} 直接引用超過 1 則")
        for q in quotes:
            if len(q.split()) > 15:
                err(f"[quote] {rel} 引用超過 15 字：{len(q.split())} 字")

# 3：index 完整性、壞連結
index_text = (WIKI / "index.md").read_text(encoding="utf-8")
for p in pages:
    rel = p.relative_to(WIKI).as_posix()
    if rel not in index_text:
        err(f"[index] wiki/index.md 沒有列出 {rel}")
for p in list(WIKI.rglob("*.md")):
    for target in re.findall(r"\]\(([^)#]+\.md)\)", p.read_text(encoding="utf-8")):
        if target.startswith("http"): continue
        if not (p.parent / target).exists():
            err(f"[link] {p.relative_to(WIKI)} 連到不存在的 {target}")

# 4：簡報對應與術語接地
html = (ROOT / "index.html").read_text(encoding="utf-8")
slides = re.findall(r'<section class="slide" data-wiki="([^"]*)" data-terms="([^"]*)">(.*?)</section>', html, re.S)
used = set()
if not slides:
    err("[slides] 找不到任何投影片")
for n, (wiki_attr, terms_attr, body) in enumerate(slides, 1):
    wiki_pages = [w.strip() for w in wiki_attr.split(",") if w.strip()]
    if not wiki_pages:
        err(f"[slides] 第 {n} 張沒有 data-wiki"); continue
    corpus = ""
    for w in wiki_pages:
        f = WIKI / w
        if not f.exists():
            err(f"[slides] 第 {n} 張的 data-wiki 不存在：{w}")
        else:
            used.add(w); corpus += f.read_text(encoding="utf-8").lower()
    for term in [t.strip() for t in terms_attr.split(",") if t.strip()]:
        if term.lower() not in corpus:
            err(f"[grounding] 第 {n} 張的術語「{term}」沒有出現在 {wiki_attr}")
    # 簡報不得出現 Wiki 沒有的 4 位數年份
    for yr in set(re.findall(r"\b(?:19|20)\d{2}\b", re.sub(r"<[^>]+>", " ", body))):
        if yr not in corpus:
            err(f"[grounding] 第 {n} 張出現年份 {yr}，但來源頁沒有")

# 5：覆蓋率
for p in pages:
    rel = p.relative_to(WIKI).as_posix()
    if rel.startswith("concepts/") and rel not in used:
        err(f"[coverage] {rel} 沒有被任何投影片使用")

print(f"檢查完成：投影片 {len(slides)} 張、Wiki 頁面 {len(pages)} 頁")
for w in warnings: print("WARN ", w)
for e in errors: print("ERROR", e)
print(f"結果：{len(errors)} 個錯誤，{len(warnings)} 個警告")
sys.exit(1 if errors else 0)
