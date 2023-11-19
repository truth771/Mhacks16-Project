from google.cloud import speech
from pathlib import Path
from pydub import AudioSegment

def speech_to_text(filename):
    client = speech.SpeechClient.from_service_account_file('/Users/truth/Downloads/key.json')

    PROJECT_ROOT = Path(__file__).parent.parent.resolve()
    RESOURCES_ROOT = PROJECT_ROOT / "resources"

    harvard_path = str(RESOURCES_ROOT / filename)

    stereo_audio = AudioSegment.from_file(harvard_path)
    mono_audio = stereo_audio.set_channels(1)
    mono_audio.export(str(RESOURCES_ROOT / "mono.wav"), format="wav")

    harvard_path = str(RESOURCES_ROOT / "mono.wav")

    with open(harvard_path, 'rb') as f:
        data = f.read()

    audio_file = speech.RecognitionAudio(content=data)

    config = speech.RecognitionConfig(
        sample_rate_hertz=44100,
        enable_automatic_punctuation=True,
        language_code='en_US'
    )

    response = client.recognize(
        config=config,
        audio=audio_file
    )

    for result in response.results:
        return result.alternatives[0].transcript