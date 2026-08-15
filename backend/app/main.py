from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import bible

app = FastAPI(title="Biblia API Vulgata")
app.include_router(bible.router)

"""Configuração do CORS para permitir requisições do frontend"""
origins = [
    "http://localhost:5173",  # endereço padrão do Vue/Vite
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(bible.router)


@app.get("/")
def root():
    return {"message": "Biblia API Vulgata"}
