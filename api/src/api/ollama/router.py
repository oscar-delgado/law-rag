from fastapi import APIRouter

from src.api.ollama.models import CreateModelRequest
from src.clients.ollama import client

router = APIRouter()


@router.get("/available_models")
def list_available_models():
    return client.list()


@router.post("/models")
def write_model(model_name: CreateModelRequest):
    return client.pull(model_name)


@router.delete("/models/{model_name}")
def delete_model(model_name: str):
    return client.delete(model_name)
