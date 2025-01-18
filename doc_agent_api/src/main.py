from fastapi import FastAPI

app = FastAPI()

@app.get('/status')
def status_route():
    return {"STATUS": "OK"}