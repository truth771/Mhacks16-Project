import speech_to_text
import gpt
import emotion
import logging
from moviepy.editor import VideoFileClip

logging.getLogger('moviepy').setLevel(logging.CRITICAL)

def main():
    question = input("Enter an interview question: ")
    video_filename = input("Enter a video of you answering that question: ")
    print()

    video = VideoFileClip(video_filename)
    audio = video.audio
    audio.write_audiofile('audio.wav',logger=None)

    transcript = speech_to_text.speech_to_text("/Users/truth/Mhacks16-Project/audio.wav")

    gpt_analysis = gpt.gpt_response(question, transcript)
    print(gpt_analysis)
    print("\n")

    emotion_dict = emotion.emotion_detection(video_filename)
    print(gpt.gpt_emotions(emotion_dict))

    

if(__name__ == "__main__"):
    main()