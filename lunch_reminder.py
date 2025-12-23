# lunch_reminder.py - runs daily via Task
import json
import requests
import sys
from datetime import datetime
import os

TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
SUBS_FILE = "/home/8HP/subscribers.json"
API = f"https://api.telegram.org/bot{TG_BOT_TOKEN}"

# Previously present original logic and output messages for reminders
def send_lunch_reminder():
    if not TG_BOT_TOKEN:
        raise ValueError("Telegram Bot Token is not set. Please set the 'TG_BOT_TOKEN' environment variable.")

    # Only run on Wednesday
    if datetime.now().weekday() != 2:
        print("Not Wednesday. Skipping.")
        exit(0)

    try:
        with open(SUBS_FILE, "r") as f:
            chat_ids = json.load(f)
    except:
        print("No subscribers found.")
        exit(0)
    
    MESSAGE = "🍽️It's Wednesday!\nTime to order next week's lunch!\nDon't skip it gang.Your future self will thank you🙏."
    
    sent = 0
    for chat_id in chat_ids:
        try:
            resp = requests.post(f"{API}/sendMessage", data={"chat_id": chat_id, "text": MESSAGE})
            if resp.status_code == 200:
                sent += 1
            else:
                print(f"❌ Failed to send to {chat_id}: {resp.json()}")
        except Exception as e:
            print(f"💥 Error sending to {chat_id}: {e}")
    
    print(f"✅ Sent reminders to {sent}/{len(chat_ids)} users.")

if __name__ == "__main__":
    try:
        send_lunch_reminder()
    except Exception as e:
        print(f"Error: {e}")
