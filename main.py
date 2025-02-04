from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from app.core.config import settings
from app.api.routes import customers, orders, kitchen, delivery
from app.api.utils.auth_middleware import auth_middleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Restaurant management system API Gateway",
    docs_url="/doc",
    openapi_url="/openapi.json"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes registration
app.include_router(
    customers.router,
    prefix="/customers",
    tags=["customers"]
)

app.include_router(
    orders.router,
    prefix="/orders",
    tags=["orders"]
)

app.include_router(
    kitchen.router,
    prefix="/kitchen",
    tags=["kitchen"]
)

app.include_router(
    delivery.router,
    prefix="/delivery",
    tags=["delivery"]
)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)