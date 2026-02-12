from fastapi import APIRouter, Form, Header, Depends, HTTPException, status
from sqlalchemy.orm import Session
from decimal import Decimal
from app.utils.add_edit_employee import add_employee
from app.utils.auth import get_current_user
from app.database import get_db

router = APIRouter()

@router.post("/add_employee")
def add_employees(
                authorization: str = Header(...),
                name: str = Form(...),
                username: str = Form(...),
                password: str = Form(...),
                phone_number: str = Form(...),
                role: str = Form(...),
                salary: Decimal = Form(...),
                target: int = Form(...),
                db: Session = Depends(get_db)):

    token = authorization.replace("Bearer ", "")
    payload = get_current_user(token)
    if payload["role"] not in ("admin", "manager"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized request")

    employee = add_employee(db, name, username, password, phone_number, role, salary, target)
    return {
        "id": employee.id,
        "name": employee.name,
        "username": employee.username
    }