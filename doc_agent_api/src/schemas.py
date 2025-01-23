from pydantic import BaseModel

class ModelOutput(BaseModel):
    input_path: str
    diagram_text: str 
    datetime: str
    http_status: int
    message: str

class ModelInput(BaseModel):
    context_path: str
    output_path: str
    prompt: str