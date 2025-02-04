from fastapi import APIRouter
from app.api.utils.utils import forward_request
from pydantic import BaseModel

router = APIRouter()

class DeliveryAssignment(BaseModel):
    deliveryPersonId: str


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

@router.post("/assign/{id}")
async def assign_delivery(id: str, assignment: DeliveryAssignment):
    """Assign delivery person"""
    return await forward_request(
        "delivery", 
        f"/deliveries/assignForDelivery?orderId={id}",
        "POST", 
        assignment.model_dump()
    )
    
@router.get("/deliveryPerson/{delivery_person_id}")
async def get_delivery_by_person(delivery_person_id: str):
    """Get delivery by delivery person ID"""
    return await forward_request("delivery", f"/deliveries/deliveryPerson/{delivery_person_id}", "GET")