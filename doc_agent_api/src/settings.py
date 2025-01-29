from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    PROJECT_PATH: str
    FILE_PATH: str
    OUTPUT_PATH: str
    INPUT_PATH: str
    GOOGLE_API_KEY: str
    MODEL: str
    API_PORT: int
    SYSTEM_INSTRUCTION: str


SETTINGS = Settings()
