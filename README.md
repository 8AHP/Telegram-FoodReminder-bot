# Telegram Food Reminder Bot

## Project Overview
The **Telegram Food Reminder Bot** is your virtual assistant for keeping track of your perishable food items. This bot helps you reduce food waste by reminding you when your stored food items are nearing their expiration dates. Built to work seamlessly with Telegram, this bot makes managing your food inventory easy and accessible.

## Features
- **Add Food Items**: Allows users to add food items along with their expiration dates.
- **Notifications**: Sends Telegram reminders before food items expire.
- **Categorization**: Organize food items into categories like fruits, vegetables, dairy, etc.
- **Edit/Delete Entries**: Update or remove items from your list as needed.
- **Easy Setup**: Simple commands to interact with the bot.

## Installation Steps
Follow these steps to set up the bot:

### Prerequisites
1. **Python 3.x**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).
2. **Telegram Account**: Create a Telegram account if you don't already have one.
3. **Bot Token**: Get a bot token from the [BotFather](https://core.telegram.org/bots#botfather) on Telegram.

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/8AHP/Telegram-FoodReminder-Bot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Telegram-FoodReminder-Bot
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root directory, and add your bot token:
   ```env
   BOT_TOKEN=<Your_Telegram_Bot_Token>
   ```
5. Run the bot:
   ```bash
   python bot.py
   ```

The bot will now be running, and you can interact with it on Telegram by searching for your bot name.

## Usage Instructions
Here’s how you can use the bot:

1. **Start the Bot:**
   Send `/start` to initialize a session with the bot.

2. **Add Food Items:**
   Use the `/add` command and provide details about the food item, e.g.,
   ```
   /add Milk 2025-12-31
   ```
   This adds milk with an expiration date of December 31, 2025.

3. **View Food List:**
   Use the `/list` command to see all your tracked food items:
   ```
   /list
   ```

4. **Update an Item:**
   Use the `/update` command with the item name and updated details:
   ```
   /update Milk 2025-12-25
   ```

5. **Delete an Item:**
   Remove an item by using:
   ```
   /delete Milk
   ```

6. **Help:**
   To see all available commands, send:
   ```
   /help
   ```

## Troubleshooting

If you encounter any issues, here are some common solutions:

- **Bot Not Responding**: Ensure the bot is running and your bot token is correct in the `.env` file.
- **Dependency Errors**: Check if all required dependencies are installed by running:
  ```bash
  pip install -r requirements.txt
  ```
- **Permission Issues**: Ensure your Telegram account has access to the bot.
- **Date Format Issues**: Always use `YYYY-MM-DD` for dates to avoid parsing errors.

For further assistance, feel free to open an issue in the repository.

---

Happy tracking! Reduce food waste and save money by keeping your kitchen organized with the Telegram Food Reminder Bot.