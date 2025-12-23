import os

TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')

# Previously present original logic and output messages for reminders
def send_lunch_reminder():
    if not TG_BOT_TOKEN:
        raise ValueError("Telegram Bot Token is not set. Please set the 'TG_BOT_TOKEN' environment variable.")

    # Your original logic to send lunch reminders goes here

    print("[Reminder] Time to grab your lunch! Don't forget to eat healthy.")

if __name__ == "__main__":
    try:
        send_lunch_reminder()
    except Exception as e:
        print(f"Error: {e}")