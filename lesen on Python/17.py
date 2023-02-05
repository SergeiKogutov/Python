import telebot

bot = telebot.TeleBot("5923964405:AAE7gh9q7BH5NWcuUFyeh-wVP97H4mABSWM")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_game(chat_id=message.chat.id, game_short_name='simplegame')

@bot.message_handler(content_types=['text'])
def calculate(message):
    if 'вычисли' in message.text:
        res = message.text.replace('вычисли', '')
        bot.reply_to(message, f'ответ = {str(eval(res))}')

@bot.callback_query_handler(func=lambda callback_query: callback_query.game_short_name == 'simplegame')
def game(call):
    bot.answer_callback_query(callback_query_id= call.id, url='https://сапёр.com/')

bot.infinity_polling()