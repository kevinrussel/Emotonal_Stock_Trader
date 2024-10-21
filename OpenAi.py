## this is for the ai portion of the project.
from openai import OpenAI
from config import *
client = OpenAI(
    api_key=aiKey
)

def OpenAiPrompt(newsprompt):

    prompt = newsprompt
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a program with the sole intention of maximizing your stock portfolio. That means buying stocks when they are good, and selling stocks when they are bad."},
            {
                "role": "user",
                "content": "give me a rating from 1-100 (100 being the best) from the view of the shareholders with this news title "+prompt+"you answer should be just a number"
            }
        ]
    )

    return(completion.choices[0].message)