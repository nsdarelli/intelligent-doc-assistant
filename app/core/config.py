from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    GEMINI_API_KEY: str
    MODEL_NAME: str = 'gemini-2.5-flash'
    EMBED_MODEL: str = 'gemini-embedding-2'
    CHROMA_PATH: str = 'storage/chroma'
    RAW_DATA_PATH: str = 'data/raw'
    COLLECTION_NAME: str = 'documents'
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 100

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()