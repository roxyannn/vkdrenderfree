import requests
import time
import threading
import random
from flask import Flask

TOKEN = "vk1.a.NpKmjOcxJbGbDJusuJvp7B5UF1RmcNxlT7rrkgp34Z5gnndkPHmak0cd41MS-hMnEROVDek9chaGqRFmS_dcIMI_lZAWR5shvsldPLysegGaCiq3yyYf44TywtLIfwkuv8JDM0x8ZiAj-LG0WA0Mdx8KunrOKZyYAoS6oq9oytbpFd3qUXYzdlsH1Aw5j8bJW5aPJaCnpsJ5XW1UUc7_xQ"
CHAT_ID = 2000000353
API_VERSION = "5.199"
MANUAL_PAYLOAD = '{"button":"daiving"}'

app = Flask(__name__)

def send_message(text=".", payload=None):
    url = "https://api.vk.com/method/messages.send"
    params = {
        "access_token": TOKEN,
        "v": API_VERSION,
        "peer_id": CHAT_ID,
        "random_id": random.randint(1, 2**63-1),
        "message": text
    }
    if payload:
        params["payload"] = payload
    r = requests.post(url, params=params).json()
    print("send_message response:", r, flush=True)
    return r

def diving_loop():
    while True:
        send_message("дайвинг")
        time.sleep(2)
        send_message(".", payload=MANUAL_PAYLOAD)
        time.sleep(605)

@app.before_first_request
def activate_job():
    t = threading.Thread(target=diving_loop, daemon=True)
    t.start()
    print("diving_loop started", flush=True)

@app.route("/")
def home():
    return "Bot is running!"
