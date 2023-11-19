import speech_to_text
import gpt

def main():
    transcript = speech_to_text.speech_to_text("harvard.wav")
    question = ""
    gpt_analysis = gpt.gpt_response(question, transcript)
    

if(__name__ == "__main__"):
    main()