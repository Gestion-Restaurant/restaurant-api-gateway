from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_customers():
    """List all customers"""
    return {"message": "List customers endpoint"}

@router.get("/{customer_id}")
async def get_customer(customer_id: str):
    """Get customer details"""
    return {"message": f"Get customer {customer_id} details"}

@router.post("/")
async def create_customer():
    """Create a new customer"""
    return {"message": "Create customer endpoint"}