from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
client = OpenAI()

# Read the companies from the file using relative path
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'code_explain.txt')

with open(file_path, 'r') as file:
    code_explain = file.read().strip()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
     {
      "role": "system",
      "content": "You are a Python Tutor and you should explain the code in more than 3 sentences."
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": f"{code_explain}"
       }
      ]
    },
  ],
  response_format={
    "type": "text"
  },
  # n=3,
  max_completion_tokens=2048,
)

for choice in response.choices:
  print(choice.message.content)