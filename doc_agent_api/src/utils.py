import os
from schemas import ModelInputPydantic, ModelOutputDTO
import google.generativeai as genai

from settings import SETTINGS


def validate_input(prompt: str, context_path: str = SETTINGS.PROJECT_PATH, model_output_path: str = SETTINGS.OUTPUT_PATH) -> ModelInputPydantic:
    
    if os.path.exists(context_path) and os.path.exists(model_output_path):
        try: 
            with open(context_path, 'r', encoding='utf-8') as c:
                context = c.read()
            
                
            if context == '' or prompt == '':
                return {'Error': 'Arquivo de contexto está vazio.'}
            
            user_prompt = ModelInputPydantic(
                context_path=context_path,
                output_path=model_output_path,
                prompt=f'{prompt}\n\n{context}'
            )
            return user_prompt
        except Exception as e: 
            return {'Error': f'Erro ao validar entrada: {e}'}
    
    

def chat_to_model(model_input: ModelInputPydantic) -> ModelOutputDTO:
    """<>
    """
    try: 
        genai.configure(api_key=SETTINGS.GOOGLE_API_KEY)
        model = genai.GenerativeModel(SETTINGS.MODEL)
        response = model.generate_content(
            model_input.prompt, 
            generation_config=genai.GenerationConfig(
                response_mime_type='application/json', response_schema=ModelOutputDTO
            ),
        )
        with open(model_input.output_path, 'a', encoding='utf-8') as f: 
            f.write(str(response))
        return response.text
    except Exception as e: 
        return {'Error': f'Erro ao validar entrada: {e}'}
    