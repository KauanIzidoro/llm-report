import os
import re
import time

import google.generativeai as genai

from settings import SETTINGS


def mock_chat_to_model(
    prompt: str,
    context=SETTINGS.PROJECT_PATH,
    model_output=SETTINGS.OUTPUT_PATH,
):
    """Gera um prompt para o modelo, utilizando um contexto de um arquivo de texto e o prompt fornecido.

    Args:
        prompt (str): O texto do prompt a ser enviado ao modelo.
        context (str, optional): O caminho do arquivo que contém o contexto. Padrão é `SETTINGS.PROJECT_PATH`.
        model_output (str, optional): O caminho do arquivo onde a resposta do modelo será gravada. Padrão é `SETTINGS.OUTPUT_PATH`.

    Returns:
        str: O prompt combinado com o contexto.
    """
    try:
        with open(context, 'r', encoding='utf-8') as c:
            context_text = c.read()

        context_prompt = f'{context_text}\n\n{prompt}'
        with open(model_output, 'a', encoding='utf-8') as f:
            f.write(f'{time.ctime}\n{context_prompt}\n\n')

        return context_prompt
    except Exception as e:
        print(f'Erro ao gerar resposta: {e}')
        return None


def receive_input(prompt: str, input_file=SETTINGS.INPUT_PATH):
    """Recebe um prompt de entrada e grava no arquivo especificado.

    Args:
        prompt (str): O texto do prompt a ser gravado.
        input_file (str, optional): O caminho do arquivo onde o prompt será gravado. Padrão é `SETTINGS.INPUT_PATH`.

    Returns:
        str: O texto do prompt gravado no arquivo.
    """
    try:
        with open(input_file, 'a', encoding='utf-8') as f:
            f.write(f'{prompt}\n\n')

        return prompt
    except Exception as e:
        print(f'Erro ao gerar resposta: {e}')
        return None


def chat_to_model_rest(
    input_file=SETTINGS.INPUT_PATH,
    model_output=SETTINGS.OUTPUT_PATH,
    context=SETTINGS.PROJECT_PATH,
):
    """Interage com o modelo usando uma API REST, lendo um prompt e contexto de arquivos e gravando a resposta gerada.

    Args:
        input_file (str, optional): O caminho do arquivo que contém o prompt de entrada. Padrão é `SETTINGS.INPUT_PATH`.
        model_output (str, optional): O caminho do arquivo onde a resposta do modelo será gravada. Padrão é `SETTINGS.OUTPUT_PATH`.
        context (str, optional): O caminho do arquivo que contém o contexto. Padrão é `SETTINGS.PROJECT_PATH`.

    Returns:
        str: O contexto combinado com o prompt.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            prompt = f.read()

        with open(context, 'r', encoding='utf-8') as c:
            context_text = c.read()

        context_prompt = f'{prompt}\n\n{context_text}'

        with open(model_output, 'a', encoding='utf-8') as m:
            m.write(f'{time.ctime}\n{context_prompt}\n\n')

        return context_prompt
    except Exception as e:
        print(f'Erro: {e}')
        return None


def chat_to_model(
    prompt: str,
    context=SETTINGS.PROJECT_PATH,
    model_output=SETTINGS.OUTPUT_PATH,
):
    """Envia um prompt para o modelo de IA e grava a resposta gerada em um arquivo.

    Args:
        prompt (str): O texto do prompt a ser enviado ao modelo.
        context (str, optional): O caminho do arquivo que contém o contexto. Padrão é `SETTINGS.PROJECT_PATH`.
        model_output (str, optional): O caminho do arquivo onde a resposta do modelo será gravada. Padrão é `SETTINGS.OUTPUT_PATH`.

    Returns:
        str: A resposta gerada pelo modelo.
    """
    try:
        with open(context, 'r', encoding='utf-8') as c:
            context_text = c.read()

        context_prompt = f'{context_text}\n\n{prompt}'

        genai.configure(api_key=SETTINGS.GOOGLE_API_KEY)
        model = genai.GenerationModel(
            model_name=SETTINGS.MODEL,
            system_instruction=SETTINGS.SYSTEM_INSTRUCTION,
        )
        response = model.generate_content([context_prompt])
        output = f'{time.acstime}\n\n{response.text}\n\n'

        with open(model_output, 'w', encoding='utf-8') as file:
            file.write(output)

        return output
    except Exception as e:
        print(f'Erro ao gerar resposta: {e}')
        return None
