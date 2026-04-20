import threading
from core.ffmpeg_multi import run_multi_stream

class MultiStreamer:
    def __init__(self):
        self.is_streaming = False

    def start(self, video, outputs, log_cb, cta1=None, cta2=None, pos1=None, pos2=None):
        if self.is_streaming:
            return False

        self.is_streaming = True

        threading.Thread(
            target=run_multi_stream,
            args=(video, outputs, log_cb, cta1, cta2, pos1, pos2),
            daemon=True
        ).start()

        return True

    def stop(self):
        import os
        os.system("pkill ffmpeg")
        self.is_streaming = False
