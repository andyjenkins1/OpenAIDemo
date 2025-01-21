from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
      {"role": "system", "content": "You are a Python Tutor"},
      {"role": "user", "content": "explain what the sum() function does in Python"},
      {"role": "assistant", "content": "The sum() function returns the numbers in a list"},
      {"role": "user", "content": "explain what the len() function does in Python"},
  ],
  response_format={
    "type": "text"
  },
  # n=3,
  max_completion_tokens=2048,
)

for choice in response.choices:
  print(choice.message.content)