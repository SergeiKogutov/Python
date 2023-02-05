import requests
import telebot


bot = telebot.TeleBot("5923964405:AAE7gh9q7BH5NWcuUFyeh-wVP97H4mABSWM")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет, как у тебя дела?")

@bot.message_handler(content_types=['text'])
def echo_all(message):
    if message.text == 'Погода':
        data = requests.get('https://wttr.in/?format=3')
        bot.reply_to(message, data.text)

bot.infinity_polling()