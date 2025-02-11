from langchain_openai import ChatOpenAI
from .config import settings

def get_llm():
    return ChatOpenAI(
        model=settings.model_name,
        api_key=settings.openai_api_key,
        temperature=0.7
    )