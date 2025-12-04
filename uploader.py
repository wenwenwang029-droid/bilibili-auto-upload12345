import os
from biliup import uploader  # GitHub Actions 会自动安装

# GitHub Actions 会用 Secrets 传入 B站 Cookie
SESSDATA = os.environ["BILI_SESSDATA"]
BILI_JCT = os.environ["BILI_JCT"]

# Windows iCloud 同步文件夹（原始字符串写法）
UPLOAD_FOLDER = r"C:\Users\Administrator\iCloudDrive\BiliAutoUpload"
UPLOADED_FOLDER = os.path.join(UPLOAD_FOLDER, "uploaded")

# 创建 uploaded 文件夹，如果不存在
if not os.path.exists(UPLOADED_FOLDER):
    os.makedirs(UPLOADED_FOLDER)

# 遍历所有 mp4 文件
for f in os.listdir(UPLOAD_FOLDER):
    if not f.endswith(".mp4"):
        continue
    filepath = os.path.join(UPLOAD_FOLDER, f)
    
    # 自动生成标题、简介
    title = f"雯雯上传 - {os.path.splitext(f)[0]}"
    desc = f"自动上传视频：{f}"
    tid = 5  # 上传到“娱乐”分区，可修改

    print(f"开始上传: {filepath}")
    
    try:
        uploader.upload_video(
            filename=filepath,
            title=title,
            desc=desc,
            tid=tid,
            sessdata=SESSDATA,
            bili_jct=BILI_JCT
        )
        print("上传成功")

        # 上传成功后移动到 uploaded 文件夹
        os.rename(filepath, os.path.join(UPLOADED_FOLDER, f))
    except Exception as e:
        print(f"上传失败: {e}")
