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
| *The Scale That Gains Weight* | Cantillon Effect & wealth redistribution | 133s | [Watch](https://youtu.be/mSHp5E3-PDs) |

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
git clone https://github.com/Lucas-Kay8/fableforge.git
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

### 🧠 Core SOP: 5-Stage Industrial Pipeline

The heart of FableForge is a **command-level executable SOP** for AI Agents, stored in [`.agents/skills/fableforge/SKILL.en.md`](./.agents/skills/fableforge/SKILL.en.md).

| Stage | What Happens | Exit Criteria |
|-------|-------------|---------------|
| **Stage 1** Concept & Asset Generation | Write allegory, generate images, synthesize voice | Image count == scene count, audio file ready |
| **Stage 1.5** BGM Matching | Mood analysis, track selection, auto-integration | BGM file ready, attribution added |
| **Stage 2** Data-Driven Timeline | Whisper transcription, frame-accurate scene alignment | Deviation < 0.2s, zero estimated values |
| **Stage 3** Static Layout Validation | Pure HTML/CSS, verify no image cropping before animation | All images display fully, DOM injected dynamically |
| **Stage 4** Pre-flight & Render | inspect → render, machine validation replaces eyeballing | inspect exits 0, duration matches audio exactly |

### 🎵 Automated BGM Integration

FableForge now supports automatic background music matching:
- **Mood-Aware**: Matches BGM based on the emotional gear of your script (e.g., *The Scale That Gains Weight* uses 'Undertow' by Scott Buckley for its atmospheric tension).
- **Auto-Ducking**: Defaults to 0.15–0.25 volume to ensure narration clarity.
- **Attribution Ready**: Automatically inserts license info into your script.

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

Inject [`.agents/skills/fableforge/SKILL.en.md`](./.agents/skills/fableforge/SKILL.en.md) into your Agent context. It will autonomously follow the 5-stage pipeline.

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

FableForge 是一个全自动视频生产管线，能将管理学概念转化为精致的短视频——包含**克隆你的声音**进行的旁白、AI 生成的视觉画面、精确到帧的字幕，以及电影级的 Ken Burns 动态效果。

> **FableForge** = Fable (寓言) × Forge (铸造): 利用 AI 将深刻的管理洞察铸造成引人入胜的寓言短片。

### ✨ 演示作品

| 标题 | 管理洞察 | 时长 | 链接 |
|-------|--------------------|----------|------|
| 《狼王的审判》 | 零和博弈与晋升陷阱 | 60s | [观看](./20260514/final_video.mp4) |
| 《无尽之桥》 | 领导力延伸与信任交付 | 60s | [观看](./20260513/final_video.mp4) |
| 《会自己变重的秤》 | 坎蒂隆效应与财富再分配 | 133s | [观看](https://youtu.be/mSHp5E3-PDs) |

> 📺 将 `final_video.mp4` 拖入浏览器或播放器即可观看。

### 🚀 快速开始

> 本项目的核心体验是用**你自己的声音**讲述寓言故事。整个流程分三个阶段，首次使用约需 30 分钟完成配置。

#### 阶段一：录制你的声音（首次必做，一劳永逸）

VoxCPM2 是一个**声纹克隆**模型，它需要你提供一段自己的声音样本，之后便能永久模拟你的音色。

**第 1 步：准备录音环境**
- 安静的房间（避免空调噪音、回声）
- 有线耳机麦克风（效果优于内置麦克风）

**第 2 步：录制 15 秒声音样本**

朗读以下这段文字：
> "大家好，我在录制自己的声音样本。这段录音将作为我的声纹模板，帮助 AI 精确还原我的音色和情感。现在是[你的名字]，感谢收听。"

- 导出为 **WAV 格式**，采样率 44100Hz 或以上
- 保存至 `voice-model/01_samples/my_voice.wav`

#### 阶段二：配置项目环境（首次）

```bash
git clone https://github.com/Lucas-Kay8/fableforge.git
cd fableforge

# 安装 FFmpeg（视频渲染必须）
curl -L https://evermeet.cx/ffmpeg/get/zip -o ffmpeg.zip && unzip ffmpeg.zip
curl -L https://evermeet.cx/ffmpeg/get/ffprobe/zip -o ffprobe.zip && unzip ffprobe.zip
mkdir -p bin && mv ffmpeg bin/ && mv ffprobe bin/ && chmod +x bin/*
```

#### 阶段三：生成你的第一个寓言视频

```bash
cp -r template/ $(date +%Y%m%d)/
cd $(date +%Y%m%d)/

# 1. 编写剧本
open 视频脚本.md

# 2. 生成配音
source ../voice-model/venv/bin/activate
python ../voice-model/generate.py   # 修改 TARGET_TEXT 为你的完整旁白
cp ../voice-model/02_output/output.wav assets/narration.wav

# 3. 预检 + 渲染
npm run check
npm run render
```

### 🏗️ 项目架构

```
.
├── template/               ← 新项目起点
├── YYYYMMDD/               ← 每期视频归档
├── .agents/skills/fableforge/
│   ├── SKILL.md            ← AI Agent 专用 SOP (核心)
│   └── SKILL.en.md         ← AI Agent 专用 SOP (英文)
├── voice-model/            ← 语音克隆模型与脚本
└── package.json
```

### 🧠 核心 SOP：五段式工业化流水线

本项目的核心是一套写给 AI Agent 的**命令级可执行 SOP**，存放于 [`.agents/skills/fableforge/SKILL.md`](./.agents/skills/fableforge/SKILL.md)。

| 阶段 | 做什么 | 退出标准 |
|------|--------|---------|
| **Stage 1** 概念与资产生成 | 创作寓言、生成图片、合成语音 | 图片数 == 分镜数，音频文件就位 |
| **Stage 1.5** BGM 自动配乐 | 情绪识别、曲库匹配、自动下载集成 | BGM 就位，署名信息补充 |
| **Stage 2** 数据驱动时间轴 | Whisper 转录，精确对齐每幕时间 | 误差 < 0.2 秒，无估算值 |
| **Stage 3** 静态排版验收 | 纯静态 HTML/CSS，验证不裁切 | 所有图片完整显示，DOM 动态注入 |
| **Stage 4** 预检与渲染 | inspect → render，机器校验 | inspect 0 报错，时长精确匹配 |

### 🎵 新功能：自动化背景音乐 (BGM)

FableForge 现已支持自动配乐：
- **情绪匹配**：根据脚本的“情绪档位”自动推荐合适的背景音乐（如《会自己变重的秤》选用了 Scott Buckley 的 'Undertow' 来烘托悬疑感）。
- **自动避让**：默认音量设为 0.15-0.25，确保背景音不掩盖人声旁白。
- **版权合规**：自动在脚本中注入作者署名和 CC 协议信息。

### 🛠️ 技术栈

| 组件 | 用途 |
|------|------|
| **HyperFrames** | 视频渲染引擎 |
| **VoxCPM2** | 声纹克隆与语音合成 |
| **Whisper** | 词级时间戳音频转录 |
| **GSAP** | 动效编排 |
| **FFmpeg** | 媒体处理 |

---

### 📄 License

MIT
