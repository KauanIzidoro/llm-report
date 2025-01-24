from pydantic import BaseModel

class ModelInputPydantic(BaseModel):
    context_path: str
    output_path: str
    prompt: str


class ModelOutputPydantic(BaseModel):
    input_path: str
    model_response: str
    datetime: str
    http_status: int
    message: str
