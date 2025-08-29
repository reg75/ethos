from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas.auth import AuthRegisterRequest, AuthRegisterResponse 
from app.services.auth_service import create_user, AuthRegisterRequest
from app.services.token_service import create_verification_token
from app.utils.auto_emails import send_verification_email

router = APIRouter(
   prefix="/auth",
   tags=["auth"]
)

# EN: Route to register a new user / BR: Rota para cadastrar novo usuário
@router.post("/register", response_model=AuthRegisterResponse)
def register_user(user: AuthRegisterRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
   try:
      new_user = create_user(db, user)

      token_row, raw_token = create_verification_token(db, new_user.id)

      background_tasks.add_task(
         send_verification_email,
            to_email=new_user.email,
            token=raw_token 
      )

      return new_user
   
   except ValueError as e:
      raise HTTPException(status_code=409, detail=str(e))
   
   