from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

from app.routers import bible, angels, saints


def custom_generate_unique_id(route: APIRoute):
    tag = route.tags[0] if route.tags else "geral"
    return f"{tag}_{route.name}"


app = FastAPI(
    title="Biblia API Vulgata", generate_unique_id_function=custom_generate_unique_id
)

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
app.include_router(angels.router)
app.include_router(saints.router)


@app.get("/")
def root():
    return {"message": "Biblia API Vulgata"}
