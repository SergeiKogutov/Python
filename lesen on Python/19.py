import telebot

bot = telebot.TeleBot("5923964405:AAE7gh9q7BH5NWcuUFyeh-wVP97H4mABSWM")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.from_user.id, 'hi, to contact technical support, write the command "/Tsupport" and then write down your question.')

@bot.message_handler(commands=['Tsupport'])
def send_welcome(message):
    data = open('Tsupport.txt', mode = 'a', encoding='utf-8')
    res = message.text.replace('/Tsupport', '')
    text = f'{message.from_user.id} {message.from_user.first_name} {message.from_user.last_name} : {res}'
    data.write(text)
    data.write('\n')
    data.close()
    bot.send_message(message.from_user.id, 'ваш запрос принят.')


bot.infinity_polling()