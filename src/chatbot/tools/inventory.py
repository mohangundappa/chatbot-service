from langchain.tools import tool
import httpx
from typing import Optional
from ..config import settings


@tool
def get_product_details(product_id: str) -> dict:
    """Retrieve detailed product specifications and descriptions"""
    try:
        response = httpx.get(
            f"{settings.inventory_api}/products/{product_id}",
            timeout=10
        )
        return response.json()
    except Exception as e:
        return {"error": f"Inventory API error: {str(e)}"}


@tool
def check_inventory(product_id: str, location: Optional[str] = None) -> dict:
    """Check product availability across retail locations"""
    try:
        params = {"product_id": product_id}
        if location:
            params["region"] = location

        response = httpx.get(
            f"{settings.inventory_api}/availability",
            params=params,
            timeout=10
        )
        return response.json()
    except Exception as e:
        return {"error": f"Inventory check failed: {str(e)}"}


@tool
def verify_stock(product_id: str, location: str = None) -> dict:
    """Verify real-time stock levels at specific locations"""
    return check_inventory(product_id, location)