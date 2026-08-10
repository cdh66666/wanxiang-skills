# 万象技能库

一个可迁移、可复用、持续进化的 Codex Skills 开源仓库。

这里收纳经过真实项目验证的工作流。每个 Skill 都是独立目录，包含触发说明、执行步骤、质量标准，以及确有必要的脚本和参考资料。换电脑后只需克隆本仓库，即可重新安装。

## 已收录

### 证据图册式调查

目录：[`skills/evidence-atlas-research`](skills/evidence-atlas-research)

适合调查产品结构、机械原理、专利方案、论文技术和竞品拆解。它要求优先使用真实专利图、论文图、官方资料与拆解照片，用少量中文说明串起动作关系，并明确区分“已确认”“专利实施例”“二手报道”和“推断”。

## 安装

### 克隆整个技能库

```powershell
git clone https://github.com/cdh66666/wanxiang-skills.git "$env:USERPROFILE\.codex\skills\万象技能库"
```

### 只安装一个 Skill

```powershell
Copy-Item -Recurse .\skills\evidence-atlas-research "$env:USERPROFILE\.codex\skills\evidence-atlas-research"
```

重新启动 Codex 或新建任务后，使用 `$evidence-atlas-research` 调用。

## 更新

```powershell
git pull
```

新增 Skill 时遵循相同结构：

```text
skills/
└── skill-name/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/      # 可选
    └── scripts/         # 可选
```

提交前请确保：说明能准确触发、原始资料可追溯、脚本不含密钥或本机绝对路径，并完成一次真实任务测试。

## 开源协议

本仓库代码与原创文字采用 [MIT License](LICENSE)。第三方专利图、论文图、照片和商标仍归其各自权利人所有；引用时应保留出处并遵守对应许可与合理使用边界。
