from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
client = OpenAI()

messages = [{"role": "system", "content": "You are a Math Tutor"},]
user_messages = ["explain what Pi is?","summarise this into no more than 3 bullet points"]

for each_msg in user_messages:
    # Create a dictionary for the user message with role and content
    user_dict = {"role": "user", "content": each_msg}
    # Append the user message dictionary to the messages list
    messages.append(user_dict)
    # Send the messages to the OpenAI API and get a response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    # Create a dictionary for the assistant's response
    assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}
    # Append the assistant's response dictionary to the messages list
    messages.append(assistant_dict)
    # Print the content of the assistant's response
    print(response.choices[0].message.content)

  