from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
client = OpenAI()

response = client.moderations.create(
    model="text-moderation-latest",
 #   input="My favourtie movie is Kill Bill"
    input="Not in a good place, want to harm myself"
)

# print(response)
print(response.results[0].flagged)
print(response.results[0].category_scores)
print(response.results[0].category_scores.self_harm)