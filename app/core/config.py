from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Basic settings
    PROJECT_NAME: str = "Restaurant API Gateway"
    VERSION: str = "1.0.0"
    
    # Service URLs (to be configured later)
    CUSTOMER_SERVICE_URL: str = "http://localhost:3000"
    KITCHEN_SERVICE_URL: str = "http://localhost:3001"
    ORDER_SERVICE_URL: str = "http://localhost:3002"
    DELIVERY_SERVICE_URL: str = "http://localhost:3003"
    
    JWT_SECRET: str

    class Config:
        env_file = ".env"

settings = Settings()