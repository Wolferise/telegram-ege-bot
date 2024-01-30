from dotenv import load_dotenv
from logger import Logger
import os
import telebot
# load secrets from .env
load_dotenv()
# initialize telegram bot backend and logger instance
bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"), parse_mode=None)
logger = Logger()


# message handling functions
@bot.message_handler(commands=['start'])
@logger.crash_log
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nЗадачи на какую тему вас интересуют?"
  markup = telebot.types.InlineKeyboardMarkup()
  button_planim = telebot.types.InlineKeyboardButton(text = 'планиметрия', callback_data='1')
  markup.add(button_planim)
  button_vector = telebot.types.InlineKeyboardButton(text='Векторы', callback_data='2')
  markup.add(button_vector)
  button_sterio = telebot.types.InlineKeyboardButton(text='Стереометрия', callback_data='3')
  markup.add(button_sterio)
  button_terver = telebot.types.InlineKeyboardButton(text='Начала теории вероятностей', callback_data='4')
  markup.add(button_terver)
  button_no = telebot.types.InlineKeyboardButton(text='Мне это не нужно!', callback_data='no')
  markup.add(button_no)
  bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(func=lambda m: True)
@logger.crash_log
def echo_all(message):
    bot.reply_to(message, message.text)
    logger.log('INFO', 'replied to message ' + message.text)

# main code
bot.infinity_polling()