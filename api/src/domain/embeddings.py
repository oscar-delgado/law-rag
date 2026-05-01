import os

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import AzureOpenAIEmbeddings

from src.settings import settings

if settings.use_local_emb:
    local_emb_model_path = "models/embeddings"
    if os.path.exists(local_emb_model_path):
        embeddings = HuggingFaceEmbeddings(model_name=local_emb_model_path)
    else:
        embeddings = HuggingFaceEmbeddings(model_name=settings.hugging_face_emb_model)
        embeddings.client.save(local_emb_model_path)
else:
    embeddings = AzureOpenAIEmbeddings(
        azure_endpoint=settings.azure_openai_endpoint,
        model=settings.azure_openai_emb_model,
    )
