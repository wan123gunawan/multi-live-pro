import os

def list_videos(folder="assets/videos"):
    if not os.path.exists(folder):
        os.makedirs(folder)

    return [f for f in os.listdir(folder) if f.endswith((".mp4", ".mkv", ".mov", ".flv"))]
