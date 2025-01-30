from pydantic import BaseModel

class ModelInput(BaseModel):
    prompt: str


class ModelOutput(BaseModel):
    model_answer: str
    mermaid_code: str
    datetime: str
    http_status: int

class ModelOutputDTO(BaseModel):
    model_answer: str
    mermaid_code: str
