import bcrypt
import string
from typing import Union

def check_min_pw_length(password, min_length=8):
   return len(password) >= min_length

def check_max_pw_length(password, max_length=64):
   return len(password) <= max_length

def check_lower(password):
   return any(char in string.ascii_lowercase for char in password)

def check_uppercase(password):
   return any(char in string.ascii_uppercase for char in password)

def check_digits(password):
   return any(char in string.digits for char in password)

def check_special_characters(password):
   return any(char in string.punctuation for char in password)

def hash_string(password: str) -> str:
   pw_bytes = password.encode('utf-8')
   salt = bcrypt.gensalt()
   hashed = bcrypt.hashpw(pw_bytes, salt)
   return hashed.decode('utf-8')

def validate_password(password: str) -> Union[bool,str]:
   if not check_min_pw_length(password):
      return "Password is too short"
   if not check_max_pw_length(password):
      return "Password is too long"

   if not (
      check_lower(password)
      and check_uppercase(password)
      and check_digits(password)
      and check_special_characters(password)
      ):
         return "Password must contain an uppercase letter, a lower case letter, a digit, and a special character."
   return True

def hash_validated_password(password: str) -> Union[str, str]:
   result = validate_password(password)

   if result is True:
      return hash_string(password)
   else:
      return result
   
