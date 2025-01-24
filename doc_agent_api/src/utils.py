import os
import time
from schemas import ModelInput, ModelOutput
import google.generativeai as genai

from settings import SETTINGS


def validate_input(prompt: str, context_path: str = SETTINGS.PROJECT_PATH, model_output_path: str = SETTINGS.OUTPUT_PATH) -> ModelInput:
    
    if os.path.exists(context_path) and os.path.exists(model_output_path):
        try: 
            with open(context_path, 'r', encoding='utf-8') as c:
                context = c.read()
            
                
            if context == '' or prompt == '':
                return {'Error': 'Arquivo de contexto está vazio.'}
            
            user_prompt = ModelInput(
                context_path=context_path,
                output_path=model_output_path,
                prompt=f'{prompt}\n\n{context}'
            )
            return user_prompt.__dict__
        except Exception as e: 
            return {'Error': f'Erro ao validar entrada: {e}'}
            
            