import os
from schemas import ModelInputPydantic, ModelOutputDTO
import google.generativeai as genai
from fastapi import UploadFile, HTTPException
from settings import SETTINGS


def validate_input(prompt: str, context_path: str = SETTINGS.PROJECT_PATH, model_output_path: str = SETTINGS.OUTPUT_PATH) -> ModelInputPydantic:
    
    if os.path.exists(context_path) and os.path.exists(model_output_path):
        try: 
            with open(context_path, 'r', encoding='utf-8') as c:
                context = c.read()
            
            if context == '' or prompt == '':
                return {'Error': 'Context file is empty.'}
            
            user_prompt = ModelInputPydantic(
                context_path=context_path,
                output_path=model_output_path,
                prompt=f'{prompt}\n\n{context}'
            )
            return user_prompt
        except Exception as e: 
            return {'Error': f'Error validating input: {e}'}
    
    

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
            f.write(str(response.text))
        return response.text
    except Exception as e: 
        return {'Error': f'Error validating input: {e}'}
    
# def store_file(file: UploadFile, file_path=SETTINGS.FILE_PATH):
#     """<>
#     """
#     file_type = file.filename.split('.')[-1].lower()
#     if file_type in ['.png', '.jpg']:
#         raise HTTPException(status_code=400, detail='Only text files will be supported.')
    
#     os.makedirs(file_path, exist_ok=True)
#     with open(os.path.join(file_path, file.filename), 'a', encoding='utf-8') as f:
#         f.write(str(file.read()))
#         return {'Message': 'File saved successfully.'}
    
async def store_file(file: UploadFile, file_path: str = SETTINGS.FILE_PATH):
    """
    Salva o arquivo recebido no diretório especificado.
    Apenas arquivos de texto são permitidos.
    """
    # Verifica a extensão do arquivo
    file_type = file.filename.split('.')[-1].lower()
    if file_type in ['png', 'jpg', 'jpeg']:
        raise HTTPException(status_code=400, detail='Apenas arquivos de texto são permitidos.')

    # Cria o diretório se não existir
    os.makedirs(file_path, exist_ok=True)

    # Define o caminho completo para salvar o arquivo
    full_path = os.path.join(file_path, file.filename)

    # Salva o arquivo
    try:
        # Lê o conteúdo do arquivo
        content = await file.read()

        # Se for um arquivo de texto, decodifica o conteúdo
        if file_type in ['txt', 'csv', 'log']:  # Adicione outras extensões de texto, se necessário
            content = content.decode('utf-8')
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            # Para outros tipos de arquivo (binários), salva diretamente
            with open(full_path, 'wb') as f:
                f.write(content)

        return {'Message': f'Arquivo "{file.filename}" salvo com sucesso em "{file_path}".'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao salvar o arquivo: {str(e)}')