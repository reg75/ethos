from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas.auth import AuthRegisterRequest, AuthRegisterResponse 
from app.services.auth_service import create_user, AuthRegisterRequest
from app.services.token_service import create_verification_token
from app.utils.auto_emails import send_verfication_email

router = APIRouter(
   prefix="/auth",
   tags=["auth"]
)

# EN: Route to register a new user / BR: Rota para cadastrar novo usuário
@router.post("/register", response_model=AuthRegisterResponse)
def register_user(user: AuthRegisterRequest, db: Session = Depends(get_db)):
   try:
      new_user = create_user(db, user)

      token = create_verification_token(db, new_user.id)

      send_verfication_email(to_email=new_user.email, token=token.token)

      return new_user
   
   except ValueError as e:
      raise HTTPException(status_code=409, detail=str(e))