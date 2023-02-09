import telebot

bot = telebot.TeleBot("5923964405:AAE7gh9q7BH5NWcuUFyeh-wVP97H4mABSWM")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.from_user.id, 'hi, to contact technical support, write the command "/tsupport" and then write down your question.')

@bot.message_handler(commands=['tsupport'])
def send_welcome(message):
    data = open('Tsupport.txt', mode = 'a', encoding='utf-8')
    res = message.text.replace('/tsupport', '')
    text = f'{message.from_user.id} {message.from_user.first_name} {message.from_user.last_name} : {res}'
    data.write(text)
    data.write('\n')
    data.close()
    bot.send_message(message.from_user.id, 'ваш запрос принят.')

@bot.message_handler(commands=['question'])
def question(message):
    data = open('Tsupport.txt', mode = 'r+', encoding='utf-8')
    question = data.readlines()
    question = question[0].replace('\n','')
    data.close
    bot.send_message(message.from_user.id, question)

@bot.message_handler(commands=['answer'])
def answer(message):
    data = open('answer.txt', mode = 'a', encoding='utf-8')
    text = message.text.replace('/answer', '')
    data.write(text)
    data.write('\n')
    data.close()

@bot.message_handler(commands=['answer_user'])
def answer_user(message):
    data = open('answer.txt', mode = 'r', encoding='utf-8')
    res = data.readlines()
    res = res[0].replace('\n', '')
    data.close()
    data = open('Tsupport.txt', mode = 'r+', encoding='utf-8')
    question = data.readlines()
    question = question[0].replace('\n','')
    data.close
    with open('Tsupport.txt', 'r') as f:
        lines = f.readlines()
    with open('Tsupport.txt', 'w') as f:
        f.writelines(lines[1:])
    with open('answer.txt', 'r') as f:
        lines = f.readlines()
    with open('answer.txt', 'w') as f:
        f.writelines(lines[1:])
    bot.send_message(message.from_user.id, question + '\n' + res)


bot.infinity_polling()