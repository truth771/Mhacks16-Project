import speech_to_text
import gpt
import emotion
from moviepy.editor import VideoFileClip

def main():
    question = input("Enter an interview question: ")
    video_filename = input("Enter a video of you answering that question: ")

    video = VideoFileClip(video_filename)
    audio = video.audio
    audio.write_audiofile('audio.wav')

    transcript = speech_to_text.speech_to_text("/Users/truth/Mhacks16-Project/audio.wav")
    gpt_analysis = gpt.gpt_response(question, transcript)
    print(gpt_analysis)

    emotion_dict = emotion.emotion_detection(video_filename)

    for i in emotion_dict:
        print("You experienced " + i + " " + str(emotion_dict[i]) + "  times")

    

if(__name__ == "__main__"):
    main()