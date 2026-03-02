from sqlalchemy import Column, Integer, String, Date, Boolean, Numeric, ForeignKey
from database import Base

class ReceivingForm(Base):
    __tablename__ = "receiving_forms"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    day = Column(String, nullable=False)
    current_date = Column(Date, nullable=False)
    customer_name = Column(String, nullable=False)
    receive_date = Column(Date, nullable=False)
    customer_phone_number = Column(String, nullable=False)
    customer_email = Column(String, nullable=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    color = Column(String, nullable=False)
    chassis_number = Column(String, nullable=False)
    plate_number = Column(String, nullable=False)
    mileage = Column(Numeric(12, 2), nullable=False)
    category = Column(String, nullable=False)
    fix_description = Column(String, nullable=False)
    total_price = Column(String, nullable=False)
    remains = Column(Numeric(12, 2), nullable=True)
    total_paid = Column(Numeric(12, 2), nullable=False)
    notes = Column(String, nullable=True)
    employee_name = Column(String, nullable=False)
    approved = Column(Boolean, nullable=False)
    repr_message = Column(String, nullable=True)
    taken_by = Column(Integer, ForeignKey("employees.id"), nullable=True)
    pdf_url = Column(String, nullable=True)
