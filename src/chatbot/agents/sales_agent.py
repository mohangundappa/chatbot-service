# src/chatbot/agents/sales_agent.py
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from ..tools import promotions
from ..config import settings


class SalesAgent:
    def __init__(self):
        self.model = ChatOpenAI(
            model=settings.agent_model,
            api_key=settings.openai_api_key
        )
        self.tools = [promotions.apply_promotion, promotions.suggest_upsells]
        self.agent = create_react_agent(
            model=self.model,
            tools=self.tools,
            prompt=self._sales_prompt()
        )

    def _sales_prompt(self):
        return f"""
        You are a sales specialist for a retail company.
        Key objectives:
        1. Increase average order value
        2. Improve conversion rates
        3. Promote loyalty programs

        Current Region: {settings.default_region}
        Tools:
        - Apply promotions
        - Suggest upsells
        - Check loyalty points

        Always:
        - Verify promotion eligibility
        - Respect customer budget
        - Maintain ethical sales practices
        """