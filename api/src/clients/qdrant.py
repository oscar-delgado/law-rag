from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore

from src.settings import settings
from src.domain.embeddings import embeddings
from src.domain.epub_reader import EpubReader

COLLECTION_NAME = "vivienda"
client = QdrantClient(url=settings.qdrant_url)


try:
    vectorstore = QdrantVectorStore(
        collection_name=COLLECTION_NAME,
        embedding=embeddings,
        client=client,
    )
except Exception:
    reader = EpubReader()
    vectorstore = QdrantVectorStore.from_documents(
        reader.read(),
        embedding=embeddings,
        url=settings.qdrant_url,
        collection_name=COLLECTION_NAME,
    )

retriever = vectorstore.as_retriever(search_kwargs={"k": 100})
