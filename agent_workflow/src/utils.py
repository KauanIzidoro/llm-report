import re
import os
from settings import SETTINGS
import google.generativeai as genai


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
    try:
        with open(context, "r", encoding="utf-8") as c:
            context_text = c.read()

        combined_prompt = f"{context_text}\n\n{prompt}"

        genai.configure(api_key=SETTINGS.GOOGLE_API_KEY)
        model = genai.GenerativeModel(model_name=SETTINGS.MODEL, 
                                      system_instruction="Você é um engenheiro de software e seu objetivo é explicar o código-fonte para novos membros da equipe.")

        response = model.generate_content([combined_prompt])
        output = response.text

        with open(model_output, "w", encoding="utf-8") as file:
            file.write(output)

        return output

    except Exception as e:
        print(f"Erro ao gerar a resposta: {e}")
        return None
