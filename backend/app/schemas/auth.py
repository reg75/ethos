from pydantic import BaseModel, EmailStr
from typing import Optional

# EN: Schema for user registration request via API
# BR: Esquema para... através da API
class AuthRegisterRequest(BaseModel):

   email: EmailStr 
   school_id: int
   password: str

# EN: Schema for user registration response via API
# BR: Esquema para... através da API
class AuthRegisterResponse(BaseModel):

   id: int
   email: EmailStr 
   school_id: int
   
   class Config:
      orm_mode = True

# EN: Schema for login request  via API
# BR: Esquema para... através da API
class AuthLoginRequest(BaseModel):

   email: EmailStr 
   password: str
   
# EN: Schema to get user details via API
# BR: Esquema para... através da API
class AuthMeResponse(BaseModel):

   id: int
   school_id: int
   first_name: Optional[str] = None
   last_name: Optional[str] = None
   email: EmailStr 
   user_role: int
   is_active: bool
   
   class Config:
      orm_mode = True

# EN: Schema for login response  via API
# BR: Esquema para... através da API
class AuthLoginResponse(BaseModel):

   access_token: str 
   token_type: str="bearer"
   user: AuthMeResponse

   class Config:
      orm_mode = True

# EN: Schema to get request logout via API
# BR: Esquema para... através da API
class AuthLogoutResponse(BaseModel):

   detail: str="Successfully logged out!"
      
   class Config:
      orm_mode = True

# EN: Schema for password reset request  via API
# BR: Esquema para... através da API
class AuthResetRequest(BaseModel):

   email: EmailStr 

# EN: Schema for password reset response  via API
# BR: Esquema para... através da API
class AuthResetResponse(BaseModel):

   detail: str="If the email exists, a password reset link has been sent."

   class Config:
      orm_mode = True

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

   class Config:
      orm_mode = True