from fastapi import APIRouter, WebSocket, status, HTTPException
from chatbot.services import ChatService
from chatbot.config import settings
from .schemas import ChatResponse, ChatRequest

router = APIRouter()
service = ChatService()


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        print("Received request")
        response = await service.process_message(
            message=request.message,
            external_chat_id=request.external_chat_id
        )
        return {
            "response": response["messages"][-1].content,
            "thread_id": service.chat_mapping[request.external_chat_id],
            "external_chat_id": request.external_chat_id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    external_chat_id = websocket.query_params.get("external_chat_id")

    if not external_chat_id:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    try:
        while True:
            message = await websocket.receive_text()
            response = await service.process_message(
                message=message,
                external_chat_id=external_chat_id
            )
            await websocket.send_json({
                "response": response["messages"][-1].content,
                "thread_id": service.chat_mapping[external_chat_id]
            })
    except Exception as e:
        await websocket.close(code=status.WS_1011_INTERNAL_ERROR)