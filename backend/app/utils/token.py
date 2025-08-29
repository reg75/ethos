import secrets
import hashlib

def generate_token(length: int = 32) -> str:
   """
   EN: Generate a secure, URL-safe token string.
   BR: Gera uma string de token segura para uso em URLs.
   """
   return secrets.token_urlsafe(length)

def hash_token(token: str):
   if isinstance(token, str):
      token = token.encode()

   token_hash = hashlib.sha256(token).hexdigest()

   return token_hash
