from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Basic settings
    PROJECT_NAME: str = "Restaurant API Gateway"
    VERSION: str = "1.0.0"
    
    # Service URLs (to be configured later)
    CUSTOMER_SERVICE_URL: str = "https://customer-service-hun2.onrender.com"
    KITCHEN_SERVICE_URL: str = "https://kitchen-service-cqr6.onrender.com"
    ORDER_SERVICE_URL: str = "https://order-service-s0lo.onrender.com"
    DELIVERY_SERVICE_URL: str = "https://delivery-service-6qzx.onrender.com"
    
    JWT_SECRET: str

    class Config:
        env_file = ".env"

settings = Settings()