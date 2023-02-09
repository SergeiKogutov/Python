import telebot

bot = telebot.TeleBot("5813683256:AAG1uyUMxrRHb-804Nm8SmMMyv2K1e0xPys")

@bot.message_handler(commands=['question'])
def question(message):
    data = open('Tsupport.txt', mode = 'r+', encoding='utf-8')
    question = data.readlines()
    question = question[0].replace('\n','')
    data.close
    with open('Tsupport.txt', 'r') as f:
        lines = f.readlines()
    with open('Tsupport.txt', 'w') as f:
        f.writelines(lines[1:])
    bot.send_message(message.from_user.id, question)


bot.infinity_polling()