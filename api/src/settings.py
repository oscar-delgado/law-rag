from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    name: str = "Law RAG"

    use_local_emb: bool = False
    use_local_llm: bool = False

    hugging_face_emb_model: str = "all-MiniLM-L6-v2"

    azure_openai_api_version: str = "2024-12-01-preview"
    azure_openai_endpoint: str = "https://azoai-02.openai.azure.com/"
    azure_openai_emb_model: str = "text-embedding-3-small"
    azure_openai_llm_model: str = "gpt-4.1-mini"

    ollama_url: str = ""
    ollama_model: str = "qwen3.5:0.8b"

    qdrant_url: str = ""


settings = Settings()
