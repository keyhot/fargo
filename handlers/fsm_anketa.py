from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime

from config import bot, ADMIN, dp
from database import bot_db


class FSMAdmin(StatesGroup):
    name = State()
    phone = State()
    email = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.name.set()
        await message.answer(f"Введите имя:")
    else:
        await message.reply("Просьба писать боту в личку.")


@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        id = await bot_db.sql_command_last()
        data['id'] = id[0][0] + 1
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Номер телефона.")


@dp.message_handler(state=FSMAdmin.phone)
async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await FSMAdmin.next()
    await message.answer("Электронная почта.")


@dp.message_handler(state=FSMAdmin.email)
async def load_email(message: types.Message, state: FSMContext):
    timenow = str(datetime.now())
    async with state.proxy() as data:
        data['email'] = message.text
        data['created_at'] = timenow
    await bot.send_message(message.chat.id, f"Имя: {data['name']}\n"
                                 + f"Телефон: {data['phone']}\n"
                                 + f"Электронная почта: {data['email']}\n")
    await bot_db.sql_command_insert(state)
    await state.finish()
    await message.answer("Регистрация завершена! Ожидайте. В ближайшее время наши сотрудники с вами свяжутся.")


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.answer("Регистрация отменена!")


def register_handlers_fsmanketa(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_registration, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(fsm_start, state=None)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_phone, state=FSMAdmin.phone)
    dp.register_message_handler(load_email, state=FSMAdmin.email)
