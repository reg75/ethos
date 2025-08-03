import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
from dotenv import load_dotenv

load_dotenv()

def send_automated_email(to_email: str, subject: str, message: str, content_type: str="text/html"):
   """
   EN: Sends an email using SendGrid. Supports HTML or plain text.
   BR: Envia um e-mail usando SendGrid. Suporta HTML ou texto simples.
   """
   
   from_email = os.getenv("DEFAULT_FROM_EMAIL", "no-reply@edify-app.co.uk")
   to_email = To(to_email)
   content = Content(content_type, message)
   mail = Mail(from_email, to_email, subject, content)

   try:
      sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
      response = sg.client.mail.send.post(request_body=mail.get())
      return response.status_code
   except Exception as e:
      raise RuntimeError(f"SendGrid Error: {e}")


def send_verification_email(to_email: str, token:str):
   """
   EN: Sends an email verfication link using SendGrid.
   BR: Envia um e-mail com link para verificação de e-mail.
   """
   
   # EN: Get the base URL for verification links from environment (fallback to localhost)
   # BR: Obtém a URL base dos links de verificação do ambiente (.env), ou usa localhost
   base_url = os.getenv("VERIFICATION_URL_BASE", "http://localhost:8000/auth/verify")
   
   # EN: Construct the full verification link with the token as a query parameter
   # BR: Monta o link completo de verificação com o token como parâmetro de consulta 
   verification_link = f"{base_url}?token={token}"
   
   # EN: Send the email using the helper function
   # BR: Envia o e-mail usando a função auxiliar
   send_automated_email(
      to_email=to_email,
      subject="Please verify your email",
      message= (
         f"<p>Thank you for registering with Edify.</p>"
         f"To verify your email please click <a href='{verification_link}'>here</a> or paste the link into your browser</p>"),
      content_type="text/html" # EN: Set content type to HTML / BR: Define o tipo de conteúdo como HTML
      )