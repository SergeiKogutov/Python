from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters import Text

bot = Bot(token="5923964405:AAE7gh9q7BH5NWcuUFyeh-wVP97H4mABSWM", parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="С пюрешкой"),
            types.KeyboardButton(text="Без пюрешки"),
            types.KeyboardButton(text="С макарошками")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)

@dp.message_handler(Text(equals="С пюрешкой"))
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!")

@dp.message_handler(Text(equals="Без пюрешки"))
async def without_puree(message: types.Message):
    await message.reply("Так невкусно!")

@dp.message_handler(Text(equals="С макарошками"))
async def without_puree(message: types.Message):
    await message.reply("Да ты крут!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)