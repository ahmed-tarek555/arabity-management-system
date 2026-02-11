from sqlalchemy.orm import Session
from app.models.customers import Customer

def add_customer(db: Session,
                 name: str,
                 phone_number: str,
                 ):

    customer = db.query(Customer).filter(Customer.phone_number == phone_number).first()
    if customer:
        raise ValueError("phone number already exist")

    new_customer = Customer(
        name=name,
        phone_number=phone_number
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

def edit_customer(
    db: Session,
    id: int,
    name: str = None,
    phone_number: str = None
):
    customer = db.query(Customer).filter(Customer.id == id).first()
    if not customer:
        return None

    if name is not None:
        customer.name = name
    if phone_number is not None:
        customer.phone_number = phone_number

    db.commit()
    db.refresh(customer)
    return customer