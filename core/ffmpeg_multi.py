import subprocess
from core.overlay import get_overlay_filter

def run_multi_stream(video_path, outputs, log_callback, cta1=None, cta2=None, pos1=None, pos2=None):

    overlay = get_overlay_filter(cta1, cta2, pos1, pos2)

    cmd = [
        "ffmpeg",
        "-re",
        "-stream_loop", "-1",
        "-i", video_path,
    ]

    if overlay:
        cmd += ["-vf", overlay]

    # encoding sekali
    cmd += [
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-b:v", "2500k",
        "-c:a", "aac",
        "-b:a", "128k",
    ]

    # MULTI OUTPUT
    for out in outputs:
        cmd += ["-f", "flv", out]

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    for line in process.stdout:
        log_callback(line.strip())

    process.wait()
