from django.conf import settings
from openai import OpenAI


class ContentClient:
    
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def generate(self,prompt,system=None):

        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=messages,
        )   
        return response.choices[0].message.content
    
