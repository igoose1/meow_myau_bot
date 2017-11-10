import random
import telebot
import time

token = "498542758:AAHMsig1Ka4ZQm-d7RAHeepSoho8gRcQlYk"


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help'])
def help(message):
    text = """
Напиши любое слово этому боту, а он добавит туда немного няшности ^^
"""
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['start'])
def start(message):
    print(str(message).encode('utf-8'))
    text = """
Любишь кошечек?
Тогда напиши любое слово этому боту, а он добавит туда немного няшности ^^
"""
    bot.send_message(message.chat.id, text)
    bot.send_photo(message.chat.id, open('start.png', 'rb'))


@bot.message_handler(content_types=["text"])
def meow(message):
    text = ""

    for word in message.text.split():
        if not random.randint(0, 2):
            text += 'мяу '
        else:
            text += word + ' '

    # text = text.lower() if random.getrandbits(1) else text.upper()
    text += '^^'
    bot.send_message(message.chat.id, text)
    time.sleep(0.2)
    bot.send_message(124343817, str(message))


if __name__ == '__main__':
    bot.polling(none_stop=True)
