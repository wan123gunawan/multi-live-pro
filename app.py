import streamlit as st
from core.streamer import MultiStreamer
from utils.logger import log
from utils.file_manager import list_videos

from platforms.facebook import get_url as fb_url
from platforms.youtube import get_url as yt_url
from platforms.tiktok import get_url as tt_url

st.title("🌍 Multi Platform Live Streaming PRO")

if "logs" not in st.session_state:
    st.session_state.logs = []

if "streamer" not in st.session_state:
    st.session_state.streamer = MultiStreamer()

# VIDEO
videos = list_videos()
video_path = None

if videos:
    selected = st.selectbox("🎥 Video", videos)
    video_path = f"assets/videos/{selected}"

# PLATFORM INPUT
st.subheader("🔗 Platform Setup")

use_fb = st.checkbox("Facebook")
fb_key = st.text_input("FB Key")

use_yt = st.checkbox("YouTube")
yt_key = st.text_input("YT Key")

use_tt = st.checkbox("TikTok")
tt_key = st.text_input("TT Key")

# BUILD OUTPUTS
outputs = []

if use_fb and fb_key:
    outputs.append(fb_url(fb_key))

if use_yt and yt_key:
    outputs.append(yt_url(yt_key))

if use_tt and tt_key:
    outputs.append(tt_url(tt_key))

# CTA
cta1 = st.file_uploader("CTA 1")
cta2 = st.file_uploader("CTA 2")

cta1_path, cta2_path = None, None

if cta1:
    cta1_path = f"assets/cta/{cta1.name}"
    with open(cta1_path, "wb") as f:
        f.write(cta1.read())

if cta2:
    cta2_path = f"assets/cta/{cta2.name}"
    with open(cta2_path, "wb") as f:
        f.write(cta2.read())

# START
if st.button("🚀 START MULTI STREAM"):
    if not video_path or not outputs:
        st.error("Video & platform wajib")
    else:
        def cb(msg):
            log(msg, st.session_state.logs)

        st.session_state.streamer.start(
            video_path,
            outputs,
            cb,
            cta1_path,
            cta2_path,
            "top-right",
            "bottom-left"
        )
        st.success("Streaming ke semua platform!")

# STOP
if st.button("⏹️ STOP"):
    st.session_state.streamer.stop()

# LOGS
st.text_area("Logs", "\n".join(st.session_state.logs[-50:]), height=300)
