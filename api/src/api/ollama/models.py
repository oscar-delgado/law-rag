from pydantic import BaseModel


class CreateModelRequest(BaseModel):
    model_name: str
