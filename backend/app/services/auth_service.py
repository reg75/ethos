from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import AuthRegisterRequest
from app.utils.auth import validate_password, hash_string


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

'''
# EN: Creates a new user / BR: 
def verify_user(db: Session, user: AuthRegisterRequest):
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
'''