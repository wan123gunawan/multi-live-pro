import streamlit as st
from processor import process_videos
import os

os.makedirs(os.path.dirname(wm1_path), exist_ok=True)
st.set_page_config(page_title="Video Watermark Pro", layout="centered")

st.title("🎬 Video Watermark Pro")

st.write("Upload video + 2 watermark, lalu proses batch otomatis.")

videos = st.file_uploader(
    "Upload Videos",
    type=["mp4"],
    accept_multiple_files=True
)

wm1 = st.file_uploader("Watermark 1 (PNG)", type=["png"])
wm2 = st.file_uploader("Watermark 2 (PNG)", type=["png"])

if st.button("🚀 Start Processing"):

    if not videos or not wm1 or not wm2:
        st.error("Lengkapi upload dulu!")
    else:
        output_files = process_videos(videos, wm1, wm2, st)

        st.success("Selesai!")

        st.write("### 📥 Download hasil")

        for file in output_files:
            with open(file, "rb") as f:
                st.download_button(
                    label=f"Download {file}",
                    data=f,
                    file_name=file,
                    mime="video/mp4"
                )
