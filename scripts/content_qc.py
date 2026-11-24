#!/usr/bin/env python3
"""QC tự động cho bài trong posts/ theo CONTENT-QC.md.

Dùng:
  python3 scripts/content_qc.py                      # quét mọi bài
  python3 scripts/content_qc.py posts/abc.md         # quét 1 bài
  python3 scripts/content_qc.py --check-links        # thêm kiểm link sống/chết
  python3 scripts/content_qc.py --report qc-reports  # ghi báo cáo Markdown
  python3 scripts/content_qc.py --strict             # exit 1 nếu có bài FAIL
"""
import argparse
import csv
import glob
import os
import re
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "data/keywords/2026-11-23/cluster-keyword-map.csv")

REQUIRED_FIELDS = ["title", "slug", "path", "description", "author", "published",
                   "updated", "dataDate", "status"]
QC_FIELDS = ["reviewer", "lastReviewed", "tested", "aiAssisted", "sources"]

PATTERNS_A = {
    "A1 mở bài sáo": r"(?i)(trong bài viết này|ngày nay,|trong những năm gần đây|trong kỷ nguyên|thời đại số|không thể phủ nhận|hãy cùng [^.\n]{0,20}tìm hiểu)",
    "A2 câu đệm": r"(?i)(đáng chú ý là|điều quan trọng (cần|là phải) lưu ý|cần lưu ý rằng|như đã đề cập)",
    "A3 placeholder": r"\[(INSERT|SOURCE|DATE|LINK|CẦN|TODO|TBD)[^\]]*\]|\bTODO\b|lorem ipsum",
    "A3 chuyên gia vô danh": r"(?i)(các |nhiều )?chuyên gia (cho rằng|nhận định|khuyên)",
    "A3 kết luận lặp": r"(?im)^#+\s*(kết luận|tóm lại|lời kết)\s*$",
    "C1 thời gian mơ hồ": r"(?i)\b(gần đây|tuần trước|hôm qua|mới đây|vừa qua)\b",
}
DESC_BAD = r"(?i)(bài viết này|this article|in this|outline|\.\.\.$|…$)"
AI_LABEL = r"(?i)AI hỗ trợ soạn thảo|AI-assisted|có sử dụng AI hỗ trợ"


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    _, fm, body = text.split("---", 2)
    data, key = {}, None
    for line in fm.splitlines():
        if re.match(r"^\s+-\s+", line) and key:
            data.setdefault(key, [])
            if isinstance(data[key], list):
                data[key].append(line.strip()[2:].strip().strip('"'))
            continue
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).split(" #")[0].strip()
        if val.startswith("[") and val.endswith("]"):
            data[key] = [v.strip().strip('"') for v in val[1:-1].split(",") if v.strip()]
        elif val == "":
            data[key] = []
        else:
            data[key] = val.strip('"')
    return data, body


def load_csv():
    if not os.path.exists(CSV_PATH):
        return []
    with open(CSV_PATH, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def check_url(url):
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "Mozilla/5.0 KimQ-QC"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return 0


def qc_post(path, posts_meta, csv_rows, check_links):
    text = open(path, encoding="utf-8").read()
    fm, body = parse_frontmatter(text)
    slug = os.path.basename(path)[:-3]
    is_pillar = fm.get("type") == "pillar"
    fails, flags, info = [], [], {}

    missing = [k for k in REQUIRED_FIELDS if not fm.get(k)]
    if missing:
        fails.append(f"Thiếu frontmatter: {', '.join(missing)}")
    missing_qc = [k for k in QC_FIELDS if k not in fm or fm.get(k) in ("", [])]
    if missing_qc:
        flags.append(f"Thiếu trường QC: {', '.join(missing_qc)}")

    desc = fm.get("description", "")
    first_para = next((p.strip() for p in body.split("\n\n") if p.strip() and not p.strip().startswith((">", "#", "|", "!"))), "")
    if re.search(DESC_BAD, desc):
        fails.append("A1 description có cụm kiểu AI hoặc bị cắt")
    if desc and desc[:80] == first_para[:80]:
        fails.append("A1 description chép câu đầu bài")
    if desc and not 70 <= len(desc) <= 200:
        flags.append(f"description dài {len(desc)} ký tự (nên 120–170)")

    for name, pat in PATTERNS_A.items():
        hits = [m.group(0) for m in re.finditer(pat, body)]
        if hits:
            msg = f"{name}: {len(hits)} chỗ ({', '.join(sorted(set(h.strip() for h in hits))[:3])})"
            (fails if name.startswith(("A1", "A3 placeholder")) else flags).append(msg)

    words = len(re.findall(r"\w+", body))
    info["words"] = words
    if is_pillar and words < 2500:
        flags.append(f"Pillar {words} từ (cần ≥ 2.500)")
    if not is_pillar and words < 1200:
        flags.append(f"Bài {words} từ (cần ≥ 1.200)")

    imgs = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", body)
    info["images"] = len(imgs)
    if len(imgs) < 3:
        fails.append(f"B1 {len(imgs)} ảnh thao tác (cần ≥ 3)")

    links = re.findall(r"\]\((https?://[^)\s]+)\)", body)
    ext = sorted({u for u in links if "kimq.tech" not in u})
    info["external"] = len(ext)
    if len(ext) < 2:
        fails.append(f"B3 {len(ext)} nguồn ngoài (cần ≥ 2)")

    reviewer = fm.get("reviewer")
    if not reviewer:
        fails.append("B2 chưa có reviewer (người thật, khác người viết)")
    elif reviewer == fm.get("author"):
        fails.append("B2 reviewer trùng author")
    if not re.search(AI_LABEL, body):
        flags.append("B4 thiếu dòng nhãn AI hỗ trợ cuối bài")

    if not fm.get("dataDate"):
        fails.append("C2 thiếu dataDate")
    if fm.get("updated") and fm.get("lastReviewed") and fm["lastReviewed"] < fm.get("published", ""):
        flags.append("lastReviewed trước ngày đăng")

    internal = re.findall(r"\]\(([a-z0-9-]+)\.md\)", body)
    if not is_pillar:
        pillar = fm.get("pillar")
        if not pillar:
            flags.append("D thiếu trường pillar")
        elif pillar not in internal:
            fails.append("D không link về pillar")
        cluster = fm.get("cluster")
        siblings = [s for s, m in posts_meta.items() if s != slug and m.get("cluster") == cluster]
        linked = [s for s in siblings if s in internal]
        need = min(2, len(siblings))
        if len(linked) < need:
            flags.append(f"D link {len(linked)}/{need} bài cùng cluster ({', '.join(s for s in siblings if s not in internal)})")
        if pillar in posts_meta:
            pillar_body = posts_meta[pillar]["_body"]
            if f"({slug}.md)" not in pillar_body:
                flags.append("D pillar chưa link tới bài này")
    else:
        children = [s for s, m in posts_meta.items() if m.get("pillar") == slug]
        missing_children = [c for c in children if c not in internal]
        if missing_children:
            fails.append(f"D pillar chưa link: {', '.join(missing_children)}")

    kws = [k.lower() for k in (fm.get("keywords") or []) if isinstance(k, str)]
    for row in csv_rows:
        kw = (row.get("main_kw") or "").lower().strip()
        if kw and kw in kws and row.get("file") != slug:
            flags.append(f"D từ khoá '{kw}' thuộc bài khác: {row.get('article')}")

    if check_links:
        dead = []
        for u in ext:
            code = check_url(u)
            if code == 0 or code >= 400:
                dead.append(f"{u} ({code or 'lỗi kết nối'})")
        if dead:
            fails.append("B3 link hỏng: " + "; ".join(dead))

    status = "FAIL" if fails else ("FLAG" if flags else "PASS")
    return {"slug": slug, "path": path, "status": status, "fails": fails, "flags": flags,
            "info": info, "title": fm.get("title", slug)}


def render(res):
    out = [f"# QC: {res['title']}", "",
           f"- Kết quả tự động: **{res['status']}**",
           f"- File: [{res['slug']}.md](../posts/{res['slug']}.md)",
           f"- Số từ: {res['info'].get('words')} · Ảnh: {res['info'].get('images')} · Nguồn ngoài: {res['info'].get('external')}", ""]
    out += ["## Lỗi phải sửa", ""] + ([f"- [ ] {x}" for x in res["fails"]] or ["- Không có"]) + [""]
    out += ["## Cần xem lại", ""] + ([f"- [ ] {x}" for x in res["flags"]] or ["- Không có"]) + [""]
    out += ["## Phần agent/người duyệt kiểm tay", "",
            "- [ ] C1: đối chiếu 3 số liệu với nguồn gốc (ghi số liệu, nguồn, kết quả)",
            "- [ ] C3: tên sản phẩm, công ty, model đúng chính tả của hãng",
            "- [ ] C4: văn bản pháp luật có số hiệu và link nguồn chính thức",
            "- [ ] EOT/SA: Effort _/5 · Originality _/5 · Talent _/5 · Accuracy _/5 (cần ≥ 15/20)",
            "- [ ] Người duyệt ký: ______ ngày ______", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--check-links", action="store_true")
    ap.add_argument("--report")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    all_posts = sorted(glob.glob(os.path.join(ROOT, "posts/*.md")))
    posts_meta = {}
    for p in all_posts:
        fm, body = parse_frontmatter(open(p, encoding="utf-8").read())
        fm["_body"] = body
        posts_meta[os.path.basename(p)[:-3]] = fm
    targets = [os.path.abspath(f) for f in a.files] or all_posts
    csv_rows = load_csv()
    results = [qc_post(p, posts_meta, csv_rows, a.check_links) for p in targets]
    for r in results:
        print(f"{r['status']:4}  {r['slug']}")
        for x in r["fails"]:
            print(f"      ✗ {x}")
        for x in r["flags"]:
            print(f"      ! {x}")
    if a.report:
        os.makedirs(a.report, exist_ok=True)
        for r in results:
            open(os.path.join(a.report, r["slug"] + ".md"), "w", encoding="utf-8").write(render(r))
        rows = ["# Tổng hợp QC tự động", "", "Sinh bởi `scripts/content_qc.py`. Phần kiểm tay xem trong từng file.", "",
                "| Bài | Kết quả | Lỗi | Cần xem | Từ | Ảnh | Nguồn |", "|---|---|---|---|---|---|---|"]
        for r in results:
            rows.append(f"| [{r['slug']}]({r['slug']}.md) | {r['status']} | {len(r['fails'])} | {len(r['flags'])} | {r['info'].get('words')} | {r['info'].get('images')} | {r['info'].get('external')} |")
        open(os.path.join(a.report, "README.md"), "w", encoding="utf-8").write("\n".join(rows) + "\n")
    counts = {s: sum(r["status"] == s for r in results) for s in ("PASS", "FLAG", "FAIL")}
    print(f"\nPASS {counts['PASS']} · FLAG {counts['FLAG']} · FAIL {counts['FAIL']}")
    if a.strict and counts["FAIL"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
