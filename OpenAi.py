## this is for the ai portion of the project.
from openai import OpenAI
from config import *
client = OpenAI(
    api_key=aiKey
)
prompt = "Troubled Boeing signals it may raise up to $25 billion to shore up finances"
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a program with the sole intention of maximizing shareholder value"},
        {
            "role": "user",
            "content": "give me a rating from 1-100 (100 being the best) from the view of the shareholders with this news title "+prompt+"you answer should be in the form ""my answer is" "followed by your number."
        }
    ]
)

print(completion.choices[0].message)