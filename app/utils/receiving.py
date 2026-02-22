from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.receivingForms_model import ReceivingForm
from datetime import date
from decimal import Decimal

def save_form(db: Session,
              day: str,
              current_date: date,
              customer_name: str,
              receive_date: date,
              customer_phone_number: str,
              customer_email: str,
              brand: str,
              model: str,
              color: str,
              chassis_number: str,
              plate_number: str,
              mileage: Decimal,
              category: str,
              fix_description: str,
              total_price: str,
              remains: Decimal,
              total_paid: Decimal,
              notes: str,
              employee_name: str,
              approved: bool):

    new_form = ReceivingForm(
        day=day,
        current_date=current_date,
        customer_name=customer_name,
        receive_date=receive_date,
        customer_phone_number=customer_phone_number,
        customer_email=customer_email,
        brand=brand,
        model=model,
        color=color,
        chassis_number=chassis_number,
        plate_number=plate_number,
        mileage=mileage,
        category=category,
        fix_description=fix_description,
        total_price=total_price,
        remains=remains,
        total_paid=total_paid,
        notes=notes,
        employee_name=employee_name,
        approved=approved
    )

    db.add(new_form)
    db.commit()
    db.refresh(new_form)
    return new_form

def approve_form(db: Session, id: int):
    form = db.query(ReceivingForm).filter(ReceivingForm.id == id).first()
    if not form:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="form doesn't exist")

    form.approved = True
    db.commit()
    db.refresh(form)
    return form
