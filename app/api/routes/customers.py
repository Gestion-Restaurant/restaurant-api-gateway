from fastapi import APIRouter
from pydantic import BaseModel
from typing import Literal
from app.api.utils.utils import forward_request

router = APIRouter()
class CustomerLogin(BaseModel):
    email: str
    password: str

class CustomerCreate(BaseModel):
    name: str
    email: str
    password: str
    role: Literal["chef", "delivery", "customer"]

@router.get("/{role}")
async def list_customers_by_role(role: Literal["chef", "delivery", "customer"]):
    """List all customers"""
    return await forward_request("customers", f"/users/{role}", "GET")

@router.post("/login")
async def login(customer: CustomerLogin):
    """Login customer"""
    return await forward_request("customers", "/auth/login", "POST", customer.model_dump())

@router.post("/register")
async def register(customer: CustomerCreate):
    """Register a new customer"""
    return await forward_request("customers", "/auth/register", "POST", customer.model_dump())

@router.get("/{customer_id}")
async def get_customer(customer_id: str):
    """Get customer details"""
    return await forward_request("customers", f"/users/{customer_id}", "GET")