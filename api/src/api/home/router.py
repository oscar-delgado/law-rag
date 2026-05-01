from fastapi import APIRouter

from src.settings import settings

router = APIRouter()


@router.get("/")
def read_root():
    return {"name": settings.name}
