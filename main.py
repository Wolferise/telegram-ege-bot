from logger import Logger
from dotenv import load_dotenv
import os
import telebot

# load secrets from .env
load_dotenv()
# initialize telegram bot backend and logger instance
bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"), parse_mode=None)
logger = Logger()


# message handling functions

@bot.message_handler(func=lambda m: True)
@logger.crash_log
def echo_all(message):
    bot.reply_to(message, message.text)
    logger.log('INFO', 'replied to message ' + message.text)

# main code
bot.infinity_polling()
