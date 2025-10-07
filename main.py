import threading
import time
import random
import requests
from flask import Flask

# === НАСТРОЙКИ ===
TOKEN = "vk1.a......"   # ⚠️ сюда вставь свой VK токен
CHAT_ID = 2000000353    # peer_id чата
API_VERSION = "5.199"
MANUAL_PAYLOAD = '{"button":"daiving"}'

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
    print("send_message response:", r)
    return r

def diving_loop():
    while True:
        try:
            send_message("дайвинг")
            time.sleep(2)
            send_message(".", payload=MANUAL_PAYLOAD)
            sleep_time = 600 + random.randint(-30, 30)
            print(f"Ждём {sleep_time} секунд...")
            time.sleep(sleep_time)
        except Exception as e:
            print("Ошибка:", e)
            time.sleep(10)

# Flask-приложение для Render
app = Flask(__name__)

@app.route("/")
def home():
    return "VK бот работает!"

# Запуск фонового потока
threading.Thread(target=diving_loop, daemon=True).start()
