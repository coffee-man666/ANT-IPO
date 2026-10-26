# 05 业务与产品（Business）— Anthropic, PBC S-1 精读提取

- **来源文件**：`../anthropic-sx1.txt`
- **负责区间**：L12090–L14572（"Business" 章全量，至 "Our Governance Structure" 之前）
- **覆盖页码**：招股书页 180–207 与 228–243。注：文件中 L13722（页码 207）之后直接跳至 L13770（页码 228），页 208–227 的内容不在本行号区间内（属本文件其他位置）；页 242 对应 L14527–14570（"Other Matters"）。
- **标注约定**：每条事实前缀 F###，`L####` 为底稿行号；英文引号为原文逐字摘录。原文中部分金额在文本版中被留空（如 "$"，后无数字），下文以「（原文留空）」标注，绝不补数。

---

## 1. 公司使命与 PBC 定位

- **F001** 使命原文（L12099–12101）："our mission is the responsible development and maintenance of advanced AI for the long-term benefit of humanity"（负责任地开发与维护先进 AI，造福人类的长远利益）。同一表述在 L12969–12970 与 L14165–14167（public benefit purpose）重复出现。
- **F002** 公司定位（L12098–12099）："Anthropic was founded in 2021 by a team of researchers responsible for many of the breakthroughs that define AI. We are first and foremost a research lab"（2021 年由奠定 AI 多项突破的研究团队创立；首先且最重要的是一家研究实验室）。L13891–13894 再次强调 "We are first and foremost a research lab"。
- **F003** 治理结构（L12553–12558）：注册为特拉华州公益公司（"incorporating as a Delaware PBC"），并设立 LTBT（原文缩写，Long-Term Benefit Trust），"with an explicit mandate to advance our mission"；公开发布安全方法论、模型评估与 Responsible Scaling Policy，"because we believe transparency is a prerequisite for trust"。
- **F004** 商业起点与收入增长（L12106–12110）："Claude has experienced the fastest enterprise adoption of any technology in history, as demonstrated by revenue growing from $0 at commercial launch in the first quarter of 2023 to $（原文留空） for the three months ended September 30, 2026."（商业发布于 2023 年一季度，收入从 0 起步。）
- **F005** 使命优先原则（L12559–12562）："We do not pursue projects based on commercial opportunity or research novelty alone; our efforts must advance our mission. When difficult tradeoffs arise between commercial gain and safety or trust, we have a clear answer."
- **F006** 使命优先的实例（L12563–12565）：2026 年 4 月前沿模型 Mythos 首发时未广泛开放，而是通过 Project Glasswing 以"门控研究预览"（gated research preview）形式向经筛选的网络安全应用组织开放，原因是其在网络漏洞发现方面能力先进。
- **F007** Company Purpose 概念（L12554、L14233）：安全/信任权衡以 "Company Purpose" 为准绳；公共利益股份机制是践行 Company Purpose 的方式之一但非唯一方式。

## 2. 五大核心优势（Our Core Advantages）

- **F008** 优势清单（L12546–12548）："We have five core advantages that define our position at the frontier: our mission and focus, our talent and culture, our frontier and safety research, our approach to compute, and our enterprise strategy."
- **F009** Mission & Focus（L12126–12130）：单一聚焦使人才、研究与算力投资集中于对人类最高价值的工作，避免优先级冲突；"we believe this requires safety and capability to advance together"。
- **F010** Talent & Culture（L12131–12135）：使命与聚焦吸引并留住世界级人才；文化是 "a low-ego, truth-seeking environment, where frontier AI capability and safety are mutually reinforcing"。
- **F011** Frontier & Safety Research（L12136–12148）：前沿能力与安全研究深度整合并直接塑造模型设计、训练与部署；每一代 Claude 模型协助构建下一代，压缩开发周期——递归动态被称为 **"closing the loop"**，被视为前沿 AI 最重要的结构性优势之一。
- **F012** 安全-能力权衡表述（L12149–12155）：在开发中及发布前后评估每个模型的风险，采取其认为适当的措施平衡能力与安全/对齐/安保，"even where doing so may moderate the rate at which we release new capabilities"；此类决策是服务于 Company Purpose 的审慎权衡。
- **F013** Approach to Compute（L12156–12166）：将算力作为"单一、可互换的池"（"a single, fungible pool"）从多个战略伙伴处管理，并按边际产出动态调度；多芯片算力架构覆盖 **AWS Trainium、Google TPUs、NVIDIA GPUs、AMD GPUs**，按价格与性能编排负载。
- **F014** 算力承诺总述（L12168–12176；L13101–13108 重复）：截至及 2026 年 9 月 30 日之后，已签采购承诺与租赁协议（含短期承诺及未起始租赁），合计承诺支出 "more than $（原文留空）"，几乎全部与算力和基础设施相关；其中约 "$（原文留空）" 预计在 2030 年 12 月 31 日前发生，其余绝大部分在 2031–2045 年间发生；约 "$（原文留空）" 未来 12 个月内到期。
- **F015** Enterprise Strategy（L12179–12186）：前沿 AI 在真实场景中最有价值；研究优先级、产品路线图、go-to-market 与 Applied AI 团队均围绕企业用例组织；客户反馈直接指导研究重点。
- **F016** 自我强化的双循环（L12328–12345）：**Improvement Loop**（企业部署反馈→模型/平台/应用改进→更广部署）与 **Investment Loop**（收入→算力/研究/人才投入→能力扩展→更大市场→更多收入）。

## 3. 企业采用与客户指标（截至 2026 年 9 月 30 日）

| 指标 | 数值（逐字） | 行号 |
|---|---|---|
| TTM 收入 ≥ $100,000 客户数 | "More than 11,900" | L12194–12195 |
| TTM 收入 ≥ $1,000,000 客户数 | "More than 1,900" | L12197 |
| TTM 收入 ≥ $10,000,000 客户数 | "Approximately 250" | L12199 |
| $100K+ 客户数（2025-09-30 对比） | "more than 950" → "more than 11,900"（2026-09-30） | L12979–12981, L13695–13697 |
| Fortune 10 覆盖 | "every company in the Fortune 10" | L12958–12959 |
| Fortune 500 覆盖 | "over 50% of the Fortune 500" | L12959–12960 |
| Global 2000 覆盖 | "over 30% of the Global 2000" | L12960 |

- **F017** 三层堆栈（L12200–12202）："We build at three layers of the stack: the models themselves, the platform for building on those models, and the applications that place Claude directly in the hands of our users."任一层的进展在三层间复利放大。
- **F018** 平台+应用交叉使用率（L12205–12207）：截至 2026 年 9 月 30 日的三个月，TTM 收入 $100K+ 客户中 "over 50%" 同时使用 Claude Platform 与至少一个第一方应用，高于截至 2025 年 12 月 31 日三个月的 "approximately 30%"。
- **F019** Fortune 500 细分覆盖（L12960–12963）：$100K+ 客户包括 10 家最大软件与 IT 服务公司中的全部 10 家、10 家最大互联网公司中的 10 家、10 家最大制药公司中的 9 家、10 家最大银行中的全部 10 家、10 家最大半导体公司中的 9 家、10 家最大医疗健康公司中的 8 家。
- **F020** Run-Rate Revenue（L12982–12984）："our Run-Rate Revenue was $（原文留空） as of October 31, 2026"。脚注 11（L12926–12934）说明：Run-Rate Revenue 为运营指标、非 GAAP 收入替代、非预测；消费型收入占收入绝大部分（"consumption-based revenue represents the substantial majority of our revenue"）且可能波动；增长率预计随时间下降；历史上包含后续被认定违反使用政策/商业条款而被限制或终止的客户收入。

## 4. 财务模型要点（Business 章内披露）

- **F021** 净收入留存率（L12255–12257；L12993–12994 重复）："Net Revenue Retention of approximately 900% as of September 30, 2026"。
- **F022** 收入 vs 算力成本增速（L12263–12269）："revenue that grew 1,368% year over year for the three months ended June 30, 2026 compared to compute and infrastructure expenses that grew 300% during the same period."
- **F023** 人均 TTM 收入（L12275–12277）：截至 2026 年 9 月 30 日 "TTM revenue per employee of over $6.6 million"，对比 2025 年 9 月 30 日的 "$1.4 million"。
- **F024** 季度收入（L12281–12286）："Our revenue was $11.6 billion for the three months ended June 30, 2026, up from $787 million for the three months ended June 30, 2025."
- **F025** 经营利润（L12288–12298）：截至 2026 年 6 月 30 日三个月经营利润率 "8%"、经营利润 "$1.0 billion"；上年同期经营利润率 "(152)%"、经营亏损 "$1.2 billion"。
- **F026** 调整后经营利润（L12300–12311）：截至 2026 年 6 月 30 日三个月 Adjusted Operating Margin "19%"、Adjusted Operating Income "$2.2 billion"；上年同期 "(129)%"、Adjusted Operating Loss "$1.0 billion"。
- **F027** 资本与现金（L12315–12323）："As of June 30, 2026, we had raised an aggregate of $141.1 billion of capital and had cash and cash equivalents of $112.4 billion and short-term investments of $19.3 billion."
- **F028** 其他运营费用增速（L13083–13085）：截至 2026 年 6 月 30 日三个月同比 "Other operating expenses increased 741%"。
- **F029** 长期投资风险的表述（L12324–12327）：必须提前数年预测算力需求；算力效率使其在需求超预期时放大回报、需求不及预期时提供财务韧性。
- **F030** 客户价值三来源（L12210–12211；L13730–13732 重复）："more productive employees, faster processes, and embedded intelligence in their products"。

## 5. "Closing the Loop"：Claude 加速 Claude（内部使用数据）

- **F031** 模型参与研发全流程（L12347–12351）：后续模型代际的研究、训练与测试大量使用 Claude，包括运行实验、生成与处理训练数据、自动化评估与安全审计、编写与审查代码。
- **F032** 高难度工程问题成功率（L12359–12361）："Claude's success rate on these problems reached approximately 90% in September 2026, up approximately 50 percentage points in nine months, based on our internal benchmarks."（缺乏明确规范的开放式工程问题。）
- **F033** 人均代码量（L12365–12369）：截至 2026 年 9 月 30 日三个月，工程师人均日均代码贡献量 "over 45 times" 2024 全年日均水平。
- **F034** 代码由 Claude 写入占比（L12369–12371；L13062–13063、L13788–13791 重复）："Over 90% of the contributions to our codebase in September 2026 were written by Claude."
- **F035** 组织杠杆（L12372–12379）：2024-12-31 至 2026-09-30，员工人数增长 "over five times"，而 2026 年 Q3 收入为 2024 年 Q4 收入的 "86 times"。
- **F036** 内部使用价值（L12387–12390）：按牌价计算的内部 Claude 使用价值从 2026 年 1 月到 9 月增长 "over 250 times"；2026 年 4 月起该月度价值首次超过月度人员费用（不含股权激励费用）。
- **F037** 安全边界（L12395–12398）：用 AI 构建 AI 可能构成重大安全风险，属 Responsible Scaling Policy 覆盖范围——该政策规定了监测与缓解所谓 "recursive self-improvement" 风险的计划。

## 6. 行业叙事与市场规模（含第三方数据）

- **F038** Powerful AI 定义（L12400–12416）：五种关键属性——（1）认知能力在大多数职业与科学领域匹敌或超越顶级人类专家；（2）可使用人类虚拟工作可及的一切界面（文本、音频、视频、直接计算机控制）；（3）可自主长时间（数小时、数天或数周）推理复杂任务并主动澄清；（4）可跨多实例协调并与人类及其他 AI 协作；（5）可通过数字连接操控实验室设备、机器人系统等物理世界设备。预期 "will become widely available within a few years"（L12400–12401）。
- **F039** Scaling Laws 渊源（L12427–12433）：基础论文 *"Scaling Laws for Neural Language Models"* 的主要作者（含 Dario Amodei、Jared Kaplan、Sam McCandlish、Tom Brown）后来联合创立 Anthropic。
- **F040** 需求判断（L12434–12439）：AI 能力将持续进步多年，需求将超过供给，"limited principally by the availability of compute"；需求将集中在前沿，企业倾向为最高价值工作选用最强模型。
- **F041** 知识工作经济价值（L12461–12462）："the work that knowledge workers perform represented more than $40 trillion in economic value globally in 2025"（附注 6 指向口径说明）。
- **F042** IDC 累计影响（L12466–12470，注 7：IDC, The Economic Impact of AI: 2026 Edition, doc # US54452226, April 2026）：AI 解决方案与服务投资 "will yield a cumulative global economic impact of $22.5 trillion by 2031"。
- **F043** IT 支出历史（L12474–12479，注 8：IDC Worldwide Black Book: Live Edition V2 2026 Forecast, July 2026）：IT 支出从 "approximately $1.2 trillion in 2006 to $4.3 trillion in 2025, a CAGR of approximately 7%"；同期的云计算支出从 0 增至 "$1.9 trillion"。
- **F044** 全球 GDP（L12484–12485，World Bank）：从 "approximately $34 trillion in 2000 to more than $118 trillion in 2025"，增长超过三倍。
- **F045** 前十大科技公司（L12486–12492）：以 2026-09-30 市值计的十大上市科技公司，合计收入从 "$68 billion" 增至 "more than $2.5 trillion"，"an increase of approximately 38 times, or approximately 11 times the rate of global GDP growth"。
- **F046** 知识工作者人口（L12721–12723，注 10：IDC, Worldwide Developer Population Growth Forecast, 2025–2029, doc # US53789825, September 2025）：全球知识工作者 "estimated to exceed one billion in 2028"。
- **F047** 制药支出（L12520–12522；L13187–13188 重复，注 9/12：IQVIA Institute, Global Medicine Use Trends 2026, February 2026）：2026 年全球药品支出 "expected to exceed $2 trillion"。
- **F048** 目标行业列表（L12499–12501）：软件开发展、商业与专业服务、网络安全、金融服务、医疗健康与生命科学。
- **F049** 安全与伦理的市场含义（L12532–12545）：AI 可能被用于网络攻击、生物领域滥用、权力与财富集中、错误对齐系统的机构性危害；企业将严格的防护、可预测的模型行为与可问责性作为选择 AI 伙伴的决定性标准（"decisive criteria in selecting an AI partner for mission-critical workloads"）。

## 7. Virtual Collaborator 叙事与 Claude Code / Claude Cowork

- **F050** Virtual Collaborator 定义（L12212–12215；L12711–12716 重复）：企业使用方式从响应离散提示的工具转向 "a Virtual Collaborator: an AI system that works alongside humans to perform complex, multi-step work at professional levels"；其承载组织授予的访问权限、系统连接与上下文。
- **F051** Claude Code 定位（L12223–12225；L12724–12734 扩展）：编码智能体，与开发者协作完成端到端软件开发（编写、规划、编辑、测试、调试、提交代码）；其成为 Virtual Collaborator 的要素是持续推理、把意图翻译为动作的 harness、维持持久状态的执行环境、工具集成与友好界面；发布后数月内自主编码成为衡量前沿 AI 进步的参照点。
- **F052** 标志性案例（L12735–12736）："NASA engineers used Claude Code to plan and write navigation commands for the Mars Perseverance rover, resulting in the first AI-planned drive on Mars."
- **F053** 发布时间线（L12750–12754）：Claude Code 于 **2025 年 2 月**以 research preview 发布；Claude Cowork 于 **2026 年 1 月**以 research preview 发布；截至 2026-09-30，Cowork 的采用速度超过同期 Claude Code。
- **F054** 产品合并（L12755–12756；L13438–13440 重复）：2026 年 9 月起将 Claude Cowork 与 Claude.ai 合并为统一应用，任何请求自动调用合适工具（复用 Cowork 能力）。
- **F055** Claude Cowork 定位（L12227–12229；L13425–13431）：知识工作智能体，具备 computer use 能力，自主研究、起草、分析、综合、执行端到端业务任务；运行于桌面/Web/移动端，可操作本地文件、已连接应用、Chrome 与桌面本身；开源插件系统可安装或构建捆绑技能/连接器/工作流的包。
- **F056** 远景表述（L12766–12771）：目标是可交给 Claude 数小时、数天或数周的开放式任务并自主执行；最终数百万 Virtual Collaborator 并行——"what we refer to as a country of geniuses in a data center"。
- **F057** 网络安全能力曲线（L12699–12703）：在卡内基梅隆研究者开发的 ExploitBench（评估 AI 利用软件漏洞能力）上，得分从 Opus 4.8 的 "40%"，到 Claude Mythos 5 的 "78%"，再到 Opus 5.5 的 "91%"，"over a period of approximately four months"。

## 8. 分发、伙伴与生态

- **F058** 云伙伴结构（L12232–12236；L12901–12911 重复）：Claude 可在三大云平台 AWS、GCP、Azure 上使用；与 CSP 联合 go-to-market，与客户建立直接合同关系同时向各 CSP 支付费用（"paying a fee to each CSP"）；该结构可强化商业协同、避免渠道冲突、自主定价并享有算力效率改进的财务收益。
- **F059** SI 与数据平台伙伴（L12236–12238）：客户可通过 SI——**Accenture、Deloitte、KPMG、PwC**——及顾问、数据平台——**Salesforce、Snowflake**——采用 Claude。
- **F060** Ode with Anthropic（L12238–12241；L12948–12952 重复）：与领先私募股权公司合作 recently launched 的 AI 服务公司，面向各行业中型公司，基于 Claude Platform 构建方案并长期支持客户；与 Applied AI 与 go-to-market 团队紧密协作。
- **F061** Claude Partner Network（L12918–12920）：2026 年 3 月 launched，"committing an initial $100 million in 2026 to fund partner training, technical certification, and joint market development"。
- **F062** 认证网络规模（L12921–12923）：截至 2026 年 9 月 30 日，"over 150,000 practitioners across over 4,000 organizations" 通过 Claude Certification Program 获得认证（含监考考试）。
- **F063** Claude Frontier Academy（L12940–12946）：2026 年 10 月 launched，"backed by a $100 million commitment"，培训客户与伙伴工程师达到自有工程师标准；目标 "to train 10,000 engineers through the Academy by the end of 2027"，首批学员来自领先咨询公司与企业的队列。
- **F064** 直销与 Applied AI 团队（L12883–12894）：direct go-to-market 团队借助有机采用势头建立高管支持；Applied AI 团队与精选客户深入共建定制方案；两者构成"混合销售+工程职能"，按地理再按行业组织。
- **F065** Prosumer 顶层漏斗（L13727–13729）：个人用户亲身体验价值后成为组织内布道者，从个人使用扩展到团队与全组织部署。

## 9. 定价、降本与扩张证据

- **F066** Claude Code 用户支出对比（L12995–12998）：截至 2026 年 9 月 30 日三个月，未使用 Claude Code 的 Claude Enterprise 用户月均支出 "less than $75"，而使用 Claude Code 的 Claude Enterprise 用户中前 5% 的支出 "approximately 20 times that amount"。
- **F067** Fable 5.1 降本（L13002–13004）：2026 年 9 月发布，相对 Fable 5 将典型负载成本降低 "approximately 25%"，复杂编码与高 agentic 任务节省 "up to 45%"。
- **F068** Opus 5.5 降本（L13004–13005）：同月发布，相对 Opus 5 将客户每任务成本降低 "approximately 40%"（降价与效率改善的组合，占比因任务而异）；因算力效率，上述改善得以在保住利润率的同时实现（L13006–13007）。
- **F069** Opus 4.5 效应（L13010–13019）：2025 年 11 月发布 Opus 4.5（能力更强、价格与每任务成本低于前代 Opus 4.1）后，季度环比收入增速从截至 2025-12-31 三个月的 "48%" 加速至截至 2026-03-31 三个月的 "132%"；2026 年 9 月发布 Opus 5.5 后大量客户从旧模型迁移。

## 10. 增长战略（七条）

- **F070** 战略总纲（L13115–13119）：持续投资于人与文化、算力与基础设施、Claude 的智能/能力/安全、Claude 的可及广度、客户采用与扩张、进入新市场、加速使命的战略交易与伙伴关系。
- **F071** Invest in our Talent and Culture（L13121–13128）：保持人才密度；用 Claude 本身实现"不与 headcount 线性同步"的增长。
- **F072** Invest in Compute（L13134–13144）：与超大规模云商和芯片供应商合作获取多元算力；打算在现有承诺之外锁定更多算力、"expand our own data center footprint"、改善算力投资成本结构；继续以多芯片编排与算法研究复利式提升算力效率。
- **F073** Advance Claude's Intelligence, Capability, and Safety（L13146–13158）：持续投资驱动每一代 Claude 模型的突破；扩展自主工作的复杂度与时长；列举专业领域（软件开发、金融服务、保险、医疗、生命科学、法律、教育、零售与商业、电信、专业服务、技术、网络安全）。
- **F074** Make Claude Available Everywhere（L13160–13168）：现有渠道包括自有平台与应用——"Claude Code, Claude Cowork, Claude.ai, Claude Security, Claude Design, and Claude Science"；云市场集成 AWS、GCP、Azure；企业应用内嵌。
- **F075** Drive Adoption Across Existing and New Customers（L13170–13181）：扩大 direct go-to-market 与 Applied AI 团队；深化云分发伙伴关系；继续投资 prosumer 渠道；通过区域办公室与伙伴扩张国际业务，"we expect international expansion to be a meaningful driver of growth"。
- **F076** Extend the Frontier into New Markets（L13183–13199）：生命科学（制药支出超 $2T）中 Claude 已被客户、生物技术伙伴与自有研究员用于药物发现与开发；已自建深度生命科学专长——"hiring industry experts, building a molecular biology lab, acquiring Coefficient Bio, and partnering with industry leaders"；以 Model Hardware Standard 进军物理工作（操控显微镜、液体处理器、现货机械臂）。
- **F077** Pursue Strategic Transactions and Partnerships（L13201–13218）：选择性并购、投资与战略合作；2026 年 4 月完成对 **Coefficient Bio, Inc.**（computational biology company）的收购以加速生命科学研究；以及 Ode with Anthropic 等。

## 11. 产品全景

### 11.1 Claude 模型家族

- **F078** 四个模型等级（L13256–13257）："The Claude model family is currently composed of four model classes: Mythos (including Fable), Opus, Sonnet, and Haiku."
- **F079** 通用能力（L13258–13259）：可单独或组合使用；"All models support text, code, and multimodal inputs."
- **F080** Mythos（含 Fable）双配置（L13261–13269）：最强模型等级，在编码与长时程 agentic 任务上表现前沿；因在漏洞发现与生物学等敏感领域能力先进，以两种配置部署——**Fable** 一般可用并运行生产级防护（阻断或限制敏感主题，可将请求路由至较弱的 Claude 模型）；**Mythos** 面向经审查的网络安全与生命科学机构/个人，防护经过校准，通过 trusted-access programs（含 **Cyber Verification Program**）提供。
- **F081** Mythos 时间线（L13270–13272）：2026 年 4 月以 "Claude Mythos Preview" 经 Project Glasswing 首次提供；2026 年 6 月 Fable 5 一般可用并向 Glasswing 参与者提供 Mythos 5；2026 年 9 月发布 Mythos 5.1 与 Fable 5.1。
- **F082** Opus（L13274–13278）：推理密集型任务的"主力机型"（workhorse）；最新发布 **Claude Opus 5.5** 定位企业 daily driver，端到端驱动项目级 agent，推进 agentic 编码、computer use 与知识工作；Opus 模型持续位居关键行业基准前列。
- **F083** Sonnet（L13280–12283）：面向日常任务的多用途等级，平衡性能、成本与速度，覆盖最广的通用场景（含多 agent 编排中的大批量 sub-agent）。
- **F084** Haiku（L13285–13287）：最低成本、最快等级，面向客服 agent、大规模文档处理等高并发负载。

### 11.2 Claude Platform（平台能力）

- **F085** 平台定位（L13290–13292）：让开发者与企业构建、管理、部署 agentic AI 应用，基础设施具备高可靠性、安全性与可用性。
- **F086** 平台功能清单（L13294–13338）：**Extended Thinking**（先进行内部推理再作答）、**Adaptive Thinking**（自动校准是否/多少推理）、**Effort Controls**（按请求指定努力级别）、**Tool Use**（原生调用外部函数与 API，支持并行执行与交错思考；搜索工具按需加载以降低 token 开销）、**Long Context**（大上下文窗口，可容纳整个代码库/文档集/长 agent 历史）、**Structured Outputs**（约束为指定 schema 如合法 JSON）、**Code Execution**（沙箱执行环境，可运行 Agent Skills 打包的脚本）、**Web Search**（原生实时联网并带引用）、**Files API**（一次上传、跨会话引用）。
- **F087** MCP（L13342–13347）："MCP is an open standard we introduced in November 2024 and donated to the Linux Foundation's Agentic AI Foundation in December 2025"；定义 Claude 及其他 AI 工具连接企业数据源、工具与工作流的通用接口；平台原生 MCP connector 自动处理连接管理、工具发现与错误处理。
- **F088** Agent Skills（L13349–13354）：把可重复任务、工作流与领域专长编码为按需加载的可复用包；预置 Word、Excel、PowerPoint、PDF 等常见格式技能，自定义技能可承载工程标准、监管流程、专有工具链。
- **F089** Model Hardware Standard（L13358–13363；L12524–12526、L13196–13197 呼应）：currently in research preview；使 AI agent 能发现、理解并安全操作实验室与制造设备（显微镜、液体处理器、现货机械臂）；模型无关，可经 MCP 等标准协议连接任何有可编程接口的设备。
- **F090** 可用性（L13370–13372）：可直接从 Anthropic 获取，也可经 AWS、GCP、Azure 获取；"Feature availability varies by deployment."
- **F091** 成本/速度/规模（L13374–13390）：**Prompt Caching**——复用的大型提示组件可缓存 "up to one hour"，"reducing cost by up to approximately 97% and latency by approximately 60% for long prompts"；**Batch Processing**——高容量异步处理降本；**Fast Mode**——低延迟响应。
- **F092** Harnesses（L13391–13409）：自主运行需要 harness（安全环境、凭据、记忆、编排循环）。两种方式：**Agent SDK**——把驱动 Claude Code 的同款生产级 harness 提供给所有开发者在其自有算力上运行（内置上下文管理、会话处理、多 agent 协调、提示优化）；**Claude Managed Agents**——由 Anthropic 托管 harness 与算力（沙箱、凭据、记忆、agent 循环），客户只定义任务、工具与护栏，新模型上线无需重建 agent 循环。

### 11.3 第一方应用与集成

- **F093** Claude Code（L13416–13421）：形态为 "terminal tool, desktop app, web interface, and mobile app"，原生集成 GitHub 与主流 IDE；处理多步软件开发任务，保持长上下文，支持并行 agent 会话。
- **F094** Claude Cowork（L13425–13431）：桌面/Web/移动的知识工作 agent，构建于 Claude Code 的 agentic 架构；返回完成的文档、表格、演示文稿与整理好的文件夹，"with no terminal or code required"。
- **F095** Claude.ai（L13433–13440）：旗舰对话产品，桌面/Web/移动可用；面向企业、团队与个人；支持文件上传、跨对话持久上下文的项目（projects）、记忆、联网搜索、实时渲染代码与文档的 artifacts；"delivers top-of-funnel demand generation for enterprise adoption"。
- **F096** Claude Security（L13442–13449）：防御性网络安全产品，"available in public beta to Claude Enterprise customers"；像安全研究员一样对代码推理、追踪数据流、发现依赖上下文的复杂漏洞；每项发现附置信度、严重度评估与复现步骤；可直接进入 Claude Code 审查并应用补丁。另见 L12704–12705（持续扫描代码库并在攻击者之前提出修复）。
- **F097** OSS Scanner（L12508–12509；L12704–12705）：recently launched，把部分安全能力延伸至企业软件所依赖的开源项目。
- **F098** Claude Tag（L13451–13458）：在 Slack 等生产力工具中协作的 agent；用户以自然语言在频道/线程中 @Claude 委派工作；借助会话上下文、企业软件工具、共享文档与频道级记忆，直接在线程内返回答案、草稿、分析与 pull request，充当"环境感知的队友"。
- **F099** Claude Design（L13460–13464）：经自然语言对话与直接编辑创建设计稿、原型、演示等视觉作品；服务设计师、市场、创始人、GTM 人士。
- **F100** Claude Science（L13466–13475）：科研 AI 工作台（桌面端），集文献分析、数据处理与论文撰写；"queries more than 60 scientific databases"；可在实验室自有机器、机构集群或按需云资源上执行计算密集负载；返回可发表的图表与稿件（原生渲染、完全可复现代码、agent 验证、可溯源结果）。

### 11.4 企业级服务与安全功能

- **F101** Claude Enterprise（L13476–13481）：客户经此访问上述产品；提供 SAML SSO 与 SCIM 配置、RBAC、审计日志、Compliance API、支持 HIPAA 合规的配置，以及集中式 IT 管理控制台（成本可见性与控制）。
- **F102** Enterprise Frontier Safeguards（L13483–13494）：2026 年 9 月 announced；自动化安全监测的活动数据存储在客户自有云账户、受客户加密密钥与访问控制保护；自动系统审查近期活动并在发现严重滥用时直接告警客户安全团队，无需 Anthropic 员工审查；与 "more than 100 customers"（金融、医疗、公共部门等）共同开发；分阶段推出， rollout 完成前合格客户享有 Fable 5 与 Fable 5.1 的零数据留存（除法律要求或打击滥用所需外，不存储其输入输出）。

### 11.5 垂直解决方案（七项）

- **F103** 总述（L13495–13503）：在通用工具不足够的行业构建垂直方案，预置领域知识、行业合规控制与预配置数据集成；经 Claude Enterprise 与 Team 计划、个人订阅计划上的领域连接器/插件、Claude Platform 以及（教育）机构级协议分发；"To date, we have launched seven vertical solutions"。
- **F104** Claude for Financial Services（L13504–13510）：为金融专业人士提供预建可定制的 AI agent（起草 pitch book、审阅财报、KYC 筛查、财务分析），直插既有数据源（市场数据、数据仓库）并运行于 Excel、PowerPoint、Word、Outlook 及 Claude 自有应用。
- **F105** Claude for Financial Advisors（L13513–13518）：面向财务顾问与财富管理公司的预建工作流（客户会议准备、跟进起草、组合再平衡审阅、遗产与税务简报），接入托管平台、组合管理与财务规划工具、CRM，内置顾问复核以助合规。
- **F106** Claude for Healthcare（L13520–13526）：面向提供方、支付方与医疗科技公司；覆盖临床推理、医疗编码、长时程 agentic 操作；支持 HIPAA 合规的医药与运营工作流；连接 CMS Coverage Database、ICD-10、NPI Registry，含 FHIR 开发与 prior authorization 审查的 agent skills。
- **F107** Claude for Life Sciences（L13528–13534）：面向计算生物学家、生物信息学家、临床试验经理与注册事务专家；覆盖有机化学、结构生物学、实验方案、生物信息管线；支持从早期发现、临床前到临床试验运营与注册申报的全链条；接入电子实验记录本、数据仓库、科学文献。
- **F108** Claude for Legal（L13536–13544）：面向法务、公司法务、律所律师与法律运营；经 MCP 连接器接入 e-discovery 与法律数据智能平台（如 Relativity）、AI 合同平台（如 Ironclad）、法律研究数据库、交易室与事项管理系统；可按团队先例、流程、升级链、风险校准与行文风格配置，控制设计支持 attorney-client privilege、ethical walls 与保密义务。
- **F109** Claude for Education（L13546–13557）：Claude for Higher Education 服务师生研管；含旨在强化批判性思维的学生 learning mode；Claude for Teachers 为经验证的美国 K-12 教师提供免费 premium Claude、教学技能库及对接循证课程的直连，课程标准覆盖 "all 50 states"。
- **F110** Claude for Government（L13559–13564）：面向美国政府机构的起草、研究、分析与编码，环境为 "FedRAMP High authorized"；美国政府以外及分类环境客户可经 Amazon Bedrock 获取 Claude 模型（受该平台授权与可用性约束）。

## 12. 基础设施与算力体系

- **F111** 多芯片平台明细（L13581–13606）：
  - **AWS Trainium**（L13584–13588）：与 Amazon 的战略合作提供定制 Trainium 芯片与算力基础设施，并有机会影响未来代际 Trainium 芯片。
  - **Google TPUs**（L13589–13592）：与 Google 和 Broadcom 的伙伴关系提供多代 TPU 平台算力。
  - **NVIDIA GPUs**（L13594–13599）：与 NVIDIA 的战略合作，加之与 Microsoft、SpaceXAI、Nscale、Lambda 及其他云提供商的安排，提供含 NVIDIA Grace Blackwell 与 Vera Rubin GPU 系统的算力，并可与 NVIDIA 直接协作优化未来硬件。
  - **AMD GPUs**（L13601–13606）：与 AMD 的关系及经批准的 AMD Helios 机架级系统制造商与第三方服务商安排，提供 AMD Instinct™ GPU（含 MI450 系列）算力，并与 AMD 开展多年工程协作。
- **F112** 多芯片策略优势（L13572–13580）：多供应商获取算力、按负载选择最优性价比芯片、与供应商协同影响未来芯片路线图。
- **F113** 新芯片导入提速（L13608–13617）：借助 Claude 与既有跨芯片族基础（含专有编排层），新芯片平台投产时间大幅缩短，降低对单一硬件供应商的依赖。
- **F114** Anthropic Direct（L13621–13629）：从固定期限购买算力转向混合模式——除云服务外，直接采购专用 AI 加速器并部署于按其规格租赁与代运营的专属数据中心；"Our first data center facility became operational this year"（首个数据中心设施于本年度投运）。
- **F115** 设备租赁（L13638–13645）：经 master equipment leases（含 "2026 Lease Arrangement"）采购 AI 加速器及 CPU、高带宽内存等组件，部署于他人代运营的专属数据中心。
- **F116** 数据中心合作（L13647–13660）：与 Fluidstack USA I Inc.（"Fluidstack"）签订 colocation and services agreement 提供数据中心开发与运营服务；已直接签订数据中心租约并预计增加；部分项目依赖融资方或伙伴为租约义务提供担保（托管该伙伴芯片/算力基础设施）；未来扩张可能依赖少数 CSP、伙伴与融资方的持续意愿与能力。
- **F117** 电力采购（L13662–13668）：需与公用事业公司另签协议，或开发 behind-the-meter 发电能力；锁定电力容量通常需长周期与大额提前承诺。
- **F118** 数据中心地理（L13669–13672；L14502–14505 呼应）：目前主要位于美国；正在国际追求额外数据中心容量以支持全部负载类型。
- **F119** 多云分发（L13676–13679）：Claude 经三大云的专属 AI 服务层提供——"Amazon Bedrock, Gemini Enterprise Agent Platform, and Microsoft Foundry"，避免供应商锁定。

## 13. 客户与商业模式

- **F120** 客户两类（L13698）："Our customers fall into two primary categories: enterprises and prosumers."
- **F121** 客户广度（L13681–13692）：从最大企业到 AI 原生公司、政府与研究机构及 prosumers；企业级用例包括保险核保、救命药临床报告撰写、网络安全威胁检测与修复、资管组合分析；AI 原生公司在 Claude 上构建下一代编码工具、设计平台与生产力应用；政府与科研机构用于材料科学到能源安全。
- **F122** 具名客户与机构（L12844–12854）：Fortune 500 客户包括 **American International Group, Inc.（AIG）** 与 **Bristol Myers Squibb**（关键任务工作流）；科研机构包括 **Garvan Institute of Medical Research、Gladstone Institutes、University of California, San Francisco（UCSF）**；**Legora** 与 **Salesforce** 在 Claude 上构建触达数百万终端用户的 AI 产品。
- **F123** Prosumer 订阅（L13713–13718）：知识工作者（研究者、开发者、分析师、作者）订阅 **Claude Pro** 与 **Claude Max**，用于复杂认知工作（起草分析、综合研究、写审代码、建财务模型、自动化工作流）；借助 Claude Cowork，非技术 prosumer 无需写代码即可构建 agentic 工作流。
- **F124** 软件开发者的三重角色（L13706–13712）：同时是客户、平台应用的架构师与组织级采用的内部布道者。
- **F125** 部署行业（L12675–12677）：金融服务、保险、医疗健康、生命科学、法律、教育、零售与商业、电信、专业服务、技术、网络安全。
- **F126** 扩张无需新部署（L13754–13759）：每个新版 Claude 模型均提升既有用例表现，客户可增加用量、使用更高订阅档位、把更多工作流搬上平台，"without a new sales cycle or procurement decision"。
- **F127** 渗透率判断（L13760–13763）：仍处渗透极早期；多数企业客户仅部署于少数团队与用例；"We believe most knowledge workers globally have not yet used frontier AI."

## 14. 文化、价值观与人才

- **F128** 员工人数（L13869–13871；L13046–13047、L13806–13808 重复）："As of September 30, 2026, we had approximately 5,300 employees worldwide"；其中多数（"a majority"）在研究、工程与产品开发职能（L13821、L13872–13873）。
- **F129** 员工昵称（L13812–13813）：员工内部被称为 "Ants"，体现协作、低 ego 文化。
- **F130** 联创连续性（L13780–13782）："All seven of Anthropic's co-founders remain active leaders in the organization."（在包括其他前沿 AI 实验室在内的科技公司中罕见。）
- **F131** 可遗憾流失率（L12580–12581）："approximately 1% regrettable attrition of our employee base overall in the TTM period ended September 30, 2026."
- **F132** 价值观（L13831–13867，七条）：Act for the Global Good；Hold Light and Shade；Be Good to Our Users；Race to the Top on Safety（"the market will reward it… companies must compete on safety"）；Do the Simple Thing That Works；Be Helpful, Honest, and Harmless（同时是 Claude 行为准则）；Put the Mission First。
- **F133** 人才谱系（L13873–13877）：团队包含 RLHF、Constitutional AI、GPT-2 与 GPT-3、mechanistic interpretability 的首创者，首个被前沿 AI 实验室正式采纳、将安全评估与模型能力阈值挂钩的 Responsible Scaling Policy 的制定者，以及 Scaling Laws 奠基论文作者（另见 L12576–12578、L12427–12433）。
- **F134** 跨学科与多元（L13877–13890）：获奖计算机科学家、物理学家、神经科学家、数学家、政策研究者及资深工程与 GTO 领导；主动从哲学、新闻、教育等非传统背景吸纳人才。
- **F135** 劳动法合规（L13884–13885）：在某些运营国家遵守当地劳动法，员工可能自动适用行业性集体谈判协议（collective bargaining agreements）。
- **F136** 文化特征（L13783–13827）：Use What We Build（90% 代码贡献由 Claude 写入，见 F034）；同时研究安全与能力（首个采纳正式 RSP 的前沿实验室，由构建模型的研究者共同制定）；追求人才密度（人均 TTM 收入 >$6.6M）；对每个职能都要求严谨（真理寻求环境，"the best argument wins"）。

## 15. 研究体系（Research-to-Product Pipeline）

- **F137** 研究哲学（L13895–13901）："do the simple thing that works"；对数据构成、模型架构与训练方法追求持续、经实证验证的改进，必须证明随规模扩大仍然成立；当前聚焦软件开发与 agentic 能力——经济影响大、安全问题在此显现（安全研究的试验场）、输出高度可验证。
- **F138** 不做什么（L13904–13907）："we do not currently focus on developing video and image generation models, despite their commercial appeal"；相应算力投向编码、agentic 技能与安全研究，该决策也提升了模型的资本效率。
- **F139** 研究文化（L13908–13911）：高度协作透明；多团队并行时以最佳实证结果为准而非最大声量或最高职级；研究速度显著快于人数增长。
- **F140** Pre-training（L13920–13927；L12605–12613 呼应）：纪律化管线——候选改进先小规模验证再消耗大量算力；进入前沿训练 run 的门槛高且严格基于证据（须证明随模型增大仍成立）；前沿训练 run 是"计划内的资本部署"，输入明确、准入标准严格。
- **F141** Post-training（L13928–13937；L12615–12620 呼应）：从微调步骤成长为最大研究领域之一，反映从助手到 agent 的市场转移；以完整、真实、达到专业复杂度的任务组合训练；该任务组合的广度与真实度构成"最持久的科学优势之一"，外部难以观察与复制。
- **F142** Inference（L13938–13942）：模型架构与推理基础设施协同设计，共享规划周期、汇报线与绩效目标；架构决策以推理经济性为优先。

## 16. 安全与研究（RSP 类机制）

- **F143** Responsible Scaling Policy 内容（L13947–13961）：描述应对 AI 灾难性风险（catastrophic risks）的方法；要求定期发布详细风险报告；每个模型发布前在灾难性风险最相关领域测试能力与可滥用性；风险报告说明评估结果、已实施的缓解措施、以及风险为何被对应收益正当化；现行版本下发布 **Frontier Safety Roadmap**，详述安全、对齐、防护与 AI 政策的可衡量进展计划，对内鞭策、对外供客户与监管者评估进度。
- **F144** 风险缓解实践（L13962–13967）：过去包括延迟发布新模型并限制初始可得性（如 Mythos 经 Project Glasswing 首发）；未来可能采取更多影响开发/发布方式与时间的措施。
- **F145** Claude's Constitution（L13970–13993）：直接用于模型训练的宪法；活文档；研究者发现以高质量宪法文件加 portraying an aligned AI 的虚构故事训练可降低 Claude 的 misalignment rate；四项优先级——Be Broadly Safe（避免不可逆行动、支持人类监督）、Be Broadly Ethical（诚实与健全道德判断）、Be Compliant with our Guidelines（遵守运营标准与绝对禁止事项）、Be Genuinely Helpful（专家级实质帮助）。
- **F146** 模型验证（L13994–14005）：RSP 之外，发布前经多阶段评估（能力、安全行为、社会影响含偏见与歧视），结果与局限公开于 model system cards；测试涵盖能力与准确性基准、事实性与幻觉评估、诚实性评估、长时程 agentic 可靠性测试、对抗性红队；发现问题经追加 post-training、调整防护与再评估处理，残余局限记录于 system card。
- **F147** 训练数据（L14006–14012）：来源包括公开互联网信息、第三方授权或委托数据集、自有模型生成的合成数据；对第三方数据源尽调（质量、来源、适用性），多含劝阻纳入个人数据的合同限制；数据治理与过滤旨在提升质量、去重并减少有害内容暴露。
- **F148** 偏见与公平（L14013–14020）：以分层方式（数据集治理、post-training 对齐、部署前评估、部署防护）管理代表性与多样性；usage policy 禁止将 Claude 用于歧视性决策，并要求对影响就业、住房或法律事项的高风险自动化决策进行人工监督。
- **F149** 认证与外部验证（L14022–14032）：已获 **ISO/IEC 42001** 认证（经独立第三方审计的 AI 管理体系）；**SOC 2** 报告与合规文件可经网站 trust center 按需获取；向外部评估者提供部署前模型访问，包括 **U.S. Center for Advancing Innovation and Standards for Super Intelligence（CAISSI）** 与 **U.K. AI Security Institute**（见 model system cards）。
- **F150** Alignment（L14033–14049）：团队关注模型是否按意图行动、不擅自采取非预期行动；行业已观察到的失准行为包括绕过网络与沙箱限制、自我提权、为达成目标采取未授权行动、干扰其他 AI agent、虚报任务完成或验证；随自主性、权限与系统集成增加，后果可能加剧；内部对齐评估显示新发布的前沿模型较前代对齐改善。
- **F151** Interpretability（L14051–13060）：将 AI 模型描述为 "grown, not built"；在 mechanistic interpretability（LLM 工作机理科学）领域被广泛认可为领导者；发展出映射模型概念形成与连接的数学技术，研究类心理状态构造，测试对内部表征的直接调整以引导行为；发布前用于检测不良行为倾向。
- **F152** Safeguards（L14061–13071）：以探针与分类器监控输入输出、针对 prompt injection 等攻击向量训练、监测自伤意念等用户安全关切；违规处置从实时响应调整到账号警告直至终止账号；公开披露政策与漏洞赏金计划（bug bounty）。
- **F153** 能力与安全的正向关系（L14074–13076）："We have observed that more capable models are generally better at recognizing and preventing high-stakes misuse"；安全措施与模型效用并非天然冲突。
- **F154** 发布流程（L14077–13085）：每次发布附详细 system card（能力与安全评估、外部测试者报告、局限与不良行为迹象）；发布前 **Frontier Red Team** 评估新模型是否赋予潜在攻击者实质新能力；Safeguards 团队维护针对恶意软件创建、钓鱼、基础设施攻击等网络滥用的专用分类器与监控。
- **F155** 发布决策机制（L14086–14101）：是否开始训练新模型等决策 case-by-case；综合考量模型能力与行为、防护与安保有效性、发布范围；计划在 pre-training、post-training 与内部部署各阶段扩展测试；据此可能延迟或暂停训练/相关研究、延迟发布、限制访问；评估亦参考 CAISSI 与 UK AI Security Institute 的自愿预部署评估；对涉及国家安全领域实质推进前沿的模型向指定政府伙伴提供扩展早期访问以便独立评估；"we do not release every model we develop for general use; when the model's capabilities warrant caution, we may restrict availability or decline to release entirely"。
- **F156** Fable 5 的受限发布（L14105–14106）：Fable 5 后续开放一般使用，但对部分网络安全、生物学与化学能力施加安全限制。
- **F157** RSP 行业影响（L14113–14114）："After we published the first version of our Responsible Scaling Policy in September 2023, two other leading frontier AI labs adopted similar frameworks within months."
- **F158** Pacing the Frontier（L14115–14125）：公开呼吁建立行业级标准（主要关于用 AI 加速 AI 开发），使能力不快于安全/对齐/安保实践；该呼吁设想与政府协作且不描述自身开发或发布时间表；第一步是对未来监管标准合规的独立验证——已开始实施独立评估员与内部风险安全团队并肩工作、拥有广泛内部访问（受法律、保密与安保限制）的项目。
- **F159** 外部评审投资（L14126–14128）："we currently anticipate investing at least $1 billion over the next five years to build external reviewer capacity with Accenture. The terms of this arrangement have not been finalized and are subject to change."
- **F160** 关键基础设施安全主张（L14137–14152）：提出六条——负责任的模型访问/资金/培训/上手支持（尤其资源不足的关键基础设施防御方）；构建可观测性与安全工具；确保 agentic 身份可追溯可问责；共享持续监控最佳实践；投资授权测试、私密披露与验证性修复；与政府、安全伙伴、开源维护者共享工具、playbook 与威胁评估。
- **F161** Project Glasswing 网络防御投入（L14155–14159）："We have committed up to $100 million in cyberdefense-related initiatives through Project Glasswing"；未来预计投入更多资源，范围、时间与金额未最终确定。

## 17. 公共利益承诺（PBC 机制）

- **F162** Societal Impacts 团队（L14173–14177）：构建隐私保护工具研究 Claude 的真实大规模使用；包括 "the largest multilingual qualitative study of its kind, in which more than 80,000 people shared in depth how they see AI shaping their lives"。
- **F163** Economics 团队与开放数据（L14178–14181）：发布 recurring data reports 与完全开放数据集 **Anthropic Economic Index**（Claude 在职业、行业、地区的使用），并建模未来经济情景。
- **F164** Anthropic Institute（L14182–14184）：跨 Anthropic 与外部伙伴及公众共享研究与内部数据的机构，共同应对 Powerful AI 的重大问题。
- **F165** Initial Public Benefit Issuance（L14194–14204）：向全资子公司 **Anthropic Public Benefit Fund**（致力于 Company Purpose）捐赠 "846,840,960 shares" Class N 普通股，占 "5% of our fully diluted shares as of June 30, 2026 (assuming full conversion of the Amazon Notes)"。
- **F166** 追加捐赠框架（L14206–14222）：董事会已批准与未来股价上涨挂钩的追加捐股框架——IPO 后，每当股价较上一里程碑上涨 50%，董事会可酌情向基金（或其他受赠方）增发最多额外 "2%" 的当时流通股份（含期权/RSU/可转证券及基金已持股份）；里程碑条件为收盘价在截至的 120 个连续交易日中至少 90 日超过阈值，且发行前十个交易日均价亦超过阈值；未来捐股由董事会酌情决定。
- **F167** 基金治理（L14223–14229）：基金股份可转让、捐赠或以注册公开发行/私募方式出售以推进公共利益倡议；董事会决定分配直至批准特定治理结构；初始管理人为 "Dario Amodei, Daniela Amodei, Jack Clark, and Dr. Neil 'Buddy' Shah"。
- **F168** 员工捐赠匹配（L14236–14242）：员工可承诺将部分股权奖励或等值现金捐给 donor-advised fund 或非营利组织，公司以 Class N 股票匹配。
- **F169** 联创慈善承诺（L14243–14244）："our co-founders have each pledged to dedicate 80% of their personal equity in Anthropic to philanthropic causes"，独立于且不适用捐赠匹配计划。
- **F170** 资源投向意图（L14187–14193）：拟将相当部分资源用于确保前沿 AI 安全并让收益广泛分配——可能包括向非营利组织、研究机构捐助，及面向原本无法接触的社区、教育者与公共机构的 Claude 可及性项目。

## 18. 竞争（Competition）

- **F171** 模型开发者竞争（L14250–14253）："We face direct competition from companies building frontier models for third-party software developers and enterprises, including **OpenAI** and **Google**, and large, well-capitalized technology companies investing to reach the frontier."（对手资本雄厚、客户基数大、可将模型集成进第一方应用。）
- **F172** 自我定位（L14254–14258、L14263–14267）：以企业为主焦点、留守并定义前沿、研究人才与算力投资效率构成差异化；面对更广的模型供给（大型公司、专业 AI 实验室、open-weight/open-source 模型——"shared weights, training data, and code… released by state actors and international and domestic research organizations"），以前沿模型兼顾最高智力任务与日常任务的高性价比应对。
- **F173** 第一方应用竞争（L14268–14272）：作为平台公司专注底座，但自建第一方应用时可能在个别品类与企业软件/应用公司竞争。
- **F174** 现状阻力（Status Quo，L14273–14281）：企业 entrenched 的遗留系统、既有流程与变革管理成本（再培训、流程重设计、内部政策、文化转变）可能延迟或阻止采用；强监管或风险厌恶行业决策者可能默认维持现状。
- **F175** 主要竞争因素（L14283–14317，13 条）：使命聚焦；留守并扩展智能前沿；招聘留任世界级研究人才；安全可靠可信赖的智能；获取训练与部署所需算力（或受供给约束、容量限制或第三方分配决策影响）；提升训练与部署效率；以可接受条款获得融资；研究-产品-GTM 一体化；维持基础设施与分发伙伴关系；吸引在 Claude Platform 上构建产品的客户；获新客并在存量客户中扩展；持续构建预判市场需求的应用；驾驭竞争格局变化（含竞争者/客户整合与竞争者间战略合作）。
- **F176** 竞争结论（L14318）："We believe that we compete favorably across these factors and are uniquely positioned at the frontier of AI."

## 19. 知识产权

- **F177** 保护体系（L14320–14328）：依赖商业秘密、版权、专利、商标法与合同限制（保密协议、许可、IP 转让协议）的组合；最关键 IP 的访问仅限少数员工；员工、承包商、顾问及第三方须签署保密与专有权利协议。
- **F178** 专利数据（L14329–14334）："As of September 30, 2026, we held 40 issued U.S. patents, with an additional 67 U.S. patent applications pending (including 32 nonprovisional and 35 provisional), and 26 issued patents in foreign jurisdictions, with an additional 12 patent applications pending."
- **F179** 商标数据（L14335–14339）："As of September 30, 2026, we held 29 registered trademarks in the United States, with an additional 11 applications pending, and 237 registered trademarks in foreign jurisdictions, with an additional 261 applications pending."
- **F180** 局限性声明（L14340–14346）：IP 法律与程序仅提供有限保护；权利可能被挑战、无效、规避、侵权、盗用或违反。

## 20. 政府监管（Government Regulation）

- **F181** 总体立场（L14347–14359）：受多法域法律法规约束，"we have been, and expect to continue to be, subject to inquiries, investigations, and subpoenas by governmental authorities"；支持政府建立促进安全有益 AI 的框架；已主动与美国及国际立法者、监管者与利益相关方互动。
- **F182** 政府合作与立法支持（L14360–14364）：与 **CAISSI** 签订协议，承诺在模型公开发布前后提供测试与评估访问；同意按同一协议向 **U.K. AI Security Institute** 提供预部署测试访问；公开支持加州 **Transparency in Frontier Artificial Intelligence Act（SB 53）**。
- **F183** 监管领域框架（L14370–14373）："The primary areas of regulation that affect our business include AI-related regulations, data privacy and security, export controls and trade regulations, and other matters such as intellectual property, employment and labor, competition and antitrust, consumer protection, and tax."
- **F184** AI 监管—美国（L14375–14388）：联邦与州两级并行；NIST 已制定 **AI Risk Management Framework**（目前自愿，但可能塑造未来强制要求）；FTC 与多州总检察长以消费者保护与隐私安全法解释并施加数据标准；多州已颁布或考虑 AI 立法；**2026 年 9 月 24 日**，纽约与新泽西州总检察长联合其他州与领地总检察长致信美国参众两院领导层，敦促国会建立前沿 AI 的全面联邦立法与安全协议。
- **F185** AI 监管—欧盟（L14388–14394）：**EU AI Act** 建立基于风险的框架；通用 AI 模型（GPAI）面临透明度、技术文档、欧盟版权合规、训练数据摘要发布等义务；具系统性风险者另有模型评估、系统性风险缓解、严重事件报告与网络安全保护义务；高风险系统须满足风险管理、数据治理、文档、透明度、人工监督、准确性、稳健性与网络安全要求。
- **F186** 违规后果（L14394–14398）：实际或被认为不合规可导致监管调查、执法、巨额罚款、诉讼、声誉损害、客户信任流失、产品可用性或性能中断、被迫不利变更、延迟新品。
- **F187** 数据隐私与安全（L14405–14431）：美国联邦/州/地方及外国法律涵盖隐私、数据保护、安全、数据本地化与数据处理；含加州 **CCPA**（披露、选择退出处理/出售/共享等义务）；FTC 与州 AG 执法；欧盟与英国 **GDPR**、欧盟 **Digital Services Act**（在线平台义务）、**Data Act**（数据切换与共享）、**Network and Information Security Directive**（风险管理与事件报告）；可能与美国政府数据访问法等冲突；合规需大量技术与组织投入。
- **F188** 出口管制与贸易（L14432–14442）：跨境提供产品受国际条约、出口管制、经济与贸易制裁、海关与当地贸易规则约束；美国商务部持续收紧出口管制并将企业列入 **Entity List**（接收特定物项需许可证），可能限制与特定潜在客户的业务。
- **F189** 对自身的直接限制事件（L14443–14446）："in June 2026, the U.S. Department of Commerce imposed worldwide export restrictions on our Fable 5 and Mythos 5 models. In collaboration with the U.S. government and industry partners, we updated our safeguards, and we re-deployed our Fable 5 and Mythos 5 models once the U.S. government lifted its restrictions."（2026 年 6 月 Fable 5 与 Mythos 5 遭全球出口限制；更新防护后限制解除、重新部署。）
- **F190** 出口管制的其他影响（L14446–14458）：类似限制若再现，可能限制人才招募、既有员工利用、模型改进与国际可用性；对 AI 加速器与算力的出口管制变化可能影响基础设施获取；他国对美公司的类似措施可能限制全球业务。
- **F191** **Other Regulations 全量**（L14459–14478）：知识产权法（专利/商标/商业秘密；AI 专利格局演变带来侵权索赔与保护不确定性；演变中的版权制度）；雇佣与劳动法（工资、雇员分类、工作条件、福利、反歧视、职场安全、解雇；错分类与演变标准或致重大责任与人力成本上升）；竞争与反垄断法（美、欧及其他法域禁止反竞争行为；对科技公司市场支配、并购与 AI 系统监管趋严可致调查、执法、罚款或要求改变商业行为）；消费者保护法（禁止不公平或欺骗性行为；或要求就 AI 系统披露、质量与安全标准）；税务（跨法域所得税、销售税、增值税等；税务机关可能不认可公司立场；国际税制变化影响有效税率）；反腐败、反贿赂、反洗钱、环境、无障碍（accessibility）、广告与政府采购法规。
- **F192** 医疗健康监管（L14479–14488）：医疗与生命科学产品及客户在该领域的使用，可能受药品、生物制品与医疗器械法规约束（含 **U.S. FDA** 及类似非美机构）、医疗欺诈与滥用法、健康信息隐私与安全法（含 **HIPAA**）、以及行医与医疗 AI 使用相关法律；违规可致执法、罚款、处罚、诉讼、声誉损害与运营限制。

## 21. 设施（Facilities）

- **F193** 办公（L14498–14501）：总部位于加州旧金山（San Francisco, California）；在欧洲与亚太设国际办公室；认为现有办公设施满足当前需求。
- **F194** 数据中心（L14502–14505）：在美国租赁数据中心并 "committed billions towards expanding U.S. computing infrastructure"；已就澳大利亚与加拿大的数据中心容量签订租约；正在美国以外其他法域争取容量；持续评估包括美国与海外的新选址。

## 22. 法律程序（Legal Proceedings）

- **F195** 总述（L14506–14518）：已涉入或未来可能涉入日常经营中产生的法律程序与索赔——知识产权争议、法律/监管合规、政府批准与授权、劳动与雇佣、反歧视、商业争议、竞争、数据隐私、客户投诉等；亦收到权利人主张 IP 侵权的函件；详见财务报表附注 13 "Legal Matters"；未来或需诉讼以自卫或确立权利；结果不可预测，抗辩与和解成本及管理层精力分散均有不利影响。
- **F196** 版权系列诉讼（L14520–14528）：已在联邦及国际法院遭遇多起基于使用版权材料训练模型的版权侵权诉讼。
- **F197** Bartz 和解（L14528–14532）：2024 年 8 月，一群作者就受版权保护书籍的侵权提起集体诉讼（**Bartz** 案）；"in September 2025, we entered into a settlement agreement with the plaintiffs to settle the case for $1.5 billion, which was approved by the district court in July 2026."（否认任何不当行为；2025 年 9 月以 15 亿美元和解，2026 年 7 月地区法院批准。）
- **F198** 抗辩立场（L14533–14535）：在各案件中 "we believe we have meritorious defenses and dispute any allegation of wrongdoing."

## 23. Other Matters（与美国政府的冲突及诉讼）

- **F199** 起因（L14536–14543）：2026 年 2 月，因公司公开表明其技术不应被用于大规模国内监控或完全自主武器（"mass domestic surveillance or fully autonomous weapons"），美国总统声明其已指示所有联邦行政机构停用公司技术；同时战争部长（Secretary of War）指示国防部将 Anthropic 列为"国家安全供应链风险"（"supply-chain risk to national security"），并声明"即刻起，与美国军方做生意的承包商、供应商或伙伴不得与我们进行任何商业活动"。
- **F200** 两封信（L14542–14544）：2026 年 3 月 4 日，战争部发出两封信——一封依据 **10 U.S.C. § 3252**，另一封依据 **FASCSA 第 4713 条**——主张公司模型、平台与应用构成供应链风险。上述行动定义为 "Challenged Actions"。
- **F201** 诉讼与禁令（L14545–14553）：在 *Anthropic PBC v. Department of War, et al.*（N.D. Cal.）与 *Anthropic PBC v. Department of War, et al.*（D.C. Cir.）中积极挑战；先获加州北区联邦地区法院初步禁令——初步禁止战争部的指令与 § 3252 供应链风险认定，并初步禁止其他被告机构执行总统指令直至案件最终解决。
- **F202** 即决判决胜利（L14554–14560）：2026 年 8 月 27 日获加州北区法院"在很大程度上支持我方"的即决判决：法院认定 Challenged Actions 是报复性行为（惩罚受美国宪法第一修正案保护的言论），侵犯第五修正案正当程序条款权利；并认定战争部长行为（尤其就 10 U.S.C. § 3252）违反《行政程序法》（APA）——超越法定权限、违法、任意且反复无常；法院作出大体支持我方的最终判决。
- **F203** 上诉与 D.C. 巡回法院（L14561–14565）：被告就初步禁令提起上诉；D.C. 巡回上诉法院拒绝了我方请求在实体审查前搁置战争部长 § 4713 供应链风险认定的动议；2026 年 9 月 25 日，D.C. 巡回法院以 2-1 分裂裁决驳回我方审查请求，认定战争部 § 4713 供应链风险认定合法，且第一修正案与第五修正案正当程序权利未受侵犯。
- **F204** 后续与影响（L14566–14570）：已提交全院重审（en banc）申请；无法预测最终结果；虽继续与政府机构合作，但不能确定诉讼结果不会对向政府机构及向美国政府销售产品服务的其他客户的销售产生不利影响，进而影响业务、财务状况与经营业绩。

---

## 附：关键数字速览（本章）

| 主题 | 数值 | 行号 |
|---|---|---|
| 商业发布 | 2023 年 Q1（收入自 $0 起） | L12107 |
| $100K+ TTM 客户 | >11,900（vs >950，2025-09-30） | L12194, L12981 |
| $1M+ / $10M+ TTM 客户 | >1,900 / ~250 | L12197, L12199 |
| NRR | ~900%（2026-09-30） | L12257 |
| 收入增速 vs 算力成本增速 | 1,368% vs 300%（2026 年 Q2 同比） | L12264–12269 |
| 人均 TTM 收入 | >$6.6M（2026-09-30）vs $1.4M（2025-09-30） | L12275–12277 |
| 季度收入 | $11.6B（2026 Q2）vs $787M（2025 Q2） | L12282–12286 |
| 经营利润率 | 8%（2026 Q2）vs (152)%（2025 Q2） | L12288–12298 |
| 调整后经营利润率 | 19% vs (129)% | L12300–12311 |
| 累计融资 / 现金 / 短期投资 | $141.1B / $112.4B / $19.3B（2026-06-30） | L12315–12323 |
| 员工数 | ~5,300（2026-09-30） | L13870 |
| 可遗憾流失率 | ~1%（TTM，至 2026-09-30） | L12580–12581 |
| 内部 Claude 代码贡献占比 | >90%（2026 年 9 月） | L12370 |
| 工程师人均日代码量 | >45 倍（vs 2024 全年日均） | L12365–12369 |
| 内部使用价值增幅 | >250 倍（2026 年 1 月→9 月，按牌价） | L12388 |
| 组织杠杆 | 人数 >5x vs 收入 86x（2024Q4→2026Q3） | L12374–12379 |
| 知识工作市场 | >$40T（2025） | L12461–12462 |
| IDC AI 经济影响 | $22.5T 累计（至 2031） | L12467–12469 |
| 知识工作者人口 | >10 亿（2028E） | L12721–12722 |
| 全球制药支出 | >$2T（2026E，IQVIA） | L12520–12521 |
| Prompt Caching | 成本 -~97%、延迟 -~60%（最长 1 小时缓存） | L13379–13383 |
| Partner Network | 初始 $100M（2026）；>150,000 认证从业者 / >4,000 组织 | L12919, L12922 |
| Frontier Academy | $100M；2027 年底前培训 10,000 工程师 | L12941, L12945 |
| Accenture 外部评审 | ≥$1B / 5 年（条款未定稿） | L14127–14128 |
| Glasswing 网络防御 | 最多 $100M | L14155 |
| 公益基金捐股 | 846,840,960 股 = 完全稀释 5%（2026-06-30） | L14194–14200 |
| 专利 | 美国授权 40 + 待审 67；外国授权 26 + 待审 12 | L14331–14333 |
| 商标 | 美国注册 29 + 待审 11；外国注册 237 + 待审 261 | L14337–14339 |
| Bartz 和解 | $1.5B（2025-09 达成，2026-07 批准） | L14531–14532 |
