import re
import os
from settings import SETTINGS
import google.generativeai as genai
from google.generativeai import caching


def input(prompt: str):
    """_summary_
    Args:
        prompt (str): texto que seja usado como prompt para interagir com o modelo.

    Raises:
        Exception: Prompts que forem caminhos de arquivos ou imagens não são permitidos.

    Returns:
        str: prompt se for válido.
    """
    if re.search(os.sep, prompt) or re.search(r"\.(png|svg|jpg)$", prompt):
        raise Exception("O prompt deve ser texto!")
    return prompt


def chat_to_model(
    prompt: str, context=SETTINGS.PROJECT_PATH, model_output=SETTINGS.OUTPUT_PATH
):
    """_summary_

    Args:
        prompt (str): texto que seja usado como prompt para interagir com o modelo.
        context (optional): Defaults to SETTINGS.PROJECT_PATH.
        model_output (optional): Defaults to SETTINGS.OUTPUT_PATH.
    """
    with open(context, "r") as c:
        context_text = c.read()

    genai.configure(api_key=SETTINGS.GOOGLE_API_KEY)
    cache = caching.CachedContent.create(
        model=SETTINGS.MODEL,
        system_instruction=(
            "You are a software engineer and your goal is to explain the source code to new squad members."
        ),
        contents=context_text,
    )
    model = genai.GenerativeModel.from_cached_content(cached_content=cache)
    try:
        response = model.generate_content([prompt])
        output = response.text
        with open(model_output, "w", encoding="utf-8") as file:
            file.write(output)
    except Exception as e:
        print(f"Erro ao gerar a resposta: {e}")
    return output