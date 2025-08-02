import secrets

def generate_token(length: int = 32) -> str:
   """
   EN: Generate a secure, URL-safe token string.
   BR: Gera uma string de token segura para uso em URLs.
   """
   return secrets.token_urlsafe(length)