# AI-Generated Text Detection Paper List

**AI 生成文本 / 机器生成文本检测论文清单 · 2024–2026**

围绕文本生成来源识别，整理 CCF A/B 会议中的检测方法、人机混写与润色识别、来源归属、规避攻击和评测工作；文本水印另设页面，相关 Findings、短文和其他会议作为补充收录。

检索快照：**2026-10-23**。年份按正式会议年份统计；2026 年仅收录截至该日可核对的记录。

> **收录数量不等于 CCF 正式论文数量。** 本清单共 384 条去重记录：首页 139 条，水印 134 条，补充 111 条。会议目录等级、论文形式和发表状态分别标注；部分主会条目的长短轨道仍待核定。

## 导航

- [收录范围与标注规则](#scope)
- [统计与会议分布](#overview)
- [检测方向列表](#papers)
  - [人机混写、润色与细粒度定位（17）](#hybrid)
  - [统计校准与误报控制（5）](#calibration)
  - [多语言与特定语言检测（3）](#multilingual)
  - [表征学习与跨域泛化（15）](#learning)
  - [零样本、生成统计与免训练方法（17）](#statistics)
  - [对齐与偏好信号（1）](#preference)
  - [语言风格与结构信号（5）](#style)
  - [其他检测方法与应用场景（35）](#applications)
  - [来源归属与作者分析（8）](#attribution)
  - [规避攻击与鲁棒性（12）](#attacks)
  - [基准、评测与检测边界（21）](#benchmarks)
- [文本水印、检测与攻击（134）](docs/watermark.md)
- [Findings、其他轨道与边界补充（111）](docs/supplementary.md)
- [检索覆盖、年度 paper list 与已知缺口](docs/coverage.md)
- [数据说明](#data) · [贡献指南](CONTRIBUTING.md)

<a id="scope"></a>

## 收录范围与标注规则

- **研究对象**：自然语言文本的生成来源，包括整篇检测、人机混写定位、AI 润色 / 改写识别、生成器归属，以及相应攻击和评测。
- **时间口径**：2024–2026 会议年，而非首次 arXiv 上传年。DetectGPT（ICML 2023）、RADAR（NeurIPS 2023）等早期工作不在本轮范围内。
- **CCF 口径**：按 **2026 年第七版目录快照**标注；其中 ICLR 为 A、IJCAI 为 B。这不是各单位对往年成果的追溯认定结论。参见 [CCF 官网](https://www.ccf.org.cn/Academic_Evaluation/By_category/)、[第七版转载说明](https://kyc.lsu.edu.cn/2026/0518/c1772a367789/page.htm)与[目录 PDF](https://kyc.lsu.edu.cn/_upload/article/files/20/77/2cbaa3754eb9aff9ed74cafed8ff/23a8de02-594c-445f-b084-69b0193c05b3.pdf)。
- **论文形式**：Short、Demo、Findings、Workshop 等不能直接按所依托会议的 A/B 等级认定，故另列。ICLR / ICML / NeurIPS 的 Poster 通常是展示形式，不能据此当作 Short。EMNLP / COLING 部分条目保留“长/短文轨道未逐篇核定”。
- **水印边界**：水印通常依赖生成端控制、密钥或其他额外信息，与无水印的事后检测分列。
- **证据与分类**：表中标签基于原索引的题名 / 已查摘要归纳。每篇仅分配一个主分组，多种属性保留在研究标签中；分组不是互斥的方法分类或性能排名。原始来源与核验层次见 [JSON](data/papers.json)。

本清单尚未覆盖所有 A/B 会议的全部年度与轨道，也未逐篇精读或复现。缺口包括 EMNLP 2026、CCS 2025 的不完整页面、WSDM 2026 等，详见[覆盖说明](docs/coverage.md)。

<a id="overview"></a>

## 统计与会议分布

| 收录板块 | 2024 | 2025 | 2026 | 合计 |
|---|---:|---:|---:|---:|
| 直接检测、归属、攻击与评测 | 39 | 50 | 50 | 139 |
| 文本水印及其检测 / 攻击 | 35 | 40 | 59 | 134 |
| Findings、短文、Demo 与其他轨道 | 25 | 34 | 22 | 81 |
| LREC-COLING 联办主会 | 5 | 0 | 0 | 5 |
| 非 A/B 目录补充 | 3 | 0 | 13 | 16 |
| 相邻问题与 Position | 2 | 1 | 6 | 9 |
| **全部记录** | **109** | **125** | **150** | **384** |

<details>
<summary>首页直接相关条目：按会议与年份展开</summary>

| 会议 | 2026 目录等级 | 2024 | 2025 | 2026 | 合计 |
|---|---|---:|---:|---:|---:|
| AAAI | A | 2 | 1 | 5 | 8 |
| ACL | A | 10 | 11 | 16 | 37 |
| CCS | A | 2 | 0 | 0 | 2 |
| CIKM | B | 0 | 0 | 2 | 2 |
| COLING | B | 0 | 7 | 0 | 7 |
| ECAI | B | 2 | 0 | 0 | 2 |
| EMNLP | B | 4 | 11 | 0 | 15 |
| ICLR | A | 6 | 5 | 7 | 18 |
| ICML | A | 1 | 1 | 7 | 9 |
| IJCAI | B | 2 | 0 | 2 | 4 |
| KDD | A | 0 | 2 | 0 | 2 |
| NAACL | B | 3 | 1 | 0 | 4 |
| NeurIPS | A | 6 | 8 | 9 | 23 |
| S&amp;P | A | 0 | 0 | 1 | 1 |
| SIGIR | A | 0 | 1 | 0 | 1 |
| USENIX Security | A | 1 | 1 | 0 | 2 |
| WWW | A | 0 | 1 | 1 | 2 |

数字 0 表示本清单未收录该会议该年的相关条目，不代表没有相关论文。

</details>

<a id="papers"></a>

## 检测方向列表（139 条）

组内按会议年份降序排列，同年按会议和题名排序。点击题名进入论文页；部分链接指向官方录用名单。

<a id="hybrid"></a>

### 人机混写、润色与细粒度定位（17 条）

| 会议 / 年份 / 目录等级 | 论文 | 形式与状态 | 研究标签 |
|---|---|---|---|
| AAAI 2026<br>A | <a id="p0665"></a>[HLPD: Aligning LLMs to Human Language Preference for Machine-Revised Text Detection](https://ojs.aaai.org/index.php/AAAI/article/view/40297) | 主会 | 人机混写/润色；对齐/偏好信号 |
| AAAI 2026<br>A | <a id="p0712"></a>[Multi-level Style Preference Optimization: An Adaptive Detection Framework for Human-Machine Hybrid Text](https://ojs.aaai.org/index.php/AAAI/article/view/40665) | 主会 | 人机混写/润色；细粒度/定位；对齐/偏好信号；语言风格/结构 |
| ACL 2026<br>A | <a id="p1059"></a>[Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection](https://aclanthology.org/2026.acl-long.235/) | Long | 人机混写/润色；细粒度/定位 |
| ACL 2026<br>A | <a id="p1092"></a>[DMHM: Density-aware Manifold Learning and Hybrid Mahalanobis Energy for LLMs-generated Text Detection](https://aclanthology.org/2026.acl-long.180/) | Long | 人机混写/润色 |
| ACL 2026<br>A | <a id="p1132"></a>[LAMCL: A Length-aware Momentum Contrastive Learning Framework for Multiscale Machine-Revised Text Detection](https://aclanthology.org/2026.acl-long.1118/) | Long | 人机混写/润色；细粒度/定位；表征/对比学习 |
| ICML 2026<br>A | <a id="p3394"></a>[On the Salience of Low-Probability Tokens for AI-Generated Text Detection: A Multiscale Uncertainty Perspective](https://proceedings.mlr.press/v306/guo26w.html) | 主会 | 细粒度/定位；概率/生成统计 |
| NeurIPS 2026<br>A | <a id="p4867"></a>[LensCT: Fine-Grained AI-Involved Text Detection via Temporal-Hierarchical Tomograms of LLM Internals](https://neurips.cc/virtual/2026/poster/151027) | 官网列出；**官网已列出，正式论文集待核** | 细粒度/定位 |
| AAAI 2025<br>A | <a id="p0365"></a>[Imitate Before Detect: Aligning Machine Stylistic Preference for Machine-Revised Text Detection](https://ojs.aaai.org/index.php/AAAI/article/view/34525) | 主会 | 人机混写/润色；对齐/偏好信号；语言风格/结构 |
| ACL 2025<br>A | <a id="p0961"></a>[HACo-Det: A Study Towards Fine-Grained Machine-Generated Text Detection under Human-AI Coauthoring](https://aclanthology.org/2025.acl-long.1069/) | Long | 人机混写/润色；细粒度/定位 |
| EMNLP 2025<br>B | <a id="p1956"></a>[Non-Existent Relationship: Fact-Aware Multi-Level Machine-Generated Text Detection](https://aclanthology.org/2025.emnlp-main.186/) | 主会；长/短文轨道未逐篇核定 | 细粒度/定位 |
| EMNLP 2025<br>B | <a id="p1976"></a>[SenDetEX: Sentence-Level AI-Generated Text Detection for Human-AI Hybrid Content via Style and Context Fusion](https://aclanthology.org/2025.emnlp-main.268/) | 主会；长/短文轨道未逐篇核定 | 人机混写/润色；细粒度/定位；语言风格/结构 |
| NeurIPS 2025<br>A | <a id="p4480"></a>[DETree: DEtecting Human-AI Collaborative Texts via Tree-Structured Hierarchical Representation Learning](https://neurips.cc/virtual/2025/poster/115391) | 官网列出 | 人机混写/润色；表征/对比学习 |
| WWW 2025<br>A | <a id="p5364"></a>[Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement](https://openreview.net/forum?id=nB1Apc36yp) | 主会 | 细粒度/定位 |
| AAAI 2024<br>A | <a id="p0188"></a>[Towards Automatic Boundary Detection for Human-AI Collaborative Hybrid Essay in Education](https://ojs.aaai.org/index.php/AAAI/article/view/30258) | 主会特别轨道：AI for Social Impact | 人机混写/润色；细粒度/定位 |
| ICLR 2024<br>A | <a id="p2627"></a>[Multiscale Positive-Unlabeled Detection of AI-Generated Texts](https://iclr.cc/virtual/2024/poster/19428) | 官网列出 | 细粒度/定位 |
| IJCAI 2024<br>B | <a id="p3520"></a>[Detecting AI-Generated Sentences in Human-AI Collaborative Hybrid Texts: Challenges, Strategies, and Insights](https://www.ijcai.org/proceedings/2024/835) | 主会/轨道待核 | 人机混写/润色；细粒度/定位 |
| NeurIPS 2024<br>A | <a id="p4269"></a>[DeTeCtive: Detecting AI-generated Text via Multi-Level Contrastive Learning](https://papers.nips.cc/paper_files/paper/2024/hash/a117a3cd54b7affad04618c77c2fb18b-Abstract-Conference.html) | 官网列出 | 细粒度/定位；表征/对比学习 |

<a id="calibration"></a>

### 统计校准与误报控制（5 条）

| 会议 / 年份 / 目录等级 | 论文 | 形式与状态 | 研究标签 |
|---|---|---|---|
| ICLR 2026<br>A | <a id="p2826"></a>[Beyond Raw Detection Scores: Markov-Informed Calibration for Boosting Machine-Generated Text Detection](https://iclr.cc/virtual/2026/poster/10009986) | 官网列出 | 统计校准/误报控制 |
| NeurIPS 2026<br>A | <a id="p4872"></a>[Log-Likelihood, Simpson’s Paradox, and the Detection of Machine-Generated Text](https://neurips.cc/virtual/2026/poster/148606) | 官网列出；**官网已列出，正式论文集待核** | 统计校准/误报控制；概率/生成统计 |
| NeurIPS 2026<br>A | <a id="p5017"></a>[TriBet: Relative E-values for Online Machine-generated Text Detection](https://neurips.cc/virtual/2026/poster/155489) | 官网列出；**官网已列出，正式论文集待核** | 统计校准/误报控制 |
| ICML 2025<br>A | <a id="p3172"></a>[Online Detection of LLM-Generated Texts via Sequential Hypothesis Testing by Betting](https://proceedings.mlr.press/v267/chen25bn.html) | 主会 | 统计校准/误报控制 |
| NeurIPS 2025<br>A | <a id="p4434"></a>[AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees](https://neurips.cc/virtual/2025/poster/120036) | 官网列出 | 统计校准/误报控制 |

<a id="multilingual"></a>

### 多语言与特定语言检测（3 条）

| 会议 / 年份 / 目录等级 | 论文 | 形式与状态 | 研究标签 |
|---|---|---|---|
| ICLR 2026<br>A | <a id="p2921"></a>[Learning From Dictionary: Enhancing Robustness of Machine-Generated Text Detection in Zero-Shot Language via Adversarial Training](https://iclr.cc/virtual/2026/poster/10008607) | 官网列出 | 零样本；多语言/跨语言 |
| ACL 2025<br>A | <a id="p0938"></a>[Detection of Human and Machine-Authored Fake News in Urdu](https://aclanthology.org/2025.acl-long.170/) | Long | 乌尔都语 |
| ACL 2025<br>A | <a id="p0979"></a>[KatFishNet: Detecting LLM-Generated Korean Text through Linguistic Feature Analysis](https://aclanthology.org/2025.acl-long.1030/) | Long | 韩语；语言风格/结构 |

<a id="learning"></a>

### 表征学习与跨域泛化（15 条）

| 会议 / 年份 / 目录等级 | 论文 | 形式与状态 | 研究标签 |
|---|---|---|---|
| AAAI 2026<br>A | <a id="p0699"></a>[MGT-Prism: Enhancing Domain Generalization for Machine-Generated Text Detection via Spectral Alignment](https://ojs.aaai.org/index.php/AAAI/article/view/40485) | 主会 | 跨域/泛化；对齐/偏好信号 |
| ACL 2026<br>A | <a id="p1061"></a>[Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection](https://aclanthology.org/2026.acl-long.120/) | Long | 跨域/泛化；表征/对比学习 |
| ACL 2026<br>A | <a id="p1099"></a>[Exons-Detect: Identifying and Amplifying Exonic Tokens via Hidden-State Discrepancy for Robust AI-Generated Text Detection](https://aclanthology.org/2026.acl-long.1211/) | Long | 表征/对比学习 |
| ICML 2026<br>A | <a id="p3247"></a>[Black-Box Detection of LLM-Generated Text Using Generalized Jensen Shannon Divergence](https://proceedings.mlr.press/v306/chen26bf.html) | 主会 | 跨域/泛化 |
| NeurIPS 2026<br>A | <a id="p4979"></a>[Steer-to-Detect: Probing Hidden Representations for Detection of LLM-Generated Texts](https://neurips.cc/virtual/2026/poster/153916) | 官网列出；**官网已列出，正式论文集待核** | 表征/对比学习 |
| ACL 2025<br>A | <a id="p0983"></a>[Learning to Rewrite: Generalized LLM-Generated Text Detection](https://aclanthology.org/2025.acl-long.322/) | Long | 跨域/泛化 |
| COLING 2025<br>B | <a id="p1602"></a>[Controlling Out-of-Domain Gaps in LLMs for Genre Classification and Generated Text Detection](https://aclanthology.org/2025.coling-main.224/) | 主会；长/短文轨道未逐篇核定 | 跨域/泛化 |
| COLING 2025<br>B | <a id="p1661"></a>[Unmasking the Imposters: How Censorship and Domain Adaptation Affect the Detection of Machine-Generated Tweets](https://aclanthology.org/2025.coling-main.607/) | 主会；长/短文轨道未逐篇核定 | 社交文本；跨域/泛化 |
| EMNLP 2025<br>B | <a id="p1905"></a>[DivScore: Zero-Shot Detection of LLM-Generated Text in Specialized Domains](https://aclanthology.org/2025.emnlp-main.971/) | 主会；长/短文轨道未逐篇核定 | 零样本；跨域/泛化 |
| KDD 2025<br>A | <a id="x005"></a>[On the Generalization and Adaptation Ability of Machine-Generated Text Detectors in Academic Writing](https://doi.org/10.1145/3711896.3737408) | Datasets and Benchmarks | 学术写作检测的泛化和适配；MGTBench-2.0资源线 |
| NAACL 2025<br>B | <a id="p4100"></a>[Kill two birds with one stone: generalized and robust AI-generated text detection via dynamic perturbations](https://aclanthology.org/2025.naacl-long.446/) | Long | 跨域/泛化 |
| NeurIPS 2025<br>A | <a id="p4529"></a>[Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection](https://neurips.cc/virtual/2025/poster/120309) | 官网列出 | 跨域/泛化 |
| ACL 2024<br>A | <a id="p0860"></a>[Does DetectGPT Fully Utilize Perturbation? Bridging Selective Perturbation to Fine-tuned Contrastive Learning Detector would be Better](https://aclanthology.org/2024.acl-long.103/) | Long | 表征/对比学习 |
| ICLR 2024<br>A | <a id="p2602"></a>[Few-Shot Detection of Machine-Generated Text using Style Representations](https://iclr.cc/virtual/2024/poster/18293) | 官网列出 | 免训练/少样本；表征/对比学习；语言风格/结构 |
| USENIX Security 2024<br>A | <a id="p5162"></a>[Deciphering Textual Authenticity: A Generalized Strategy through the Lens of Large Language Semantics for Detecting Human vs. Machine-Generated Text](https://www.usenix.org/conference/usenixsecurity24/presentation/bethany) | 官网列出 | 跨域/泛化 |

<a id="statistics"></a>

### 零样本、生成统计与免训练方法（17 条）

| 会议 / 年份 / 目录等级 | 论文 | 形式与状态 | 研究标签 |
|---|---|---|---|
| AAAI 2026<br>A | <a id="p0792"></a>[SpecDetect: Simple, Fast, and Training-Free Detection of LLM-Generated Text via Spectral Analysis](https://ojs.aaai.org/index.php/AAAI/article/view/40510) | 主会 | 免训练/少样本 |
| ACL 2026<br>A | <a id="p1211"></a>[Zero-Shot Detection of LLM-Generated Text using Temperature Sensitivity](https://aclanthology.org/2026.acl-long.1748/) | Long | 零样本；概率/生成统计 |
| ICML 2026<br>A | <a id="p3372"></a>[Minimizing Mismatch Risk: A Prototype-Based Routing Framework for Zero-shot LLM-generated Text Detection](https://proceedings.mlr.press/v306/sun26b.html) | 主会 | 零样本 |
| ICML 2026<br>A | <a id="p3466"></a>[Telescope: Improving Zero Shot Detection of LLM Generated Content By Measuring Token Repetition Probability](https://proceedings.mlr.press/v306/nassif26a.html) | 主会 | 零样本；概率/生成统计 |
| IJCAI 2026<br>B | <a id="p3727"></a>[Information Entropy for LLM-generated Text Detection](https://www.ijcai.org/proceedings/2026/226) | 主会/轨道待核 | 概率/生成统计 |
| NeurIPS 2026<br>A | <a id="p4707"></a>[Alignment Imprint: Zero-Shot AI-Generated Text Detection via Provable Preference Discrepancy](https://neurips.cc/virtual/2026/poster/151776) | 官网列出；**官网已列出，正式论文集待核** | 零样本；对齐/偏好信号 |
| NeurIPS 2026<br>A | <a id="p4925"></a>[Pref-DetectGPT: Unveiling Machine-Generated Text via Preference-Aware Curvature Measurement](https://neurips.cc/virtual/2026/poster/152231) | 官网列出；**官网已列出，正式论文集待核** | 对齐/偏好信号；概率/生成统计 |
| COLING 2025<br>B | <a id="p1662"></a>[Who Wrote This? The Key to Zero-Shot LLM-Generated Text Detection Is GECScore](https://aclanthology.org/2025.coling-main.684/) | 主会；长/短文轨道未逐篇核定 | 零样本 |
| EMNLP 2025<br>B | <a id="p1912"></a>[Enhancing LLM Text Detection with Retrieved Contexts and Logits Distribution Consistency](https://aclanthology.org/2025.emnlp-main.503/) | 主会；长/短文轨道未逐篇核定 | 概率/生成统计 |
| ICLR 2025<br>A | <a id="p2716"></a>[Glimpse: Enabling White-Box Methods to Use Proprietary Models for Zero-Shot LLM-Generated Text Detection](https://iclr.cc/virtual/2025/poster/29149) | 官网列出 | 零样本 |
| ICLR 2025<br>A | <a id="p2791"></a>[Training-free LLM-generated Text Detection by Mining Token Probability Sequences](https://iclr.cc/virtual/2025/poster/27889) | 官网列出 | 免训练/少样本；概率/生成统计 |
| NeurIPS 2025<br>A | <a id="p4687"></a>[Zero-Shot Detection of LLM-Generated Text via Implicit Reward Model](https://neurips.cc/virtual/2025/poster/120141) | 官网列出 | 零样本；对齐/偏好信号 |
| EMNLP 2024<br>B | <a id="p1860"></a>[Zero-Shot Detection of LLM-Generated Text using Token Cohesiveness](https://aclanthology.org/2024.emnlp-main.971/) | 主会；长/短文轨道未逐篇核定 | 零样本 |
| ICLR 2024<br>A | <a id="p2596"></a>[DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text](https://iclr.cc/virtual/2024/poster/18444) | 官网列出 | 免训练/少样本 |
| ICLR 2024<br>A | <a id="p2601"></a>[Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature](https://iclr.cc/virtual/2024/poster/19201) | 官网列出 | 零样本；概率/生成统计 |
| ICML 2024<br>A | <a id="p3097"></a>[Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text](https://proceedings.mlr.press/v235/hans24a.html) | 主会 | 零样本 |
| NeurIPS 2024<br>A | <a id="p4259"></a>[DALD: Improving Logits-based Detector without Logits from Black-box LLMs](https://papers.nips.cc/paper_files/paper/2024/hash/62e5f22b5dae99ec700be622df4fbe0d-Abstract-Conference.html) | 官网列出 | 概率/生成统计 |

<a id="preference"></a>

### 对齐与偏好信号（1 条）

| 会议 / 年份 / 目录等级 | 论文 | 形式与状态 | 研究标签 |
|---|---|---|---|
| NeurIPS 2024<br>A | <a id="p4360"></a>[ReMoDetect: Reward Models Recognize Aligned LLM's Generations](https://papers.nips.cc/paper_files/paper/2024/hash/058373e239c542eae6cb796e4dc521da-Abstract-Conference.html) | 官网列出 | 对齐/偏好信号 |

<a id="style"></a>

### 语言风格与结构信号（5 条）

| 会议 / 年份 / 目录等级 | 论文 | 形式与状态 | 研究标签 |
|---|---|---|---|
| ACL 2026<br>A | <a id="p1068"></a>[CoCoNUTS: Concentrating on Content while Neglecting Uninformative Textual Styles for AI-Generated Peer Review Detection](https://aclanthology.org/2026.acl-long.1240/) | Long | 同行评审场景；语言风格/结构 |
| ICLR 2026<br>A | <a id="p2903"></a>[HLD: Approximate Hierarchical Linguistic Distribution Modeling for LLM-Generated Text Detection](https://iclr.cc/virtual/2026/poster/10007709) | 官网列出 | 语言风格/结构 |
| NeurIPS 2026<br>A | <a id="p5029"></a>[VERITAS: Veracity-Enhanced Robust Identification of LLM-generated Text Against Style-shifts](https://neurips.cc/virtual/2026/poster/148411) | 官网列出；**官网已列出，正式论文集待核** | 语言风格/结构 |
| EMNLP 2025<br>B | <a id="p1951"></a>[MoSEs: Uncertainty-Aware AI-Generated Text Detection via Mixture of Stylistics Experts with Conditional Thresholds](https://aclanthology.org/2025.emnlp-main.294/) | 主会；长/短文轨道未逐篇核定 | 语言风格/结构 |
| ACL 2024<br>A | <a id="p0888"></a>[Threads of Subtlety: Detecting Machine-Generated Texts Through Discourse Motifs](https://aclanthology.org/2024.acl-long.298/) | Long | 语言风格/结构 |

<a id="applications"></a>

### 其他检测方法与应用场景（35 条）

| 会议 / 年份 / 目录等级 | 论文 | 形式与状态 | 研究标签 |
|---|---|---|---|
| AAAI 2026<br>A | <a id="p0706"></a>[Model-Agnostic Sentiment Distribution Stability Analysis for Robust LLM-Generated Texts Detection](https://ojs.aaai.org/index.php/AAAI/article/view/40872) | 主会 | 检测方法/应用 |
| ACL 2026<br>A | <a id="p1137"></a>[LLM-Generated Text May Harm Your Retrieval! A Robust Detection Strategy for Retrieval-Augmented Generation](https://aclanthology.org/2026.acl-long.1475/) | Long | 检测方法/应用 |
| ACL 2026<br>A | <a id="p1201"></a>[Verifiable LLM-Generated Text Detection via Projected Semantic-Structural Distributions](https://aclanthology.org/2026.acl-long.638/) | Long | 检测方法/应用 |
| CIKM 2026<br>B | <a id="p1491"></a>[Adversarial Creation and Detection of AI-Generated Social Bot Content](https://doi.org/10.1145/3799682.3841070) | 官网列出；**官网已列出，正式论文集待核** | 社交文本 |
| CIKM 2026<br>B | <a id="p1530"></a>[GRAIN: Detecting AI-Generated News via Article-Level Structure](https://doi.org/10.1145/3799682.3839924) | 官网列出；**官网已列出，正式论文集待核** | 检测方法/应用 |
| ICLR 2026<br>A | <a id="p2843"></a>[D&amp;R: Recovery-based AI-Generated Text Detection via a Single Black-box LLM Call](https://iclr.cc/virtual/2026/poster/10010576) | 官网列出 | 检测方法/应用 |
| ICLR 2026<br>A | <a id="p2920"></a>[Learn-to-Distance: Distance Learning for Detecting LLM-Generated Text](https://iclr.cc/virtual/2026/poster/10011726) | 官网列出 | 检测方法/应用 |
| ICLR 2026<br>A | <a id="p3003"></a>[TSM-Bench: Detecting LLM-Generated Text in Real-World Wikipedia Editing Practices](https://iclr.cc/virtual/2026/poster/10006430) | 官网列出 | 检测方法/应用 |
| ICML 2026<br>A | <a id="p3451"></a>[Sem-Detect: Semantic Level Detection of AI Generated Peer-Reviews](https://proceedings.mlr.press/v306/duarte26a.html) | 主会 | 同行评审场景 |
| IJCAI 2026<br>B | <a id="p3757"></a>[VaryBalance: Detecting LLM-Generated Text Through Variation](https://www.ijcai.org/proceedings/2026/648) | 主会/轨道待核 | 检测方法/应用 |
| NeurIPS 2026<br>A | <a id="p4836"></a>[Hitting a Moving Target: Test-Time Adaptation for AI Text Detection under Continual Distribution Shift](https://neurips.cc/virtual/2026/poster/153619) | 官网列出；**官网已列出，正式论文集待核** | 检测方法/应用 |
| S&amp;P 2026<br>A | <a id="p5077"></a>[AI Wrote My Paper and All I Got Was This False Negative:* Measuring the Efficacy of Commercial AI Text Detectors](https://sp2026.ieee-security.org/accepted-papers.html#collapse-90) | 官网列出 | 检测方法/应用 |
| WWW 2026<br>A | <a id="x011"></a>[LLMs Killed Q&amp;A Stars? Analyzing the Impact of LLM-Generated Answers on an Online Q&amp;A Platform](https://wsp-lab.github.io/papers/shin-qna-www26.pdf) | 主会Research Track | 集成检测器识别生成回答，分析真实问答平台影响；官网名单和作者仓库均已核 |
| ACL 2025<br>A | <a id="p1038"></a>[Who Writes What: Unveiling the Impact of Author Roles on AI-generated Text Detection](https://aclanthology.org/2025.acl-long.1292/) | Long | 检测方法/应用 |
| COLING 2025<br>B | <a id="p1589"></a>[AIDER: a Robust and Topic-Independent Framework for Detecting AI-Generated Text](https://aclanthology.org/2025.coling-main.625/) | 主会；长/短文轨道未逐篇核定 | 检测方法/应用 |
| COLING 2025<br>B | <a id="p1638"></a>[MAGRET: Machine-generated Text Detection with Rewritten Texts](https://aclanthology.org/2025.coling-main.557/) | 主会；长/短文轨道未逐篇核定 | 检测方法/应用 |
| EMNLP 2025<br>B | <a id="p1881"></a>[Beyond Checkmate: Exploring the Creative Choke Points for AI Generated Texts](https://aclanthology.org/2025.emnlp-main.600/) | 主会；长/短文轨道未逐篇核定 | 检测方法/应用 |
| EMNLP 2025<br>B | <a id="p1943"></a>[Machine-generated text detection prevents language model collapse](https://aclanthology.org/2025.emnlp-main.1506/) | 主会；长/短文轨道未逐篇核定 | 检测方法/应用 |
| ICLR 2025<br>A | <a id="p2703"></a>[Deep Kernel Relative Test for Machine-generated Text Detection](https://iclr.cc/virtual/2025/poster/27688) | 官网列出 | 检测方法/应用 |
| ICLR 2025<br>A | <a id="z041"></a>[Inspection and Control of Self-Generated-Text Recognition Ability in Llama3-8b-Instruct](https://iclr.cc/virtual/2025/poster/27838) | 官网列出 | 检测方法/应用 |
| NeurIPS 2025<br>A | <a id="p4436"></a>[Advancing Machine-Generated Text Detection from an Easy to Hard Supervision Perspective](https://neurips.cc/virtual/2025/poster/119371) | 官网列出 | 检测方法/应用 |
| NeurIPS 2025<br>A | <a id="p4486"></a>[DNA-DetectLLM: Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm](https://neurips.cc/virtual/2025/poster/115141) | 官网列出 | 检测方法/应用 |
| NeurIPS 2025<br>A | <a id="p4538"></a>[IPAD: Inverse Prompt for AI Detection - A Robust and Interpretable LLM-Generated Text Detector](https://neurips.cc/virtual/2025/poster/120042) | 官网列出 | 检测方法/应用 |
| AAAI 2024<br>A | <a id="p0139"></a>[OUTFOX: LLM-Generated Essay Detection Through In-Context Learning with Adversarially Generated Examples](https://ojs.aaai.org/index.php/AAAI/article/view/30120) | 主会特别轨道：Safe, Robust and Responsible AI | 检测方法/应用 |
| ACL 2024<br>A | <a id="p0842"></a>[A Ship of Theseus: Curious Cases of Paraphrasing in LLM-Generated Texts](https://aclanthology.org/2024.acl-long.357/) | Long | 检测方法/应用 |
| ACL 2024<br>A | <a id="p0844"></a>[AI ‘News’ Content Farms Are Easy to Make and Hard to Detect: A Case Study in Italian](https://aclanthology.org/2024.acl-long.817/) | Long | 检测方法/应用 |
| ACL 2024<br>A | <a id="p0849"></a>[Are AI-Generated Text Detectors Robust to Adversarial Perturbations?](https://aclanthology.org/2024.acl-long.327/) | Long | 检测方法/应用 |
| ACL 2024<br>A | <a id="p0881"></a>[Navigating the Shadows: Unveiling Effective Disturbances for Modern AI Content Detectors](https://aclanthology.org/2024.acl-long.584/) | Long | 检测方法/应用 |
| EMNLP 2024<br>B | <a id="p1846"></a>[Text Fluoroscopy: Detecting LLM-Generated Text through Intrinsic Features](https://aclanthology.org/2024.emnlp-main.885/) | 主会；长/短文轨道未逐篇核定 | 检测方法/应用 |
| ICLR 2024<br>A | <a id="p2591"></a>[Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy](https://iclr.cc/virtual/2024/poster/19498) | 官网列出 | 检测方法/应用 |
| ICLR 2024<br>A | <a id="p2643"></a>[Raidar: geneRative AI Detection viA Rewriting](https://iclr.cc/virtual/2024/poster/18333) | 官网列出 | 检测方法/应用 |
| IJCAI 2024<br>B | <a id="p3576"></a>[Ten Words Only Still Help: Improving Black-Box AI-Generated Text Detection via Proxy-Guided Efficient Re-Sampling](https://www.ijcai.org/proceedings/2024/55) | 主会/轨道待核 | 检测方法/应用 |
| NAACL 2024<br>B | <a id="p4039"></a>[Ghostbuster: Detecting Text Ghostwritten by Large Language Models](https://aclanthology.org/2024.naacl-long.95/) | Long | 检测方法/应用 |
| NeurIPS 2024<br>A | <a id="p4239"></a>[BiScope: AI-generated Text Detection by Checking Memorization of Preceding Tokens](https://papers.nips.cc/paper_files/paper/2024/hash/bc808cf2d2444b0abcceca366b771389-Abstract-Conference.html) | 官网列出 | 检测方法/应用 |
| NeurIPS 2024<br>A | <a id="p4285"></a>[DPIC: Decoupling Prompt and Intrinsic Characteristics for LLM Generated Text Detection](https://papers.nips.cc/paper_files/paper/2024/hash/1d35af80e775e342f4cd3792e4405837-Abstract-Conference.html) | 官网列出 | 检测方法/应用 |

<a id="attribution"></a>

### 来源归属与作者分析（8 条）

| 会议 / 年份 / 目录等级 | 论文 | 形式与状态 | 研究标签 |
|---|---|---|---|
| ACL 2026<br>A | <a id="p1052"></a>[Authorship Attribution in Multilingual Machine-Generated Texts](https://aclanthology.org/2026.acl-long.2091/) | Long | 多语言/跨语言 |
| ACL 2026<br>A | <a id="p1101"></a>[Explainable Disentangled Representation Learning for Generalizable Authorship Attribution in the Era of Generative AI](https://aclanthology.org/2026.acl-long.2018/) | Long | 跨域/泛化；表征/对比学习 |
| ICML 2026<br>A | <a id="p3303"></a>[Every Step Counts: Decoding Trajectories as Authorship Fingerprints of dLLMs](https://proceedings.mlr.press/v306/li26ir.html) | 主会 | 来源归属/作者分析 |
| ACL 2025<br>A | <a id="p1040"></a>[XDAC: XAI-Driven Detection and Attribution of LLM-Generated News Comments in Korean](https://aclanthology.org/2025.acl-long.1108/) | Long | 韩语 |
| EMNLP 2025<br>B | <a id="p1963"></a>[Profiler: Black-box AI-generated Text Origin Detection via Context-aware Inference Pattern Analysis](https://aclanthology.org/2025.emnlp-main.1265/) | 主会；长/短文轨道未逐篇核定 | 来源归属/作者分析 |
| SIGIR 2025<br>A | <a id="p5128"></a>[Continual Origin Tracing of LLM-Generated Text](https://sigir2025.dei.unipd.it/accepted-papers.html) | full papers | 来源归属/作者分析 |
| ECAI 2024<br>B | <a id="x003"></a>[Is Contrasting All You Need? Contrastive Learning for the Detection and Attribution of AI-generated Text](https://doi.org/10.3233/FAIA240862) | 主会 | WhosAI；对比学习与来源归属 |
| ECAI 2024<br>B | <a id="x004"></a>[TopFormer: Topology-Aware Authorship Attribution of Deepfake Texts with Diverse Writing Styles](https://doi.org/10.3233/FAIA240647) | 主会 | 多种写作风格下的生成器归属 |

<a id="attacks"></a>

### 规避攻击与鲁棒性（12 条）

| 会议 / 年份 / 目录等级 | 论文 | 形式与状态 | 研究标签 |
|---|---|---|---|
| ACL 2026<br>A | <a id="p1206"></a>[When Personalization Tricks Detectors: The Feature-Inversion Trap in Machine-Generated Text Detection](https://aclanthology.org/2026.acl-long.1998/) | Long | 检测攻击与鲁棒性 |
| ICML 2026<br>A | <a id="p3231"></a>[Attacks on Machine-Text Detectors Retain Stylistic Fingerprints](https://proceedings.mlr.press/v306/rivera-soto26a.html) | 主会 | 语言风格/结构 |
| NeurIPS 2026<br>A | <a id="p4952"></a>[RobustStress: Stress-Testing AI-Generated Text Detectors under Gradual Perturbations](https://neurips.cc/virtual/2026/poster/139092) | 官网列出；**官网已列出，正式论文集待核** | 检测攻击与鲁棒性 |
| ACL 2025<br>A | <a id="p0976"></a>[Iron Sharpens Iron: Defending Against Attacks in Machine-Generated Text Detection with Adversarial Training](https://aclanthology.org/2025.acl-long.155/) | Long | 检测攻击与鲁棒性 |
| EMNLP 2025<br>B | <a id="p1986"></a>[TempParaphraser: “Heating Up” Text to Evade AI-Text Detection through Paraphrasing](https://aclanthology.org/2025.emnlp-main.1607/) | 主会；长/短文轨道未逐篇核定 | 检测攻击与鲁棒性 |
| EMNLP 2025<br>B | <a id="p2012"></a>[Your Language Model Can Secretly Write Like Humans: Contrastive Paraphrase Attacks on LLM-Generated Text Detectors](https://aclanthology.org/2025.emnlp-main.433/) | 主会；长/短文轨道未逐篇核定 | 表征/对比学习 |
| ICLR 2025<br>A | <a id="p2723"></a>[Humanizing the Machine: Proxy Attacks to Mislead LLM Detectors](https://iclr.cc/virtual/2025/poster/29761) | 官网列出 | 检测攻击与鲁棒性 |
| KDD 2025<br>A | <a id="x006"></a>[TH-Bench: Evaluating Evading Attacks via Humanizing AI Text on Machine-Generated Text Detectors](https://doi.org/10.1145/3711896.3737418) | Datasets and Benchmarks | humanization规避攻击评测 |
| NeurIPS 2025<br>A | <a id="p4437"></a>[Adversarial Paraphrasing: A Universal Attack for Humanizing AI-Generated Text](https://neurips.cc/virtual/2025/poster/116833) | 官网列出 | 检测攻击与鲁棒性 |
| USENIX Security 2025<br>A | <a id="p5225"></a>[GradEscape: A Gradient-Based Evader Against AI-Generated Text Detectors](https://www.usenix.org/conference/usenixsecurity25/presentation/meng) | 官网列出 | 检测攻击与鲁棒性 |
| ACL 2024<br>A | <a id="p0887"></a>[Stumbling Blocks: Stress Testing the Robustness of Machine-Generated Text Detectors Under Attacks](https://aclanthology.org/2024.acl-long.160/) | Long | 检测攻击与鲁棒性 |
| EMNLP 2024<br>B | <a id="p1837"></a>[RAFT: Realistic Attacks to Fool Text Detectors](https://aclanthology.org/2024.emnlp-main.939/) | 主会；长/短文轨道未逐篇核定 | 检测攻击与鲁棒性 |

<a id="benchmarks"></a>

### 基准、评测与检测边界（21 条）

| 会议 / 年份 / 目录等级 | 论文 | 形式与状态 | 研究标签 |
|---|---|---|---|
| ACL 2026<br>A | <a id="p1086"></a>[DetectRL-X: Towards Reliable Multilingual and Real-World LLM-Generated Text Detection](https://aclanthology.org/2026.acl-long.1773/) | Long | 多语言/跨语言 |
| ACL 2026<br>A | <a id="p1124"></a>[Identifying Bias in Machine-generated Text Detection](https://aclanthology.org/2026.acl-long.109/) | Long | 基准/评测/检测边界 |
| ACL 2026<br>A | <a id="p1128"></a>[Is Human-Like Text Liked by Humans? Multilingual Human Detection and Preference Against AI](https://aclanthology.org/2026.acl-long.639/) | Long | 多语言/跨语言；对齐/偏好信号 |
| ACL 2026<br>A | <a id="p1207"></a>[Who Wrote This Line? Evaluating the Detection of LLM-Generated Classical Chinese Poetry](https://aclanthology.org/2026.acl-long.245/) | Long | 中文 |
| ICLR 2026<br>A | <a id="p2917"></a>[Is Your Paper Being Reviewed by an LLM? Benchmarking AI Text Detection in Peer Review](https://iclr.cc/virtual/2026/poster/10010349) | 官网列出 | 同行评审场景 |
| ACL 2025<br>A | <a id="p0912"></a>[Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media](https://aclanthology.org/2025.acl-long.1120/) | Long | 社交文本 |
| ACL 2025<br>A | <a id="p1000"></a>[MultiSocial: Multilingual Benchmark of Machine-Generated Text Detection of Social-Media Texts](https://aclanthology.org/2025.acl-long.36/) | Long | 多语言/跨语言；社交文本 |
| ACL 2025<br>A | <a id="p1007"></a>[People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text](https://aclanthology.org/2025.acl-long.267/) | Long | 基准/评测/检测边界 |
| ACL 2025<br>A | <a id="p1012"></a>[Reliably Bounding False Positives: A Zero-Shot Machine-Generated Text Detection Framework via Multiscaled Conformal Prediction](https://aclanthology.org/2025.acl-long.601/) | Long | 零样本；细粒度/定位；统计校准/误报控制 |
| COLING 2025<br>B | <a id="p1619"></a>[Exploring the Limitations of Detecting Machine-Generated Text](https://aclanthology.org/2025.coling-main.288/) | 主会；长/短文轨道未逐篇核定 | 基准/评测/检测边界 |
| COLING 2025<br>B | <a id="p1626"></a>[HLU: Human Vs LLM Generated Text Detection Dataset for Urdu at Multiple Granularities](https://aclanthology.org/2025.coling-main.235/) | 主会；长/短文轨道未逐篇核定 | 乌尔都语 |
| EMNLP 2025<br>B | <a id="p1958"></a>[OpenTuringBench: An Open-Model-based Benchmark and Framework for Machine-Generated Text Detection and Attribution](https://aclanthology.org/2025.emnlp-main.1354/) | 主会；长/短文轨道未逐篇核定 | 基准/评测/检测边界 |
| ACL 2024<br>A | <a id="p0877"></a>[M4GT-Bench: Evaluation Benchmark for Black-Box Machine-Generated Text Detection](https://aclanthology.org/2024.acl-long.218/) | Long | 基准/评测/检测边界 |
| ACL 2024<br>A | <a id="p0878"></a>[MAGE: Machine-generated Text Detection in the Wild](https://aclanthology.org/2024.acl-long.3/) | Long | 基准/评测/检测边界 |
| ACL 2024<br>A | <a id="p0884"></a>[RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors](https://aclanthology.org/2024.acl-long.674/) | Long | 基准/评测/检测边界 |
| CCS 2024<br>A | <a id="x001"></a>[MGTBench: Benchmarking Machine-Generated Text Detection](https://doi.org/10.1145/3658644.3670344) | 主会 | 检测器、泛化及攻击评测 |
| CCS 2024<br>A | <a id="x002"></a>[On the Detectability of ChatGPT Content: Benchmarking, Methodology, and Evaluation through the Lens of Academic Writing](https://doi.org/10.1145/3658644.3670392) | 主会 | CheckGPT；学术写作与润色检测；正式题名不同于早期预印本 |
| EMNLP 2024<br>B | <a id="p1861"></a>[‘Quis custodiet ipsos custodes?’ Who will watch the watchmen? On Detecting AI-generated peer-reviews](https://aclanthology.org/2024.emnlp-main.1262/) | 主会；长/短文轨道未逐篇核定 | 同行评审场景 |
| NAACL 2024<br>B | <a id="p4021"></a>[BUST: Benchmark for the evaluation of detectors of LLM-Generated Text](https://aclanthology.org/2024.naacl-long.444/) | Long | 基准/评测/检测边界 |
| NAACL 2024<br>B | <a id="p4030"></a>[Does GPT-4 pass the Turing test?](https://aclanthology.org/2024.naacl-long.290/) | Long | 基准/评测/检测边界 |
| NeurIPS 2024<br>A | <a id="p4270"></a>[DetectRL: Benchmarking LLM-Generated Text Detection in Real-World Scenarios](https://papers.nips.cc/paper_files/paper/2024/hash/b61bdf7e9f64c04ec75a26e781e2ad51-Abstract-Datasets_and_Benchmarks_Track.html) | 官网列出 | 基准/评测/检测边界 |

<a id="data"></a>

## 数据与维护

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
