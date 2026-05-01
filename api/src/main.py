from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.rag.router import router as rag_router
from src.api.ollama.router import router as ollama_router
from src.api.home.router import router as home_router

app = FastAPI()


app.include_router(rag_router, tags=["RAG"])
app.include_router(ollama_router, tags=["Ollama"])
app.include_router(home_router, tags=["Home"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
