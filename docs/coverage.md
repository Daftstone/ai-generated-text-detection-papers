# 检索覆盖、来源与版本说明

[返回首页](../README.md) · [水印列表](watermark.md) · [补充条目](supplementary.md)

本页保留原索引的检索来源与缺口记录。检索快照：**2026-10-23**；时间范围为 **2024–2026 会议年**。整理为 GitHub 版本不代表重新完成了逐条联网核验，后续新增或修正应更新这里的日期和记录。

目录等级依据：[CCF 官方入口](https://www.ccf.org.cn/Academic_Evaluation/By_category/)、[第七版转载说明](https://kyc.lsu.edu.cn/2026/0518/c1772a367789/page.htm)、[已核对目录 PDF](https://kyc.lsu.edu.cn/_upload/article/files/20/77/2cbaa3754eb9aff9ed74cafed8ff/23a8de02-594c-445f-b084-69b0193c05b3.pdf)。等级属于 2026 目录快照，不能直接作为往年成果认定结论。

## 年度 paper list 与覆盖边界

主要采用“年度paper list/论文集标题扫描 → 题名与摘要筛选 → 官方论文页/出版记录交叉核对”。关键词含 machine-generated / AI-generated / LLM-generated / machine-revised / text detection / authorship / attribution / human-AI / watermark / evasion / paraphrasing 等。官方XML允许按卷别识别Long、Short、Findings等。初步标题扫描产生5,409条候选题录，候选还包含大量其他检测任务，随后进行筛选；这个数字不是相关论文数量。

| 会议/来源 | 已实际加载的年度入口 | 本次覆盖边界 |
|---|---|---|
| ACL | [2024](https://aclanthology.org/events/acl-2024/) · [2025](https://aclanthology.org/events/acl-2025/) · [2026](https://aclanthology.org/events/acl-2026/) | 官方XML完整加载，主会和其他卷分开 |
| EMNLP | [2024](https://aclanthology.org/events/emnlp-2024/) · [2025](https://aclanthology.org/events/emnlp-2025/) · [2026名单页](https://2026.emnlp.org/program/main_papers/) | 2024/2025官方XML完整加载；截至检索时2026名单页仅有标题、未给出可提取清单，Anthology XML亦未取得；2026明确存在缺口 |
| NAACL | [2024](https://aclanthology.org/events/naacl-2024/) · [2025](https://aclanthology.org/events/naacl-2025/) | 官方XML完整加载；未把2026 EACL当NAACL |
| COLING | [LREC-COLING 2024](https://aclanthology.org/events/lrec-2024/) · [2025](https://aclanthology.org/events/coling-2025/) | 官方XML完整加载；联办单列。2026 IJCNLP/AACL不是COLING |
| ICLR | [2024](https://iclr.cc/virtual/2024/papers.html) · [2025](https://iclr.cc/virtual/2025/papers.html) · [2026](https://iclr.cc/virtual/2026/papers.html) | 三届官网paper list扫描，选中条目进一步查paper页和摘要 |
| ICML | [2024](https://proceedings.mlr.press/v235/) · [2025](https://proceedings.mlr.press/v267/) · [2026](https://proceedings.mlr.press/v306/) | 三届PMLR论文集＋官网paper list，Position单列 |
| NeurIPS | [2024论文集](https://papers.nips.cc/paper_files/paper/2024) · [2025官网](https://neurips.cc/virtual/2025/papers.html) · [2026官网](https://neurips.cc/virtual/2026/papers.html) | 官网名单和论文页扫描；D&B与特殊/Position轨道需按原页区分；2026未以投稿页冒充录用 |
| AAAI | [官方论文集](https://ojs.aaai.org/index.php/AAAI/issue/archive) · [2024题录镜像](https://github.com/papercopilot/paperlists/blob/main/aaai/aaai2024.json) · [2025题录镜像](https://github.com/papercopilot/paperlists/blob/main/aaai/aaai2025.json) · [2026题录镜像](https://huggingface.co/datasets/ai-conferences/AAAI2026) | 原站批量连接受限，用结构化二级镜像发现候选，重要检测条目通过官方论文页复核；不能把镜像当独立原始证据 |
| IJCAI / ECAI | [IJCAI 2024](https://www.ijcai.org/proceedings/2024/) · [2025](https://www.ijcai.org/proceedings/2025/) · [IJCAI/ECAI 2026](https://www.ijcai.org/proceedings/2026/) · [ECAI 2024名单](https://www.ecai2024.eu/programme/accepted-papers) | 三届IJCAI、ECAI 2024扫描；ECAI 2025未完成整届paper list核查 |
| KDD | [2024研究轨道](https://kdd.org/kdd2024/research-track-papers/) · [2025研究轨道](https://kdd.org/kdd2025/research-track-papers-2/) · [2025 D&B](https://kdd.org/kdd2025/datasets-and-benchmarks-track-papers-2/) · [2026](https://kdd2026.kdd.org/papers/) | 2026解析两轮官网内嵌JSON共1,415条；2024不代表所有伴随轨道均已穷尽 |
| SIGIR | [2024论文集](https://sigir-2024.github.io/proceedings) · [2025名单](https://sigir2025.dei.unipd.it/accepted-papers.html) · [2026官网内嵌名单](https://sigir2026.org/) | 三届入口扫描；2026低资源特殊轨道单列 |
| CIKM | [2024 ACM SIGWEB题录](https://www.sigweb.org/toc/cikm24.html) · [2025名单](https://www.cikm2025.org/program/accepted-papers) · [2026 program](https://cikm2026.diag.uniroma1.it/program/) | 2025按fp/sp/rp识别形式；PersonaGen是resource；2026依官网program |
| WWW / WSDM | [WWW 2024](https://www.sigweb.org/toc/www24.html) · [WWW 2024 Companion](https://www.sigweb.org/toc/www24a.html) · [WWW 2025题录镜像](https://github.com/papercopilot/paperlists/blob/main/www/www2025.json) · [WWW 2026研究轨道名单](https://www2026.thewebconf.org/accepted/research-tracks.html) · [WSDM 2024](https://www.sigweb.org/toc/wsdm24.html) · [WSDM 2025](https://www.sigweb.org/toc/wsdm25.html) | WWW 2026研究轨道已扫描；伴随轨道和WSDM 2026未完整抓取，不能声称整届已查全 |
| CCS | [2024](https://www.sigsac.org/ccs/CCS2024/program/accepted-papers.html) · [2025](https://www.sigsac.org/ccs/CCS2025/accepted-papers/) · [2026](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) | 2024/2026名单完整抓取；2025返回内容不完整，明确保留缺口 |
| USENIX Security | [2024](https://www.usenix.org/conference/usenixsecurity24/technical-sessions) · [2025](https://www.usenix.org/conference/usenixsecurity25/technical-sessions) · [2026](https://www.usenix.org/conference/usenixsecurity26/technical-sessions) | 三届technical sessions及选中论文页 |
| S&P | [2024](https://sp2024.ieee-security.org/accepted-papers.html) · [2025](https://sp2025.ieee-security.org/accepted-papers.html) · [2026](https://sp2026.ieee-security.org/accepted-papers.html) | 名单扫描；部分纯文本标题不是锚点，原始页面一并保留，仍存在漏检风险 |
| NDSS | [2024](https://www.ndss-symposium.org/ndss2024/accepted-papers/) · [2025](https://www.ndss-symposium.org/ndss2025/accepted-papers/) · [2026](https://www.ndss-symposium.org/ndss2026/accepted-papers/) | 三届主会名单；不能将DEMASQ等可能的Workshop工作直接算主会 |
| 其他 | [ECML-PKDD 2025](https://ecmlpkdd.org/2025/accepted-papers/) · [COLT 2024](https://proceedings.mlr.press/v247/) · [ACM MM 2024镜像](https://github.com/papercopilot/paperlists/blob/main/acmmm/acmmm2024.json) | 另做ICDM/SDM/ICDE/ESORICS/RAID等定向搜索；未完成所有CCF A/B会议、所有年度的逐卷核查；不报告“无相关论文”的强结论 |

## 版本与排除记录

- **年份按正式会议年**：Fast-DetectGPT、DNA-GPT、OUTFOX等可以有2023预印本，但正式发表是2024，因此纳入。DetectGPT（ICML 2023）、RADAR（NeurIPS 2023）不在本次2024–2026清单范围内。
- **CheckGPT题名已核对**：清单使用CCS 2024的正式题名，而不是早期“Check Me If You Can…”；两者不重复计数。
- **水印与事后检测分开**：模型所有权水印、训练集审计、embedding服务水印不能自动当成普通文本来源检测。本索引主动排除了大多数此类条目；模型所有权相关工作仅作为相邻问题示例单列。
- **相同数据资源不等于独立证据**：M4/M4GT-Bench/SemEval任务、RAID及其共享任务有继承关系；清单按论文计数，不能把这些论文数量当作互相独立的benchmark数量。
- **发现官方元数据错误**：COLING 2025的Post-Hoc Watermarking页面误贴AgentSimp摘要，已核对官方PDF首页；中文说明不采用错误摘要。
- **筛除标题近似的误检**：例如Stability-Weighted Direction Regularization实际为AI图像检测，On the Coexistence and Ensembling of Watermarks实际为图像水印；二者未纳入结果。
- **未确认录用不纳入正式清单**：arXiv、OpenReview的“under review”本身不构成会议录用证据；例如此前线索BRED没有因此被写成已录用ICLR 2026。

## 证据强度和局限

未计入上述总数的待核线索：

- [Old N-Grams Never Die: Towards Identifying LLMs-Generated Text using Antique N-Grams](https://openreview.net/pdf?id=oOf83pSxUP)：检索到的原始PDF仍写under review，未在本次已抓取的ICLR 2026录用名单中匹配到；不据第三方聚合站将其写成已录用。
- [When New Generators Arrive: Lifelong Machine-Generated Text Attribution via Ridge Feature Transfer（作者团队页面）](https://github.com/AntCPLab/AntCPLab.github.io/blob/master/index.md)：作者公开页面声称EMNLP 2026 main录用；本次未取得官方完整名单和正式论文记录，保留为需交叉核对的线索。

原索引以题名、会议/卷别、年份和可追溯入口作为事实字段；仍待确认的论文形式与发表状态保留标记。中文研究切入点是基于题名/摘要的归纳。部分条目只查到官方名单，摘要、最终题名或长短轨道未能全部核定，已经标记。本文没有复现算法、重新计算指标，也没有把不同benchmark结果合成性能排名。

这份清单对ACL、ICLR、ICML、NeurIPS等重点会议覆盖较深，但不能称为所有CCF A/B会议近三年无遗漏清单。最明显的待补部分是EMNLP 2026、WWW 2026伴随轨道、CCS 2025不完整页面、WSDM 2026，以及若干B类会议的其他年度。另用recognition / identifying / machine-written等表述补扫描，补入自我生成文本识别、AI释义片段定位和采样可检测性等容易漏掉的工作。

配套 [CSV](../data/papers.csv) 与 [JSON](../data/papers.json) 保留每条来源、核验层次、文章形式和状态，便于筛选和复查。本仓库提供的是筛选后的题录与列表生成脚本，不包含原始检索缓存、批量爬取脚本或论文全文。
