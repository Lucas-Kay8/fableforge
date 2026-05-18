---
name: fableforge
description: FableForge 寓言铸造厂的核心 AI Agent SOP。支持两种生产模式：模式 A（纯图片寓言视频）和模式 B（视频 B-roll + 文字叠加）。包含从概念生成、剧本创作、TTS 配音、素材采集、到 HyperFrames 视频渲染的完整工业化 SOP，以及视觉风格指南与技术陷阱手册。
---

# 🔨 FableForge · 寓言铸造厂 AI Agent SOP

本 Skill 是一份**命令级可执行 SOP**，而非经验教训集。每个 Stage 均包含**具体执行命令**和**退出验收标准**，严禁跳步或在退出标准未满足时进入下一阶段。

---

## 0. 剧本规格标准（内容优先定档制）

**核心原则：故事的可理解性永远优先于时长限制。**

视频时长不是预设的固定值，而是由故事内容倒推得出的。错误的做法是「先定 60 秒，然后把故事往里塞」；正确的做法是「先确认故事讲完需要多少字，再据此选档」。

### 0.1 三档体系

| 档位 | 适用场景 | 旁白总字数 | 预估时长 | 分镜数 |
|------|---------|-----------|---------|-------|
| S · 短片 | 单一概念解释、管理金句 | 200～450 字 | 60～120 秒 | 1+8~12+1 |
| M · 标准 | 完整寓言（2-3 个角色弧线） | 450～900 字 | 120～270 秒 | 1+12~20+1 |
| L · 长篇 | 多段式寓言 / 连续案例 | 900～1500 字 | 270～420 秒 | 1+20~30+1 |

> 超过 1500 字的故事必须拆成上下集（每集独立成片，各自包含封面和结尾）。

### 0.2 定档公式

```
旁白总字数 = 原始故事中【不可删减要素】的合计字数（见 0.3）
预估时长(秒) = 旁白总字数 ÷ 3.5（中文语速）
根据预估时长选择对应档位
```

### 0.3 不可删减要素（叙事完整性红线）

以下要素如果被删除，观众将无法独立理解视频内容。**剧本转化阶段（Stage 1.2）严禁删除这些要素：**

| 要素类型 | 说明 | 删除后果 |
|---------|------|----------|
| 因果链 | A 导致 B 导致 C 的逻辑关系 | 观众不知道「为什么」 |
| 角色动机 | 角色为什么要做这件事 | 角色变成功能符号 |
| 关键对话 | 推动情节转折的台词 | 悬念和冲突消失 |
| 转折触发 | 让角色/观众认知翻转的事件 | 「啊哈时刻」丧失 |
| 结局因果 | 结论与前文的逻辑闭环 | 观众觉得结论是硬塞的 |

**可以精简的要素：**
- 重复的环境描写（保留首次，后续可省略）
- 纯装饰性的形容词堆叠
- 不影响主线的次要角色互动
- 已被画面传达的信息（如「山很高」——画面已经表达了）

### 0.4 通用规格（所有档位共享）

| 规格项 | 标准值 | 说明 |
|--------|--------|------|
| 每幕旁白字数 | 中文 30～80 字 / 英文 20～50 词 | 中文约 3.5 字/秒，英文约 2.5 词/秒 |
| 每幕预估时长 | 5 ～ 15 秒 | 最终以音频实测为准 |
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

**风格圣经工作流（强制）：**

图片风格不一致的根因是：每个提示词都是独立的，AI 模型对「古代寺庙」的理解每次都不一样。解决方案是在生成任何图片之前，先编写一份**风格圣经**，作为所有提示词的**刚性前缀**。

**步骤 1 — 编写风格圣经（写入 `视频脚本.md` 的「视觉风格」章节）：**

必须定义以下 5 个维度，缺一不可：

```markdown
## 视觉风格（风格圣经）

### 文化锚点
- **时代与地域**：{如「唐代中国」「维多利亚英国」「赛博朋克东京」}
- **建筑特征**：{如「斗拱、青瓦、木构梁柱」}
- **服饰特征**：{如「圆领袍、交领汉服、明光铠甲」}
- **道具/器物**：{如「青铜油灯、竹简、毛笔」}

### 色调与光影
- **主色调**：{如「墨色底蕴 + 暖金灯火」}
- **光源方向**：{如「左侧 45° 暖光」}
- **质感**：{如「微水墨纹理、宣纸颗粒感」}

### 排除清单（负面提示）
- {如「严禁出现日式元素：鸟居、和服、榻榻米、障子门」}
- {如「严禁出现欧式元素：哥特尖拱、西式铠甲、石砌城堡」}
```

**步骤 2 — 组装提示词公式：**

所有图片的提示词必须严格遵循以下模板：

```
[画幅指令], [文化锚点], [本幕画面描述], [色调光影], [质量后缀]. [排除清单].
```

示例：
```
Cinematic vertical shot, 9:16 aspect ratio. Ancient Chinese Tang Dynasty style.
A young monk in grey round-collar robes holds a bronze oil lamp in a temple courtyard
with Dougong bracket architecture and grey tile roofing.
Ink-wash atmosphere, warm golden lamplight against dark shadows, subtle rice-paper texture.
hyper-realistic details, cinematic lighting, 8K.
No Japanese elements, no Western elements, no modern objects.
```

**步骤 3 — 角色锚定卡（有固定角色的剧本必须执行）：**

角色面部一致性是 AI 图片生成的最大短板。仅靠文字描述无法保证同一角色在多张图中长得一样。必须建立**角色锚定卡**。

```
1. 为每个角色定义「角色特征词组」（5~10 个关键词）
   示例：「年轻僧人，圆脸，剃度，灰色圆领直裰，草鞋，瘦弱身材」
2. 将角色特征词组写入风格圣经
3. 每张含该角色的图，提示词必须原样包含此特征词组
4. 【进阶】首次生成主角图后，保存该图作为「参考锚图」
   后续含同一角色的场景，使用 image-to-image 或
   将锚图作为参考图传入 generate_image 的 ImagePaths 参数，
   提示词追加："same character as reference, maintain facial features"
```

> ⚠️ 角色锚图的效果取决于生图模型的 image-to-image 能力。
> 当前 DALL-E 3 不支持参考图输入，此步骤暂为「提示词锚定」模式。
> 未来切换到支持参考图的模型（如 Flux、SD3）后，可启用完整锚图工作流。

**逐张自检：**
- [ ] **封面图 (scene_cover)**：视觉冲击力极强，具备悬念感，能瞬间抓住注意力。
- [ ] **结尾图 (scene_end)**：意境深远，具备“神性”或“哲学感”，完美呼应主题并实现情感/认知升华。
- [ ] 主体在画面上 1/3，底部有足够深色安全区供字幕叠加
- [ ] 图片情绪与该幕的「情绪档位」匹配（档位 3 的图不能是平静场景）
- [ ] 全片光影/色调风格一致
- [ ] 无明显 AI 瑕疵（多余手指、文字乱码、比例失调等）

---

## 0.6 生产模式决策（内容定型后执行）

FableForge 支持两种生产模式。**在用户确认内容方向后、动手写剧本之前**，必须先确定生产模式。

### 两种模式概览

| 维度 | 模式 A：纯图片 | 模式 B：视频 + 文字叠加 |
|------|-------------|----------------------|
| **适用题材** | 寓言故事、有角色弧线的隐喻 | 职场分析、管理洞察、观点输出 |
| **画幅** | 16:9 横屏（1920×1080） | 9:16 竖屏（1080×1920） |
| **视觉素材** | AI 生成的场景图片 | Pexels/Pixabay 免费 B-roll 视频 |
| **文字呈现** | 底部字幕条 | 全屏文字叠加排版（暗化遮罩 + 大字） |
| **叙事结构** | 角色驱动的故事弧线 | 论点驱动的拆解/金句输出 |
| **产出节奏** | 较慢（等图片生成 + 风格校准） | 较快（视频下载 + FFmpeg 裁剪） |

### 快速决策表

| 判断条件 | 选择 |
|---------|------|
| 有具体角色名字和对话（僧人、狼王、船夫……） | 模式 A |
| 叙事主语是「我」「你」「我们」「很多公司」 | 模式 B |
| 需要展示隐喻（灯 → 认知、桥 → 管理） | 模式 A |
| 需要展示数据对比（3 → 13）、金句输出 | 模式 B |
| 用户明确说"拍成视频" / "竖版" / "短视频" | 模式 B |
| 用户明确说"写个寓言" / "讲个故事" | 模式 A |

> ⚠️ 用户可在停机确认时手动覆盖 AI 的模式推荐。模式确定后写入 `视频脚本.md` 头部的「内容定档」章节。

### 模式选定后的流程分叉

- **模式 A**：走 §1.5A（图片素材生成）→ §3.2（横屏 HTML 模板）→ 正常流程
- **模式 B**：走 §1.5B（视频 B-roll 采集）→ §3.2B（竖屏 HTML + 文字叠加模板）→ 正常流程
- 其余阶段（概念、剧本、TTS、BGM、音频解析、动画、渲染、发布）两种模式共享。

---

## Stage 1：概念、剧本与物料生成

### 1.1 概念生成（须停机等待用户确认）

使用以下提示词模板生成寓言故事：

> "请你从[指定领域]里，选择一个博士生水平的概念。然后写一个寓言故事，用间接的方式把这个概念讲清楚。不要一开始就说答案，尽量到故事快结束的时候，才让人意识到原来讲的是这个概念。故事结束后，再解释这个概念，以及故事里的隐喻分别对应什么。"

**去重检查**：生成前扫描工作空间内所有 `YYYYMMDD/视频脚本.md`，确保主题不与历史作品重复。

⛔ **此步完成后必须停机，将寓言故事完整展示给用户，等待明确确认。未经确认严禁继续。**

### 1.2 内容定档（用户确认故事后立即执行）

在动手写剧本之前，必须先完成内容定档。这是防止「好故事变烂视频」的关键步骤。

**步骤：**

1. **标记不可删减要素**：逐段扫描用户确认的故事原文，用以下标签标记：
   - `[因果]` — 因果链节点
   - `[动机]` — 角色动机
   - `[对话]` — 推动剧情的关键台词
   - `[转折]` — 认知翻转事件
   - `[闭环]` — 结局因果

2. **计算最低旁白字数**：将所有标记要素的文本合计，得出「不可压缩下限」。

3. **选档**：根据合计字数，在 §0.1 三档体系中选择对应档位。

4. **输出定档报告**（写入 `视频脚本.md` 头部）：
   ```markdown
   ## 内容定档
   - **原始故事字数**：{X} 字
   - **不可删减要素字数**：{Y} 字
   - **选定档位**：{S/M/L}
   - **预估旁白总字数**：{Z} 字
   - **预估视频时长**：{Z ÷ 3.5} 秒
   ```

⛔ **如果不可删减要素字数 > 450（S 档上限），严禁使用 S 档强行压缩。必须升档。**

### 1.3 剧本转化

将故事按选定档位的规格拆解为分镜剧本，写入 `YYYYMMDD/视频脚本.md`。

**叙事完整性自检（剧本写完后必须执行，全部通过才能进入下一步）：**

- [ ] **盲测**：让一个没读过原文的人只看剧本旁白，能否独立理解故事的起因、经过、结局？如果不能，说明删多了。
- [ ] **因果链完整**：每个「结论」都有对应的「事件」作为铺垫，没有凭空冒出的道理。
- [ ] **角色有行为**：每个角色至少有一个具体动作或一句对话，不能只靠旁白概括（如 ❌「富商来了」→ ✅「富商拍出明珠说：亮才有用」）。
- [ ] **转折有过程**：角色的态度转变必须有触发事件，不能直接跳到结论（如 ❌「富商沉默了」→ ✅「明珠照得白茫茫一片，富商走了三步就被石头绊倒——他沉默了」）。

剧本格式模板：
```markdown
## 分镜 scene_cover — 封面/标题幕
- **情绪档位**：1
- **旁白**：{通常为视频标题或引导句}
- **画面描述**：{高吸引力、悬念感强的提示词}

## 分镜 {N} — {幕名}
- **时间（草稿估算）**：第 {X} ～ {Y} 秒
- **情绪档位**：{1/2/3/4}
- **旁白**：{中文30~80字}
- **画面描述**：{图片提示词，中英文均可}

## 分镜 scene_end — 结尾/升华幕
- **情绪档位**：4
- **旁白**：{点题金句，不超过 20 字}
- **画面描述**：{意境深远、呼应主题的提示词}
```

### 1.4 TTS 语音生成

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

### 1.5A 图片素材生成（模式 A）

> ℹ️ 仅模式 A（纯图片）执行此步。模式 B 跳转至 §1.5B。

按剧本中每幕的"画面描述"逐一生成图片，命名严格遵循 `scene1.png`、`scene2.png` ... `scene{N}.png`，保存至 `YYYYMMDD/assets/`。

**批量生成策略（应对 API 配额限流）：**

图片生成 API 通常有速率限制（如每窗口期 5 张）。为避免流程阻塞，采用以下策略：

1. **先批量准备提示词**：在生成前，将全部场景的提示词按风格圣经公式组装完毕，写入剧本。
2. **分批生成 + 穿插其他工作**：每批生成到限流后，立即切换到其他 Stage 的工作（如音频分析、HTML 搭建），不要干等。
3. **生成即归档**：每张图生成后立即 `cp` 到 `assets/` 目录并验证文件名，避免最后批量操作时遗漏。
4. **断点续传**：用 `ls assets/scene*.png | wc -l` 检查进度，只生成缺失的图片。

### 1.5B 视频 B-roll 素材采集与裁剪（模式 B）

> ℹ️ 仅模式 B（视频 + 文字叠加）执行此步。模式 A 跳转至 §1.5A。

**步骤 1 — B-roll 关键词策划：**

根据每幕的情绪和主题，在 `视频脚本.md` 中列出搜索关键词：
```markdown
## B-roll 素材规划
| 幕 | 情绪 | 搜索关键词 | 画幅偏好 |
|----|------|-----------|---------|
| scene1 | 压迫/悬疑 | dark office, laptop screen | 竖屏优先 |
| scene2 | 忙碌/混乱 | meeting room, people talking | 竖屏优先 |
| scene7 | 升华/开阔 | city night, aerial view | 横屏可接受 |
```

**步骤 2 — 素材探测（浏览器手动或自动）：**

在 Pexels (https://pexels.com/search/videos/) 搜索关键词，获取视频直链。优先选择：
- 竖屏 9:16（`_1080_1920_` 或 `_1440_2560_`）
- 时长 ≥ 10 秒（裁剪后留 ≤ 20 秒）
- 无水印、免版税

**步骤 3 — 编写自动化下载脚本 `download_and_process.py`：**

脚本必须包含以下能力（参考实现见 `20260518_org_slowdown/download_and_process.py`）：

```python
VIDEO_MAP = {
    "scene1.mp4": {"url": "https://videos.pexels.com/...", "is_vertical": True},
    "scene2.mp4": {"url": "https://videos.pexels.com/...", "is_vertical": False},
    # ...
}
```

**下载容错规范：**
- `curl -L -k --retry 5 --retry-delay 3 -H "User-Agent: Mozilla/5.0 ..."` — Pexels CDN 需要浏览器 UA，且 SSL 连接不稳定
- 若 curl 返回非零但文件通过 `ffprobe` 校验 → 视为下载成功（Cloudflare 常在传输末尾断开连接）
- 已存在的有效视频自动跳过（断点续传）

**FFmpeg 竖屏裁剪规范：**

| 原片画幅 | FFmpeg filter | 说明 |
|---------|--------------|------|
| 9:16 竖屏 | `scale=1080:1920` | 直接缩放 |
| 16:9 横屏 | `crop=ih*9/16:ih,scale=1080:1920` | 居中裁剪后缩放 |

所有视频统一参数：`-t 20 -c:v libx264 -crf 18 -an -y`（限时长 20s，去音轨）

**步骤 4 — 运行脚本：**
```bash
export PATH=./bin:$PATH
python3 download_and_process.py
```

**✅ Stage 1（素材）退出标准：**

模式 A：
```bash
ls YYYYMMDD/assets/ | grep -E "^scene_(cover|end)\.png$|^scene[0-9]+\.png$" | wc -l  # == 剧本分镜数
```
- [ ] `assets/` 下图片数量 == 剧本分镜数（含 cover 和 end）
- [ ] 图片命名符合规范（scene_cover, scene1~N, scene_end）

模式 B：
- [ ] `assets/` 下每幕对应的 `.mp4` 文件已就位且通过 `ffprobe` 校验
- [ ] 所有视频为 1080×1920 竖屏、无音轨、时长 ≤ 20s

通用：
- [ ] `assets/narration.wav` 已生成

### 1.6 BGM 背景音乐匹配

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

**✅ Stage 1.6 退出标准：**
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

### 2.2 获取精确断句时间戳（三级方案，按精度递减选择）

**方案 A — Whisper 词级转录（精度最高，优先推荐）：**
```bash
npx hyperframes transcribe YYYYMMDD/assets/narration.wav
# 生成 YYYYMMDD/assets/transcript.json，包含词级时间戳
# 直接按句末时间戳切分场景，误差 < 0.1s
```

**方案 B — RMS 能量分析 + 字数比例交叉验证（Whisper 不可用时）：**
```bash
export PATH=./bin:$PATH
# 1. 提取 RMS 能量流
ffmpeg -v error -i YYYYMMDD/assets/narration.wav \
  -af astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=rms.txt \
  -f null -

# 2. 用 Python 脚本分析静默段（>= 0.85s 的低能量区间为段间分界）
# 3. 将 RMS 检测到的分界与「字数比例推算」交叉验证：
#    - 按各段旁白字数比例分配总时长，得出各段预估 start
#    - 在预估 start ± 8s 范围内找最近的 RMS 静默段
#    - 取静默段结束时间作为实际 scene start
```

> ⚠️ TTS 工具（如 VoxCPM2）的段间静默长度不稳定，句内停顿可能被误判为段间分界。
> 交叉验证可有效过滤误判，但仍不如 Whisper 精确。

**方案 C — 纯字数比例分配（兜底方案）：**
```python
# 当 RMS 分析不可靠时（如 TTS crossfade 过重），直接按字数分配
# 误差 ±2s，对 10s+ 的场景可接受
for scene in scenes:
    scene.duration = scene.char_count / total_chars * total_audio_duration
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
- [ ] Whisper `transcript.json` 已生成，或 RMS 分析 + 字数交叉验证已完成，或纯字数比例已计算
- [ ] 所有分镜的 `start + duration` 之和与音频总时长误差 < 0.5 秒
- [ ] 标注所使用的方案等级（A/B/C），方便后续迭代时升级

---

## Stage 3：静态排版构建与验收

### 3.1 创建项目目录

```bash
mkdir -p YYYYMMDD/assets
# 初始化 index.html（手动创建，参考下方 HTML 模板）
```

### 3.2 HTML 基础模板 — 模式 A（强制规范）

> ℹ️ 以下为模式 A（纯图片）的 HTML/CSS 规范。模式 B 请跳转至 §3.2B。
> 完整参考实现见 `template/index.html` 和 `template/style.css`。以下仅列出关键约束。

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

### 3.3 CSS 布局规范 — 模式 A（强制）

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

### 3.2B HTML 基础模板 — 模式 B（视频 + 文字叠加）

> ℹ️ 以下为模式 B 的 HTML/CSS 规范。参考实现见 `20260518_org_slowdown/index.html` 和 `style.css`。

**根容器（竖屏画幅）：**
```html
<div id="composition"
     data-composition-id="composition"
     data-width="1080"
     data-height="1920"
     data-start="0"
     data-duration="{音频总时长}">
```

**⚠️ 视频标签扁平化铁律（最重要的规则）：**

`<video>` 标签**必须**是 `#composition` 的**直接子元素**。严禁将 `<video data-start="...">` 嵌套在任何带有 `data-start` 的 `<div>` 内部，否则 HyperFrames 渲染器无法管理视频播放，**视频将冻结在第一帧**。

```html
<!-- ✅ 正确：视频作为舞台的扁平直接子元素 -->
<video id="v-scene1" class="clip bg-video" src="assets/scene1.mp4" muted playsinline
       data-start="0" data-duration="8" data-track-index="3"></video>
<video id="v-scene2" class="clip bg-video" src="assets/scene2.mp4" muted playsinline
       data-start="8" data-duration="10" data-track-index="3"></video>

<!-- 文字叠加层：独立的场景 div，不含 <video> -->
<div id="scene1" class="clip"
     data-start="0" data-duration="8" data-track-index="1"
     style="z-index: 1;">
  <div class="dim-overlay"></div>
  <div class="bottom-gradient"></div>
  <div class="text-layer text-layer--bottom">
    <div id="s1-line1" class="body-text">旁白文本</div>
    <div id="s1-line2" class="headline">冲击<span class="accent">金句</span>。</div>
  </div>
</div>
```

```html
<!-- ❌ 错误：视频嵌套在带 data-start 的 div 内 → 渲染冻结 -->
<div id="scene1" class="clip" data-start="0" data-duration="8">
  <video class="bg-video" src="assets/scene1.mp4" data-start="0" ...></video>
</div>
```

**视频标签必备属性清单：**

| 属性 | 说明 |
|------|------|
| `id` | 唯一标识，如 `v-scene1`（缺少则渲染冻结） |
| `class="clip bg-video"` | `clip` 让框架管理可见性，`bg-video` 应用视频样式 |
| `muted playsinline` | HyperFrames 接管播放，严禁加 `autoplay` 或 `loop` |
| `data-start` | 视频在时间轴上的起始秒数 |
| `data-duration` | 视频播放时长 |
| `data-track-index` | 设为 `3`（与音频轨 0、场景轨 1/2 错开） |

**全局装饰层（模式 B 推荐）：**
```html
<div class="vignette"></div>      <!-- 暗角 -->
<div class="noise-overlay"></div>  <!-- 胶片噪点 -->
```

### 3.3B CSS 规范 — 模式 B（文字叠加排版）

**核心 CSS 铁律：**
```css
.bg-video {
  position: absolute; inset: 0;
  width: 100%; height: 100%;
  object-fit: cover;
  opacity: 1; /* 👈 必须！覆盖 .clip 的默认 opacity: 0 */
}

.dim-overlay {
  position: absolute; inset: 0;
  background: rgba(0, 0, 0, 0.55); /* 确保文字可读 */
}

.bottom-gradient {
  position: absolute; bottom: 0; left: 0; right: 0;
  height: 600px;
  background: linear-gradient(to top, rgba(10,10,10,0.95) 0%, transparent 100%);
  z-index: 1;
}
```

**文字叠加组件库：**

| 组件 | CSS 类 | 字号 | 用途 |
|------|--------|------|------|
| 大标题金句 | `.headline` | 72px / 900w | 核心冲击句 |
| 超大数字 | `.headline--huge` | 160px | 数据对比（3 → 13） |
| 正文旁白 | `.body-text` | 48px / 400w | 常规叙述 |
| 小字说明 | `.caption-text` | 36px | 补充信息 |
| 强调色 | `.accent` | — | 关键词高亮 |
| 不等号卡 | `.neq` + `.text-card` | 96px | 「A ≠ B」对比卡片 |
| 分屏对比 | `.split-compare` | — | 错误 vs 正确对比 |

**文字定位方式：**
- `.text-layer--bottom`：底部三分之一（大多数叙述场景）
- `.text-layer--center`：垂直居中（金句升华、数字冲击）

### 3.4 静态验收（加入动画前的检查）

用浏览器打开 `index.html`，截图确认：

模式 A：
- [ ] 每张图片完整显示，无裁切，无偏移
- [ ] 图片在 1920×1080 的黑色背景内居中

模式 B：
- [ ] 视频背景可见（非黑屏），文字叠加清晰可读
- [ ] `dim-overlay` 暗化效果适当（文字不被视频干扰）
- [ ] 全屏文字卡（如「A ≠ B」）显示正确

**✅ Stage 3 退出标准：**
- [ ] 纯静态下所有视觉素材（图片或视频）100% 正确显示
- [ ] `data-composition-id`、`data-width`、`data-height` 已正确设置
- [ ] 模式 A：字幕通过 `textContent` 注入；模式 B：文字叠加 DOM 结构完整
- [ ] `npx hyperframes lint .` 报 **0 error(s)**

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

### 4.1.1 情绪驱动转场匹配

场景之间的转场不应千篇一律。根据**下一幕的情绪档位**选择对应转场：

| 下一幕情绪档位 | 转场方式 | GSAP 代码 | 视觉效果 |
|-------------|---------|----------|--------|
| 1（舒缓叙事） | 慢溶解 | `fromTo(next, {opacity:0}, {opacity:1, duration:1.2, ease:"power1.inOut"})` | 平静过渡，如水墨晕染 |
| 2（紧张蓄力） | 标准交叉淡化 | `fromTo(next, {opacity:0}, {opacity:1, duration:0.5, ease:"none"})` | 默认节奏 |
| 3（高潮爆发） | 硬切 + 微缩放 | `tl.set(next, {opacity:1}); fromTo(next, {scale:1.05}, {scale:1.0, duration:0.3})` | 冲击感 |
| 4（沉默留白） | 淡入黑 → 淡出黑 | `先 to(prev, {opacity:0, duration:0.8}), 延迟 0.5s, 再 fromTo(next, {opacity:0}, {opacity:1, duration:1.0})` | 呼吸感，给观众消化时间 |

> 当前实现仍使用统一 0.5s 交叉淡化。在后续迭代中可按此表升级。

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

### 5.1 视频脚本元数据与多平台宣发策划补充

在 `视频脚本.md` 中补充技术元数据与 **「小红书/短视频爆款宣发策划」**，确保视频具备出厂即可一键分发的高效爆款能力。

#### 1. 技术参数补充（脚本底部）
```markdown
## 技术参数
- **声纹**：VoxCPM2 用户克隆 / Kokoro am_adam
- **实测时长**：{ffprobe 实测值}s
- **BGM**：{BGM 名称} by {BGM 作者} (CC BY 4.0)
- **YouTube**：{URL}
```

#### 2. 小红书/短视频宣发策划（脚本最下方）
在 `视频脚本.md` 的最底部，**强制追加**小红书专属的宣发案策划，包含：
1. **爆款标题推荐**（至少 3-4 个）：
   - *写作公式 1 (痛点直击)*：`[痛点表情] + 痛点揭露/反差怪象 + 为什么会这样？`（例如：🤯 职场怪象：为什么招的人越贵，公司反而越慢？）
   - *写作公式 2 (认知颠覆)*：`[警示表情] + 戳破某种常见幻觉/认知错误！`（例如：🚫 戳破老板的幻觉：个体优秀 ≠ 组织高效！）
   - *写作公式 3 (具体数字)*：`[下降/冲突表情] + 极端数字对比 + 场景重现`（例如：📉 协同内耗：本来3人能决定的事，为什么变成了13人讨论？）
2. **封面/配图文字建议**：设计大字冲击的主副标题，做首屏抓手。
3. **小红书正文文案**：
   - 使用丰富的 **Emoji** 进行段落排版，提升可读性。
   - 包含：**痛点共情**（点明现状） + **干货输出**（列出 3 点精辟洞察或引述视频金句） + **互动钩子**（引导评论区分享见解，如“你们公司也是这样吗？”） + **精准热门标签**（如 `#职场那些事儿 #组织架构 #管理思维 #职场内耗`）。

*规范模板示例：*
```markdown
## 5. 小红书宣发策划

### 爆款标题推荐
1. [小红书标题 1]
2. [小红书标题 2]
3. [小红书标题 3]

### 封面/配图文字建议
- **主标题**：[极简有力]
- **副标题**：[点题/对比]

### 小红书正文文案
[带有丰富 Emoji、干货条理明晰、包含互动提问和小红书热门 Tag 的 300-500 字社交文案]
```

### 5.2 README 更新

在 `README.md` 的「演示作品」表格中追加新作品条目（中英文双语部分均需更新）。

### 5.3 Git 归档

**仅 commit，不自动 push。** 推送时机由用户决定。

```bash
git add YYYYMMDD/ README.md
git commit -m "feat: Add {video_title} project"
# git push 由用户按需执行，不自动推送
```

**✅ Stage 5 退出标准：**
- [ ] `视频脚本.md` 包含完整元数据（声纹、时长、BGM、YouTube 链接）以及小红书爆款标题与宣发策划文案
- [ ] `README.md` 中英双语演示作品表格已更新
- [ ] `git commit` 成功

---

## 附录 A：视觉风格指南

### 风格决策原则

- **动态适配**：视觉风格必须完全服务于故事。可选国风写意、现代极简、蒸汽朋克、赛博朋克或电影感实拍风格。
- **自洽性**：全片所有图片的色调、光影和元素必须统一，严禁跨时空混搭（除非剧情要求）。
- **文化锚点优先于美感**：当「好看」和「文化准确」冲突时，选文化准确。一张唐代故事里出现的日式庭院，再好看也是错误。

### 常见文化锚点速查表

| 文化设定 | 建筑关键词 | 服饰关键词 | 常见误导（必须排除） |
|---------|-----------|-----------|-------------------|
| 唐宋中国 | Dougong brackets, grey tiles, wooden beams, moon gate | Round-collar robe, Hanfu, Mingguang armor | 鸟居, 和服, 榻榻米, 哥特尖拱 |
| 明清中国 | Upturned eaves, red lacquer columns, courtyard houses | Changshan, Qipao, Mandarin collar | 和服, 韩服, 维多利亚裙 |
| 日本和风 | Torii gate, tatami, shoji screens, engawa | Kimono, hakama, geta sandals | 斗拱, 汉服, 旗袍 |
| 中世纪欧洲 | Gothic arches, stone castle, stained glass | Chainmail, surcoat, leather boots | 东方建筑, 丝绸长袍 |
| 赛博朋克 | Neon signs, holographic ads, megastructures | LED-trimmed jacket, visor, cybernetic limbs | 古典建筑, 自然光 |

### 图片提示词工程

- **公式**：`[画幅指令] + [文化锚点] + [本幕内容] + [色调光影] + [质量后缀] + [排除清单]`
- **质量后缀**：`hyper-realistic details, cinematic lighting, masterpiece, 8K`
- **排除清单格式**：`No [culture A] elements, no [culture B] elements, no modern objects.`
- **中文文字生成**（架构图/概念图专用）：`A [style] visualization with Chinese labels. Main node: "核心词". Sub-nodes: "关联词1", "关联词2". Professional design, glowing connections.`

---

## 附录 B：已知技术陷阱速查

**模式 A（纯图片）陷阱：**

| 现象 | 根因 | 修复 |
|------|------|------|
| 图片裁切/偏移 | GSAP 矩阵覆盖了 `translate` 居中 | 改用 `object-fit: contain`，绝不用 `translate` |
| 正方形图片顶部被裁 | `object-fit: cover` 裁切了主体 | 强制 16:9 生图，或改用 `contain` + 毛玻璃背景 |
| 视频提前截断/少幕 | 字幕中含未转义的 `<` `>` 破坏 DOM | 改用 `textContent` 注入 |
| 画面色偏 | img 标签含 `filter: hue-rotate(...)` | 删除该 filter |

**模式 B（视频 + 文字叠加）陷阱：**

| 现象 | 根因 | 修复 |
|------|------|------|
| 视频背景全黑 | `.clip` 默认 `opacity: 0`，视频继承了 | `.bg-video { opacity: 1; }` 物理覆盖 |
| 渲染后视频冻结在第一帧 | `<video data-start>` 嵌套在 `<div data-start>` 内 | 扁平化为 `#composition` 的直接子元素 |
| `media_missing_id` 错误 | `<video>` 没有 `id` 属性 | 每个 `<video>` 加唯一 `id` |
| Pexels 下载 SSL 报错 | Cloudflare 在传输末尾断开连接 | curl `--retry 5`，若文件通过 `ffprobe` 校验则视为成功 |
| 横屏视频裁切后比例变形 | 直接 scale 而非先 crop | 横屏用 `crop=ih*9/16:ih,scale=1080:1920` |

**通用陷阱：**

| 现象 | 根因 | 修复 |
|------|------|------|
| `inspect` 报 `totalDuration undefined` | 根容器缺少 `data-duration` | 补上 `data-duration="{音频总长}"` |
| `inspect` 报错 / MP4 时长随机 | 违反渲染合约 | 时间轴永远 `paused: true`，不写 `play()` |
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

**模式 A（纯图片寺言视频）：**
```text
/YYYYMMDD/
  ├── index.html          (核心时间轴，Stage 3/4 产物)
  ├── assets/
  │   ├── scene_cover.png (封面图，高吸引力)
  │   ├── scene1.png      (场景图)
  │   ├── scene{N}.png
  │   ├── scene_end.png   (结尾图，点题升华)
  │   ├── narration.wav   (TTS 配音，Stage 1.3 产物)
  │   ├── bgm.mp3         (背景音乐，Stage 1.6 产物)
  │   └── transcript.json (Whisper 时间戳，Stage 2.2 产物)
  ├── 视频脚本.md          (剧本，Stage 1.2 产物)
  └── promo_video.mp4     (最终成品，Stage 4.3 产物，Git 豁免名单)
```

**模式 B（视频 + 文字叠加）：**
```text
/YYYYMMDD_{project_name}/
  ├── index.html               (核心时间轴，竖屏 1080×1920)
  ├── style.css                (独立样式表，文字叠加组件库)
  ├── download_and_process.py   (B-roll 自动化下载/裁剪脚本)
  ├── assets/
  │   ├── scene1.mp4 ~ sceneN.mp4  (裁剪后的 B-roll 视频，1080×1920，无音轨)
  │   ├── narration.wav            (TTS 配音)
  │   └── bgm.mp3                  (背景音乐)
  ├── 视频脚本.md                   (剧本 + B-roll 素材规划表)
  └── renders/
      └── {project}_YYYY-MM-DD_HH-MM-SS.mp4  (渲染成品)
```
