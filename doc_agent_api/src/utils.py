import os
import shutil
from datetime import datetime
from typing import Dict, Any
import json
from schemas import ModelInput, ModelOutput, ModelOutputDTO
import google.generativeai as genai
from fastapi import UploadFile, HTTPException
from settings import SETTINGS



def storage_context_file(user_file: UploadFile):
    """_summary_

    Args:
        user_file (UploadFile): File uploaded by the user.

    Returns:
        HTTP Object: Status of the file upload.

    Description:
        Receive files and storage in local memory.
    """
    try:
        if user_file.filename.endswith((".jpeg",".png",".jpg", ".svg")):
            return "unsupported file format"
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
        
    with open(os.path.join(SETTINGS.USER_FILE_PATH, user_file.filename), "wb") as buffer:
        shutil.copyfileobj(user_file.file, buffer)
    return HTTPException(status_code=201, detail="context file created.")

        
def process_user_input(user_input: str) -> ModelInput:
    """Validate and process the user input.

    Args:
        user_input (str): string input from the user.

    Returns:
        ModelInput: Schema of the validated user input.
    
    Description: 
        Validate and process the user input. Each input is saved in a separate JSON file.
    """
    if user_input is None or user_input == '':
        return 'user prompt is empty'
    
    context = ''
    for files in os.listdir(SETTINGS.USER_FILE_PATH):
        file_path = os.path.join(SETTINGS.USER_FILE_PATH, files)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    context += f.read() 
            except UnicodeDecodeError:
                print('error while trying to read files')
    
    validate_prompt = ModelInput(
        prompt=f'{user_input}\n\n{context}'
    )
    
    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    json_filename = f"user_input_{timestamp}.json"
    json_filepath = os.path.join(SETTINGS.USER_INPUT_PATH, json_filename)
    
    data_to_save = {
        'user_input': user_input,
        'context': context,
        'prompt': validate_prompt.prompt,
        'timestamp': timestamp
    }
    
    try:
        with open(json_filepath, "w", encoding='utf-8') as json_file:
            json.dump(data_to_save, json_file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f'error while trying to write JSON file: {e}')
    return validate_prompt

def list_chat_files(directory_path: str) -> list[dict]:
    """_summary_
    """
    json_local_data = []

    for filename in os.listdir(path=directory_path):
            file_path = os.path.join(directory_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    json_local_data.append(data)
            except Exception as e:
                print(f"Error reading file {filename}: {e}")
            return json_local_data
    

# def chat_to_model(input_to_model: ModelInput) -> ModelOutput:
#     """_summary_

#     Args:
#         _input (ModelInput): Schema of the validade user input.

#     Returns:
#         ModelOutput: Schema of the model output.

#     Description:
#         Setup the model and send prompt for Gemini API.
#     """
#     try:
#         genai.configure(api_key=SETTINGS.GOOGLE_API_KEY)
#         model = genai.GenerativeModel(model_name=SETTINGS.MODEL, system_instruction=SETTINGS.SYSTEM_INSTRUCTION)
#         response = model.generate_content(
#             input_to_model.prompt, 
#             generation_config=genai.types.GenerationConfig(
#                 response_mime_type='application/json', 
#                 response_schema=ModelOutputDTO,
#             ),
#         )
#         model_output = ModelOutput(
#             model_answer=json.loads(response.text)['model_answer'],
#             mermaid_code=json.loads(response.text)['mermaid_code'],
#             datetime=datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
#             http_status='200'
#         )
#         with open(SETTINGS.OUTPUT_PATH, 'a') as f:
#             f.write(str({
#                 'model_answer': model_output.model_answer,
#                 'mermaid_code': model_output.mermaid_code,
#                 'datetime': model_output.datetime,
#                 'httP_status': model_output.http_status
#             }))
#         return model_output
#     except Exception as e:
#         print(str(e))

def chat_to_model(input_to_model: ModelInput) -> ModelOutput:
    """_summary_

    Args:
        input_to_model (ModelInput): Schema of the validated user input.

    Returns:
        ModelOutput: Schema of the model output.

    Description:
        Setup the model and send prompt for Gemini API.
    """
    try:
        genai.configure(api_key=SETTINGS.GOOGLE_API_KEY)
        model = genai.GenerativeModel(model_name=SETTINGS.MODEL, system_instruction=SETTINGS.SYSTEM_INSTRUCTION)
        response = model.generate_content(
            input_to_model.prompt, 
            generation_config=genai.types.GenerationConfig(
                response_mime_type='application/json', 
                response_schema=ModelOutputDTO,
            ),
        )
        model_output = ModelOutput(
            model_answer=json.loads(response.text)['model_answer'],
            mermaid_code=json.loads(response.text)['mermaid_code'],
            datetime=datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
            http_status='200'
        )
        timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        json_filename = f"user_input_{timestamp}.json"
        json_filepath = os.path.join(SETTINGS.OUTPUT_PATH, json_filename)

        data_to_save = {
            'model_answer': model_output.model_answer,
            'mermaid_code': model_output.mermaid_code,
            'datetime': model_output.datetime,
            'http_status': model_output.http_status
        }
        with open(json_filepath, 'w', encoding='utf-8') as json_file:
            json.dump(data_to_save, json_file, ensure_ascii=False, indent=4)
    except Exception as e:
            print(f'error while trying to write JSON file: {e}')
    return model_output


    
