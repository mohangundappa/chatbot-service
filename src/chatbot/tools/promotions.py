# src/chatbot/tools/promotions.py
from langchain.tools import tool
import httpx
from ..config import settings

@tool
def apply_promotion(customer_id: str, cart_total: float) -> dict:
    """Apply eligible promotions to customer's cart"""
    try:
        response = httpx.post(
            f"{settings.promotion_api}/apply",
            json={"customer_id": customer_id, "amount": cart_total}
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@tool
def suggest_upsells(customer_id: str) -> list:
    """Generate personalized upsell suggestions"""
    try:
        response = httpx.get(
            f"{settings.promotion_api}/suggestions/{customer_id}"
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}