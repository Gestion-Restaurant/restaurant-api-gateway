from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
import jwt
from app.core.config import settings
from typing import Optional
from functools import wraps

security = HTTPBearer()

async def verify_jwt(token: str) -> Optional[dict]:
    try:
        # Récupérer le token des cookies
        decoded_token = jwt.decode(
            token,
            settings.JWT_SECRET, 
            algorithms=["HS256"]
        )
        return decoded_token
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expiré")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Token invalide")

def auth_middleware():
    async def middleware(request: Request, call_next):
        try:
            # Récupérer le token du cookie
            token = request.cookies.get("auth_token")
            if not token:
                raise HTTPException(
                    status_code=401,
                    detail="Non authentifié"
                )
            
            # Vérifier et décoder le token
            user_data = await verify_jwt(token)
            # Ajouter les infos utilisateur à la requête
            request.state.user = user_data
            
            # Continuer le traitement
            response = await call_next(request)
            return response
            
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    return middleware