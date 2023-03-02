from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, ReplyKeyboardMarkup, KeyboardButton
from config import bot, dp, ADMIN
from keyboards import client_kb
from database import bot_db


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.full_name}!\n\n'
                                            + f'- Мы официальная польская рекрутинговая компания и агентство по трудоустройству в одном лице.\n\n'
                                            + f'- Работа без посредников.\n\n'
                                            + f'- Мы имеем долгую историю и опыт в получении виз для наших работников из многих стран (Кыргызстан, Узбекистан, Казахстан, Украина, Таджикистан и тд).\n\n'
                                            + f'- Мы добиваемся получения визы, если беспрекословно следовать нашим советам. В крайнем случае подаём апелляцию. Кандидату могут отказать в визе, если он наговорил глупостей на интервью в консульстве или имел какие либо проблемы с законом.\n\n'
                                            + f'- Каждый наш кандидат, который получит визу и будет работать по нашим вакансиям гарантировано получит ВНЖ Польши (карту побыта).\n\n'
                                            + f'- Мы оказываем полный комплекс услуг для как для кандидатов на визу (анкета, запись в визовый центр, весь пакет документов+приглашение), так и для приехавших на работу от нас (песель, замена прав, карта побыта, помощь с жильём, замена работодателя и прочее).\n\n'
                                            + f'- Для тех кто закрепится в Польше у нас всегда будут предложения по работе в странах западной Европы\n\n'
                                            , reply_markup=client_kb.start_markup)


# @dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await bot.send_message(message.chat.id, '/start - Информация о нас\n/help - Команды\n')


async def delete_data(message: types.Message):
    if message.from_user.id in ADMIN and message.chat.type == "private":
        users = await bot_db.sql_command_all()
        for user in users:
            await bot.send_message(message.from_user.id,
                                 text=f'Имя: {user[1]}\nТел. : {user[2]}\nЭл. почта: {user[3]}\n',
                                 reply_markup=InlineKeyboardMarkup().add(
                                     InlineKeyboardButton(
                                         f"Удалить {user[1]}",
                                         callback_data=f"delete {user[0]}"
                                     )
                                 ))
    else:
        await message.reply("Вы не являетесь администратором!")


async def complete_delete(call: types.CallbackQuery):
    await bot_db.sql_command_delete(call.data.replace("delete ", ""))
    await call.answer(text="Пользователь удален!", show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(help_handler, commands=['help'])
    dp.register_message_handler(delete_data, commands=['admin'])
    dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith('delete '))