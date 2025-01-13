from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

class OrderItem(BaseModel):
    product_id: str
    quantity: int

class OrderCreate(BaseModel):
    items: List[OrderItem]
    customer_id: str

router = APIRouter()

@router.get("/")
async def list_orders():
    """List all orders"""
    return {"message": "List orders endpoint"}

@router.post("/")
async def create_order(order: OrderCreate):
    """Create a new order"""
    return {
        "message": "Create order endpoint",
        "order": order.model_dump()
    }

@router.get("/{order_id}")
async def get_order(order_id: str):
    """Get order details"""
    return {"message": f"Get order {order_id} details"}