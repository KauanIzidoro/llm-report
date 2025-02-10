from fastapi import APIRouter, WebSocket, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from settings import SETTINGS

from utils import storage_context_file, process_user_input, chat_to_model, list_chat_files

router = APIRouter()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat4Vision</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
                padding: 0;
                background-color: #f4f4f9;
                color: #333;
            }
            h1 {
                color: #444;
            }
            form {
                display: flex;
                gap: 10px; 
                align-items: center;
                margin-bottom: 20px;
            }
            input[type="text"], input[type="file"] {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 14px;
            }
            button {
                padding: 8px 16px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 14px;
            }
            button:hover {
                background-color: #0056b3;
            }
            #messages {
                list-style-type: none;
                padding: 0;
            }
            #messages li {
                background-color: #e9ecef;
                padding: 10px;
                margin-bottom: 5px;
                border-radius: 4px;
            }
        </style>
    </head>
    <body>
        <h1>DocAgentChat</h1>
        <form onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off" placeholder="Message DocAgent" />
            <button type="submit">Send</button>
        </form>
        <form id="fileForm" onsubmit="uploadFile(event)">
            <input type="file" id="fileInput" name="file" />
            <button type="submit">Upload File</button>
        </form>
        <ul id="messages"></ul>

        <script>
            var ws = new WebSocket("ws://localhost:5459/chat");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages');
                var message = document.createElement('li');
                var content = document.createTextNode(event.data);
                message.appendChild(content);
                messages.appendChild(message);
            };

            function sendMessage(event) {
                event.preventDefault();
                var input = document.getElementById("messageText");
                if (input.value.trim() !== "") {
                    ws.send(input.value);
                    input.value = '';
                }
            }

            async function uploadFile(event) {
                event.preventDefault();
                const fileInput = document.getElementById('fileInput');
                const file = fileInput.files[0];
                if (file) {
                    const formData = new FormData();
                    formData.append('file', file);

                    try {
                        const response = await fetch('http://127.0.0.1:5459/up-file', {
                            method: 'POST',
                            body: formData
                        });
                        const result = await response.json();
                        console.log(result);
                        alert('File uploaded successfully!');
                    } catch (error) {
                        console.error('Upload');
                        alert('uploading file');
                    }
                } else {
                    alert('Please select a file to upload');
                }
            }
        </script>
    </body>
</html>
"""


@router.get('/', tags=['Test Page'])
def get():
    return HTMLResponse(html)

@router.post('/up-file', tags=['File upload'])
async def upload_file(file: UploadFile = File(...)):
    """_summary_

    Args:
        file (UploadFile, optional): Defaults to File(...).

    Returns:
        file_status (str): Status of the file upload.
    """
    file_status = storage_context_file(user_file=file)
    return file_status

@router.websocket('/chat')
async def rt_chat(ws: WebSocket):
    """_summary_

    Args:
        ws (WebSocket): _description_

    """
    await ws.accept()
    while True:
        user_prompt = await ws.receive_text()
        validate_prompt = process_user_input(user_input=user_prompt)
        response = chat_to_model(input_to_model=validate_prompt)
        await ws.send_text(str(response))

@router.get('/history-input', tags=['Query data: List user inputs'])
async def user_inputs():
    """_summary_

    Description:
        List all inputs from the user.
    """
    user_input_data = list_chat_files(SETTINGS.USER_INPUT_PATH)
    if not user_input_data:
        raise HTTPException(status_code=404, detail="No JSON files found in the directory.")
    return user_input_data


@router.get('/agent-outputs', tags=['Query data: List model outputs'])
async def agent_outputs():
    """_summary_

    Description:
        List all outputs from the model.
    """
    model_output_data = list_chat_files(directory_path=SETTINGS.OUTPUT_PATH)
    if not model_output_data:
        raise HTTPException(status_code=404, detail="No JSON files found in the directory.")
    return model_output_data


