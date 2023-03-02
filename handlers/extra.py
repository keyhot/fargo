from config import bot, dp
from aiogram import types, Dispatcher
from random import choice


# @dp.message_handler()
async def echo(message: types.Message):
    pass


def register_handlers_extra(dp: Dispatcher):
    dp.message_handler(echo)
