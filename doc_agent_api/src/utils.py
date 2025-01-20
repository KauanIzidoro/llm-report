import re 
import os 
from settings import SETTINGS
import time
import google.generativeai as genai


def validate_input(text_prompt: str):
    """_summary_
    Args:
        text_prompt (str): texto que seja usado como prompt para interagir com o modelo.

    Raises:
        Exception: Prompts que forem caminhos de arquivos ou imagens não são permitidos.

    Returns:
        str: prompt se for válido.
    """
    if re.search(os.sep, text_prompt) or re.search(r"\.(png|svg|jpg)$", text_prompt):
        raise Exception("O prompt deve ser texto!")
    return text_prompt


        
    