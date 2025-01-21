import uvicorn
from fastapi import FastAPI

from routes import router
from settings import SETTINGS

app = FastAPI(title='DocAgentAPI', version='0.1.0')
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, port=SETTINGS.API_PORT)
