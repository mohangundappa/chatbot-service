from typing import Dict
from uuid import uuid4
from langchain_core.messages import HumanMessage
from .config import settings
from .graph import create_graph


class ChatService:
    def __init__(self):
        self.app = create_graph()
        self.chat_mapping: Dict[str, str] = {}  # external_chat_id -> thread_id

    async def get_or_create_thread(self, external_chat_id: str) -> str:
        """Get existing thread ID or create new one for external chat ID"""
        if external_chat_id in self.chat_mapping:
            return self.chat_mapping[external_chat_id]

        new_thread_id = str(uuid4())
        self.chat_mapping[external_chat_id] = new_thread_id
        return new_thread_id


    async def process_message(self, message: str, external_chat_id: str):

        thread_id = await self.get_or_create_thread(external_chat_id)
        config = {"configurable": {"thread_id": thread_id}}

        # Create new message list with config
        input_messages = [HumanMessage(message)]
        return  self.app.invoke({"messages": input_messages}, config)