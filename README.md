# Restaurant API Gateway

This project is a Restaurant API Gateway built using FastAPI. It acts as a gateway to various microservices such as customers, orders, kitchen, and delivery.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Gestion-Restaurant/restaurant-api-gateway.git
    cd restaurant-api-gateway
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt

4. Create a [.env](http://_vscodecontentref_/14) file in the root directory and add the following content:
    ```env
    JWT_SECRET="jwt_secret_key"
    ```

## Running the Application

To run the application, use the following command:
```sh
uvicorn main:app --reload
```

The application will be available at http://localhost:8000.


## Middleware
The authentication middleware is defined in auth_middleware.py. It verifies the JWT token from the request cookies.
