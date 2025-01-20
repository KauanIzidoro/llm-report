import uvicorn 
from settings import SETTINGS
from fastapi import FastAPI
from routes import router

app = FastAPI(title='DocAgent', version='0.1.0')
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app,port=SETTINGS.API_PORT)
    