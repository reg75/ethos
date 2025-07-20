from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas.auth import AuthRegisterRequest, AuthRegisterResponse 
from app.services.auth_service import AuthRegisterRequest

router = APIRouter(
   prefix="/auth",
   tags=["auth"]
)

@router.post("/register", response_model=AuthRegisterResponse)
def register_user(user: AuthRegisterRequest, db: Session = Depends(get_db)):
   try:
      new_user = create_user(db, user)
      return AuthRegisterResponse(**new_user)
   except ValueError as e:
      raise HTTPException(status_code=404, detail=str(e))