from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
client = OpenAI()

# Read the course comments from the file using relative path
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'classification.txt')

with open(file_path, 'r') as file:
    course_classification = file.read().strip()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": f"classify the sentiment in the two statements and then provide a summary count for each classfication {course_classification}"     
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