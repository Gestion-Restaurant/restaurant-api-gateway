from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Basic settings
    PROJECT_NAME: str = "Restaurant API Gateway"
    VERSION: str = "1.0.0"
    
    # Service URLs (to be configured later)
    CUSTOMER_SERVICE_URL: str = ""
    ORDER_SERVICE_URL: str = ""
    KITCHEN_SERVICE_URL: str = ""
    DELIVERY_SERVICE_URL: str = ""
    
    class Config:
        env_file = ".env"

settings = Settings()