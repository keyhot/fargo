import random
import sqlite3
import psycopg2
import os

from config import bot


def sql_create():
    global db, cursor
    # db = sqlite3.connect("db.sqlite3")
    # cursor = db.cursor()
    db = psycopg2.connect(
        host=os.environ.get('PSQL_DB_HOST'),
        database=os.environ.get('PSQL_DB_NAME'),
        user=os.environ.get('PSQL_USER'),
        password=os.environ.get('PSQL_PASSWORD'),
        sslmode='require',
    )
    cursor = db.cursor()
    print('CONNECTED TO POSTGRES!')
    cursor.execute("CREATE TABLE IF NOT EXISTS homepage_member "
               "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "name TEXT, phone TEXT,"
               "email TEXT)")
    cursor.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        print(tuple(data.values()))
        cursor.execute("INSERT INTO homepage_member VALUES "
                       "(?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM homepage_member").fetchall()
    random_user = random.choice(result)
    await bot.send_photo(message.from_user.id, random_user[1],
                         caption=f"Name: {random_user[2]}\n"
                                 f"Description: {random_user[3]}\n"
                                 f"Price: {random_user[4]}\n")


async def sql_command_last():
    return cursor.execute("SELECT * FROM homepage_member ORDER BY id DESC LIMIT 1").fetchall()


async def sql_command_all():
    return cursor.execute("SELECT * FROM homepage_member").fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM homepage_member WHERE id == ?", (id, ))
    db.commit()


async def sql_commands_get_all_id():
    return cursor.execute("SELECT id FROM homepage_member").fetchall()


async def sql_command_last_job():
    return cursor.execute("SELECT * FROM homepage_job ORDER BY id DESC LIMIT 1").fetchall()


async def sql_command_all_job():
    return cursor.execute("SELECT * FROM homepage_job").fetchall()


async def sql_commands_get_all_id_job():
    return cursor.execute("SELECT id FROM homepage_job").fetchall()
