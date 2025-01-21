from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
client = OpenAI()

# Read the companies from the file using relative path
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'companies.txt')

with open(file_path, 'r') as file:
    companies_text = file.read().strip()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": f"Categorize the following companies: {companies_text}"
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