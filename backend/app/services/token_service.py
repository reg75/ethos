from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.user import Token, User, TokenPurposeEnum 
from app.utils import generate_token, hash_token


def create_token(db, user_id, purpose, expiry_minutes):
    """
    EN: Creates and stores a secure token for a specific purpose (e.g. email verification).
    BR: Cria e armazena um token seguro para um propósito específico (ex: verificação de e-mail).
    """   
   
    now = datetime.now(timezone.utc) #Gets current time

    raw_token = generate_token() # Sent via email

    hashed_token = hash_token(raw_token) # Stored in db

    token_row = Token(
        user_id=user_id,
        token_hash = hashed_token,
        purpose=purpose,
        created_at=now,
        expires_at=now + timedelta(minutes=expiry_minutes),
        used=False)

    # EN: Add token to database
    try:
        db.add(token_row)
        db.commit()
        db.refresh(token_row)
        return token_row,  raw_token
   
    except Exception as e:
        db.rollback()
        raise e


def create_verification_token(db: Session, user_id: int):
    """
    EN: Creates and stores a secure token for email verification.
    BR: Cria e armazena um token seguro para verificação de e-mail.
    """
    expiry_minutes = 4320 # 3 days / 3 dias
   
    return create_token(db, user_id, TokenPurposeEnum.CONFIRM_EMAIL, expiry_minutes)


def create_password_reset_token(db: Session, user_id: int):
    """
    EN: Creates and stores a secure token for resetting a password.
    BR: Cria e armazena um token seguro para redefinição de senha.
    """
    expiry_minutes = 60 # One hour / uma hora
   
    return create_token(db, user_id, TokenPurposeEnum.PASSWORD_RESET, expiry_minutes)

@dataclass(frozen=True)
class PeekResult:
    used: bool
    user_is_verified: bool
    expires_at: datetime

def peek_token(db: Session, token_str: str, expected_purpose: TokenPurposeEnum) -> PeekResult|None:
    now = datetime.now(timezone.utc)
    
    token_hash = hash_token(token_str)

    token = (
        db.query(Token)
        .filter_by(token_hash=token_hash,
                   purpose=expected_purpose)
        .first()
    )

    if token is None or token.expires_at < now:
        return None
    
    return PeekResult(
        used=token.used,
        user_is_verified=token.user.is_verified,
        expires_at=token.expires_at,
    )

def peek_verification_token(db: Session, token_str: str) -> PeekResult | None:

    expected_purpose = TokenPurposeEnum.CONFIRM_EMAIL

    return peek_token(db=db, token_str=token_str, expected_purpose=expected_purpose)

def peek_password_reset_token(db: Session, token_str: str) -> PeekResult | None:

    expected_purpose = TokenPurposeEnum.PASSWORD_RESET

    return peek_token(db=db, token_str=token_str, expected_purpose=expected_purpose)

def verify_token(db: Session, token_str: str, expected_purpose: TokenPurposeEnum) -> Token:
    """
    EN: Verifies a token's validity, expiry, and purpose. Returns token if valid.
    BR: Verifica validade, expiração e propósito de um token. Retorna o token se válido.
    """   
    now = datetime.now(timezone.utc)
    
    token_hash = hash_token(token_str)

    token = (
        db.query(Token)
        .filter_by(token_hash=token_hash, 
                   purpose=expected_purpose)
        .with_for_update()
        .first()
    )

    # Checks if it is a token
    if not token or token.used or token.expires_at < now:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Invalid or expired token!")
   
    return token

def verify_verification_token(db: Session, verification_token: str):
    """
    EN: Verifies the validity, expiry, correct purpose of an email verification token. Returns token if valid.
    BR: Verifica validade, expiração e propósito correto de um token de verificação de e-mail. Retorna o token se válido.
    """  
    expected_purpose = TokenPurposeEnum.CONFIRM_EMAIL
   
    return verify_token(db=db, token_str=verification_token, expected_purpose=expected_purpose)

def verify_password_reset_token(db: Session, verification_token: str):
    """
    EN: Verifies the validity, expiry, correct purpose of a password reset token. Returns token if valid.
    BR: Verifica validade, expiração e propósito correto de um token de redefinição de senha. Retorna o token se válido.
    """  
    expected_purpose = TokenPurposeEnum.PASSWORD_RESET
   
    return verify_token(db=db, token_str=verification_token, expected_purpose=expected_purpose)

