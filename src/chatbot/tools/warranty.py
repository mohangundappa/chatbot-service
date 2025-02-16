# src/chatbot/tools/warranty.py
from langchain.tools import tool
import httpx
from ..config import settings

@tool
def check_warranty_status(product_id: str) -> dict:
    """Check warranty coverage for a product"""
    try:
        response = httpx.get(
            f"{settings.warranty_api}/coverage",
            params={"product_id": product_id}
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}