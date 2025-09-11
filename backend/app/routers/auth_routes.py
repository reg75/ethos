from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session

from fastapi.responses import RedirectResponse

from app.db import get_db
from app.config import FRONTEND_URL
from app.schemas.auth import AuthRegisterRequest, AuthRegisterResponse 
from app.services.auth_service import create_user, AuthRegisterRequest, verify_user
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
   
@router.get("/verify")
def verify_email(token: str, db: Session = Depends(get_db)):
   try:
      verify_user(db, token)

      redirect_url = f"{FRONTEND_URL}/login?verified=1"

      return RedirectResponse(
         url=redirect_url,
         status_code=303,
         headers={
            "Referrer-Policy": "no-referrer",
            "Cache-Control": "no-store",
         },
      )
   
   except Exception:

      error_url = f"{FRONTEND_URL}/verify?error=invalid"

      return RedirectResponse(
         url=error_url,
         status_code=303,
         headers={
            "Referrer-Policy": "no-referrer",
            "Cache-Control": "no-store",
         }

      )
   
