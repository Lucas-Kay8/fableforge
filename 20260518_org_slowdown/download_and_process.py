import os
import subprocess
import shutil

# 视频直链与目标文件名映射
VIDEO_MAP = {
    "laptop_dark.mp4": {
        "url": "https://videos.pexels.com/video-files/19532053/19532053-hd_1080_1920_30fps.mp4",
        "is_vertical": True
    },
    "meeting.mp4": {
        "url": "https://videos.pexels.com/video-files/6930645/6930645-uhd_1440_2560_25fps.mp4",
        "is_vertical": True
    },
    "walking_office.mp4": {
        "url": "https://videos.pexels.com/video-files/7652205/7652205-uhd_1440_2560_30fps.mp4",
        "is_vertical": True
    },
    "busy_office.mp4": {
        "url": "https://videos.pexels.com/video-files/6951393/6951393-uhd_2560_1440_25fps.mp4",
        "is_vertical": False
    },
    "typing.mp4": {
        "url": "https://videos.pexels.com/video-files/7822022/7822022-hd_1080_1920_30fps.mp4",
        "is_vertical": True
    },
    "code_screen.mp4": {
        "url": "https://videos.pexels.com/video-files/34459460/14601224_1080_1920_25fps.mp4",
        "is_vertical": True
    },
    "city_night.mp4": {
        "url": "https://videos.pexels.com/video-files/34835533/14766154_2560_1440_24fps.mp4",
        "is_vertical": False
    },
    "laptop_glow.mp4": {
        "url": "https://videos.pexels.com/video-files/4565731/4565731-uhd_2560_1440_25fps.mp4",
        "is_vertical": False
    }
}

ASSETS_DIR = "/Users/lucas/Work/09.Antigravity/视频生成/20260518_org_slowdown/assets"
WORKPLACE_BGM = "/Users/lucas/Work/09.Antigravity/视频生成/20260516_busy_vs_results/assets/bgm.mp3"

def is_valid_video(file_path):
    if not os.path.exists(file_path):
        return False
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1", file_path
    ]
    env = os.environ.copy()
    env["PATH"] = "/Users/lucas/Work/09.Antigravity/视频生成/bin:" + env.get("PATH", "")
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    return result.returncode == 0

def download_file(url, output_path):
    print(f"📥 正在下载: {url} -> {output_path}")
    # 增加 curl --retry 5 --retry-delay 3 增强网络容错率
    cmd = [
        "curl", "-L", "-k",
        "--retry", "5", "--retry-delay", "3",
        "-H", "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "-o", output_path,
        url
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"✅ 下载成功: {output_path}")
        return True
    else:
        # 如果 curl 报错（例如最后的 SSL Syscall 报错），但文件已经完整下载且是一个有效视频，我们依然认为成功！
        if is_valid_video(output_path):
            print(f"⚠️ 下载过程中出现非致命网络波动，但视频文件校验完整。继续处理: {output_path}")
            return True
        print(f"❌ 下载失败: {result.stderr.decode('utf-8')}")
        return False

def process_video(input_path, output_path, is_vertical):
    print(f"🎬 正在使用 FFmpeg 处理视频: {input_path} -> {output_path}")
    
    if is_vertical:
        filter_str = "scale=1080:1920"
    else:
        filter_str = "crop=ih*9/16:ih,scale=1080:1920"
        
    cmd = [
        "ffmpeg", "-i", input_path,
        "-vf", filter_str,
        "-t", "20",
        "-c:v", "libx264", "-crf", "18",
        "-an",
        output_path,
        "-y"
    ]
    
    env = os.environ.copy()
    env["PATH"] = "/Users/lucas/Work/09.Antigravity/视频生成/bin:" + env.get("PATH", "")
    
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    if result.returncode == 0:
        print(f"✅ 处理完成: {output_path}")
        return True
    else:
        print(f"❌ FFmpeg 处理失败: {result.stderr.decode('utf-8')}")
        return False

def main():
    if not os.path.exists(ASSETS_DIR):
        os.makedirs(ASSETS_DIR)
        
    # 1. 复制 BGM
    dest_bgm = os.path.join(ASSETS_DIR, "bgm.mp3")
    if os.path.exists(WORKPLACE_BGM):
        print(f"🎵 正在从职场效能项目复制 BGM: {WORKPLACE_BGM} -> {dest_bgm}")
        shutil.copy(WORKPLACE_BGM, dest_bgm)
        print("✅ BGM 复制成功！")
    else:
        print("⚠️ 未找到职场效能项目的 BGM，请检查路径。")
        
    # 2. 下载并处理每个视频
    for filename, info in VIDEO_MAP.items():
        raw_path = os.path.join(ASSETS_DIR, f"raw_{filename}")
        final_path = os.path.join(ASSETS_DIR, filename)
        
        # 2.1 检查最终视频是否已经处理完成且有效
        if is_valid_video(final_path):
            print(f"⏭️ 视频已存在且校验完整，跳过: {final_path}")
            continue
            
        # 2.2 检查临时下载的原片是否已存在且有效（断点续传）
        need_download = True
        if is_valid_video(raw_path):
            print(f"📂 发现已下载完成的原片临时文件，直接处理: {raw_path}")
            need_download = False
            
        # 2.3 执行下载
        download_success = True
        if need_download:
            download_success = download_file(info["url"], raw_path)
            
        # 2.4 执行处理
        if download_success:
            if process_video(raw_path, final_path, info["is_vertical"]):
                if os.path.exists(raw_path):
                    os.remove(raw_path)
                    print(f"🧹 已删除临时文件: {raw_path}")
            else:
                print(f"❌ 视频处理失败: {filename}")
        else:
            print(f"❌ 视频下载失败: {filename}")
            
    print("\n🎉 所有素材自动化处理流程完成！")

if __name__ == "__main__":
    main()
