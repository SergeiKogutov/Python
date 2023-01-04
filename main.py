from aiogram import Bot, Dispatcher, executor, types
from pygismeteo import Gismeteo

# bot_init
bot = Bot(token="5813683256:AAG1uyUMxrRHb-804Nm8SmMMyv2K1e0xPys")
dp = Dispatcher(bot)

# def
@dp.message_handler()
async def echo(message: types.Message):
    gismeteo = Gismeteo()
    search_results = gismeteo.search.by_query(message.text)
    city_id = search_results[0].id
    current = gismeteo.current.by_id(city_id)

    resp_msg = f"{search_results[0].name}\n"
    resp_msg += f"Текущая температура: {round(current.temperature.air.c)}\n"
    resp_msg += f"Состояние погоды: {current.description.full}\n"
    resp_msg += f"Влажность: {current.humidity.percent}"
    await message.answer(resp_msg)

# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)