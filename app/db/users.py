from sqlalchemy import Column , String, Text, DateTime, func, UUID
from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_true= True), primary_key=True, index=True, server_default=func.gen_random_uuid())
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password= Column(String, nullable= False)
    created_at = Column(DateTime(timezone=True),  nullable=False , server_default= func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False , server_default= func.now(), onupdate=func.now())
