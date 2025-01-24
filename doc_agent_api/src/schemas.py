from pydantic import BaseModel
import typing_extensions as typing

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
    
class ModelPrompt(typing.TypedDict):
    context_path: str
    output_path: str 
    prompt: str 
    
    
class ModelOutput(typing.TypedDict):
    input_path: str
    diagram_text: str
    datetime: str
    http_status: int
    message: str
