from redis import Redis
from langchain_redis import RedisVectorStore
from langchain_openai import OpenAIEmbeddings
from .config import settings

class MemoryManager:
    def __init__(self):
        self.redis = Redis.from_url(settings.redis_url)
        self.embeddings = OpenAIEmbeddings()
        self.vectorstore = RedisVectorStore(
            embedding=self.embeddings,
            index_name="retail_memories",
            redis_url=settings.redis_url
        )

    def get_context(self, customer_id: str):
        return self.vectorstore.similarity_search(
            query=f"customer:{customer_id}",
            k=3,
            return_metadata=True
        )

    def update_context(self, customer_id: str, data: dict):
        self.vectorstore.add_texts(
            texts=[data["messages"][-1]["content"]],
            metadatas=[{"customer_id": customer_id}]
        )