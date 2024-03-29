from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

vacancies_button = InlineKeyboardButton("Вакансии", callback_data="vac")
questions_button = InlineKeyboardButton("Часто задаваемые вопросы", callback_data="que")
fsm_button = InlineKeyboardButton("Оставить заявку", callback_data="fsm")

start_markup = InlineKeyboardMarkup(row_width=1).insert(questions_button).insert(vacancies_button).insert(fsm_button)

cancel_button = KeyboardButton("ОТМЕНА/CANCEL")
cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(cancel_button)