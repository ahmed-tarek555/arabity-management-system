from fastapi import APIRouter, Form, Depends, HTTPException, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from utils.customers import add_customer, edit_customer, delete_customer
from utils.auth import get_current_user
from models.customers_model import Customer
from database import get_db

templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix="/customers")

@router.post("/add_customer")
def add_customers(request: Request,
                  name: str = Form(...),
                  phone_number: str = Form(...),
                  db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Missing token")
    payload = get_current_user(token)
    if payload["role"] not in ("admin", "manager"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized request")

    customer = add_customer(db, name, phone_number, was_called=False)
    return {"detail": "Added Successfully"}

@router.patch("/edit_customer/{id}")
def edit_customers(request: Request,
                   id: str,
                   name: str = Form(None),
                   phone_number: str = Form(None),
                   db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Missing token")
    payload = get_current_user(token)
    if payload["role"] not in ("admin", "manager"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized request")

    customer = edit_customer(db, id, name, phone_number, was_called=None)
    return {"details": "Success"}