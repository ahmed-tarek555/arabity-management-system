import requests
import os
import base64
from io import BytesIO

BREVO_API_KEY = "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"
BREVO_URL = "https://api.brevo.com/v3/smtp/email"

SENDER_EMAIL = "ahmeddad334@gmail.com"

def send_email(
    to: str,
    subject: str,
    body: str,
    pdf_stream: BytesIO | None = None,
):
    try:
        payload = {
            "sender": {
                "email": SENDER_EMAIL,
                "name": "Arabity",
            },
            "to": [{"email": to}],
            "subject": subject,
            "textContent": body,
        }

        if pdf_stream is not None:
            payload["attachment"] = [{
                "name": "form.pdf",
                "content": base64.b64encode(pdf_stream.getvalue()).decode(),
            }]

        headers = {
            "api-key": BREVO_API_KEY,
            "Content-Type": "application/json",
        }

        r = requests.post(
            BREVO_URL,
            json=payload,
            headers=headers,
            timeout=10,
        )

        if r.status_code >= 400:
            raise Exception(r.text)

        return

    except Exception as e:
        print("Email sending failed:", e)
        return