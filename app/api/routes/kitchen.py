from fastapi import APIRouter

router = APIRouter()

@router.get("/menu")
async def get_menu():
    """Get restaurant menu"""
    return {"message": "Get menu endpoint"}

@router.get("/orders")
async def get_kitchen_orders():
    """Get kitchen orders"""
    return {"message": "Get kitchen orders endpoint"}