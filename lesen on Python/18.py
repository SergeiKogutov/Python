import telebot
from telebot import types

bot = telebot.TeleBot("5923964405:AAE7gh9q7BH5NWcuUFyeh-wVP97H4mABSWM")

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('оповещение')
markup.add(itembtn1)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.from_user.id, "Привет, как у тебя дела?", reply_markup=markup)

@bot.message_handler(commands=['reg'])
def send_welcome(message):
    id = str(message.from_user.id)
    data = open('registr.txt', mode = 'r', encoding='utf-8')
    registr = data.readlines()
    data.close()
    resolt = ''.join(registr)
    if id in resolt:
        bot.reply_to(message, 'вы уже зарегистрированы')
    else:
        data = open('registr.txt', mode = 'a', encoding='utf-8')
        text = f'{id}'
        data.writelines(text)
        data.writelines('\n')
        data.close()
        bot.reply_to(message, 'регистрация прошла успешно')

@bot.message_handler(content_types=['text'])
def alert(message):
    if message.text == 'оповещение':
        id = str(message.from_user.id)
        data = open('registr.txt', mode = 'r', encoding='utf-8')
        registr = data.readlines()
        data.close()
        for id in registr:    
            bot.send_message(id, 'hello')

@bot.message_handler(content_types=['text'])
def loger(message):
    data = open('loger.txt', mode = 'a', encoding='utf-8')
    text = f'{message.from_user.first_name} {message.from_user.last_name} : {message.text}'
    data.writelines(text)
    data.writelines('\n')
    data.close()
    bot.reply_to(message, message.text)

bot.infinity_polling()