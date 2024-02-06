from dotenv import load_dotenv
from logger import Logger
import os
import telebot
import buttons
import messages
# load secrets from .env
load_dotenv()
# initialize telegram bot backend and logger instance
bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"), parse_mode=None)
logger = Logger()


# message handling functions
@bot.message_handler(commands=['start'])
@logger.crash_log
def theme_selection(message):
  bot_response = messages.greeting(message.from_user.first_name, message.from_user.last_name)
  markup = telebot.types.InlineKeyboardMarkup()
  for button in buttons.start:
      markup.add(telebot.types.InlineKeyboardButton(text=button['text'], callback_data=button['callback_data']))
  bot.send_message(message.chat.id, bot_response, parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
@logger.crash_log
def theme_selection_response(function_call):
  if function_call.message:
     if function_call.data == "1":
        second_mess = "О! Это хорошая и очень интересная тема! У неё есть несколько подтем:"
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Решение прямоугольного треугольника", url="https://math-ege.sdamgia.ru/test?theme=79"))
        markup.add(telebot.types.InlineKeyboardButton("Решение равнобедренного треугольника", url="https://math-ege.sdamgia.ru/test?theme=90"))
        markup.add(telebot.types.InlineKeyboardButton("Треугольники общего вида", url="https://math-ege.sdamgia.ru/test?theme=96"))
        markup.add(telebot.types.InlineKeyboardButton("Параллелограммы", url="https://math-ege.sdamgia.ru/test?theme=102"))
        markup.add(telebot.types.InlineKeyboardButton("Трапеция", url="https://math-ege.sdamgia.ru/test?theme=94"))
        markup.add(telebot.types.InlineKeyboardButton("Центральные и вписанные углы", url="https://math-ege.sdamgia.ru/test?theme=111"))
        markup.add(telebot.types.InlineKeyboardButton("Касательная, хорда, секущая", url="https://math-ege.sdamgia.ru/test?theme=112"))
        markup.add(telebot.types.InlineKeyboardButton("Вписанные окружности", url="https://math-ege.sdamgia.ru/test?theme=113"))
        markup.add(telebot.types.InlineKeyboardButton("Описанные окружности", url="https://math-ege.sdamgia.ru/test?theme=114"))
        bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        bot.answer_callback_query(function_call.id)
     elif function_call.data == "2":
        second_mess = "По этой теме только 1 тип задач:"
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Векторы и операции с ними", url="https://math-ege.sdamgia.ru/test?theme=182"))
        bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
     elif function_call.data == "3":
        second_mess = "Это немаловажные темы!"
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Куб", url="https://math-ege.sdamgia.ru/test?theme=192"))
        markup.add(telebot.types.InlineKeyboardButton("Прямоугольный параллелепипед", url="https://math-ege.sdamgia.ru/test?theme=193"))
        markup.add(telebot.types.InlineKeyboardButton("Элементы составных многогранников", url="https://math-ege.sdamgia.ru/test?theme=180"))
        markup.add(telebot.types.InlineKeyboardButton("Площадь поверхности составного многогранника", url="https://math-ege.sdamgia.ru/test?theme=148"))
        markup.add(telebot.types.InlineKeyboardButton("Объем составного многогранника", url="https://math-ege.sdamgia.ru/test?theme=140"))
        markup.add(telebot.types.InlineKeyboardButton("Призма", url="https://math-ege.sdamgia.ru/test?theme=178"))
        markup.add(telebot.types.InlineKeyboardButton("Пирамида", url="https://math-ege.sdamgia.ru/test?theme=177"))
        markup.add(telebot.types.InlineKeyboardButton("Комбинации тел", url="https://math-ege.sdamgia.ru/test?theme=197"))
        markup.add(telebot.types.InlineKeyboardButton("Цилиндр", url="https://math-ege.sdamgia.ru/test?theme=194"))
        markup.add(telebot.types.InlineKeyboardButton("Конус", url="https://math-ege.sdamgia.ru/test?theme=144"))
        markup.add(telebot.types.InlineKeyboardButton("Шар", url="https://math-ege.sdamgia.ru/test?theme=151"))
        bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
     elif function_call.data == "4":
        second_mess = "По этой теме только 1 тип задач:"
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Классическое определение вероятности", url="https://math-ege.sdamgia.ru/test?theme=166"))
        bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
     elif function_call.data == "5":
        second_mess = "Теория вероятностей может казаться сложной, но вам только кажется!"
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Теоремы о вероятностях событий", url="https://math-ege.sdamgia.ru/test?theme=185"))
        markup.add(telebot.types.InlineKeyboardButton("Новые задания банка MathЕГЭ", url="https://math-ege.sdamgia.ru/test?theme=265"))
        bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
     elif function_call.data == "6":
        second_mess = "Это простые уравнения!"
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Линейные, квадратные, кубические уравнения", url="https://math-ege.sdamgia.ru/test?theme=14"))
        markup.add(telebot.types.InlineKeyboardButton("Рациональные уравнения", url="https://math-ege.sdamgia.ru/test?theme=9"))
        markup.add(telebot.types.InlineKeyboardButton("Иррациональные уравнения", url="https://math-ege.sdamgia.ru/test?theme=10"))
        markup.add(telebot.types.InlineKeyboardButton("Показательные уравнения", url="https://math-ege.sdamgia.ru/test?theme=11"))
        markup.add(telebot.types.InlineKeyboardButton("Логарифмические уравнения", url="https://math-ege.sdamgia.ru/test?theme=12"))
        markup.add(telebot.types.InlineKeyboardButton("Тригонометрические уравнения", url="https://math-ege.sdamgia.ru/test?theme=13"))
        bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
     elif function_call.data == "7":
        second_mess = "Обычная алгебра"
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Преобразования числовых рациональных выражений", url="https://math-ege.sdamgia.ru/test?theme=55"))
        markup.add(telebot.types.InlineKeyboardButton("Преобразования алгебраических выражений и дробей", url="https://math-ege.sdamgia.ru/test?theme=60"))
        markup.add(telebot.types.InlineKeyboardButton("Вычисление значений степенных выражений", url="https://math-ege.sdamgia.ru/test?theme=57"))
        markup.add(telebot.types.InlineKeyboardButton("Действия со степенями", url="https://math-ege.sdamgia.ru/test?theme=62"))
        markup.add(telebot.types.InlineKeyboardButton("Преобразования числовых иррациональных выражений", url="https://math-ege.sdamgia.ru/test?theme=56"))
        markup.add(telebot.types.InlineKeyboardButton("Преобразования буквенных иррациональных выражений", url="https://math-ege.sdamgia.ru/test?theme=61"))
        markup.add(telebot.types.InlineKeyboardButton("Преобразования числовых логарифмических выражений", url="https://math-ege.sdamgia.ru/test?theme=58"))
        markup.add(telebot.types.InlineKeyboardButton("Преобразования буквенных логарифмических выражений", url="https://math-ege.sdamgia.ru/test?theme=63"))
        markup.add(telebot.types.InlineKeyboardButton("Вычисление значений тригонометрических выражений", url="https://math-ege.sdamgia.ru/test?theme=65"))
        markup.add(telebot.types.InlineKeyboardButton("Преобразования числовых тригонометрических выражений", url="https://math-ege.sdamgia.ru/test?theme=59"))
        markup.add(telebot.types.InlineKeyboardButton("Преобразования буквенных тригонометрических выражений", url="https://math-ege.sdamgia.ru/test?theme=64"))
        bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
     elif function_call.data == "8":
        second_mess = "Это может вызывать трудности!"
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Физический смысл производной", url="https://math-ege.sdamgia.ru/test?theme=69"))
        markup.add(telebot.types.InlineKeyboardButton("Геометрический смысл производной, касательная", url="https://math-ege.sdamgia.ru/test?theme=68"))
        markup.add(telebot.types.InlineKeyboardButton("Применение производной к исследованию функций", url="https://math-ege.sdamgia.ru/test?theme=70"))
        markup.add(telebot.types.InlineKeyboardButton("Первообразная", url="https://math-ege.sdamgia.ru/test?theme=183"))
        bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
     elif function_call.data == "9":
        second_mess = "можем пожелать удачи!"
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Линейные уравнения и неравенства", url="https://math-ege.sdamgia.ru/test?theme=71"))
        markup.add(telebot.types.InlineKeyboardButton("Квадратные и степенные уравнения и неравенства", url="https://math-ege.sdamgia.ru/test?theme=72"))
        markup.add(telebot.types.InlineKeyboardButton("Рациональные уравнения и неравенства", url="https://math-ege.sdamgia.ru/test?theme=76"))
        markup.add(telebot.types.InlineKeyboardButton("Иррациональные уравнения и неравенства", url="https://math-ege.sdamgia.ru/test?theme=77"))
        markup.add(telebot.types.InlineKeyboardButton("Показательные уравнения и неравенства", url="https://math-ege.sdamgia.ru/test?theme=73"))
        markup.add(telebot.types.InlineKeyboardButton("Логарифмические уравнения и неравенства", url="https://math-ege.sdamgia.ru/test?theme=74"))
        markup.add(telebot.types.InlineKeyboardButton("Тригонометрические уравнения и неравенства", url="https://math-ege.sdamgia.ru/test?theme=75"))
        markup.add(telebot.types.InlineKeyboardButton("Разные задачи", url="https://math-ege.sdamgia.ru/test?theme=184"))
        bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
     elif function_call.data == "10":
        second_mess = "Это сложно, но интересно!"
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("Задачи на проценты, сплавы и смеси", url="https://math-ege.sdamgia.ru/test?theme=88"))
        markup.add(telebot.types.InlineKeyboardButton("Задачи на движение по прямой", url="https://math-ege.sdamgia.ru/test?theme=84"))
        markup.add(telebot.types.InlineKeyboardButton("Задачи на движение по окружности", url="https://math-ege.sdamgia.ru/test?theme=85"))
        markup.add(telebot.types.InlineKeyboardButton("Задачи на движение по воде", url="https://math-ege.sdamgia.ru/test?theme=86"))
        markup.add(telebot.types.InlineKeyboardButton("Задачи на совместную работу", url="https://math-ege.sdamgia.ru/test?theme=87"))
        markup.add(telebot.types.InlineKeyboardButton("Задачи на прогрессии", url="https://math-ege.sdamgia.ru/test?theme=89"))
        bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
     elif function_call.data == "no":
        second_mess = "Просто перейди по ссылке:"
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton("А вот и ссылка:" , url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
        bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
      '''
     bot_response = messages.theme_select_response[function_call.data]
     markup = telebot.types.InlineKeyboardMarkup()
     for button in buttons.theme_response[function_call.data]:
        markup.add(telebot.types.InlineKeyboardButton(text=button['text'],
                                                      url=button['url']))
        bot.send_message(function_call.message.chat.id, bot_response, reply_markup=markup)
     '''
          

@bot.message_handler(func=lambda m: True)
@logger.crash_log
def echo_all(message):
    bot.reply_to(message, message.text)
    logger.log('INFO', 'replied to message ' + message.text)

# main code
bot.infinity_polling()