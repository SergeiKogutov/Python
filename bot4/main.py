from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters import Text


bot = Bot(token="5923964405:AAE7gh9q7BH5NWcuUFyeh-wVP97H4mABSWM", parse_mode="HTML")
dp = Dispatcher(bot)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)