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
          "text": "You are an AI Tutor"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is OpenAI?"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "OpenAI is an artificial intelligence research lab and company that aims to ensure that artificial general intelligence (AGI) benefits all of humanity. Founded in December 2015, OpenAI was created with the mission to conduct research in AI and develop it in a safe and transparent manner. It was started as a non-profit organization, but later transitioned to a \"capped-profit\" model with the establishment of OpenAI LP in 2019, which allows them to attract investment while ensuring that returns are capped.\n\nOpenAI is known for developing various advanced AI models, including:\n\n- **GPT (Generative Pre-trained Transformer)**: A series of language models that can generate human-like text. GPT-3 is one of their most well-known models, known for its impressive ability to produce coherent and contextually appropriate responses.\n  \n- **DALL-E**: An AI system capable of generating images from textual descriptions, showcasing creative capabilities in generating visuals.\n\n- **Codex**: A descendant of GPT-3, designed to assist with programming tasks by generating code from natural language prompts.\n\nOpenAI engages in both open research and creating partnerships to promote responsible AI development, actively working on ethical considerations and the long-term impacts of AI on society."
        }
      ]
    }
  ],
  response_format={
    "type": "text"
  },
  temperature=1,
  max_completion_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
print(response.choices[0].message.content)