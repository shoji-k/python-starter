import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)
model = "gpt-3.5-turbo"

stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Give me a number out of 10"}],
    stream=True,
    temperature=0,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
