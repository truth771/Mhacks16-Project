import asyncio
import speech_to_text
import os
import ssl
print(ssl.OPENSSL_VERSION)

from dotenv import load_dotenv
from hume import HumeStreamClient, TranscriptionConfig
from hume.models.config import LanguageConfig

load_dotenv()
transcript = speech_to_text.speech_to_text("harvard.wav")
samples = [
    transcript
]

async def main():
    API_KEY = os.environ["API_KEY2"]
    client = HumeStreamClient(API_KEY)
    config = LanguageConfig()
    async with client.connect([config]) as socket:
        for sample in samples:
            result = await socket.send_text(sample)
            emotions = result["language"]["predictions"][0]["emotions"]
            print(emotions)

asyncio.run(main())
