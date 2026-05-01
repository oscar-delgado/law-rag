from ollama import Client

from src.settings import settings


# Documentation: https://github.com/ollama/ollama-python?tab=readme-ov-file#api
client = Client(host=settings.ollama_url)
