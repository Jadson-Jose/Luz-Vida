from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from app.config import ADMIN_PASSWORD, ADMIN_USERNAME
from app.security import create_access_token

router = APIRouter(prefix="/api/auth", tags=["auth"])


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
def login(data: LoginRequest):
    if data.username != ADMIN_USERNAME or data.password != ADMIN_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
        )
    token = create_access_token({"sub": "admin"})
    return {"access_token": token, "token_type": "bearer"}
