from sqlalchemy import Column, Integer, String,Float
from datetime import datetime
from .database import Base

class Memo(Base):
    __tablename__ = "memo"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(20),nullable=False)
    content = Column(String(50),nullable=False)