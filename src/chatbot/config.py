from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    model_name: str = "gpt-4o-mini"
    app_env: str = "production"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()