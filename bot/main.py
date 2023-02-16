import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

# keybord
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Основная информация🗝")
    item2 = types.KeyboardButton("Обратная связь📞")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть источником информации.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def petya(message):
    if message.chat.type == 'private':
        if message.text == "Основная информация🗝":
            bot.send_message(message.chat.id, "Очки виртуальной реальности с инновационной технологией для перемещения из одного места в другое. Где бы вы не находились, вы сможете оказаться в любом желаемом месте только при условии того что в том месте находится специальная камера, для считывания местности. Такие очки помогут находится в нужном месте людям, которые не могут по разным причинам появится в том или ином месте.")
        elif message.text == "Обратная связь📞":
            bot.send_message(message.chat.id, "инстаграм: @key.nto")
        else:
            bot.send_message(message.chat.id, "Я вас не понял")

bot.polling(none_stop=True)