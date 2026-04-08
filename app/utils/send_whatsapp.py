import requests

ACCESS_TOKEN = "token"
PHONE_NUMBER_ID = "phone_number_id"

def send_whatsapp_message(phone: str, message: str):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": phone,
        "type": "text",
        "text": {"body": message}
    }

    res = requests.post(url, headers=headers, json=data)

    return res.json()

def send_messages(numbers, message):
    for phone_number in numbers:
        try:
            res = send_whatsapp_message("20"+phone_number, message)
            print(phone_number, res)
        except Exception as e:
            print("Failed sending to ", phone_number, e)