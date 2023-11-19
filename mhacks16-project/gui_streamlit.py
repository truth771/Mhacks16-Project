import streamlit as st
import pandas as pd
import speech_to_text
import gpt
import emotion
import time
import logging
from moviepy.editor import VideoFileClip

logging.getLogger('moviepy').setLevel(logging.CRITICAL)
st.title("Interview.prep()")

video_filename = st.file_uploader("Choose a video file")

if video_filename is not None:
    video_bytes = video_filename.read()
    new_file = '/Users/truth/MHacks16-Project/mhacks16-project/videos/uploadedInterview.mp4'
    with open('/Users/truth/MHacks16-Project/mhacks16-project/videos/uploadedInterview.mp4', 'wb') as out:
        out.write(video_bytes)
    st.video(video_filename)
    question = st.text_input("Enter the interview question: ")
    while not question:
        continue
    st.write("Processing the response (~1 min)...")

    video = VideoFileClip(new_file)  # Now you should be able to use this with moviepy
    audio = video.audio
    audio.write_audiofile('audio.wav',logger=None)

    transcript = speech_to_text.speech_to_text("/Users/truth/Mhacks16-Project/audio.wav")

    st.write(gpt.gpt_response(question, transcript))
    st.write("\n")
    st.write("Processing the emotions (~2-5 min)...")

    emotion_dict = emotion.emotion_detection(new_file)
    emotions_output = gpt.gpt_emotions(emotion_dict)
    st.write(emotions_output)

    time.sleep(5)
    st.subheader("Feel free to upload more clips for feedback!")
