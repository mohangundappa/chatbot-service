from fastapi import APIRouter, Depends
from .schemas import ChatRequest, ChatResponse
from chatbot.api.dependencies import get_supervisor
from ..supervisor import RetailSupervisor

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def handle_chat(
    request: ChatRequest,
    supervisor: RetailSupervisor = Depends(get_supervisor)
):
    result = await supervisor.process_message(
        customer_id=request.customer_id,
        message=request.message
    )
    return {
        "response": result["messages"][-1]["content"],
        "agent": result["metadata"]["final_agent"],
        "context_id": request.customer_id
    }