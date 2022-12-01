from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from translater import RuEnTranslater

TOKEN = ''
bot = Bot(TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    await message.answer('Привет!\nЯ перевожу русский текст написанный на английской раскладке!')

@dp.message_handler()
async def translate(message: types.Message):
    try:
        await message.answer(RuEnTranslater(str(message.text)))
    except:
        await message.answer("Введите верный формат текста!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
