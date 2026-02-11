from fastapi import APIRouter, Form, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import Employee
from app.utils.password import verify_password
from app.utils.jwt import create_access_token
from app.database import get_db

router = APIRouter()

@router.get("/login")
async def login(username: str = Form(...),
                password: str = Form(...),
                db: Session = Depends(get_db)):
    user = db.query(Employee).filter(Employee.username == username).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    token = create_access_token({
        "sub": str(user.id),
        "role": user.role
    })
    return {"access_token": token}
