# Напишите программу, удаляющую из текста все слова, содержащие "абв". создав бот

import telebot

token = '5803370605:AAHCc4pBsUMroUtfh4fG_HyLHSY1lfJOdd8'                   # ''
bot=telebot.TeleBot('5803370605:AAHCc4pBsUMroUtfh4fG_HyLHSY1lfJOdd8')      # token

@bot.message_handler(commands=["start"])
def start (m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь)')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    s = message.text
    c = 'абв'
    user_mes = list(filter(lambda s: not c in s, s.split()))
    user_mes = ' '. join(user_mes)
    bot.send_message(message.chat.id, user_mes)


bot.polling(none_stop=True, interval=0)