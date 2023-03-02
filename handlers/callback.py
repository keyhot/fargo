from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
from aiogram import types, Dispatcher
from .fsm_anketa import fsm_start
from database.bot_db import sql_command_delete


@dp.callback_query_handler(lambda call: call.data == "que")
async def questions(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup(row_width=5)
    button1 = InlineKeyboardButton('1', callback_data='button_call_1')
    button2 = InlineKeyboardButton('2', callback_data='button_call_2')
    button3 = InlineKeyboardButton('3', callback_data='button_call_3')
    button4 = InlineKeyboardButton('4', callback_data='button_call_4')
    button5 = InlineKeyboardButton('5', callback_data='button_call_5')

    markup.insert(button1).insert(button2).insert(button3).insert(button4).insert(button5)
    await bot.send_message(call.message.chat.id, f'1. Какие типы вакансий доступны для человека с моей квалификацией и опытом?\n\n'
                           + f'2. В каких странах или регионах Европы больше всего возможностей трудоустройства для выходцев из Центральной Азии?\n\n'
                           + f'3. Каков процесс получения рабочей визы или разрешения на работу в странах, где мне интересно работать?\n\n'
                           + f'4. Каковы расходы на проживание и средние зарплаты в странах, где мне интересно работать?\n\n'
                           + f'5. Сколько времени обычно занимает процесс найма?'
                           , reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data == "fsm")
async def application(call: types.CallbackQuery):
    await fsm_start(call.message)


@dp.callback_query_handler(lambda call: call.data == "vac")
async def vacancies(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Next', callback_data='button_call_2')
    markup.add(button)

    await bot.send_message(call.message.chat.id, f'В процессе',  reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def ans_1(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, f'Какие типы вакансий доступны для человека с моей квалификацией и опытом?\nТипы рабочих мест, которые доступны для кого-то с вашей квалификацией и опытом, будут зависеть от ваших конкретных навыков и опыта. Вы также можете рассмотреть возможность трудоустройства в отраслях, которые преобладают в вашей стране, поскольку у вас могут быть уникальные навыки, востребованные в определенных секторах.')


@dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def ans_2(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, f'В каких странах или регионах Европы больше всего возможностей трудоустройства для выходцев из Центральной Азии?\nЭто будет зависеть от конкретного рынка труда и ваших навыков и опыта. Тем не менее, некоторые страны Европы, которые, как известно, предлагают хорошие возможности трудоустройства для выходцев из Центральной Азии, включают Германию, Польшу , Бельгию , и тд.')


@dp.callback_query_handler(lambda call: call.data == "button_call_3")
async def ans_3(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, f'Каков процесс получения рабочей визы или разрешения на работу в странах, где мне интересно работать?\nПроцесс получения рабочей визы или разрешения на работу зависит от страны, в которой вы хотите работать. Однако, как правило, вам нужно будет получить предложение о работе от работодателя в этой стране, прежде чем вы сможете подать заявление на получение рабочей визы. Работодатель, как правило, должен спонсировать ваше заявление на получение визы, и вам также может потребоваться предоставить доказательства вашей квалификации и опыта работы.')


@dp.callback_query_handler(lambda call: call.data == "button_call_4")
async def ans_4(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, f'Каковы расходы на проживание и средние зарплаты в странах, где мне интересно работать?\nРасходы на проживание и средняя заработная плата будут варьироваться в зависимости от страны и региона, где вы хотите работать. Однако в целом страны Восточной Европы, как правило, имеют более невысокие расходы на проживание и заработную плату по сравнению со странами Западной Европы. Вы можете изучить стоимость жизни и среднюю заработную плату в конкретных странах или регионах, где вы заинтересованы работать, чтобы лучше понять, чего ожидать.')


@dp.callback_query_handler(lambda call: call.data == "button_call_5")
async def ans_5(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, f'Сколько времени обычно занимает процесс найма?\nПроцесс найма может варьироваться в зависимости от конкретной работы и работодателя. Однако в целом процесс набора может занять несколько недель или даже месяцев, в зависимости от сложности роли и количества претендентов.')


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(questions, lambda call: call.data == "que")
    dp.register_callback_query_handler(application, lambda call: call.data == "fsm")
    dp.register_callback_query_handler(vacancies, lambda call: call.data == "vac")