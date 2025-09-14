from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import AuthRegisterRequest
from app.utils.auth import validate_password, hash_string
from app.services.token_service import verify_verification_token


def check_existing_email(db: Session, email: str) -> bool:
      return db.query(User).filter_by(email=email).first() is not None

# EN: Creates a new user / BR: 
def create_user(db: Session, user: AuthRegisterRequest):
      # EN: Check if email exists / BR: 
      if check_existing_email(db, user.email):
         raise ValueError("Email already exists")
      
      # EN: Validate password
      validation_result = validate_password(user.password)
      if validation_result is not True:
            raise ValueError(validation_result)
      
      # EN: Hash password
      hashed_pw = hash_string(user.password)

      # EN: Create user object
      new_user = User(
         email=user.email,
         password_hash=hashed_pw,
         school_id=user.school_id,
         user_role_id=1
         )   
      
      # EN: Add user to database
      db.add(new_user)
      db.commit()
      db.refresh(new_user)
      
      return new_user


def verify_user(db: Session, token_str: str) -> None:
      """
      EN: Consumes an email verification token. Validates and locks the token,
      sets the user as verified, marks the token as used, and commits.
    
      BR: Consome um token de verificação de e-mail. Valida e bloqueia o token,
      define o usuário como verificado, marca o token como usado e confirma.
      """
      now = datetime.now(timezone.utc)

      token = verify_verification_token(
           db=db,
           verification_token=token_str
           )
      
      user = db.get(User, token.user_id)

      if not user.is_verified:
           user.is_verified = True

      token.used = True
      token.used_at = now
      
      db.commit()

def login_user