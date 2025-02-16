# src/chatbot/api/dependencies.py
from chatbot.supervisor import RetailSupervisor
from functools import lru_cache

@lru_cache
def get_supervisor() -> RetailSupervisor:
    return RetailSupervisor()