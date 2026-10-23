#!/usr/bin/env python3
"""Generate the GitHub paper list from data/papers.json (Python 3.9+, stdlib only)."""

import argparse
import csv
import io
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_DATE = "2026-10-23"
FIELDS = [
    "uid", "year", "venue", "ccf_2026", "section", "category", "paper_type",
    "title", "focus_zh", "url", "source_list", "verification", "publication_status",
]
GROUPS = [
    ("hybrid", "人机混写、润色与细粒度定位"),
    ("calibration", "统计校准与误报控制"),
    ("multilingual", "多语言与特定语言检测"),
    ("learning", "表征学习与跨域泛化"),
    ("statistics", "零样本、生成统计与免训练方法"),
    ("preference", "对齐与偏好信号"),
    ("style", "语言风格与结构信号"),
    ("applications", "其他检测方法与应用场景"),
    ("attribution", "来源归属与作者分析"),
    ("attacks", "规避攻击与鲁棒性"),
    ("benchmarks", "基准、评测与检测边界"),
]


def group_key(p):
    # Only classify using the existing category/focus labels; do not invent claims.
    category, focus = p["category"], p["focus_zh"]
    for label, key in [
        ("基准/评测/检测边界", "benchmarks"),
        ("检测攻击与鲁棒性", "attacks"),
        ("来源归属/作者分析", "attribution"),
    ]:
        if category == label:
            return key
    for terms, key in [
        (("人机混写", "细粒度", "定位", "润色"), "hybrid"),
        (("统计校准", "误报"), "calibration"),
        (("多语言", "跨语言", "韩语", "乌尔都语", "中文"), "multilingual"),
        (("跨域", "泛化", "表征", "对比学习"), "learning"),
        (("零样本", "概率/生成统计", "免训练"), "statistics"),
        (("对齐/偏好",), "preference"),
        (("语言风格/结构",), "style"),
    ]:
        if any(term in focus for term in terms):
            return key
    return "applications"


def safe(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(
        ">", "&gt;"
    ).replace("|", "&#124;").replace("[", "&#91;").replace(
        "]", "&#93;"
    ).replace("\n", " ").replace("\r", " ")


def ordered(papers):
    return sorted(papers, key=lambda p: (-p["year"], p["venue"].casefold(), p["title"].casefold()))


def table(papers):
    lines = [
        "| 会议 / 年份 / 目录等级 | 论文 | 形式与状态 | 研究标签 |",
        "|---|---|---|---|",
    ]
    for p in ordered(papers):
        form = p["paper_type"]
        form = {"long": "Long", "short": "Short", "main": "主会",
                "1": "LREC 卷 1（原始卷号）"}.get(form, form)
        if p["publication_status"] != "论文集/官网题录可核":
            form += "；**官网已列出，正式论文集待核**"
        venue = f"{safe(p['venue'])} {p['year']}<br>{safe(p['ccf_2026'])}"
        title = f'<a id="{p["uid"].lower()}"></a>[{safe(p["title"])}]({p["url"]})'
        focus = p["focus_zh"].replace("已用web工具读取", "已核对")
        lines.append(f"| {venue} | {title} | {safe(form)} | {safe(focus)} |")
    return "\n".join(lines) + "\n"


def heading(anchor, title, level=2):
    return f'<a id="{anchor}"></a>\n\n{"#" * level} {title}\n'


def load_papers():
    papers = json.loads((ROOT / "data/papers.json").read_text(encoding="utf-8"))
    ids, urls = set(), set()
    for p in papers:
        missing = set(FIELDS) - p.keys()
        if missing:
            raise ValueError(f"Missing fields: {missing}")
        if p["uid"] in ids or p["url"] in urls:
            raise ValueError(f"Duplicate ID or paper URL: {p['uid']}")
        ids.add(p["uid"])
        urls.add(p["url"])
        if p["year"] not in (2024, 2025, 2026):
            raise ValueError(f"Out-of-scope year: {p['uid']}")
        if not p["section"].startswith(tuple(f"{i}. " for i in range(1, 7))):
            raise ValueError(f"Unknown section: {p['section']}")
        for field in ("url", "source_list"):
            parsed = urlsplit(p[field])
            if parsed.scheme not in ("https", "http") or not parsed.netloc:
                raise ValueError(f"Invalid URL in {p['uid']}: {field}")
    return papers


def build(papers):
    sections = {i: [p for p in papers if p["section"].startswith(f"{i}. ")] for i in range(1, 7)}
    core, water = sections[1], sections[2]
    supplements = sum(len(sections[i]) for i in range(3, 7))
    parts = [f"""# AI-Generated Text Detection Paper List

**AI 生成文本 / 机器生成文本检测论文清单 · 2024–2026**

围绕文本生成来源识别，整理 CCF A/B 会议中的检测方法、人机混写与润色识别、来源归属、规避攻击和评测工作；文本水印另设页面，相关 Findings、短文和其他会议作为补充收录。

检索快照：**{SNAPSHOT_DATE}**。年份按正式会议年份统计；2026 年仅收录截至该日可核对的记录。

> **收录数量不等于 CCF 正式论文数量。** 本清单共 {len(papers)} 条去重记录：首页 {len(core)} 条，水印 {len(water)} 条，补充 {supplements} 条。会议目录等级、论文形式和发表状态分别标注；部分主会条目的长短轨道仍待核定。

## 导航

- [收录范围与标注规则](#scope)
- [统计与会议分布](#overview)
- [检测方向列表](#papers)
"""]
    for key, title in GROUPS:
        n = sum(group_key(p) == key for p in core)
        if n:
            parts.append(f"  - [{title}（{n}）](#{key})\n")
    parts.append(f"""- [文本水印、检测与攻击（{len(water)}）](docs/watermark.md)
- [Findings、其他轨道与边界补充（{supplements}）](docs/supplementary.md)
- [检索覆盖、年度 paper list 与已知缺口](docs/coverage.md)
- [数据说明](#data) · [贡献指南](CONTRIBUTING.md)

""")
    parts.append(heading("scope", "收录范围与标注规则"))
    parts.append("""
- **研究对象**：自然语言文本的生成来源，包括整篇检测、人机混写定位、AI 润色 / 改写识别、生成器归属，以及相应攻击和评测。
- **时间口径**：2024–2026 会议年，而非首次 arXiv 上传年。DetectGPT（ICML 2023）、RADAR（NeurIPS 2023）等早期工作不在本轮范围内。
- **CCF 口径**：按 **2026 年第七版目录快照**标注；其中 ICLR 为 A、IJCAI 为 B。这不是各单位对往年成果的追溯认定结论。参见 [CCF 官网](https://www.ccf.org.cn/Academic_Evaluation/By_category/)、[第七版转载说明](https://kyc.lsu.edu.cn/2026/0518/c1772a367789/page.htm)与[目录 PDF](https://kyc.lsu.edu.cn/_upload/article/files/20/77/2cbaa3754eb9aff9ed74cafed8ff/23a8de02-594c-445f-b084-69b0193c05b3.pdf)。
- **论文形式**：Short、Demo、Findings、Workshop 等不能直接按所依托会议的 A/B 等级认定，故另列。ICLR / ICML / NeurIPS 的 Poster 通常是展示形式，不能据此当作 Short。EMNLP / COLING 部分条目保留“长/短文轨道未逐篇核定”。
- **水印边界**：水印通常依赖生成端控制、密钥或其他额外信息，与无水印的事后检测分列。
- **证据与分类**：表中标签基于原索引的题名 / 已查摘要归纳。每篇仅分配一个主分组，多种属性保留在研究标签中；分组不是互斥的方法分类或性能排名。原始来源与核验层次见 [JSON](data/papers.json)。

本清单尚未覆盖所有 A/B 会议的全部年度与轨道，也未逐篇精读或复现。缺口包括 EMNLP 2026、CCS 2025 的不完整页面、WSDM 2026 等，详见[覆盖说明](docs/coverage.md)。

""")
    parts.append(heading("overview", "统计与会议分布"))
    parts.append("\n| 收录板块 | 2024 | 2025 | 2026 | 合计 |\n|---|---:|---:|---:|---:|\n")
    labels = ["直接检测、归属、攻击与评测", "文本水印及其检测 / 攻击", "Findings、短文、Demo 与其他轨道", "LREC-COLING 联办主会", "非 A/B 目录补充", "相邻问题与 Position"]
    for i, label in enumerate(labels, 1):
        counts = Counter(p["year"] for p in sections[i])
        parts.append(f"| {label} | {counts[2024]} | {counts[2025]} | {counts[2026]} | {len(sections[i])} |\n")
    counts = Counter(p["year"] for p in papers)
    parts.append(f"| **全部记录** | **{counts[2024]}** | **{counts[2025]}** | **{counts[2026]}** | **{len(papers)}** |\n\n")
    parts.append("<details>\n<summary>首页直接相关条目：按会议与年份展开</summary>\n\n| 会议 | 2026 目录等级 | 2024 | 2025 | 2026 | 合计 |\n|---|---|---:|---:|---:|---:|\n")
    for venue in sorted({p["venue"] for p in core}):
        subset = [p for p in core if p["venue"] == venue]
        counts = Counter(p["year"] for p in subset)
        grades = " / ".join(sorted({p["ccf_2026"] for p in subset}))
        parts.append(f"| {safe(venue)} | {grades} | {counts[2024]} | {counts[2025]} | {counts[2026]} | {len(subset)} |\n")
    parts.append("\n数字 0 表示本清单未收录该会议该年的相关条目，不代表没有相关论文。\n\n</details>\n\n")
    parts.append(heading("papers", f"检测方向列表（{len(core)} 条）"))
    parts.append("\n组内按会议年份降序排列，同年按会议和题名排序。点击题名进入论文页；部分链接指向官方录用名单。\n\n")
    for key, title in GROUPS:
        subset = [p for p in core if group_key(p) == key]
        if subset:
            parts.append(heading(key, f"{title}（{len(subset)} 条）", 3))
            parts.append("\n" + table(subset) + "\n")
    parts.append(heading("data", "数据与维护"))
    parts.append("""
- [papers.json](data/papers.json)：完整元数据，作为维护的数据源；保留稳定 ID、会议年、目录等级、论文形式、来源和核验记录。
- [papers.csv](data/papers.csv)：同一批记录，UTF-8 BOM 编码，方便用 Excel 筛选。
- [覆盖说明](docs/coverage.md)：年度论文集入口、检索方法、版本纠错及待核线索。
- [贡献指南](CONTRIBUTING.md)：新增论文、补全轨道或纠正元数据的要求。

在仓库根目录运行以下命令即可重新生成列表和 CSV，只需 Python 3.9 或更高版本，无第三方依赖：

```bash
python scripts/build_readme.py
python scripts/build_readme.py --check
```

`--check` 检查元数据基本结构及生成文件是否同步；它不联网验证论文链接和录用状态。更新数据时，请同步核对本页的检索日期与覆盖说明。

论文、PDF 和代码的权利归各自权利人。此仓库仅整理题录与链接，不代为授予论文或第三方代码许可。
""")

    watermark = ["# 文本水印、检测与攻击\n\n[返回首页](../README.md) · [补充条目](supplementary.md) · [覆盖说明](coverage.md)\n\n",
                 f"共 **{len(water)} 条**，来自主索引的水印板块。检索快照：{SNAPSHOT_DATE}。\n\n",
                 "水印依赖的生成端控制、密钥或其他额外信息，应与无水印的事后检测区别理解。表中目录等级不代表对具体论文形式的认定；部分条目仅核到官网名单，状态保留如下。\n\n",
                 "按年份浏览：" + " · ".join(f"[{year}](#year-{year})" for year in (2026, 2025, 2024)) + "\n\n"]
    for year in (2026, 2025, 2024):
        subset = [p for p in water if p["year"] == year]
        watermark += [heading(f"year-{year}", f"{year}（{len(subset)} 条）"), "\n" + table(subset) + "\n"]

    supplemental = ["# 补充条目与研究边界\n\n[返回首页](../README.md) · [水印列表](watermark.md) · [覆盖说明](coverage.md)\n\n",
                    f"共 **{supplements} 条**，检索快照：{SNAPSHOT_DATE}。这些条目用于补充研究脉络，不能整体计作 CCF A/B 正式论文。\n\n"]
    descriptions = {
        3: "这些论文的 Findings、Short、Demo 等形式不直接套用所依托会议的 A/B 等级。研究标签包含检测和水印两类，未计入首页与水印主列表。",
        4: "CCF 目录列 COLING，而不独立列 LREC；LREC-COLING 2024 的联办成果认定需按所在单位口径处理。",
        5: "EACL、LREC 等不能仅因收录于 ACL Anthology 就标成 CCF A/B。",
        6: "包含多模态、事实真伪、模型所有权以及 Position 等邻近问题；具体边界见各条研究标签。即使会议属于 A/B，也不代表论文是本清单关注的通用文本来源检测方法。",
    }
    for i in range(3, 7):
        supplemental.append(f"- [{labels[i - 1]}（{len(sections[i])}）](#section-{i})\n")
    supplemental.append("\n")
    for i in range(3, 7):
        supplemental += [heading(f"section-{i}", f"{labels[i - 1]}（{len(sections[i])} 条）"),
                         "\n" + descriptions[i] + "\n\n", table(sections[i]), "\n"]

    csv_buffer = io.StringIO(newline="")
    writer = csv.DictWriter(csv_buffer, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows({key: p[key] for key in FIELDS} for p in papers)
    return {
        "README.md": ("".join(parts).rstrip() + "\n").encode("utf-8"),
        "docs/watermark.md": ("".join(watermark).rstrip() + "\n").encode("utf-8"),
        "docs/supplementary.md": ("".join(supplemental).rstrip() + "\n").encode("utf-8"),
        "data/papers.csv": csv_buffer.getvalue().encode("utf-8-sig"),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check generated files without writing")
    args = parser.parse_args()
    papers = load_papers()
    outputs = build(papers)
    outdated = []
    for relative, content in outputs.items():
        path = ROOT / relative
        if args.check:
            if not path.exists() or path.read_bytes() != content:
                outdated.append(relative)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
    if outdated:
        parser.exit(1, "Outdated files: " + ", ".join(outdated) + "\n")
    print(f"{'Checked' if args.check else 'Generated'} {len(outputs)} files; {len(papers)} records.")


if __name__ == "__main__":
    main()
