from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.api.utils.utils import forward_request

router = APIRouter()

class DishCreate(BaseModel):
    name: str
    description: str
    price: float
    restaurantId: str
    isAvailable: bool = True
    

@router.get("/restaurant/{restaurant_id}")
async def get_kitchen_orders(restaurant_id: str):
    """Get kitchen dishes"""
    return await forward_request("kitchen", f"/dishes/restaurant/{restaurant_id}", "GET")

@router.get("/dishes/restaurant/{restaurant_id}")
async def get_kitchen_dishes(restaurant_id: str):
    """Get kitchen dishes"""
    return await forward_request("kitchen", f"/dishes/restaurant/{restaurant_id}", "GET")

@router.get("/{order_id}")
async def get_order(order_id: str):
    """Get order details"""
    return await forward_request("kitchen", f"/dishes/{order_id}", "GET")

@router.post("/")
async def create_dish(request: Request, dish: DishCreate):
    """Create a new dish"""
    auth_token = request.cookies.get("auth_token") or request.headers.get("cookie")
    print("Auth token:", auth_token)
    
    return await forward_request(
        service="kitchen",
        path="/dishes",
        method="POST",
        data=dish.model_dump(),
        headers={"Authorization": auth_token}
    )

@router.put("/{dish_id}")
async def update_dish(dish_id: str, dish: DishCreate):
    """Update order details"""
    return await forward_request("kitchen", f"/dishes/{dish_id}", "PUT", dish.model_dump())

@router.delete("/{dish_id}")
async def delete_dish(dish_id: str):
    """Delete order"""
    return await forward_request("kitchen", f"/dishes/{dish_id}", "DELETE")
