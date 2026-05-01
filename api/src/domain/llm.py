from langchain_openai import AzureChatOpenAI
from langchain_ollama import ChatOllama

from src.settings import settings

if settings.use_local_llm:
    llm = ChatOllama(
        base_url=settings.ollama_url,
        model=settings.ollama_model,
        temperature=0.0,
    )
else:
    llm = AzureChatOpenAI(
        api_version=settings.azure_openai_api_version,
        azure_endpoint=settings.azure_openai_endpoint,
        deployment_name=settings.azure_openai_llm_model,
        temperature=0.0,
    )
