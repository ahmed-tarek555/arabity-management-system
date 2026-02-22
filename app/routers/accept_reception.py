from fastapi import APIRouter, HTTPException, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import get_db
from utils.auth import get_current_user
from utils.receiving import save_form, approve_form
from utils.pdf import generate_receiving_form_pdf
from models.receivingForms_model import ReceivingForm

router = APIRouter(prefix="/accept")
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def get_receiving_page(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Missing token")
    payload = get_current_user(token)
    if payload["role"] not in ("admin", "manager"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")

    return templates.TemplateResponse("accept-reception.html", {"request": request})
