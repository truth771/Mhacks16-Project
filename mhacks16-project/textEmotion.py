import asyncio

from hume import HumeStreamClient
from hume.models.config import LanguageConfig

samples = [
   
]

async def main():
    client = HumeStreamClient("uz60UCRzGzUlXef4s1kQa9ErZjqIP2JUy5da7BFqDzE1gKa0")
    config = LanguageConfig()
    async with client.connect([config]) as socket:
        for sample in samples:
            result = await socket.send_text(sample)
            emotions = result["language"]["predictions"][0]["emotions"]
            print(emotions)

asyncio.run(main())