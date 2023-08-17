from aiogram import types



async def welcome_message(message:types.Message):
    text ="""
         Привет , я бот для игры угадай фильм по эмоджи.
         Что бы начать игру, отправь мне сообщение "Start"
         """
    await message.answer(text)
    