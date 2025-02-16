from langgraph_supervisor import create_supervisor
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from .config import settings
from chatbot.agents.returns_agent import ReturnsAgent
from chatbot.agents.product_agent import ProductAgent
from chatbot.agents.sales_agent import SalesAgent
from .memory import MemoryManager


class RetailSupervisor:
    def __init__(self):
        self.memory = MemoryManager()
        self.model = ChatOpenAI(
            model=settings.supervisor_model,
            api_key=settings.openai_api_key
        )
        self.agents = self._initialize_agents()
        self.workflow = create_supervisor(
            list(self.agents.values()),
            model=self.model,
            prompt=self._supervisor_prompt()
        ).compile()

    def _initialize_agents(self):
        return {
            "returns": ReturnsAgent(),
            "product": ProductAgent(),
            "sales": SalesAgent()
        }

    def _supervisor_prompt(self):
        return f"""
        You are a retail customer service supervisor managing:
        - Returns Agent: Handles returns/exchanges/warranty
        - Product Agent: Provides product info and inventory
        - Sales Agent: Handles purchases and promotions

        Current Region: {settings.default_region}
        Max Handoffs: {settings.max_handoffs}

        Route requests based on:
        1. Keywords: return, exchange, warranty → Returns Agent
        2. Product questions → Product Agent
        3. Purchase intent → Sales Agent
        """

    async def process_message(self, customer_id: str, message: str):
        context = self.memory.get_context(customer_id)
        result = await self.workflow.ainvoke({
            "messages": [{
                "role": "user",
                "content": message,
                "metadata": {
                    "customer_id": customer_id,
                    "region": settings.default_region,
                    **context
                }
            }]
        })
        self.memory.update_context(customer_id, result)
        return result