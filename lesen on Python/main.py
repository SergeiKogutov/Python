from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hide_link
from aiogram.dispatcher.filters import Text
# from aiogram.utils import ReplyKeyboardBuilder

# bot init
bot = Bot(token="5923964405:AAE7gh9q7BH5NWcuUFyeh-wVP97H4mABSWM", parse_mode="HTML")
dp = Dispatcher(bot)
mylist = [1, 2, 3]

#  echo
# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

# dice
@dp.message_handler(commands=["dice"])
async def cmd_dice(message: types.Message):
    await message.answer(mylist)
    await message.answer_dice(emoji="🎲")

#  list
# @dp.message_handler(commands=["add_to_list"])
# async def cmd_add_to_list(message: types.Message, mylist: mylist):
#     mylist.append(7)
#     await message.answer("Добавлено число 7")


# @dp.message_handler(commands=["show_list"])
# async def cmd_show_list(message: types.Message, mylist: mylist):
#     await message.answer(f"Ваш список: {mylist}")

@dp.message_handler(commands=["test"])
async def any_message(message: types.Message):
    await message.answer("Hello, <b>world</b>!", parse_mode="HTML")
    await message.answer("Hello, *world*\!", parse_mode="MarkdownV2")
    await message.answer("Сообщение с <u>HTML-разметкой</u>")
    await message.answer("Сообщение без <s>какой-либо разметки</s>", parse_mode=None)

@dp.message_handler(commands=["name"])
async def cmd_name(message: types.Message, command: Command):
    if command.args:
        await message.answer(f"Привет, <b>{command.args}</b>")
    else:
        await message.answer("Пожалуйста, укажи своё имя после команды /name!")

@dp.message_handler(commands=["hidden_link"])
async def cmd_hidden_link(message: types.Message):
    await message.answer(
        f"{hide_link('https://telegra.ph/file/562a512448876923e28c3.png')}"
        f"Документация Telegram: *существует*\n"
        f"Пользователи: *не читают документацию*\n"
        f"Груша:"
    )

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

# @dp.message_handler(commands="reply_builder")
# async def reply_builder(message: types.Message):
#     builder = ReplyKeyboardBuilder()
#     for i in range(1, 17):
#         builder.add(types.KeyboardButton(text=str(i)))
#     builder.adjust(4)
#     await message.answer(
#         "Выберите число:",
#         reply_markup=builder.as_markup(resize_keyboard=True),
#     )

# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)