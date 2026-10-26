# 数据安全与信息分级（Safety Tracks）

> **本仓库当前为 GitHub 私有仓库。** 若转为公开，**凡被 git 跟踪的文件即视为已公开。**
> 本文件只描述轨道结构与流程，**不点名受限内容本身**——受限清单是本地文件
> `private/classification.md`（git 忽略，永不入库）。

---

## 一、四条轨道（Tracks）

| 级别 | 名称 | 定义 | 允许 git 跟踪 | 允许对外发布 |
|---|---|---|---|---|
| **L0 公开** | Public | 已公开的原始资料（如 SEC 申报文件及其忠实译文） | ✅ | ✅（仍需过发布门） |
| **L1 内部** | Internal | 仅含公开事实、可溯源引用的自产分析与笔记 | ✅ | ⚠️ 须通过 `--publish` 检查 + 人工复核 |
| **L2 受限** | Restricted | **项目定义的受限内容**（清单见本地 `private/classification.md`） | ❌ 只放 `private/`（已忽略） | ❌ 永不 |
| **L3 凭据** | Credentials | cookie（如 `z_c_*`）、API key / token、私钥、密码 | ❌ 不得写入仓库任何位置 | ❌ 永不 |

**判定原则**：
- 事实来自公开来源、可溯源 → 最高 L1；
- 一旦流出会暴露「不该公开的立场、意图或隐私」（具体清单见本地）→ 至少 L2；
- 一旦流出需要「吊销轮换」→ L3。

## 二、目录与轨道绑定

| 路径 | 轨道 | 说明 |
|---|---|---|
| `docs/` | L0 | 原始公开资料，只读，不写入任何个人内容 |
| `analysis/` `notes/` `models/` | L1 | 仅放公开事实 + 可溯源引用的分析产物 |
| `data/` | L1 | 已清洗、可公开引用的外部数据 |
| `data/raw/` | 不入库 | 终端/爬虫原始导出通常**禁止再分发**（已忽略） |
| `private/` | L2 | **唯一**存放受限内容的地方（已忽略，仅 README 作路标被跟踪）；清单在 `private/classification.md` |
| `scripts/safety/config.json` | 本地 | 扫描器实际配置（含敏感关键词），已忽略；入库样例为 `config.example.json` |
| `.zhihu-publish-output/` | 不入库 | 发布管道产物，含本地路径与潜在凭据（已忽略） |
| `.env` `*.pem` `*.key` | L3 | 已忽略；凭据原则上放系统钥匙串/环境，不落盘仓库 |

## 三、自动强制（Enforcement）

### pre-commit 钩子（拦截入库）

本机已执行 `git config core.hooksPath scripts/hooks`。每次 `git commit` 时自动运行
`python3 scripts/safety/scan.py --staged`，扫描**暂存区新增内容**：

| 检查项 | 级别 |
|---|---|
| 命中 L3 凭据特征（cookie / API key / token / 私钥 / 密钥赋值） | 🚫 BLOCK |
| 文件位于受限路径（见 config） | 🚫 BLOCK |
| 命中受限标记（见 §五） | 🚫 BLOCK |
| 命中敏感内容关键词（清单在本地 `config.json`，不入库） | ⚠️ WARN（提示移入 `private/`） |
| 泄露本机绝对路径（`/Users/…`、`/home/…`、`C:\Users\…`） | ⚠️ WARN |

### 发布门（拦截外发）

对外发布任何文稿（知乎、GitHub Pages、博客、邮件附件）之前：

```bash
python3 scripts/safety/scan.py --publish <文稿路径>
```

发布模式下**敏感关键词、本机路径、受限路径引用、受限标记全部为 BLOCK**。
仅在确要公开发表敏感观点时，才可加 `--allow-sensitive` 显式放行（凭据与受限标记不可放行）。

### 工作区巡检

```bash
python3 scripts/safety/scan.py          # 扫描全部 git 可见文件（tracked + 未忽略的 untracked）
```

## 四、发布轨道（知乎 / GitHub Pages / 外发）流程

1. 素材只取自 L0 / L1（公开来源 + 可溯源引用的分析）；
2. 生成文稿后运行 `scan.py --publish <文稿>`，BLOCK 清零；
3. 人工复核一遍（工具拦模式，人拦语义）；
4. `.zhihu-publish-output/` 永不入库；**draft 头部的 `<!-- zhihu-sync draft … -->` 注释块含本机绝对路径，发布正文时必须整块剔除**；
5. 发布的 request/response 含账号交互痕迹，留在忽略目录内，不外传；
6. **GitHub Pages 视为外发通道**：Pages 实际服务的每个 HTML（如 `index.html` 跳转的 dashboard）在提交前都应过一遍 `scan.py --publish`。

## 五、标记约定（Markers）

- 整篇/某节为 L2 时，在文件任意位置写标记：`<!-- data-class: restricted -->`
  （扫描器对**被跟踪文件**命中即 BLOCK——用于内容被误移出 `private/` 时的第二道防线）；
- L2 文件统一放 `private/`，首行写上述标记；
- 策略文档与扫描器自身豁免标记/关键词检查（否则会拦截自己），但**不豁免凭据扫描**。

## 六、事故处置

| 场景 | 处置 |
|---|---|
| 凭据入库且**已推送** | 立即吊销/轮换凭据 → `git filter-repo` 清理历史 → 强推；通知协作者重新克隆 |
| 凭据入库未推送 | `git reset`/amend 撤销即可 |
| 受限内容误入公开文章 | 平台删稿 → 本地移入 `private/` → 评估暴露面，必要时调整口径 |
| 误报 | 修改本地 `config.json`（关键词收窄 / 豁免清单），不新增凭据豁免 |

## 七、仓库可见性

当前为**私有仓库**。若转公开：
- 本文件与扫描器保持通用描述，受限清单永远只在本地（`private/classification.md` 与 `config.json`）；
- 转公开前跑一次工作区巡检 + 全历史敏感串核查；
- 公开窗口期内推送过的内容应视为已扩散，转私有不溯及既往。

## 八、快捷命令

```bash
python3 scripts/safety/scan.py                          # 工作区巡检
python3 scripts/safety/scan.py --staged                 # 暂存区检查（pre-commit 同款）
python3 scripts/safety/scan.py --publish path/to/draft  # 发布门
```
