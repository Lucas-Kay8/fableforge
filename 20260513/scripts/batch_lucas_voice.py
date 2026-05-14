import os
import sys
import torch
import numpy as np
import soundfile as sf

# Add the voice model directory to sys.path to ensure imports work
VOICE_MODEL_DIR = "/Users/lucas/Work/09.Antigravity/语音模型"
sys.path.append(VOICE_MODEL_DIR)

from voxcpm import VoxCPM

# CONFIG
REFERENCE_WAV = os.path.join(VOICE_MODEL_DIR, "01_人声采样/my_voice_v2.wav")
PROMPT_TEXT = "我是卢卡斯，正在测试巅峰语音克隆技术。这段音频将作为我的声纹模板，帮助模型精确还原我的音色 and 情感。希望接下来的生成效果能让我惊艳。"
CFG_VALUE = 2.0
INFERENCE_STEPS = 40
SWEET_SPOT_CHARS = 130
CROSSFADE_MS = 100

def smart_split(text, sweet_spot=SWEET_SPOT_CHARS):
    text = text.strip()
    if "|||" in text:
        return [p.strip() for p in text.split("|||") if p.strip()]
    if len(text) <= sweet_spot:
        return [text]
    mid = len(text) // 2
    search_start = int(len(text) * 0.35)
    search_end = int(len(text) * 0.65)
    best_pos = None
    best_dist = float('inf')
    for i in range(search_start, search_end):
        if text[i] in '。？！.?!':
            dist = abs(i - mid)
            if dist < best_dist:
                best_dist = dist
                best_pos = i + 1
    if best_pos:
        return [text[:best_pos].strip(), text[best_pos:].strip()]
    return [text]

def crossfade(seg1, seg2, sample_rate, ms=CROSSFADE_MS):
    overlap = int(sample_rate * ms / 1000)
    if overlap > len(seg1) or overlap > len(seg2):
        return np.concatenate([seg1, seg2])
    fade_out = np.linspace(1.0, 0.0, overlap)
    fade_in = np.linspace(0.0, 1.0, overlap)
    mixed = seg1[-overlap:] * fade_out + seg2[:overlap] * fade_in
    return np.concatenate([seg1[:-overlap], mixed, seg2[overlap:]])

def generate_voice(text, output_file):
    print(f"🎙️ Generating: {output_file}")
    vox = VoxCPM.from_pretrained("openbmb/VoxCPM2", load_denoiser=False)
    model = vox.tts_model
    sample_rate = model.sample_rate
    
    fixed_cache = model.build_prompt_cache(
        reference_wav_path=REFERENCE_WAV,
        trim_silence_vad=True
    )
    
    segments = smart_split(text)
    wav_parts = []
    
    for seg in segments:
        gen = model._generate_with_prompt_cache(
            target_text=seg,
            prompt_cache=fixed_cache,
            cfg_value=CFG_VALUE,
            inference_timesteps=INFERENCE_STEPS,
            retry_badcase=True,
            retry_badcase_max_times=3
        )
        wav_tensor, _, _ = next(gen)
        wav_np = wav_tensor.squeeze(0).cpu().numpy()
        wav_parts.append(wav_np)
    
    if len(wav_parts) == 1:
        final_wav = wav_parts[0]
    else:
        final_wav = wav_parts[0]
        for part in wav_parts[1:]:
            final_wav = crossfade(final_wav, part, sample_rate)
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    sf.write(output_file, final_wav, sample_rate)
    print(f"✅ Saved to {output_file}")

if __name__ == "__main__":
    os.environ["HF_HUB_OFFLINE"] = "1"
    
    narration_files = [
        ("scripts/narration_1.txt", "assets/audio/narration_1_v3.wav"),
        ("scripts/narration_2.txt", "assets/audio/narration_2_v3.wav"),
        ("scripts/narration_3.txt", "assets/audio/narration_3_v3.wav"),
        ("scripts/narration_4.txt", "assets/audio/narration_4_v3.wav"),
        ("scripts/narration_5.txt", "assets/audio/narration_5_v3.wav"),
        ("scripts/narration_6.txt", "assets/audio/narration_6_v3.wav"),
        ("scripts/narration_7.txt", "assets/audio/narration_7_v3.wav"),
        ("scripts/narration_8.txt", "assets/audio/narration_8_v3.wav"),
        ("scripts/narration_9.txt", "assets/audio/narration_9_v3.wav"),
    ]
    
    for txt_path, wav_path in narration_files:
        if os.path.exists(txt_path):
            with open(txt_path, "r", encoding="utf-8") as f:
                text = f.read().strip()
            generate_voice(text, wav_path)
