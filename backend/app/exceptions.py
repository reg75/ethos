class VerificationError(Exception):
    """EN: Base class for all email verification errors.
    BR: Classe base para todos os erros de verificação de e-mail."""
    pass

class TokenNotFoundError(VerificationError):
    """EN: Raised when the token does not exist.
    BR: Lançado quando o token não existe."""
    pass

class TokenAlreadyUsedError(VerificationError):
    """EN: Raised when the token has already been used.
    BR: Lançado quando o token já foi utilizado."""
    pass 

class TokenExpiredError(VerificationError):
    """EN: Raised when the token has expired.
    BR: Lançado quando o token expirou."""
    pass

class AuthError(Exception):
    """
    EN: Base class for authentication-related errors (never shown to the user).
    BR: Classe base para erros de autenticação (nunca exibidos ao usuário).
    """
    pass

class AuthFailed(AuthError):
    """
    EN: Generic authentication failure (bad credentials or unverified).
    BR: Falha genérica de autenticação (credenciais inválidas ou não verificado).
    """
    pass

class UnverifiedUser(AuthError):
    """
    EN: User exists but is not verified (map to same 401 response).
    BR: Usuário existe, mas não está verificado (mesma resposta 401).
    """
    pass

class AccountLocked(AuthError):
    """
    EN: Account locked due to policy (throttling, admin lock, etc.).
    BR: Conta bloqueada por política (limite, bloqueio administrativo, etc.).
    """