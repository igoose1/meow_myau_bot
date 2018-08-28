import random
import telebot
import logging

token = "<TOKEN>"
REPLAYCING_TEXT = 'мяу'
END_TEXT = '^^'
help_text = """Напиши любое слово этому боту, а он добавит туда немного няшности ^^
"""
file_id = None

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.logging('{id} -> help'.format(id=message.chat.id))
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['start'])
def start_message(message):
    help_mesasge(message)
    file_id = bot.send_photo(
            message.chat.id,
            file_id or open('start.png', 'rb'))


@bot.message_handler(content_types=["text"])
def meow(message):
    res_list = list()
    for word in message.text.split():
        if random.choice([True] + [False] * 2):
            res_list.append(REPLAYCING_TEXT)
        else:
            res_list.append(word)

    res_list.append(END_TEXT)
    bot.send_message(message.chat.id, ' '.join(res_list))


if __name__ == '__main__':
    bot.polling(none_stop=True)
