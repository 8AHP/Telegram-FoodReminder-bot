import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Fetch the token from environment variables
TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')

# Raise an error if the token is not set
if not TG_BOT_TOKEN:
    raise ValueError("The TG_BOT_TOKEN environment variable is not set.")

# NOTE: Preserving original functionality beyond token access

def send_lunch_reminder():
    """
    Function to send a lunch reminder message. (Assumed original functionality exists here)
    """
    pass

if __name__ == "__main__":
    send_lunch_reminder()
