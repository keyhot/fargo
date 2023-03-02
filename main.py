from aiogram.utils import executor
from config import dp
import logging

from handlers import client, callback, fsm_anketa, extra
from database.bot_db import sql_create


async def on_startup(_):
    sql_create()

client.register_handlers_client(dp)
fsm_anketa.register_handlers_fsmanketa(dp)
callback.register_handlers_callback(dp)
extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
