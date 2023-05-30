import telebot
from extancions import *
from config import *


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Приветствую!'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['convert'])
def values(message: telebot.types.Message):
    text = "Выберите валюту, из которой конвертировать: "
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, base_handler)
def base_handler(message: telebot.types.Message):
    base = message.text.strip()
    text = "Выберите валюту, в которую конвертировать: "
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, sym_handler, base)
def sym_handler(message: telebot.types.Message, base):
    sym = message.text.strip()
    text = "Выберите  количество конвертируемой валюты: "
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, amount_handler, base, sym)
def amount_handler(message: telebot.types.Message, base, sym):
    amount = message.text.strip()
    try:
        new_price = Converter.get_price(base, sum, amount)
    except ApiException as e:
        bot.send_message(message.chat.id, f'Ошибка в команде:\n{e}')

    else:
        text = f"Цена {amount} {base} в {sum}: {new_price}"
        bot.send_message(message.chat.id, text)












bot.polling()

