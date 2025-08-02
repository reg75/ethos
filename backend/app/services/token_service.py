from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from app.models.user import Token 
from app.utils import generate_token

def create_token(db, user_id, purpose, expiry_minutes):
   """
   EN: Creates and stores a secure token for a specific purpose (e.g. email verification).
   BR: Cria e armazena um token seguro para um propósito específico (ex: verificação de e-mail).
   """   
   
   now = datetime.now(timezone.utc) #Gets current time

   token = Token(
      user_id=user_id,
      token=generate_token(),
      purpose=purpose,
      created_at=now,
      expires_at=now + timedelta(minutes=expiry_minutes),
      used=False)

   # EN: Add token to database
   try:
      db.add(token)
      db.commit()
      db.refresh(token)
      return token
   except Exception as e:
      db.rollback()
      raise e