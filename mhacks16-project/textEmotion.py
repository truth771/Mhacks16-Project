import asyncio
import speech_to_text

from hume import HumeStreamClient, TranscriptionConfig
from hume.models.config import LanguageConfig
samples=[]
def speechtext():
    transcript = speech_to_text.speech_to_text("harvard.wav")
    samples = [
        transcript
    ]
    main()


async def main():
    client = HumeStreamClient("uz60UCRzGzUlXef4s1kQa9ErZjqIP2JUy5da7BFqDzE1gKa0")
    config = LanguageConfig()
    async with client.connect([config]) as socket:
        for sample in samples:
            result = await socket.send_text(sample)
            emotions = result["language"]["predictions"][0]["emotions"]
            print(emotions)

asyncio.run(main())
speechtext()