from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

class ChatRequest(BaseModel):
    """Schema for incoming chat requests"""
    message: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        example="Do you have this product in stock?",
        description="User's message to the chatbot"
    )
    external_chat_id: str = Field(
        ...,
        min_length=6,
        example="cust_12345",
        description="External identifier for the conversation"
    )
    customer_id: Optional[str] = Field(
        None,
        example="user_67890",
        description="Optional customer identifier"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "message": "Where is my order?",
                "external_chat_id": "chat_abc123",
                "customer_id": "cust_456"
            }
        }
    )

class ChatResponse(BaseModel):
    """Schema for chatbot responses"""
    response: str = Field(
        ...,
        example="Your order is in transit and will arrive by Friday.",
        description="Chatbot's generated response"
    )
    thread_id: str = Field(
        ...,
        example="thread_xyz789",
        description="Internal conversation thread ID"
    )
    external_chat_id: str = Field(
        ...,
        example="chat_abc123",
        description="External identifier provided in request"
    )
    agent: str = Field(
        ...,
        example="returns_agent",
        description="Which agent handled the request",
        pattern="^(returns|product|sales)_agent$"
    )
    timestamp: datetime = Field(
        default_factory=datetime.now,
        example="2024-03-15T14:30:00Z",
        description="Time of response generation"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "response": "Your return has been processed successfully.",
                "thread_id": "thread_xyz789",
                "external_chat_id": "chat_abc123",
                "agent": "returns_agent",
                "timestamp": "2024-03-15T14:30:00Z"
            }
        }
    )
