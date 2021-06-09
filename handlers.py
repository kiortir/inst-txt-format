# -*- coding: utf-8 -*-

from telegram.ext import MessageHandler, Filters, CommandHandler


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Добрый день! Задайте Ваш вопрос, и наш менеджер ответит в ближайшее время.')


def tele_help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='''Вы можете задать все вопросы здесь, но для связи также доступен телефон:
                             
8 (495) 127-79-54

Время работы:
Отдел продаж — с 09:00 до 20:00
Офис при производстве — с 10:00 до 18:00
''')


def setup_dispatcher(dp):
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', tele_help))
    return dp
