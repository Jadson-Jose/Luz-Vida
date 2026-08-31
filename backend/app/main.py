from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from app.config import CORS_ORIGINS
from app.routers import angels, auth, bible, saints, stats

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="Biblia API Vulgata")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Total-Count", "X-Skip", "X-Limit"],
)

app.include_router(auth.router)
app.include_router(bible.router)
app.include_router(angels.router)
app.include_router(saints.router)
app.include_router(stats.router)


@app.get("/")
def root():
    return {"mensagem": "Biblia API Vulgata"}
