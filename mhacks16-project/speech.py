from pathlib import Path

import speech_recognition as sr


PROJECT_ROOT = Path(__file__).parent.parent.resolve()
RESOURCES_ROOT = PROJECT_ROOT / "resources"

harvard_path = str(RESOURCES_ROOT / "harvard.wav")
r = sr.Recognizer()
harvard = sr.AudioFile(harvard_path)
with harvard as source:
    audio = r.record(source)

type(audio)
r.recognize_google_cloud(audio)
