# import telebot
# from currency_converter import CurrencyConverter
# from telebot import types
# import  requests
# import webbrowser
# from telebot import types
# import sqlite3
# # Конвертация валюты
# c = CurrencyConverter()
# amount = 0
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Добро пожаловать в бот-конвертер! Введите сумму конвертации')
#     bot.register_next_step_handler(message, summa)
#
# def summa(message):
#     global amount
#     try:
#         amount = int(message.text.strip())
#     except ValueError:
#         bot.send_message(message.chat.id, 'Неверный формат. Впишите сумму')
#         bot.register_next_step_handler(message, summa)
#         return
#
#     if amount >= 1:
#         markup = types.InlineKeyboardMarkup(row_width=2)
#         btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='USD/EUR')
#         btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='EUR/USD')
#         btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='USD/EUR')
#         btn4 = types.InlineKeyboardButton('Другое значение', callback_data='ELSE')
#         markup.add(btn1, btn2, btn3, btn4)
#         bot.send_message(message.chat.id, 'Выберите валютную пару', reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, 'Число должно быть больше 0. Впишите сумму')
#         bot.register_next_step_handler(message, summa)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.data != 'ELSE':
#         values = call.data.split('/')
#         res = c.convert(amount, values[0], values[1])
#         bot.send_message(call.message.chat.id, f'Получается: {round(res, 2)}, можете выполнять новый запрос')
#         bot.register_next_step_handler(call.message, summa)
#     else:
#         bot.send_message(call.message.chat.id, 'Введите пару значений через слэш')
#         bot.register_next_step_handler(call.message, my_currency)
#
# def my_currency(message):
#     try:
#         values = message.text.upper().split('/')
#         res = c.convert(amount, values[0], values[1])
#         bot.send_message(message.chat.id, f'Получается: {round(res, 2)}, можете выполнять новый запрос')
#         bot.register_next_step_handler(message, summa)
#     except Exception:
#         bot.send_message(message.chat.id, 'Что-то пошло не так. Впишите сумму корректно')
#         bot.register_next_step_handler(message, my_currency)
# name = None
# # Прогноз погоды
# APIweather = 'bb5b8c4fd7d2b4e10e3d95887207df9c'
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название город')
#
# @bot.message_handler(content_types=['text'])
# def get_weather(message):
#     city = message.text.strip().lower()
#     response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIweather}&units=metric&lang=ru')
#     if response.status_code == 200:
#         data = response.json()
#         weather = data['weather'][0]['description']
#         temp = round(data['main']['temp'])
#         feels_like = round(data['main']['feels_like'])
#         bot.reply_to(message, f'Сейчас в городе {city.capitalize()}\n'
#                               f'Погода {weather}\n'
#                               f'Температура равна {temp}°C, по ощущениям {feels_like}°C')
#
#         image = 'sunny.jpeg' if weather > str(5.0) else 'notsunny.png'
#         file = open('./' + image, 'rb')
#         bot.send_photo(message.chat.id, file)
#     else:
#         bot.reply_to(message, 'Не удалось получить данные о погоде. Проверьте название города.')



# При команде /site или /website высылает ответ
# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('https://i.postimg.cc/8cYGJr95/image.jpg')
#
# При команде со словом высылает фотку и прикрепляет к ней кнопки
# @bot.message_handler(commands=['bleach'])
# def bleach(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('Перейти на сайт')
#     markup.row(btn1)
#     btn2 = types.KeyboardButton('Удалить фото')
#     btn3 = types.KeyboardButton('Изменить текст')
#     markup.row(btn2, btn3)
#     file = open('./bleach.jpg', 'rb')
#     bot.send_photo(message.chat.id, file, reply_markup=markup)
#     bot.register_next_step_handler(message, on_click)
#
# # Функция для клика на кнопки
# def on_click(message):
#     if message.text == 'Перейти на сайт':
#         bot.send_message(message.chat.id, 'Smth is open')
#     elif message.text == 'Удалить фото':
#         bot.send_message(message.chat.id, 'Smth is deleted')
#     elif message.text == 'Изменить текст':
#         bot.send_message(message.chat.id, 'Smth is edited')
#     else:
#         bot.send_message(message.chat.id, 'Unknown')
#
# # Функция help
# @bot.message_handler(commands=['help'])
# def help(message):
#     bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')
#
# # Функция при отправке фото боту
# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://www.google.com/')
#     markup.row(btn1)
#     btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
#     btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
#     markup.row(btn2, btn3)
#     bot.reply_to(message, 'Какое красивое фото!😍', reply_markup=markup)
#
# # Функция для удаления предпоследнего смс после получения фотки
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#     elif callback.data == 'edit':
#         bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

# def main(message):
#     file = open('./bleach.jpg', 'rb')
#     bot.send_photo(message.chat.id, file)
#     # Создаем таблицу, если она не существует
#     conn = sqlite3.connect('forfun.db')
#     sql = conn.cursor()
#     sql.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             pass TEXT NOT NULL
#         )
#     ''')
#     conn.commit()
#     sql.close()
#     conn.close()
#
#     bot.send_message(message.chat.id, 'Привет! Давай тебя зарегистрируем. Введи свое имя:')
#     bot.register_next_step_handler(message, user_name)
#
#
# def user_name(message):
#     name = message.text.strip()
#     if not name:
#         bot.send_message(message.chat.id, 'Имя не может быть пустым. Попробуй снова.')
#         bot.register_next_step_handler(message, user_name)
#         return
#
#     bot.send_message(message.chat.id, 'Теперь введи пароль:')
#     bot.register_next_step_handler(message, user_pass, name)
#
#
# def user_pass(message, name):
#     password = message.text.strip()
#
#     # Проверка пароля
#     if len(password) < 6:
#         bot.send_message(message.chat.id, 'Пароль должен быть не менее 6 символов. Попробуй снова.')
#         bot.register_next_step_handler(message, user_pass, name)
#         return
#     if not any(char.isdigit() for char in password):
#         bot.send_message(message.chat.id, 'Пароль должен содержать хотя бы одну цифру. Попробуй снова.')
#         bot.register_next_step_handler(message, user_pass, name)
#         return
#     if not any(char.isupper() for char in password):
#         bot.send_message(message.chat.id, 'Пароль должен содержать хотя бы одну заглавную букву. Попробуй снова.')
#         bot.register_next_step_handler(message, user_pass, name)
#         return
#
#     # Сохраняем данные в базу
#     conn = sqlite3.connect('forfun.db')
#     sql = conn.cursor()
#     try:
#         sql.execute('INSERT INTO users (name, pass) VALUES (?, ?)', (name, password))
#         conn.commit()
#
#         # Создаем кнопки
#         markup = telebot.types.InlineKeyboardMarkup()
#         markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
#
#         bot.send_message(message.chat.id, 'Вы успешно зарегистрировались!', reply_markup=markup)
#     except sqlite3.Error as e:
#         bot.send_message(message.chat.id, f'Ошибка при регистрации: {e}')
#     finally:
#         sql.close()
#         conn.close()
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'users')
# def list_users(call):
#     # Подключение к базе данных и получение списка пользователей
#     conn = sqlite3.connect('forfun.db')
#     sql = conn.cursor()
#     try:
#         sql.execute('SELECT name FROM users')
#         users = sql.fetchall()
#         if users:
#             user_list = '\n'.join(user[0] for user in users)
#             bot.send_message(call.message.chat.id, f'Список пользователей:\n{user_list}')
#         else:
#             bot.send_message(call.message.chat.id, 'Пользователей пока нет.')
#     except sqlite3.Error as e:
#         bot.send_message(call.message.chat.id, f'Ошибка при получении списка пользователей: {e}')
#     finally:
#         sql.close()
#         conn.close()

# bot = telebot.TeleBot('7650145975:AAEZSo4RVCmSwZaoIK9sCTWeXDQ4pdbAfac')
# bot.polling(non_stop=True)

import logging
from aiogram import Bot, Dispatcher
import asyncio
from aiogram.filters import CommandStart
from aiogram.types import Message
bot = Bot('7650145975:AAEZSo4RVCmSwZaoIK9sCTWeXDQ4pdbAfac')
dp = Dispatcher()
async def main():
    await dp.start_polling(bot)

@dp.message(CommandStart)
async def cmd_start(message: Message):
    await message.answer('Привет')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')