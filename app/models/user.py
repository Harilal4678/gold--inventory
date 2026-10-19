from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.database import Base

class User(Base):
    __tablename__= "users"
    
    id =  Column(Integer,primary_key=True,index=True)
    tenant_id=Column(Integer,ForeignKey("tenants.id"),nullable=False, index=True)
    fullname= Column(String(150),nullable=False)
    email=Column(String(150),unique=True,nullable=False,index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(30), nullable=False, default="staff")
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    
    