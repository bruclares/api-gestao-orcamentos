from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api import deps
from app.crud import users as crud_user
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserCreate, db: Session = Depends(deps.get_db)):
    """
    Cria um novo usuário no sistema.
    """
    # verifica se email já existe
    user_exists = crud_user.get_user_by_email(db, email=user_in.email)
    if user_exists:
        raise HTTPException(
            status_code=400,
            detail="Este e-mail já está cadastrado no sistema."
        )
    
    # cria o usuário
    user = crud_user.create_user(db=db, user=user_in)

    return user