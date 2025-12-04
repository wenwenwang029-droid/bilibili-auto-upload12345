import os
import requests
import json

# GitHub Actions 会用 Secrets 传入你的 B站信息
SESSDATA = os.environ["BILI_SESSDATA"]
BILI_JCT = os.environ["BILI_JCT"]

headers = {
    "Cookie": f"SESSDATA={SESSDATA}; bili_jct={BILI_JCT}",
    "User-Agent": "Mozilla/5.0"
}

UPLOAD_FOLDER = "C:\\Users\\Administrator\\iCloudDrive\\BiliAutoUpload"
def upload_video(file_path):
    print(f"开始上传: {file_path}")
    # 这里是伪示例，B站上传接口复杂，需要使用官方 API 或第三方库
    print("上传成功（示例）")

def main():
    files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith(".mp4")]
    for f in files:
        path = os.path.join(UPLOAD_FOLDER, f)
        upload_video(path)

if __name__ == "__main__":
    main()
