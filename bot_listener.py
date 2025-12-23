import os
from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
if not TG_BOT_TOKEN:
    raise EnvironmentError("'TG_BOT_TOKEN' environment variable is not set!")

bot = Bot(token=TG_BOT_TOKEN)
updater = Updater(bot=bot, use_context=True)


##############################
# Your other bot code here! #
##############################