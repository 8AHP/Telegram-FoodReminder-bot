# bot_listener.py - runs 24/7 in a Console
import json
import time
import requests
import sys
import os

sys.path.append('/home/8HP')
from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

from dotenv import load_dotenv
load_dotenv()  # Load variables from .env

TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
# Ensure that the environment variable is set correctly
if not TG_BOT_TOKEN:
    raise ValueError("TG_BOT_TOKEN is missing. Check your .env file.")

API = f"https://api.telegram.org/bot{TG_BOT_TOKEN}"
SUBS_FILE = os.environ.get("SUBS_FILE", "/home/8HP/subscribers.json")

bot = Bot(token=TG_BOT_TOKEN)
updater = Updater(bot=bot, use_context=True)

def get_updates(offset=None):
    params = {"timeout": 100, "offset": offset}
    try:
        resp = requests.get(f"{API}/getUpdates", params=params)
        return resp.json()
    except:
        return {"ok": False}

def save_subscriber(chat_id):
    # Load existing
    try:
        with open(SUBS_FILE, "r") as f:
            subs = json.load(f)
    except:
        subs = []

    # Avoid duplicates
    if chat_id not in subs:
        subs.append(chat_id)
        with open(SUBS_FILE, "w") as f:
            json.dump(subs, f)
        print(f"✅ New subscriber: {chat_id}")
    else:
        print(f"ℹ️ Already subscribed: {chat_id}")

def send_welcome(chat_id):
    msg = "✅ You're in!\nEvery Wed 10 AM, I'll remind ya!🎈"
    requests.post(f"{API}/sendMessage", data={"chat_id": chat_id, "text": msg})

# Main loop
print("Bot listener started.")
offset = None
while True:
    try:
        result = get_updates(offset)
        if result.get("ok") and result.get("result"):
            for update in result["result"]:
                offset = update["update_id"] + 1
                message = update.get("message")
                if message and "text" in message:
                    text = message["text"]
                    chat_id = message["chat"]["id"]
                    if text == "/start":
                        save_subscriber(chat_id)
                        send_welcome(chat_id)
        print("Bot listener Ended.")
        time.sleep(1)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
