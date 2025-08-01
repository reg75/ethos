from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas.auth import AuthRegisterRequest, AuthRegisterResponse 
from app.services.auth_service import create_user, AuthRegisterRequest

router = APIRouter(
   prefix="/auth",
   tags=["auth"]
)

# EN: Route to register a new user / BR: Rota para cadastrar novo usuário
@router.post("/register", response_model=AuthRegisterResponse)
def register_user(user: AuthRegisterRequest, db: Session = Depends(get_db)):
   try:
      new_user = create_user(db, user)
      return new_user
   except ValueError as e:
      raise HTTPException(status_code=404, detail=str(e))