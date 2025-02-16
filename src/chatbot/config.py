from pydantic import Field, field_validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Core Configuration
    openai_api_key: str = Field(..., description="OpenAI API key")
    app_env: str = Field(default="production", pattern="^(prod|stage|dev)$")

    # Model Configuration
    supervisor_model: str = Field("gpt-4o-mini", description="Supervisor model")
    agent_model: str = Field("gpt-4o-mini", description="Base agent model")

    # Retail Configuration
    default_region: str = Field("us-west", description="Default retail region")
    max_handoffs: int = Field(3, ge=1, description="Max agent transfers")

    # Redis Configuration
    redis_url: str = Field("redis://localhost:6379", description="Redis connection URL")

    inventory_api: str = Field("https://inventory.example.com/v1", description="Base URL for inventory service")

    model_config = {
        "env_file": ".env",
        "extra": "ignore",
        "env_prefix": "RETAIL_",
    }

    @field_validator("supervisor_model", "agent_model")
    @classmethod
    def validate_models(cls, v):
        allowed = ["gpt-4o", "gpt-4o-mini"]
        if v not in allowed:
            raise ValueError(f"Allowed models: {allowed}")
        return v

settings = Settings()
