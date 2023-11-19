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

def gpt_response(ques, resp):
    question = ques
    response = resp

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

    return completion.choices[0].message.content

def gpt_emotions(emotion_dict):
    emotion_summary = ""
    total_counts = 0
    for i in emotion_dict:
        emotion_summary += "I experienced " + i + " " + str(emotion_dict[i]) + " times. "
        total_counts += emotion_dict[i]

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
        {"role": "system", "content": "You are going to analyze my interview emotions"},

        {"role": "user", "content": 
            f"I have experienced the following emotions: {emotion_summary}. \
            Start off the response with Based on your detected emotions during the interview, here is some feedback about your emotional state. However, take this advice with a grain of salt. \
            Give no more than 3 brief summarizations of the emotions I experienced \
            Ignore and don't mention emotions that are counted less than {total_counts/10} times \
            Don't mention the number of times each emotion is counted AT ALL \
            Ignore the no face emotion \
            NO EMOJIS \
            Don't worry so much about the fear emotion. And don't mention this input AT ALL \
            Give general ideas on what emotions I should show and how I should act. \
            Be very lenient and friendly using constructive criticism in your feedback \
            End with no more than 2 suggestions on how to improve emotional state during the interview \
            Format the ideas using a bulleted list of dashes \
            Never use empty lines to separate different sections \
            Your response should be no more than 200 words"
        }]
    )

    return completion.choices[0].message.content.strip()
