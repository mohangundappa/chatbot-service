from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from ..tools import warranty, inventory
from ..config import settings


class ReturnsAgent:
    def __init__(self):
        self.model = ChatOpenAI(
            model=settings.agent_model,
            api_key=settings.openai_api_key
        )
        self.tools = [warranty.check_status, inventory.verify_stock]
        self.agent = create_react_agent(
            model=self.model,
            tools=self.tools,
            prompt=self._returns_prompt()
        )

    def _returns_prompt(self):
        return """
        You are a returns specialist for a retail company.
        Key responsibilities:
        1. Validate return eligibility
        2. Check warranty status
        3. Initiate replacement inventory checks
        4. Follow regional policies ({region})

        Always:
        - Confirm order details first
        - Provide clear next steps
        - Offer store credit options
        """