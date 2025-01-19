from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "You Are A Cake Baker"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Get me a recipe to make a cake"
        }
      ]
    },
  ],
  response_format={
    "type": "text"
  },
  n=3,
  max_completion_tokens=2048,
)
print(response)

for choice in response.choices:
  print(choice.message.content)