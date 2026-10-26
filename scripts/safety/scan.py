#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
safety-tracks 数据安全扫描器（通用版）—— 分级与规则见本项目 SECURITY.md。

配置：与本文件同目录的 config.json（可选；缺失时使用内置默认）。
  restricted_paths         受限路径（这些路径下的内容禁止入库/外发）
  restricted_path_exempt   受限路径中允许跟踪的例外（如 private/README.md）
  sensitive_keywords       敏感内容关键词（正则片段；repo 模式 WARN，publish 模式 BLOCK）
  sensitive_scan_prefixes  只在这些路径前缀下扫关键词（空列表 = 全部文件）
  doc_exempt               豁免关键词/标记检查的文件（策略文档自身；凭据扫描不豁免）
  extra_patterns           项目附加规则 [{"name","regex","level":"secret"|"sensitive"}]

模式：
  默认            工作区巡检（tracked + 未忽略的 untracked）
  --staged        暂存区检查（pre-commit 钩子使用）
  --publish FILE  发布门：检查待外发的单个文稿
  --allow-sensitive（仅发布模式）确认要公开敏感观点时，将敏感关键词降为 WARN

退出码：0 通过；1 存在 BLOCK；2 扫描器自身错误。
"""

import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# 配置
# ---------------------------------------------------------------------------

DEFAULT_CONFIG = {
    "restricted_paths": ["private/", "data/raw/"],
    "restricted_path_exempt": ["private/README.md"],
    "sensitive_keywords": [],
    "sensitive_scan_prefixes": [],
    "doc_exempt": [
        "SECURITY.md", "README.md", "private/README.md",
        "scripts/safety/scan.py", "scripts/safety/config.json",
        "scripts/hooks/pre-commit",
    ],
    "extra_patterns": [],
}


def load_config():
    cfg = dict(DEFAULT_CONFIG)
    path = os.path.join(HERE, "config.json")
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as fh:
                cfg.update(json.load(fh))
        except (OSError, ValueError) as e:
            print(f"[ERROR] config.json 解析失败：{e}")
            sys.exit(2)
    return cfg


# ---------------------------------------------------------------------------
# 通用规则（凭据）+ 项目规则（来自 config）
# ---------------------------------------------------------------------------

SECRET_RULES = [
    ("L3凭据·知乎Cookie",
     re.compile(r"z_c_[\"'=:\s]*[A-Za-z0-9%_\-]{16,}")),
    ("L3凭据·OpenAI风格key",
     re.compile(r"\bsk-[A-Za-z0-9_\-]{20,}")),
    ("L3凭据·GitHub token",
     re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}")),
    ("L3凭据·GitHub PAT",
     re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}")),
    ("L3凭据·AWS AccessKey",
     re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("L3凭据·Google API key",
     re.compile(r"\bAIza[0-9A-Za-z_\-]{30,}")),
    ("L3凭据·Slack token",
     re.compile(r"\bxox[abprs]-[A-Za-z0-9\-]{10,}")),
    ("L3凭据·私钥",
     re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY(?: BLOCK)?-----")),
    ("L3凭据·Bearer token",
     re.compile(r"\bBearer\s+[A-Za-z0-9._\-]{20,}")),
    ("L3凭据·JWT",
     re.compile(r"\beyJ[A-Za-z0-9_\-]{10,}\.eyJ[A-Za-z0-9_\-]{10,}\.")),
    ("L3凭据·疑似密钥赋值",
     re.compile(r"\b(?:api[_-]?key|apikey|secret|passwd|password|access[_-]?token)\b"
                r"\s*[=:]\s*[\"']?[A-Za-z0-9+/_\-]{16,}[\"']?", re.IGNORECASE)),
]

# 受限标记：被跟踪文件命中即 BLOCK（防止 L2 内容被误移出受限目录）
RESTRICTED_MARKER_RE = re.compile(
    r"data-class\s*:\s*restricted|<!--\s*(?:restricted|confidential)\s*-->|"
    r":::\s*restricted|INTERNAL[- ]ONLY|【受限】|【机密】"
)

# 本机绝对路径（泄露用户名/目录结构；Windows 形态一并覆盖）
LOCAL_PATH_RE = re.compile(
    r"/Users/[A-Za-z0-9_.\-]+/|/home/[A-Za-z0-9_.\-]+/|[A-Za-z]:\\\\Users\\\\"
)


def build_rules(cfg):
    """返回 (restricted_re, restricted_exempt, sensitive_rules, prefixes, doc_exempt)。"""
    parts = [re.escape(p.strip("/")) for p in cfg["restricted_paths"] if p.strip("/")]
    restricted_re = re.compile(r"(?:^|/)(?:" + "|".join(parts) + r")(?:/|$)") if parts else None
    exempt = set(cfg["restricted_path_exempt"])

    sensitive_rules = []
    kw = [k for k in cfg["sensitive_keywords"] if k]
    if kw:
        try:
            sensitive_rules.append(("敏感内容关键词", re.compile("|".join(kw))))
        except re.error as e:
            print(f"[ERROR] config.json sensitive_keywords 正则非法：{e}")
            sys.exit(2)
    for p in cfg.get("extra_patterns", []):
        level = p.get("level", "sensitive")
        name = p.get("name", "附加规则")
        try:
            rx = re.compile(p["regex"])
        except (KeyError, re.error) as e:
            print(f"[ERROR] config.json extra_patterns[{name}] 非法：{e}")
            sys.exit(2)
        if level == "secret":
            SECRET_RULES.append((f"L3凭据·{name}", rx))
        else:
            sensitive_rules.append((f"敏感·{name}", rx))
    return restricted_re, exempt, sensitive_rules, list(cfg["sensitive_scan_prefixes"]), set(cfg["doc_exempt"])


# ---------------------------------------------------------------------------
# 工具
# ---------------------------------------------------------------------------

def git(root, *args):
    return subprocess.run(["git", *args], cwd=root,
                          capture_output=True, text=True, check=True).stdout


def mask(matched):
    return matched[:6] + "…(已脱敏，勿回显完整内容)"


class Report:
    def __init__(self):
        self.items = []  # (level, location, rule, detail)

    def add(self, level, location, rule, detail):
        self.items.append((level, location, rule, detail))

    def downgrade_sensitive(self):
        self.items = [("WARN" if "敏感" in rule else lvl, loc, rule, det)
                      for lvl, loc, rule, det in self.items]

    @property
    def blocked(self):
        return any(lvl == "BLOCK" for lvl, *_ in self.items)

    def dump(self, title):
        print(f"== {title} ==")
        if not self.items:
            print("  ✔ 未发现违规")
            return
        for lvl, loc, rule, detail in self.items:
            print(f"  [{lvl}] {loc}  {rule}  {detail}")
        n_block = sum(1 for lvl, *_ in self.items if lvl == "BLOCK")
        print(f"== 共 {n_block} 项 BLOCK / {len(self.items) - n_block} 项 WARN ==")


# ---------------------------------------------------------------------------
# 检查
# ---------------------------------------------------------------------------

def check_path(path, report, restricted_re, exempt):
    if restricted_re is None or path in exempt:
        return
    if restricted_re.search(path):
        report.add("BLOCK", path, "受限路径",
                   "属于受限目录（见 SECURITY.md），禁止入库或外发")


def check_text(path, text, report, mode, line_no, rules):
    restricted_re, exempt, sensitive_rules, prefixes, doc_exempt = rules
    loc = f"{path}:{line_no}" if line_no else path
    doc_exempt = path in doc_exempt

    # 1) 凭据——任何模式、任何文件都是 BLOCK
    for name, rx in SECRET_RULES:
        for m in rx.finditer(text):
            report.add("BLOCK", loc, name, mask(m.group(0)))

    # 2) 受限标记
    if not doc_exempt and RESTRICTED_MARKER_RE.search(text):
        report.add("BLOCK", loc, "受限标记",
                   "内容带 restricted/confidential 标记（L2），须移入受限目录且不得外发")

    # 3) 本机绝对路径
    m = LOCAL_PATH_RE.search(text)
    if m:
        report.add("BLOCK" if mode == "publish" else "WARN", loc, "本机路径泄露", mask(m.group(0)))

    # 4) 敏感关键词（跳过豁免文档；repo 模式下 prefixes 非空时只扫指定前缀；
    #    发布门对整篇外发文稿生效，不受 prefixes 限制——外发文件常在 prefixes 之外）
    in_scope = mode == "publish" or not prefixes or path.startswith(tuple(prefixes))
    if not doc_exempt and in_scope:
        for name, rx in sensitive_rules:
            m = rx.search(text)
            if m:
                report.add("BLOCK" if mode == "publish" else "WARN", loc, name,
                           f"命中「{m.group(0)}」——敏感内容属受限级，应放受限目录；"
                           f"外发须 --allow-sensitive 显式确认")

    # 5) 发布模式：正文引用受限目录也算违规
    if mode == "publish" and restricted_re is not None and restricted_re.search(text):
        report.add("BLOCK", loc, "引用受限路径", "文稿提及受限目录内容")


# ---------------------------------------------------------------------------
# 扫描模式
# ---------------------------------------------------------------------------

def scan_worktree(root, report, rules):
    files = sorted(set(git(root, "ls-files", "-zco", "--exclude-standard").split("\0")) - {""})
    for path in files:
        check_path(path, report, rules[0], rules[1])
        try:
            with open(os.path.join(root, path), encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError as e:
            report.add("WARN", path, "读取失败", str(e))
            continue
        check_text(path, text, report, "repo", None, rules)


def scan_staged(root, report, rules):
    staged = [f for f in git(root, "diff", "--cached", "--name-only", "-z").split("\0") if f]
    for path in staged:
        check_path(path, report, rules[0], rules[1])

    diff = git(root, "diff", "--cached", "--no-color", "-U0")
    path, line_no = None, 0
    for raw in diff.splitlines():
        if raw.startswith("+++ b/"):
            path, line_no = raw[6:], 0
            continue
        m = re.match(r"@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@", raw)
        if m:
            line_no = int(m.group(1))
            continue
        if raw.startswith("+") and path:
            check_text(path, raw[1:], report, "repo", line_no, rules)
            line_no += 1


def scan_publish(target, report, rules, allow_sensitive):
    try:
        with open(target, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except OSError as e:
        print(f"[ERROR] 无法读取 {target}: {e}")
        sys.exit(2)
    check_text(target, text, report, "publish", None, rules)
    if allow_sensitive:
        report.downgrade_sensitive()


# ---------------------------------------------------------------------------
# 入口
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="safety-tracks 数据安全扫描器（见 SECURITY.md）")
    ap.add_argument("--staged", action="store_true", help="只扫暂存区（pre-commit 用）")
    ap.add_argument("--publish", metavar="FILE", help="发布门：检查待外发的单个文稿")
    ap.add_argument("--allow-sensitive", action="store_true",
                    help="仅发布模式：确认要公开敏感观点时，将敏感关键词降为 WARN")
    args = ap.parse_args()

    try:
        root = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except subprocess.CalledProcessError:
        print("[ERROR] 不在 git 仓库内，无法扫描")
        sys.exit(2)

    try:
        rules = build_rules(load_config())
        report = Report()
        if args.publish:
            scan_publish(args.publish, report, rules, args.allow_sensitive)
            report.dump(f"发布门 · {args.publish}")
        elif args.staged:
            scan_staged(root, report, rules)
            report.dump("暂存区检查")
        else:
            scan_worktree(root, report, rules)
            report.dump("工作区巡检")
        if report.blocked:
            print("结果：🚫 拦截。处置方式见 SECURITY.md 事故处置一节。")
            sys.exit(1)
        print("结果：✔ 通过")
        sys.exit(0)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] git 调用失败：{e}")
        sys.exit(2)


if __name__ == "__main__":
    main()
