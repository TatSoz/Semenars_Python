# Создайте программу для игры с конфетами человек против человека.

import telebot
import random

'''from telebot import types # для указание типов  '''

token = ''
bot = telebot.TeleBot('')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')


candies = 0
max_candies = 28


@bot.message_handler(commands=["game"])
def game(message):
    global candies
    candies = 101
    bot.send_message(message.chat.id, f'На столе {candies} конфет ')


@bot.message_handler(content_types=["text"])
def inputs(message):
    global candies
    if candies <= 0:
        bot.send_message(message.chat.id, 'Игра окончена! ')
        handle_text(message)
        return
    else:
        bot.send_message(message.chat.id, 'Возьмите конфеты! ')

    try:
        can = int(message.text)
        candies = candies - can
        bot.send_message(message.chat.id, f'На столе {candies} конфет ')
        ran_can = random.randint(1, max_candies)
        candies = candies - ran_can
        bot.send_message(message.chat.id, f'Бот взял {ran_can}, на столе {candies} конфет ')
    except ValueError:
        bot.send_message(message.chat.id, 'Ошибка! Введите число! ')


bot.polling(none_stop=True, interval=0)





