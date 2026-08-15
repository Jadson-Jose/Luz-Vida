import os

from fastapi import Header, HTTPException, status

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "dev-secret-token")  # defina em produção!


async def require_admin(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token ausente"
        )
    schema, _, token = authorization.partition(" ")
    if schema.lower() != "bearer" or token != ADMIN_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido"
        )
    return True
