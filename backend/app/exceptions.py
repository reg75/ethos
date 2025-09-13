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

