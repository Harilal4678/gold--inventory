from sqlalchemy import  String, Boolean, Column, func, Integer, DateTime

from app.database import Base

class tenant(Base):
    
    __tablename__= "tenants"
    
    id = Column(Integer,index=True,primary_key=True)
    name=Column(String(150),nullable =False)
    email=Column(String(150),nullable=False,index=True)
    phone=Column(String(150),nullable=True)
    is_active=Column(Boolean,nullable=False,default=True,server_default="true")
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    
    
    
    
    