#!/usr/bin/env python3
"""Chèn ảnh chụp màn hình từ data/screenshots.json vào bài.

Ảnh đặt sau đoạn đầu tiên dưới tiêu đề `after`, kèm chú thích có link nguồn và ngày chụp.
Chạy lại nhiều lần không bị chèn trùng. Dùng: python3 scripts/insert_images.py [slug ...]
"""
import json
import os
import sys
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def fmt_date(iso):
    y, m, d = iso.split("-")
    return f"{d}/{m}/{y}"


def block(slug, shot):
    domain = urlparse(shot["url"]).netloc.replace("www.", "")
    return [
        f"![{shot['alt']}](../images/{slug}/{shot['name']}.webp)",
        "",
        f"*Ảnh chụp màn hình: {shot['alt']}. Nguồn: [{domain}]({shot['url']}), chụp ngày {fmt_date(shot['captured'])}.*",
        "",
    ]


def insert(slug, shots):
    path = os.path.join(ROOT, "posts", f"{slug}.md")
    lines = open(path, encoding="utf-8").read().split("\n")
    changed = 0
    for shot in shots:
        ref = f"../images/{slug}/{shot['name']}.webp"
        if any(ref in l for l in lines):
            continue
        if not os.path.exists(os.path.join(ROOT, "images", slug, f"{shot['name']}.webp")):
            print(f"  thiếu file ảnh: {slug}/{shot['name']}")
            continue
        try:
            i = lines.index(shot["after"]) + 1
        except ValueError:
            print(f"  không thấy tiêu đề: {slug} | {shot['after']}")
            continue
        while i < len(lines) and not lines[i].strip():
            i += 1
        if i < len(lines) and not lines[i].startswith("#"):
            while i < len(lines) and lines[i].strip():
                i += 1
        lines[i:i] = [""] + block(slug, shot)[:-1]
        changed += 1
    if changed:
        open(path, "w", encoding="utf-8").write("\n".join(lines))
    print(f"{slug}: chèn {changed} ảnh")


def main():
    spec = json.load(open(os.path.join(ROOT, "data/screenshots.json"), encoding="utf-8"))
    for slug in sys.argv[1:] or spec:
        insert(slug, spec.get(slug, []))


if __name__ == "__main__":
    main()
