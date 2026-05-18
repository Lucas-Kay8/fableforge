# 🤝 贡献指南 (Contributing Guide)

感谢您关注并决定为 **FableForge / ai-video-studio** 技能包贡献力量！作为一个将管理学、心理学等硬核深刻概念，自动铸造成高质感视频的 OpenClaw 智能 Agent 技能，我们非常热烈地欢迎社区开发者与我们共建。

为了保持项目的高质量和严谨性，请在参与贡献前阅读以下指南：

---

## 🛠️ 本地开发环境设置

1. **克隆仓库并安装开发依赖**：
   ```bash
   git clone https://github.com/Lucas-Kay8/fableforge.git
   cd fableforge
   npm install
   ```

2. **本地进行 Lint 与语法预检**：
   我们在 package.json 中配置了极度严苛的机器自动化校验，用于检查 HTML 结构兼容性、CSS 渲染合理性以及 StaticGuard 门禁：
   ```bash
   # 执行一键检查
   npm run check
   ```
   **在提交任何 PR 前，确保此命令的返回结果为 0 报错 (Exit code 0)**。

---

## 📐 技能 SOP 修改规范

如果您发现了 FableForge 5 阶段制片流水线有可以被继续完善的地方，并决定修改 [.agents/skills/fableforge/SKILL.md](file:///.agents/skills/fableforge/SKILL.md) 技能文档：
1. **中英双语同步**：修改主中文技能的同时，必须确保在 `.agents/skills/fableforge/SKILL.en.md` 英文文档中同步更新英文描述。
2. **规范版本号**：如果 SOP 规范发生了破坏性改动（Breaking Change），请相应调整 YAML Frontmatter 头部里的 `version` 版本号。

---

## 📝 提交 Commit 消息规范

我们推荐使用行业通用的 **Angular Commit Message 规范**，这将让每一次技能迭代的历史记录都极为清爽。每次提交消息应遵循以下格式：

```
<type>: <description>
```

### 常用标签 (`type`)：
- `feat`: 引入了新的制片阶段、新排版风格 CSS 或新工具链适配
- `fix`: 修复了渲染被裁切、 unescaped 字符解析、音画偏差等 Bug
- `docs`: 修改了 README、SOP 文档或使用说明
- `style`: 仅仅是格式化、排版修改，不改变代码逻辑
- `refactor`: 重构核心 timeline 编排逻辑
- `chore`: 升级 ClawHub 版本、修改 `.gitignore` 等琐碎任务

---

## 📮 PR 提交流程

1. **Fork** 本仓库并从 `main` 分支切出您的 Feature 分支。
2. 在本地完成修改，并务必通过 `npm run check` 的自动化校验。
3. 提交 Commit 消息并推送回您的 Fork 仓。
4. 在本仓库提交一个 **Pull Request**，PR 模板中的自检 Checklist 会引导您进行最后一步确认。
5. 我们的核心维护团队会迅速为您进行 Review 并合并！

再一次感谢您让 AI 视频制片的工业化流水线变得更加卓越！🚀
