import os

from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()
API_KEY = os.environ["API_KEY"]

client = AzureOpenAI(
    api_key=API_KEY,
    azure_endpoint="https://api.umgpt.umich.edu/azure-openai-api/ptu",
    api_version="2023-03-15-preview",
)

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
        },
        {
            "role": "user",
            "content": "Compose a poem that explains the concept of recursion in programming.",
        },
    ],
)

print(completion.choices[0].message.content)
