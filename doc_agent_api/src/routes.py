from fastapi import APIRouter, WebSocket
from fastapi.responses import HTMLResponse
from utils import validate_input, mock_chat_to_model
router = APIRouter()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat4Vision</title>
    </head>
    <body>
        <h1>DocAgentChat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

html_rest = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat4Vision</title>
    </head>
    <body>
        <h1>DocAgentChat (REST)</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

@router.get('/')
def get():
    return HTMLResponse(html)

    
@router.websocket('/ws')
async def rt_chat(ws: WebSocket):
    await ws.accept()
    while True:
        text_prompt = await ws.receive_text()
        validate_prompt = validate_input(text_prompt=text_prompt)
        model_output = mock_chat_to_model(prompt=validate_prompt)
        await ws.send_text(model_output)
        
@router.get('/rest')
def rest_chat():
    return HTMLResponse(html_rest)

@router.post('/chat')
def rest_chat(user_prompt: str):
    validate_prompt = validate_input(text_prompt=user_prompt)
    model_output = mock_chat_to_model(prompt=validate_prompt)
    return {"response": model_output}
    