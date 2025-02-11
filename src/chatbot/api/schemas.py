from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str
    external_chat_id: str = Field(...,
                                 description="Client-provided unique chat identifier")

class ChatResponse(BaseModel):
    response: str
    thread_id: str
    external_chat_id: str