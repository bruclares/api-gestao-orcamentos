from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.endpoints import users, login
from app.db import base

app = FastAPI(title=settings.PROJECT_NAME)

# Inclui as rotas de usuários
# Tudo que estiver em 'users' vai começar com /api/v1/users
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])

@app.get("/")
def read_root():
    return{"message": "API de Gestão de Orçamentos está ON!"}