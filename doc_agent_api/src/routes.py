from fastapi import APIRouter
from utils import validate_input
router = APIRouter()

@router.post('/input')
def prompt(text_prompt: str):
    return validate_input(text_prompt)
    