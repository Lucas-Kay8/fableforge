---
name: fableforge
description: FableForge 寓言铸造厂的核心 AI Agent SOP。专门用于制作高品质"寓言/管理洞察"类视频的 Skill。包含从概念生成、寓言创作、TTS 配音、到 HyperFrames 视频渲染的完整工业化 SOP，以及视觉风格指南与技术陷阱手册。
---

# 🔨 FableForge · 寓言铸造厂 AI Agent SOP

本 Skill 是一份**命令级可执行 SOP**，而非经验教训集。每个 Stage 均包含**具体执行命令**和**退出验收标准**，严禁跳步或在退出标准未满足时进入下一阶段。

---

## 0. 剧本规格标准（强制约束）

在开始任何生产之前，必须理解并遵守以下硬性规格。**所有偏离规格的剧本必须打回重写，不得进入生产阶段。**

| 规格项 | 标准值 | 说明 |
|--------|--------|------|
| 总时长 | 60 ～ 120 秒 | 短视频推荐 60s，深度洞察可延长至 120s |
| 分镜数量 | 1 + N + 1 幕 | 1张封面 + N张正文(8~12) + 1张结尾 |
| 每幕旁白字数 | 中文 30～60 字 / 英文 20～40 词 | 中文约 3.5 字/秒，英文约 2.5 词/秒 |
| 每幕预估时长 | 5 ～ 12 秒 | 最终以音频实测为准，此处仅为剧本阶段的草稿估算 |
| 分镜编号格式 | `scene_cover`, `scene1`~`scene{N}`, `scene_end` | 与 `assets/` 下的图片名严格一一对应 |
| 旁白与分镜对应 | 1 幕 == 1 张图 == 1 段旁白 | 封面通常对应标题旁白，结尾对应金句旁白 |

---

## 0.5 质量门禁（三重内容验收）

视频质量的上限由三个核心因素决定。**每一重门禁未通过，不得进入下一阶段。**

### 门禁一：故事验收（概念生成后、停机确认前执行）

AI 容易生成"结构正确但洞察平庸"的故事。在向用户展示寓言之前，必须完成以下自检：

**选题标准（加入生成提示词中）：**
> 选择的管理学概念必须同时满足：**听起来反直觉、说破后令人不适、在职场中普遍存在但极少被正视**。"努力就有回报"这类正能量概念不符合标准。

**强制自检（全部通过方可提交用户确认）：**
- [ ] **反常识测试**：这个洞察是"大家都知道"还是"大家都经历但从没被命名"的？前者没传播价值，重写。
- [ ] **悬念测试**：用户在第 10 秒能否猜到结局？能猜到 = 隐喻太直白，必须加反转，重写。
- [ ] **不适感测试**：结局是否让人感到轻微不舒服或醍醐灌顶？没有不适感就没有洞察深度，重写。
- [ ] **现实锚定测试**：故事结尾的解释，是否映射到了用户**今天就可能遭遇**的具体职场场景？

---

### 门禁二：脚本节奏验收（剧本转化后执行）

脚本是情绪的乐谱。全片节奏必须有弧线，禁止"一直是同一个情绪档位"的平铺。

**情绪档位定义：**

| 档位 | 名称 | 字数参考 | 用途 |
|------|------|---------|------|
| 1 | 舒缓叙事 | 40～60 字 | 开场建立世界观 |
| 2 | 紧张蓄力 | 30～50 字 | 冲突展开阶段 |
| 3 | 高潮爆发 | 20～40 字 | 关键转折点 |
| 4 | 沉默留白 | ≤ 15 字 | 结论落地的停顿幕 |

**强制节奏弧线（60 秒标准模板）：**
```
开场：1 → 1 → 2   （平稳建立，轻微升温）
发展：2 → 2 → 3   （冲突升级，节奏加快）
高潮：3 → 3 → 4   （最紧张，之后突然静止）
结论：4 → 1        （留白后，用最少的字落地）
```

**脚本写作铁律：**
- **写感受，不写动作**。旁白描述情绪状态，而不是画面动作：
  - ❌ `"十只狼排成一列，在山谷中等待狼王的命令。"`
  - ✅ `"山谷里没有声音。只有风，和等待者屏住的呼吸。"`
- **结论幕字数减半**：最后一幕旁白不超过 20 字。越重要的道理，越要用更少的字。
- **剧本格式补充档位字段**：每幕增加 `- **情绪档位**：{1/2/3/4}` 字段，作为图片提示词和语音语调的指导依据。

---

### 门禁三：图片质量验收（图片生成后、进入 Stage 2 前执行）

**构图与画幅规范（强制）：**
- **画幅固定**：必须生成 **9:16 竖屏**图片（DALL-E 3 使用 `1024x1792`）。严禁使用横屏图片。
- **主体位置**：主体人物/物件必须在画面**上方 1/3** 区域，底部留给字幕区。
- **提示词必加**：`cinematic vertical shot, 9:16 aspect ratio, subject positioned in upper third of frame, dark atmospheric space at bottom`
- **全片一致性**：主光源方向统一，保持跨幕视觉连贯。

**风格锁定工作流：**
```
1. scene1 正常生成 → 确认风格满意后，将其提示词核心词组存为「风格前缀」
2. scene2 ～ scene{N}：每个提示词开头追加风格前缀
   格式："[首图核心风格], [光影描述], same art style, —"
```

**角色一致性（有固定角色的剧本必须执行）：**
```
1. 先生成一张「角色圣经」参考图（正面全身，无背景）
2. 写明角色特征词组（毛色/体型/眼神/标志性特征）
3. 每张含该角色的图，提示词必须包含此特征词组
```

**逐张自检：**
- [ ] **封面图 (scene_cover)**：视觉冲击力极强，具备悬念感，能瞬间抓住注意力。
- [ ] **结尾图 (scene_end)**：意境深远，具备“神性”或“哲学感”，完美呼应主题并实现情感/认知升华。
- [ ] 主体在画面上 1/3，底部有足够深色安全区供字幕叠加
- [ ] 图片情绪与该幕的「情绪档位」匹配（档位 3 的图不能是平静场景）
- [ ] 全片光影/色调风格一致
- [ ] 无明显 AI 瑕疵（多余手指、文字乱码、比例失调等）

---

## Stage 1：概念、剧本与物料生成

### 1.1 概念生成（须停机等待用户确认）

使用以下提示词模板生成寓言故事：

> "请你从[指定领域]里，选择一个博士生水平的概念。然后写一个寓言故事，用间接的方式把这个概念讲清楚。不要一开始就说答案，尽量到故事快结束的时候，才让人意识到原来讲的是这个概念。故事结束后，再解释这个概念，以及故事里的隐喻分别对应什么。"

**去重检查**：生成前扫描工作空间内所有 `YYYYMMDD/视频脚本.md`，确保主题不与历史作品重复。

⛔ **此步完成后必须停机，将寓言故事完整展示给用户，等待明确确认。未经确认严禁继续。**

### 1.2 剧本转化（用户确认后执行）

将故事按规格标准拆解为分镜剧本，写入 `YYYYMMDD/视频脚本.md`。

剧本格式模板：
```markdown
## 分镜 scene_cover — 封面/标题幕
- **情绪档位**：1
- **旁白**：{通常为视频标题或引导句}
- **画面描述**：{高吸引力、悬念感强的提示词}

## 分镜 {N} — {幕名}
- **时间（草稿估算）**：第 {X} ～ {Y} 秒
- **情绪档位**：{1/2/3/4}
- **旁白**：{中文30~60字 / 英文20~40词}
- **画面描述**：{图片提示词，中英文均可}

## 分镜 scene_end — 结尾/升华幕
- **情绪档位**：4
- **旁白**：{点题金句，不超过 20 字}
- **画面描述**：{意境深远、呼应主题的提示词}
```

### 1.3 TTS 语音生成

**声纹选择（优先意识）：**
- **默认原则**：优先检查 `/语音模型/voxenv` 环境。若存在，**必须**使用用户的声纹克隆生成旁白。
- **降级方案**：仅在用户明确要求或克隆环境不可用时，才使用 Kokoro 等通用模型。

**语音节奏优化：**

VoxCPM2 的情绪输出相对平稳，需要在文本层面手动注入戏剧感。处理规则：

- 在核心关键词前插入 `……`，让模型自动降速放重音
- 超过 130 字的段落用 `|||` 在语气转折处手动分段
- 档位 4（沉默留白幕）的旁白每个词组之间都加 `……`

```
❌ 平铺直叙：
"你以为选出了战将，其实你只选出了最擅长残杀队友的屠夫。"

✅ 有停顿感的版本：
"你以为……选出了战将。|||其实，你只筛选出了——最擅长残杀队友的……屠夫。"
```

在项目目录下执行：

```bash
# 使用本地 VoxCPM2 模型生成语音（必须使用虚拟环境的 Python）
# 1. 复制并编辑生成脚本（每个项目独立一份）
cp /Users/lucas/Work/09.Antigravity/语音模型/generate_cantillon.py \
   /Users/lucas/Work/09.Antigravity/语音模型/generate_{project_name}.py
# 2. 编辑 TARGET_TEXT、OUTPUT_FILE 等变量
# 3. 运行
/Users/lucas/Work/09.Antigravity/语音模型/voxenv/bin/python3 \
  /Users/lucas/Work/09.Antigravity/语音模型/generate_{project_name}.py
```

### 1.4 图片素材生成

按剧本中每幕的"画面描述"逐一生成图片，命名严格遵循 `scene1.png`、`scene2.png` ... `scene{N}.png`，保存至 `YYYYMMDD/assets/`。

**✅ Stage 1 退出标准（全部满足方可进入 Stage 2）：**
```bash
# 执行以下核查命令，输出应全部为绿色 OK
ls YYYYMMDD/assets/ | grep -E "^scene_(cover|end)\.png$|^scene[0-9]+\.png$" | wc -l  # 输出数量应 == 剧本总分镜数
ls YYYYMMDD/assets/narration.wav  # 文件必须存在
```
- [ ] `assets/` 下图片数量 == 剧本分镜数（含 cover 和 end）
- [ ] `assets/narration.wav` 已生成
- [ ] 图片命名符合规范（scene_cover, scene1~N, scene_end）

### 1.5 BGM 背景音乐匹配

BGM 是情绪的推手，必须在 Stage 2 之前完成匹配。

**BGM 匹配工作流：**
1. **情绪识别**：分析剧本中各幕的「情绪档位」，提取核心关键词（如：Suspense, Epic, Minimalist, Melancholic）。
2. **曲库搜索**：从免版税音乐库（如 Scott Buckley, Pixabay, Bensound）搜索并下载 1 首全局背景音。
3. **参数配置**：
   - `data-track-index`: 设为 `-1`（始终位于底层）。
   - `data-volume`: 默认设为 `0.15` ～ `0.25`（通过 preview 实时调整，严禁盖过旁白）。
4. **集成到 index.html**：
   ```html
   <audio id="bgm" src="assets/bgm.mp3" data-start="0" data-duration="{视频总长}" data-track-index="-1" data-volume="0.25"></audio>
   ```

**✅ Stage 1.5 退出标准：**
- [ ] `assets/bgm.mp3` 已就位。
- [ ] `视频脚本.md` 已补充 BGM 署名信息（含作者、链接及 CC 协议）。

---

## Stage 2：音频解析与数据驱动时间轴

### 2.1 获取音频精确时长

```bash
export PATH=./bin:$PATH
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 YYYYMMDD/assets/narration.wav
# 记录输出的 duration=XX.XXXXXX，这是视频总时长的唯一权威数据
```

### 2.2 获取精确断句时间戳（二选一）

**方案 A — Whisper 转录（推荐，精度最高）：**
```bash
npx hyperframes transcribe YYYYMMDD/assets/narration.wav
# 生成 YYYYMMDD/assets/transcript.json，包含词级时间戳
```

**方案 B — 静音检测分割（音频停顿明显时使用）：**
```bash
export PATH=./bin:$PATH
ffmpeg -i YYYYMMDD/assets/narration.wav -af silencedetect=noise=-30dB:duration=0.3 -f null - 2>&1 | grep silence
# 记录每个 silence_end 时间点作为场景切换点
```

### 2.3 将时间戳映射到分镜

根据 2.2 的输出，将每幕的 `data-start` 和 `data-duration` 精确填入剧本或直接生成为 JS 数组：

```js
// 由音频数据派生，禁止手动估算
const scenes = [
  { id: "scene1", start: 0,    duration: 5.8,  subtitle: "旁白文本..." },
  { id: "scene2", start: 5.8,  duration: 6.2,  subtitle: "旁白文本..." },
  // ...
];
```

**✅ Stage 2 退出标准：**
- [ ] `transcript.json` 已生成 或 `silencedetect` 输出已记录
- [ ] 所有分镜的 `start + duration` 之和与音频总时长误差 < 0.2 秒
- [ ] `data-start` 全部来自实测数据，无任何估算值

---

## Stage 3：静态排版构建与验收

### 3.1 创建项目目录

```bash
mkdir -p YYYYMMDD/assets
# 初始化 index.html（手动创建，参考下方 HTML 模板）
```

### 3.2 HTML 基础模板（强制规范）

> ℹ️ 完整参考实现见 `template/index.html` 和 `template/style.css`。以下仅列出关键约束。

**根容器必须包含 4 个 data-* 属性（缺一不可）：**
```html
<div id="composition"
     data-composition-id="composition"
     data-width="1920"
     data-height="1080"
     data-duration="{Stage 2.1 获取的音频总时长}">
```

**场景 DOM 结构（由 JS 动态生成，严禁硬编码）：**
```
scene.clip
  ├─ img.bg-fill    ← 背景模糊层（object-fit: cover + blur）
  ├─ img.fg-main    ← 主体图片层
  └─ div.overlay
       └─ div.subtitle  ← 字幕（通过 textContent 写入）
```

**GSAP 铁律：**
```js
const tl = gsap.timeline({ paused: true }); // 永远 paused: true
window.__timelines = window.__timelines || {};
window.__timelines["composition"] = tl; // key 必须与 data-composition-id 一致
```

**图片引用规范：**
- 使用 `assets/${id}.png`（如 `assets/scene1.png`），与 scene 数据的 id 字段一致

### 3.3 CSS 布局规范（强制）

> ℹ️ 完整实现见 `template/style.css`。以下仅列出核心规则。

**`object-fit` 决策树（根据图片画幅选择）：**

| 图片画幅 | fg-main | bg-fill | 效果 |
|---------|---------|---------|------|
| 16:9 横版（推荐） | `object-fit: cover` | 不需要 | 完美填充，无黑边 |
| 非标画幅（正方形等） | `object-fit: contain` | 需要（blur + cover） | 毛玻璃背景填充黑边 |

```css
/* 背景模糊层（非 16:9 素材时使用） */
.bg-fill {
  position: absolute; inset: 0;
  object-fit: cover;
  filter: blur(20px) brightness(0.4);
  transform: scale(1.1); /* 补偿 blur 边缘虚化 */
}

/* 主体图片层：严禁使用 translate 居中 */
.fg-main {
  position: absolute; inset: 0;
  object-fit: contain; /* 或 cover，见上方决策树 */
  transform-origin: center center;
}
```

### 3.4 静态验收（加入动画前的检查）

用浏览器打开 `index.html`，截图确认：
- [ ] 每张图片完整显示，无裁切，无偏移
- [ ] 图片在 1920×1080 的黑色背景内居中

**✅ Stage 3 退出标准：**
- [ ] 纯静态（无 GSAP 动画）下所有图片 100% 完整显示
- [ ] `data-composition-id`、`data-width`、`data-height` 已正确设置
- [ ] 字幕通过 `textContent` 注入，不存在硬编码的 HTML 字符串

---

## Stage 4：动画集成与预检发版

### 4.1 加入 GSAP 动画

在静态验收通过后，才可加入动效。可用动画菜单：

| 动效 | 代码模板 | 适用场景 |
|------|---------|--------|
| Ken Burns 缩放 | `fromTo(img, {scale:1.0}, {scale:1.06, ease:"none"})` | 所有场景默认 |
| Ken Burns 平移 | `fromTo(img, {x:-20}, {x:0, ease:"none"})` | 宽场景横向扫描 |
| 字幕淡入 | `from(sub, {opacity:0, y:20, duration:0.8, ease:"power2.out"})` | 所有场景可选 |
| 场景交叉淡化 | `to(div, {opacity:0, duration:0.5}, start+duration-0.25)` | 场景过渡 |
| 光晕脉冲 | `to(glow, {opacity:0.4, repeat:-1, yoyo:true, duration:2})` | 火焰/光源场景 |

### 4.2 强制预检（渲染前的最后防线）

```bash
export PATH=./bin:$PATH
npx hyperframes@latest inspect YYYYMMDD/
```

**✅ Stage 4 退出标准（必须全部满足，才允许执行 render）：**
- [ ] `inspect` 命令退出码为 0（无报错）
- [ ] 控制台输出的 `totalDuration` 与 Stage 2.1 测量的音频时长误差 < 0.2 秒
- [ ] 无任何 `StaticGuard` 警告

### 4.3 渲染导出

```bash
export PATH=./bin:$PATH
# 强制使用 promo_video.mp4 以便自动同步到 GitHub (受 .gitignore 豁免)
npx hyperframes@latest render YYYYMMDD/ -o YYYYMMDD/promo_video.mp4 --force-new
```

---

## Stage 5：发布与归档

### 5.1 视频脚本元数据补充

在 `视频脚本.md` 中补充以下字段：

```markdown
## 技术参数
- **声纹**：VoxCPM2 用户克隆 / Kokoro am_adam
- **实测时长**：{ffprobe 实测值}s
- **BGM**：{BGM 名称} by {BGM 作者} (CC BY 4.0)
- **YouTube**：{URL}
```

### 5.2 README 更新

在 `README.md` 的「演示作品」表格中追加新作品条目（中英文双语部分均需更新）。

### 5.3 Git 同步

```bash
git add YYYYMMDD/ README.md
git commit -m "feat: Add {video_title} project"
git push origin main
```

**✅ Stage 5 退出标准：**
- [ ] `视频脚本.md` 包含完整元数据（声纹、时长、BGM、YouTube 链接）
- [ ] `README.md` 中英双语演示作品表格已更新
- [ ] `git push` 成功

---

## 附录 A：视觉风格指南

### 风格决策原则

- **动态适配**：视觉风格必须完全服务于故事。可选国风写意、现代极简、蒸汽朋克、赛博朋克或电影感实拍风格。
- **自洽性**：全片所有图片的色调、光影和元素必须统一，严禁跨时空混搭（除非剧情要求）。

### 图片提示词工程

- **基调优先**：先定画风（`Cinematic realistic style` / `Oriental brush painting` / `Minimalist vector art`）。
- **质量后缀**：每个提示词末尾统一加 `hyper-realistic details, cinematic lighting, masterpiece, 8K`。
- **中文文字生成**（架构图/概念图专用）：`A [style] visualization with Chinese labels. Main node: "核心词". Sub-nodes: "关联词1", "关联词2". Professional design, glowing connections.`

---

## 附录 B：已知技术陷阱速查

| 现象 | 根因 | 修复 |
|------|------|------|
| 图片裁切/偏移 | GSAP 矩阵覆盖了 `translate` 居中 | 改用 `object-fit: contain`，绝不用 `translate` |
| 正方形图片顶部被裁 | `object-fit: cover` 裁切了主体 | 强制 16:9 生图，或改用 `contain` + 毛玻璃背景 |
| 视频提前截断/少幕 | 字幕中含未转义的 `<` `>` 破坏 DOM | 改用 `textContent` 注入 |
| `inspect` 报 `totalDuration undefined` | 根容器缺少 `data-duration` | 补上 `data-duration="{音频总长}"` |
| `inspect` 报错 / MP4 时长随机 | 违反渲染合约 | 时间轴永远 `paused: true`，不写 `play()` |
| 画面色偏 | img 标签含 `filter: hue-rotate(...)` | 删除该 filter |
| `FFmpeg not found` | 环境未配置 | `export PATH=./bin:$PATH` |

---

## 附录 C：环境配置（一次性）

```bash
# 下载 FFmpeg 静态二进制（Mac）
curl -L https://evermeet.cx/ffmpeg/get/zip -o ffmpeg.zip && unzip ffmpeg.zip
curl -L https://evermeet.cx/ffmpeg/get/ffprobe/zip -o ffprobe.zip && unzip ffprobe.zip
mkdir -p bin && mv ffmpeg bin/ && mv ffprobe bin/ && chmod +x bin/*

# 语音生成路径
# /Users/lucas/Work/09.Antigravity/语音模型
```

---

## 附录 D：项目归档结构

```text
/YYYYMMDD/
  ├── index.html          (核心时间轴，Stage 3/4 产物)
  ├── assets/
  │   ├── scene_cover.png (封面图，高吸引力)
  │   ├── scene1.png      (场景图)
  │   ├── scene{N}.png
  │   ├── scene_end.png   (结尾图，点题升华)
  │   ├── narration.wav   (TTS 配音，Stage 1.3 产物)
  │   ├── bgm.mp3         (背景音乐，Stage 1.5 产物)
  │   └── transcript.json (Whisper 时间戳，Stage 2.2 产物)
  ├── 视频脚本.md          (剧本，Stage 1.2 产物)
  └── promo_video.mp4     (最终成品，Stage 4.3 产物，Git 豁免名单)
```
