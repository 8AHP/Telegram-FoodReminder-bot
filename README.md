# Telegram Lunch Reminder Bot

## Project Overview

The **Telegram Lunch Reminder Bot** is a simple Telegram-based automation tool designed to remind users to order their university lunch for the upcoming week. It runs daily and sends a reminder message **at 10:00 AM UTC+3:30 every Wednesday**, ensuring you and your group never miss the order deadline!

---

## Features

- 📅 **Weekly Reminder**: Sends a Telegram message at 10:00 AM (your local time: UTC+3:30) every Wednesday.
- 🔗 **Telegram Bot API**: Built with secure communication, the bot interacts directly with Telegram's HTTP API.
- 🔒 **Environment Configuration**: Tokens and file paths are configurable via `.env` files for deployment security.

---

## How It Works

1. **Bot Automation**:
   - The bot runs in the background on a server or task scheduler.
   - It sends the **lunch reminder message** to all subscribed users weekly.
   
2. **Reminder Logic**:
   - **Trigger Time**: The script triggers a notification every **Wednesday at 10:00 AM**.
   - Reads from a list of subscribers stored in `subscribers.json`.
   - Sends a message to all users in the list using Telegram’s Bot API.

3. **Message Example**:
    ```
    🍽️ It's Wednesday! Time to order next week's lunch! 
    Don't skip it, gang. Your future self will thank you 🙏.
    ```

---

## Installation and Setup

For setting up the Telegram Lunch Reminder Bot, follow these steps:

### Prerequisites
1. **Python 3.8+**: Ensure Python is installed on your system.
2. **Bot Token**: Obtain a Telegram Bot Token using [BotFather](https://core.telegram.org/bots#botfather).
3. **Server/Task Scheduler**: Deploy the script to a server or set it up as a cron job for scheduled execution.

---

### Steps to Install

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/8AHP/Telegram-FoodReminder-Bot.git
   cd Telegram-FoodReminder-Bot
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up `.env` File**:
   - Create a `.env` file by copying the provided `.env.example`:
     ```bash
     cp .env.example .env
     ```
   - Update the `TG_BOT_TOKEN` variable with your bot token:
     ```env
     TG_BOT_TOKEN="your-telegram-bot-api-token"
     ```

4. **Subscribe Users**:
   - Manually update the `subscribers.json` file or let users subscribe via a bot listener.

5. **Schedule the Bot**:
   - Use cron or task schedulers to execute `lunch_reminder.py` at 10:00 AM every Wednesday.
   - Example for crontab:
     ```bash
     30 6 * * 3 python3 /path-to-bot/lunch_reminder.py
     ```

---

## Environment Variables

The bot uses an `.env` file for secure configuration:
- **`TG_BOT_TOKEN`**: Telegram Bot Token
- **`SUBS_FILE`**: Path to the JSON file where subscriber chat IDs are stored (default: `/home/8HP/subscribers.json`).

### `.env Example`:
```dotenv
# Telegram Bot API token
TG_BOT_TOKEN="your-bot-token-here"

# Path to subscribers.json file
SUBS_FILE="/path/to/subscribers.json"
```

---

## File Overview

### 1. `lunch_reminder.py`
- Responsible for:
  - Sending predefined reminder messages to all subscribers **only on Wednesday**.
- Reads:
  - `subscribers.json` for user IDs.
  - `.env` for token configuration.

### 2. `bot_listener.py`
- Optional entry point for user-subscription handling (e.g., `/start` command).

### 3. `.env` and `.env.example`
- `.env`: Local configuration file (excluded from version control).
- `.env.example`: Template for your `.env` file.

### 4. `subscribers.json`
- Stores user chat IDs for reminders.

---

## Support

If you encounter issues:
- Ensure the bot token in `.env` is correct and the bot is active.
- Confirm that `subscribers.json` is read/write accessible by the bot.
- Use a reliable task scheduler (like cron).

---

Stay fed, stay productive! 🍽️