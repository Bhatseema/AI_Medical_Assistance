from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

class GroqLLM:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate(self, prompt):
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",   # fast + free model
            messages=[
                {"role": "system", "content": "You are a helpful medical assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=512
        )

        return response.choices[0].message.content