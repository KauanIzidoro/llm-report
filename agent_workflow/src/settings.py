from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    PROJECT_PATH: str
    OUTPUT_PATH: str
    GOOGLE_API_KEY: str
    MODEL: str


SETTINGS = Settings()
