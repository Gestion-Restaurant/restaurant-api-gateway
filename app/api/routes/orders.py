from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from app.api.utils.utils import forward_request
from enum import Enum

class DeliveryStatus(str, Enum):
    PENDING = "pending"
    IN_KITCHEN = "in_kitchen"
    READY_FOR_DELIVERY = "ready_for_delivery"
    ASSIGNED = "assigned"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"

class OrderItem(BaseModel):
    itemId: str
    name: str
    quantity: int
    price: float

class OrderCreate(BaseModel):
    clientId: str
    restaurantId: str
    items: List[OrderItem]
    totalAmount: float

class OrderStatus(BaseModel):
    status: DeliveryStatus

router = APIRouter()

@router.get("/")
async def list_orders():
    """List all orders"""
    return await forward_request("orders", "/orders", "GET")

@router.get("/by-id/{id}")
async def get_order_by_id(id: str):
    """Get order by ID"""
    return await forward_request("orders", f"/orders/by-id/{id}", "GET")

@router.get("/by-id-client/{client_id}")
async def get_orders_by_client(client_id: str):
    """Get orders by client ID"""
    return await forward_request("orders", f"/orders/by-id-client/{client_id}", "GET")

@router.post("/")
async def create_order(order: OrderCreate):
    """Create a new order"""
    return await forward_request("orders", "/orders", "POST", order.model_dump())

@router.put("/by-id/{id}")
async def update_order(id: str, order: OrderCreate):
    """Update order"""
    return await forward_request("orders", f"/orders/by-id/{id}", "PUT", order.model_dump())

@router.patch("/by-id/{id}")
async def update_order_status(id: str, status: OrderStatus):
    """Update order status"""
    return await forward_request("orders", f"/orders/by-id/{id}", "PATCH", status.model_dump())

@router.delete("/by-id/{id}")
async def delete_order(id: str):
    """Delete order"""
    return await forward_request("orders", f"/orders/by-id/{id}", "DELETE")