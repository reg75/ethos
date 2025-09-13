from fastapi.responses import RedirectResponse

SECURE_REDIRECT_HEADERS = {
               "Referrer-Policy": "no-referrer",
               "Cache-Control": "no-store",
               "Pragma": "no-cache",
            }

def redirect(url: str, status_code: int = 303) -> RedirectResponse:
    """
    EN: Return a secure redirect response (303 by default) with safe headers.
    BR: Retorna uma resposta de redirecionamento segura (303 por padrão) com cabeçalhos de segurança.
    """
    return RedirectResponse(
            url=url,
            status_code=status_code,
            headers=SECURE_REDIRECT_HEADERS,
    )
