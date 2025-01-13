from fastapi import APIRouter

router = APIRouter()

@router.get("/orders")
async def get_deliveries():
    """Get all deliveries"""
    return {"message": "Get deliveries endpoint"}

@router.get("/orders/{order_id}")
async def get_delivery(order_id: str):
    """Get delivery status"""
    return {"message": f"Get delivery status for order {order_id}"}