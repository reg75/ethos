from pydantic import BaseModel, EmailStr
from typing import Optional

# EN: Schema for user registration request via API
# BR: Esquema para cadastro de usuário atravésvia da API
class AuthRegisterRequest(BaseModel):

   email: EmailStr 
   school_id: int
   password: str

# EN: Schema for user registration response via API
# BR: Esquema para resposta de cadastro de usuário via API
class AuthRegisterResponse(BaseModel):

   id: int
   email: EmailStr 
   school_id: int
   
   model_config = {
      "from_attributes": True
   }
   
# EN: Schema for login request  via API
# BR: Esquema para... através da API
class AuthLoginRequest(BaseModel):

   email: EmailStr 
   password: str
   remember_me: bool = False
   
# EN: Schema to get user details via API
# BR: Esquema para... através da API
class AuthMeResponse(BaseModel):

   id: int
   school_id: int
   first_name: Optional[str] = None
   last_name: Optional[str] = None
   email: EmailStr 
   user_role_id: int
   is_active: bool
   
   model_config = {
      "from_attributes": True
   }

# EN: Schema for login response  via API
# BR: Esquema para... através da API
class AuthLoginResponse(BaseModel):

   ok: bool = True
   user: AuthMeResponse

# EN: Schema to get request logout via API
# BR: Esquema para... através da API
class AuthLogoutResponse(BaseModel):

   ok: bool = True

# EN: Schema for password reset request  via API
# BR: Esquema para... através da API
class AuthResetRequest(BaseModel):

   email: EmailStr 

# EN: Schema for password reset response  via API
# BR: Esquema para... através da API
class AuthResetResponse(BaseModel):

   detail: str="If the email exists, a password reset link has been sent."

   model_config = {
      "from_attributes": True
   }

# EN: Schema for complete password reset (request)  via API
# BR: Esquema para... através da API
class AuthCompleteResetRequest(BaseModel):

   token: str
   new_password: str 

# EN: Schema for complete password reset (response)  via API
# BR: Esquema para... através da API
class AuthCompleteResetResponse(BaseModel):

   detail: str="Your password has been changed."
   access_token: str
   token_type: str="bearer"
   user: AuthMeResponse

   model_config = {
      "from_attributes": True
   }