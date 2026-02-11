from sqlalchemy import select
from database import SessionLocal
from models.employees import  Employee
from sqlalchemy.exc import IntegrityError
from app.utils.password import hash_password

name = "Ahmed"
username = "captain_ahmed@admin"
password = "password123"
phone_number = "01146494815"
role = "admin"

session = SessionLocal()

try:
    stmt = select(Employee.id).where(Employee.username == username, Employee.role == "admin")
    current_admin = session.execute(stmt).first()

    if current_admin:
        raise ValueError("admin already exists")

    new_admin = Employee(
        name = name,
        username=username,
        password=hash_password(password),
        phone_number=phone_number,
        role=role
    )

    session.add(new_admin)
    session.commit()
    session.refresh(new_admin)

    print(f"Admin {username} was added successfuly.")

except IntegrityError:
    session.rollback()
    raise ValueError("admin already exists")

finally:
    session.close()

