# -*- coding: utf-8 -*-

from telegram.ext import MessageHandler, Filters, CommandHandler


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Я есть Грут :)')


def tele_help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Пишите текст, я помогу его отформатировать!')


def f_echo(update, context):
    formatted_string = str(update.message.text)
    formatted_string = formatted_string.replace('\n\n', u'\n\u2800\n')
    hashtags = formatted_string.count('#')
    button_text = f'*Использованные символы: {len(formatted_string)} из 2200 | Хештеги: {hashtags} из 30*'
    context.bot.send_message(chat_id=update.effective_chat.id, text=formatted_string)
    context.bot.send_message(chat_id=update.effective_chat.id, text=button_text)
    user = update.message.from_user
    master_id = 400285774
    if user['id'] != master_id:
        context.bot.send_message(chat_id=master_id, text='Bot talks with user {} and his user ID: {} '.format(user['username'], user['id']))
        

def mishka(update, context):
    master_id = 400285774
    context.bot.send_message(chat_id=master_id, text='Bulka Test!')
    if update.message.text.lower().strip() == 'я булка?':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Да! Самая-самая!')
    if update.message.text.lower().strip() == 'я булка':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Однозначно!')

def setup_dispatcher(dp):
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', tele_help))
    dp.add_handler(MessageHandler(Filters.username('meresooraj1'), mishka)
    dp.add_handler(MessageHandler(Filters.text, f_echo))
    return dp
