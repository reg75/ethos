from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# EN: Schema for creating new observation via API
# BR: Esquema para criar uma nova observação através da API
class Create_Observation(BaseModel):

   Observation_Teacher: int 
   Observation_Class: str
   Observation_Focus: str
   Observation_Strengths: Optional[str]
   Observation_Weaknesses: Optional[str]
   Observation_Comments: Optional[str]

   class Config:
      orm_mode = True