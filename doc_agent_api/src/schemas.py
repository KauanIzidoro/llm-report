from pydantic import BaseModel


class ModelInput(BaseModel):
    context_path: str
    output_path: str
    prompt: str


class ModelOutput(BaseModel):
    input_path: str
    diagram_text: str
    datetime: str
    http_status: int
    message: str
