from fastapi import APIRouter
from app.api.utils.utils import forward_request

router = APIRouter()

@router.get("", include_in_schema=True)
async def get_deliveries():
    """Get all deliveries"""
    return await forward_request("delivery", "/deliveries", "GET")

@router.get("/orders/{order_id}")
async def get_delivery_by_order(order_id: str):
    """Get delivery by order ID"""
    return await forward_request("delivery", f"/deliveries/orders/{order_id}", "GET")

@router.patch("/status/{order_id}")
async def update_delivery_status(order_id: str, status: str):
    """Update delivery status"""
    return await forward_request(
        "delivery", 
        f"/deliveries/status/{order_id}", 
        "PATCH", 
        {"status": status}
    )

@router.post("/assign/{order_id}")
async def assign_delivery(order_id: str, delivery_person_id: str):
    """Assign delivery person"""
    return await forward_request(
        "delivery", 
        f"/deliveries/assign/{order_id}", 
        "POST", 
        {"deliveryPersonId": delivery_person_id}
    )