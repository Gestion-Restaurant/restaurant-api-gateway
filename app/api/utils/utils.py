from typing import Any, Dict
from fastapi import HTTPException
import httpx
from app.core.config import settings

async def forward_request(
    service: str, 
    path: str, 
    method: str = "GET", 
    data: Dict = None,
    headers: Dict[str, str] = None
) -> Any:
    async with httpx.AsyncClient() as client:
        try:
            url = f"{get_service_url(service)}{path}"
            if method == "GET":
                response = await client.get(url, headers=headers)
            elif method == "POST":
                response = await client.post(url, json=data, headers=headers)
            elif method == "PUT":
                response = await client.put(url, json=data, headers=headers)
            elif method == "PATCH":
                response = await client.patch(url, json=data, headers=headers)
            elif method == "DELETE":
                response = await client.delete(url, headers=headers)
            
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(status_code=e.response.status_code if hasattr(e, 'response') else 500,
                            detail=str(e))


def get_service_url(service: str) -> str:
    if (service == "customers"):
        return settings.CUSTOMER_SERVICE_URL
    elif (service == "orders"):
        return settings.ORDER_SERVICE_URL
    elif (service == "kitchen"):
        return settings.KITCHEN_SERVICE_URL
    elif (service == "delivery"):
        return settings.DELIVERY_SERVICE_URL
    else:
        raise ValueError("Invalid service name")