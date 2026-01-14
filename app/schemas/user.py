from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

# base: campos comuns que tod usuário tem
class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None
    is_active: bool = True

# create: o que precisamos para criar 
class UserCreate(UserBase):
    password: str = Field(min_length=6, max_length=100)

# response: o que devolvemos para o front (senha não pode aparecer aqui)
class UserResponse(UserBase):
    id: UUID
    created_at: datetime

    # configuração para o oydantic ler os dados do SQLAlchemy
    class Config:
        from_attributes = True