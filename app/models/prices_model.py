from sqlalchemy import Column, Integer, String, Numeric
from database import Base

class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    category = Column(String, nullable=False)
    name = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)