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
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "classify the sentiment in the two statements"
              "Good, i like the way the course designed. It is a quick recap of all the java concepts.thanks"
              "The quizzes can be better"
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

for choice in response.choices:
  print(choice.message.content)