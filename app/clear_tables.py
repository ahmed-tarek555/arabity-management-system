from sqlalchemy import delete
from app.models.employees import Employee
from app.database import  SessionLocal

session = SessionLocal()

try:
    session.execute(delete(Employee))
    session.commit()
finally:
    session.close()