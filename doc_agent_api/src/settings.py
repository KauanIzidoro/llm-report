from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()
class Settings(BaseSettings):
    USER_INPUT_PATH: str
    USER_FILE_PATH: str
    OUTPUT_PATH: str
    GOOGLE_API_KEY: str
    MODEL: str
    API_PORT: str
    SYSTEM_INSTRUCTION: str


SETTINGS = Settings()
