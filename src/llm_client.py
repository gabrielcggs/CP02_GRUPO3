import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

class LLMClient:

    def __init__(self):

        self.host = os.getenv("OLLAMA_HOST")
        self.model = os.getenv("MODEL_NAME")

    def chat(
        self,
        prompt,
        system="",
        temp=0.5,
        max_tokens=300
    ):

        inicio = time.time()

        url = f"{self.host}/api/chat"

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": system
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False,
            "options": {
                "temperature": temp,
                "num_predict": max_tokens
            }
        }

        response = requests.post(url, json=payload)

        fim = time.time()

        resposta = response.json()["message"]["content"]

        return {
            "resposta": resposta,
            "tokens_prompt": len(prompt.split()),
            "tokens_resposta": len(resposta.split()),
            "tempo_ms": round((fim - inicio) * 1000, 2)
        }