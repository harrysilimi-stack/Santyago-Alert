import requests
from config import TOKEN, CHAT_ID


def send_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": f"⚠️ Santyago Alert\n\n{message}"
    }

    requests.post(url, data=data)

    print("Alert Sent")
