from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    OPENAI_API_KEY:str 

    OPENAI_MODEL: str = "gpt-5-mini"

    EMBEDDING_MODEL: str = (
        "text-embedding-3-small"
    )

    UPLOAD_DIRECTORY: str = "uploads"

    VECTOR_STORE_DIRECTORY: str = "data/vector_store"

    CHUNK_SIZE: int = 500

    CHUNK_OVERLAP: int = 100

    EMBEDDING_DIMENSION:int=1536

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )
   


settings = Settings()