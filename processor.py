import os
import subprocess

def process_videos(videos, wm1, wm2, st):

    os.makedirs("input", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    wm1_path = "assets/wm1.png"
    wm2_path = "assets/wm2.png"

    # save watermark
    with open(wm1_path, "wb") as f:
        f.write(wm1.read())

    with open(wm2_path, "wb") as f:
        f.write(wm2.read())

    output_files = []
    total = len(videos)

    progress = st.progress(0)
    status = st.empty()

    for i, video in enumerate(videos):

        input_path = f"input/video_{i}.mp4"
        output_path = f"output/output_{i}.mp4"

        with open(input_path, "wb") as f:
            f.write(video.read())

        # 🎯 FFmpeg with 2 moving watermarks
        cmd = f"""
        ffmpeg -y -i "{input_path}" -i "{wm1_path}" -i "{wm2_path}" -filter_complex "
        [1:v]scale=iw*0.10:-1[wm1];
        [2:v]scale=iw*0.08:-1[wm2];

        [0:v][wm1]overlay=x='mod(t*80,W)':y='mod(t*40,H)'[tmp];
        [tmp][wm2]overlay=x='W-mod(t*60,W)':y='H-mod(t*30,H)'
        " "{output_path}"
        """

        subprocess.run(cmd, shell=True)

        output_files.append(output_path)

        progress.progress((i + 1) / total)
        status.text(f"Processing {i+1}/{total}")

    return output_files
