from sqlalchemy import Column, Integer, String
from database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)