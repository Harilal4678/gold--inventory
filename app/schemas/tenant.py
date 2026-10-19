from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime


class tenantcreate(BaseModel):
    name : str
    email : EmailStr
    phone : str| None=None
    is_active:bool=True
    
    
class tenantResponse(BaseModel):
    id:int
    name:str
    phone : str| None=None
    is_active:bool=True
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
    
    
class tenantupdate(BaseModel):
    id: int
    name:str
    phone: str|None=None
    
    


    


    
    


    