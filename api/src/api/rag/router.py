from fastapi import APIRouter

from src.api.rag.models import QuestionRequest
from src.domain.rag import rag_chain

router = APIRouter()


@router.post("/question", tags=["RAG"])
def write_question(request: QuestionRequest):
    return rag_chain.invoke(request.question)
