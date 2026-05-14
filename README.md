<div align="center">

# 🔨 FableForge
### 寓言铸造厂

**AI-powered Chinese allegory video pipeline**
*Give an AI Agent a playbook, and it will forge a management allegory short film — in your own voice.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![HyperFrames](https://img.shields.io/badge/Powered%20by-HyperFrames-blue)](https://hyperframes.heygen.com)
[![VoxCPM2](https://img.shields.io/badge/Voice-VoxCPM2-green)](https://pypi.org/project/voxcpm/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org)

**[English](#english) · [中文](#中文)**

</div>

---

<a name="english"></a>
## 🇬🇧 English

FableForge is a fully automated video production pipeline that turns a management concept into a polished short video — complete with narration in **your cloned voice**, AI-generated visuals, frame-accurate subtitles, and cinematic Ken Burns motion.

> **FableForge** = Fable × Forge: Forge a deep management insight into a compelling allegorical short film using AI.

### ✨ Demo Works

| Title | Management Insight | Duration | Link |
|-------|--------------------|----------|------|
| *The Wolf King's Trial* | Zero-sum competition & the promotion trap | 60s | [Watch](./20260514/final_video.mp4) |
| *The Endless Bridge* | Leadership extension & trust transfer | 60s | [Watch](./20260513/final_video.mp4) |

> 📺 Drag `final_video.mp4` into a browser or media player to watch.

### 🚀 Quick Start

> The core experience: narrating your allegory **in your own cloned voice**. First-time setup takes ~30 minutes.

#### Phase 1 — Record Your Voice (once, forever)

VoxCPM2 is a voice-cloning model. It needs a 15-second sample of your voice, then permanently mimics your timbre.

**Step 1 — Prepare your recording environment**
- Quiet room (no AC noise or echo)
- Any recording app (Mac QuickTime is fine, or Audacity)
- Wired headset mic (much better than built-in)

**Step 2 — Record a 15-second voice sample**

Read this text naturally (don't slow down):
> *"Hi, I'm recording my voice sample. This audio will serve as my voiceprint template, helping the AI accurately reproduce my tone and emotion. This is [your name], thank you for listening."*

Export as **WAV**, 44100 Hz or higher. Save to `voice-model/01_samples/my_voice.wav`.

**Step 3 — Install VoxCPM2**

```bash
python3 -m venv voice-model/venv
source voice-model/venv/bin/activate
pip install voxcpm soundfile torch numpy
# First run auto-downloads the VoxCPM2 model (~4 GB)
```

**Step 4 — Test voice cloning**

```bash
cp voice-model/generate.py.example voice-model/generate.py
# Edit generate.py → set REFERENCE_WAV and PROMPT_TEXT
python voice-model/generate.py
# Output appears in voice-model/02_output/ — play it to verify
```

#### Phase 2 — Configure the Project (once)

```bash
git clone https://github.com/your-username/fableforge.git
cd fableforge

# Install FFmpeg (required for rendering)
curl -L https://evermeet.cx/ffmpeg/get/zip -o ffmpeg.zip && unzip ffmpeg.zip
curl -L https://evermeet.cx/ffmpeg/get/ffprobe/zip -o ffprobe.zip && unzip ffprobe.zip
mkdir -p bin && mv ffmpeg bin/ && mv ffprobe bin/ && chmod +x bin/*
```

#### Phase 3 — Generate Your First Allegory Video

```bash
cp -r template/ $(date +%Y%m%d)/
cd $(date +%Y%m%d)/

# 1. Write your script (fill in the storyboard template)
open script-template.md      # English template
# open 视频脚本.md            # Chinese template

# 2. Generate images with Midjourney / Flux / DALL·E
# Name them scene1.png, scene2.png ... → put in assets/

# 3. Generate narration in your voice
source ../voice-model/venv/bin/activate
python ../voice-model/generate.py   # set TARGET_TEXT to your full narration
cp ../voice-model/02_output/*.wav assets/narration.wav

# 4. Transcribe audio → get precise timestamps
export PATH=../bin:$PATH
npx hyperframes transcribe assets/narration.wav

# 5. Validate + Render
npm run check   # verify timeline integrity
npm run render  # output: final_video.mp4
```

### 🏗️ Project Structure

```
fableforge/
├── template/
│   ├── index.html          ← HyperFrames timeline template
│   ├── style.css           ← Video composition styles
│   ├── script-template.md  ← English storyboard template
│   └── 视频脚本.md          ← Chinese storyboard template
│
├── YYYYMMDD/               ← Per-episode archive
│   ├── index.html
│   ├── assets/
│   │   ├── scene1.png … scene{N}.png
│   │   ├── narration.wav
│   │   └── transcript.json
│   └── final_video.mp4
│
├── voice-model/
│   ├── generate.py.example ← Voice generation script template
│   └── README.md           ← Recording guide
│
├── .agents/skills/fableforge/
│   ├── SKILL.md            ← AI Agent SOP (Chinese)
│   └── SKILL.en.md         ← AI Agent SOP (English)
│
└── package.json
```

### 🧠 Core SOP: 4-Stage Industrial Pipeline

The heart of FableForge is a **command-level executable SOP** for AI Agents, stored in [`.agents/skills/fableforge/SKILL.en.md`](./.agents/skills/chinese-allegory-video-production/SKILL.en.md).

| Stage | What Happens | Exit Criteria |
|-------|-------------|---------------|
| **Stage 1** Concept & Asset Generation | Write allegory, generate images, synthesize voice | Image count == scene count, audio file ready |
| **Stage 2** Data-Driven Timeline | Whisper transcription, frame-accurate scene alignment | Deviation < 0.2s, zero estimated values |
| **Stage 3** Static Layout Validation | Pure HTML/CSS, verify no image cropping before animation | All images display fully, DOM injected dynamically |
| **Stage 4** Pre-flight & Render | inspect → render, machine validation replaces eyeballing | inspect exits 0, duration matches audio exactly |

### 🛠️ Tech Stack

| Component | Role | Link |
|-----------|------|------|
| **HyperFrames** | HTML-to-MP4 deterministic render engine | [hyperframes.heygen.com](https://hyperframes.heygen.com) |
| **VoxCPM2** | Personal voice cloning & TTS synthesis | [PyPI](https://pypi.org/project/voxcpm/) |
| **Whisper** | Word-level timestamp transcription | [github.com/openai/whisper](https://github.com/openai/whisper) |
| **GSAP** | Ken Burns zoom & motion choreography | [gsap.com](https://gsap.com) |
| **FFmpeg** | Audio duration analysis & silence detection | [ffmpeg.org](https://ffmpeg.org) |

### 📦 For Content Creators (no code)

1. Open `template/script-template.md` and fill in your storyboard
2. Generate images with Midjourney / Flux / DALL·E → name them `scene1.png`...`scene{N}.png` → drop into `assets/`
3. Generate `narration.wav` with any TTS tool → drop into `assets/`
4. Run `npm run check && npm run render`

### 📦 For AI Engineers (Agent integration)

Inject [`.agents/skills/chinese-allegory-video-production/SKILL.en.md`](./.agents/skills/chinese-allegory-video-production/SKILL.en.md) into your Agent context. It will autonomously follow the 4-stage pipeline.

Compatible with: **Claude** / **Gemini** / **Cursor** / **VS Code Copilot**

### 🙏 Acknowledgements

| Project | Role in FableForge |
|---------|-------------------|
| [HyperFrames](https://hyperframes.heygen.com) by HeyGen | Core video render pipeline |
| [VoxCPM2](https://pypi.org/project/voxcpm/) | Voice cloning engine |
| [OpenAI Whisper](https://github.com/openai/whisper) | Audio transcription (MIT License) |

### 🤝 Contributing

PRs welcome for:
- New allegory video examples (add to a `YYYYMMDD/` directory)
- Additional visual style CSS templates
- TTS / Whisper adapters for other languages

### 📄 License · MIT

---

<a name="中文"></a>
## 🇨🇳 中文



---

## 🚀 快速开始

> 本项目的核心体验是用**你自己的声音**讲述寓言故事。整个流程分三个阶段，首次使用约需 30 分钟完成配置。

---

### 阶段一：录制你的声音（首次必做，一劳永逸）

VoxCPM2 是一个**声纹克隆**模型，它需要你提供一段自己的声音样本，之后便能永久模拟你的音色。

**第 1 步：准备录音环境**
- 安静的房间（避免空调噪音、回声）
- 任意录音软件（Mac 自带的 QuickTime 即可，或使用 Audacity）
- 有线耳机麦克风（比内置麦克风效果好很多）

**第 2 步：录制 15 秒声音样本**

朗读以下这段文字（语速自然，不要过慢）：
> "大家好，我在录制自己的声音样本。这段录音将作为我的声纹模板，帮助 AI 精确还原我的音色和情感。现在是[你的名字]，感谢收听。"

- 导出为 **WAV 格式**，采样率 44100Hz 或以上
- 保存至本项目的 `voice-model/01_samples/my_voice.wav`

**第 3 步：安装 VoxCPM2 语音克隆环境**

```bash
# 创建 Python 虚拟环境（推荐 Python 3.10+）
python3 -m venv voice-model/venv
source voice-model/venv/bin/activate

# 安装依赖
pip install voxcpm soundfile torch numpy

# 首次运行会自动从 HuggingFace 下载 VoxCPM2 模型（约 4GB，需等待）
```

**第 4 步：测试声音克隆**

```bash
# 复制通用生成脚本
cp voice-model/generate.py.example voice-model/generate.py

# 编辑 generate.py，修改 CONFIG 区域的两个路径
# REFERENCE_WAV = "voice-model/01_samples/my_voice.wav"   ← 你的声音样本
# PROMPT_TEXT = "你朗读样本时说的那段文字"                  ← 必须与录音内容一致

# 运行测试
source voice-model/venv/bin/activate
python voice-model/generate.py
# 成功后会在 voice-model/02_output/ 生成测试音频，播放验证效果
```

---

### 阶段二：配置项目环境（首次）

```bash
# 1. 克隆仓库
git clone https://github.com/your-username/fableforge.git
cd fableforge

# 2. 安装 FFmpeg（视频渲染必须）
curl -L https://evermeet.cx/ffmpeg/get/zip -o ffmpeg.zip && unzip ffmpeg.zip
curl -L https://evermeet.cx/ffmpeg/get/ffprobe/zip -o ffprobe.zip && unzip ffprobe.zip
mkdir -p bin && mv ffmpeg bin/ && mv ffprobe bin/ && chmod +x bin/*
```

---

### 阶段三：生成你的第一个寓言视频

```bash
# 1. 从模板创建今天的项目
cp -r template/ $(date +%Y%m%d)/
cd $(date +%Y%m%d)/

# 2. 编写剧本（按模板格式填写分镜旁白）
open 视频脚本.md

# 3. 生成图片
# 用 Midjourney / Flux / DALL·E 按每幕"画面描述"生成图片
# 命名为 scene1.png, scene2.png ... 放入 assets/

# 4. 用你的声音生成配音
source ../voice-model/venv/bin/activate
python ../voice-model/generate.py   # 修改 TARGET_TEXT 为你的完整旁白
cp ../voice-model/02_output/output.wav assets/narration.wav

# 5. 音频转录（获取精确时间戳）
export PATH=../bin:$PATH
npx hyperframes transcribe assets/narration.wav

# 6. 预检 + 渲染
npm run check   # 确认时间轴完整无误
npm run render  # 输出 final_video.mp4
```

---

## 🏗️ 项目架构

```
.
├── template/               ← 新项目起点（从这里 fork）
│   ├── index.html          ← HyperFrames 时间轴模板
│   ├── assets/             ← 放你的图片和音频
│   └── 视频脚本.md          ← 剧本模板
│
├── YYYYMMDD/               ← 每期视频的归档目录
│   ├── index.html
│   ├── assets/
│   │   ├── scene1.png … scene{N}.png
│   │   ├── narration.wav
│   │   └── transcript.json
│   ├── 视频脚本.md
│   └── final_video.mp4
│
├── .agents/skills/
│   └── chinese-allegory-video-production/
│       └── SKILL.md        ← AI Agent 专用 SOP（核心文档）
│
├── AGENTS.md               ← AI 工作空间配置
└── package.json
```

---

## 🧠 核心 SOP：四段式工业化流水线

本项目的核心是一套写给 AI Agent 的**命令级可执行 SOP**，存放于 [`.agents/skills/chinese-allegory-video-production/SKILL.md`](./.agents/skills/chinese-allegory-video-production/SKILL.md)。

它将整个生产过程切割为四个不可跳过的阶段，每个阶段都有**具体命令**和**退出验收标准**：

| 阶段 | 做什么 | 退出标准 |
|------|--------|---------|
| **Stage 1** 概念与资产生成 | 创作寓言、生成图片、合成语音 | 图片数 == 分镜数，音频文件就位 |
| **Stage 2** 数据驱动时间轴 | Whisper 转录，精确对齐每幕时间 | 误差 < 0.2 秒，无估算值 |
| **Stage 3** 静态排版验收 | 纯静态 HTML/CSS，先验证图片不裁切 | 所有图片完整显示，DOM 动态注入 |
| **Stage 4** 预检与渲染 | inspect → render，机器校验代替肉眼 | inspect 0 报错，时长精确匹配 |

---

## 🛠️ 技术栈

| 组件 | 用途 | 项目地址 |
|------|------|----------|
| **HyperFrames** | HTML 驱动的视频渲染引擎（核心） | [hyperframes.heygen.com](https://hyperframes.heygen.com) |
| **VoxCPM2** | 高保真个人声纹克隆与 TTS 语音合成 | [voxcpm on PyPI](https://pypi.org/project/voxcpm/) |
| **Whisper** | 词级时间戳音频转录 | [github.com/openai/whisper](https://github.com/openai/whisper) |
| **GSAP** | Ken Burns 缩放与动效编排 | [gsap.com](https://gsap.com) |
| **FFmpeg** | 音频时长分析 & 静音检测 | [ffmpeg.org](https://ffmpeg.org) |

---

## 🙏 致谢与开源声明 (Acknowledgements)

本项目站在以下开源项目的肩膀上构建，感谢原作者的贡献：

### [HyperFrames](https://hyperframes.heygen.com) by HeyGen
本项目的视频渲染核心完全基于 HyperFrames 框架。HyperFrames 提供了 HTML/JS 到 MP4 的确定性渲染管线，是本项目实现"代码即视频"的技术基石。
- 官网文档：https://hyperframes.heygen.com/introduction
- 开源协议：请参阅 HyperFrames 官方许可

### [VoxCPM2](https://pypi.org/project/voxcpm/)
本项目的语音合成功能基于 VoxCPM2 实现个人声纹克隆。VoxCPM2 的双段直出策略在保证音色准确性的同时有效避免了长文本的回声失真问题。
- 使用方式：通过 `voxcpm` Python 包调用
- 安装：`pip install voxcpm`

### [OpenAI Whisper](https://github.com/openai/whisper)
通过 `npx hyperframes transcribe` 调用 Whisper 模型，实现音频的词级时间戳解析，用于将旁白精确对齐到每一幕分镜。
- 开源协议：MIT License

---

## 📦 给内容创作者（零代码使用）

1. 打开 `template/视频脚本.md`，填写你的故事分镜
2. 用 AI 工具（Midjourney / Flux / DALL·E）生成对应图片，命名为 `scene1.png` ... `scene{N}.png`，放入 `assets/`
3. 用任意 TTS 工具生成 `narration.wav`，放入 `assets/`
4. 运行 `npm run check && npm run render`

---

## 📦 给 AI 工程师（Agent 集成）

本项目支持与以下 AI Agent 框架集成：

- **Anthropic Claude** / **Google Gemini**（通过 `AGENTS.md` + `SKILL.md` 注入上下文）
- **Cursor** / **VS Code Copilot**（直接读取 `.agents/` 目录）

将 `.agents/skills/chinese-allegory-video-production/SKILL.md` 注入你的 Agent 上下文，它会自动遵循四段式流水线完成生产。

---

## 🤝 贡献

欢迎 PR 贡献以下内容：
- 新的寓言视频案例（放入 `YYYYMMDD/` 目录）
- 更多视觉风格的 CSS 模板
- 其他语言的 TTS/Whisper 适配方案

---

## 📄 License

MIT
