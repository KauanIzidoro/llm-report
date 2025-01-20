from fastapi import APIRouter
from utils import validate_input, mock_chat_to_model
router = APIRouter()

@router.post('/input')
def prompt(text_prompt: str):
    prompt = validate_input(text_prompt=text_prompt)
    return mock_chat_to_model(prompt=prompt)
    