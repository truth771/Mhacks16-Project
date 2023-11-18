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

question = "Tell me about yourself."
response = "I’m currently an account executive at Smith, where I handle our top-performing client. Before that, I worked at an agency where I was on three different major national healthcare brands. And while I really enjoyed the work that I did, I’d love the chance to dig in much deeper with one specific healthcare company, which is why I’m so excited about this opportunity with Metro Health Center."

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
    {"role": "system", "content": "You are interviewer for a prestigious company"},

    {"role": "user", "content": 
        f"I am answering the question: {question}. \
        Please let me know how I can improve my answer in the following way. \
        If there are no major issues, just say: That looks good! and do not give recomendations. \
        Be very lenient. \
        If and only if there is a major issue, then do the following. \
        Give general ideas on what to add and support the ideas with examples. \
        Format the ideas using numbers. \
        Then give a completed example of a response with all the ideas incorporated. \
        My response is below. \n {response}"
    }]
)

print(completion.choices[0].message.content)
