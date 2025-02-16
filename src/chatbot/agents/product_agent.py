from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from ..tools import inventory
from ..config import settings


class ProductAgent:
    def __init__(self):
        self.model = ChatOpenAI(
            model=settings.agent_model,
            api_key=settings.openai_api_key
        )
        self.tools = [inventory.get_product_details, inventory.check_inventory]
        self.agent = create_react_agent(
            model=self.model,
            tools=self.tools,
            prompt=self._product_prompt()
        )

    def _product_prompt(self):
        return f"""
        You are a product expert for a retail company.
        Responsibilities:
        1. Provide detailed product specifications
        2. Check regional availability ({settings.default_region})
        3. Suggest alternatives
        4. Explain product features

        Always:
        - Verify current stock levels
        - Consider regional preferences
        - Mention warranty information
        """