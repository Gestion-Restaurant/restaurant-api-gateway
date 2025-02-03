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
    restaurantId: str

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

@router.get("/byId/{id}")
async def get_order_by_id(id: str):
    """Get order by ID"""
    return await forward_request("orders", f"/orders/by-id/{id}", "GET")

@router.get("/ByIdClient/{client_id}")
async def get_orders_by_client(client_id: str):
    """Get orders by client ID"""
    return await forward_request("orders", f"/orders/ByIdClient/{client_id}", "GET")

@router.post("/")
async def create_order(order: OrderCreate):
    """Create a new order"""
    return await forward_request("orders", "/orders", "POST", order.model_dump())

@router.put("/byId/{id}")
async def update_order(id: str, order: OrderCreate):
    """Update order"""
    return await forward_request("orders", f"/orders/by-id/{id}", "PUT", order.model_dump())

@router.patch("/byId/{id}")
async def update_order_status(id: str, status: OrderStatus):
    """Update order status"""
    return await forward_request("orders", f"/orders/byId/{id}", "PATCH", status.model_dump())

@router.get("/restaurant/{restaurant_id}")
async def get_restaurant_orders(restaurant_id: str):
    """Get orders by restaurant ID"""
    return await forward_request("orders", f"/orders/restaurant/{restaurant_id}", "GET")