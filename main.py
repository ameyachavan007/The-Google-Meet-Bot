import logging
import os
from telegram.ext import CommandHandler, Job, run_async
from telegram import ChatAction
from boi import updater, dp, browser
from boi.login import login
from boi.meet import meet
from dotenv import load_dotenv


load_dotenv()

userId = -587495317


@run_async
def ping(update, context):
    browser.save_screenshot("ss.png")
    context.bot.send_chat_action(
        chat_id=userId, action=ChatAction.UPLOAD_PHOTO)
    context.bot.send_photo(
        chat_id=userId, photo=open('ss.png', 'rb'), timeout=120)
    os.remove('ss.png')


def help(update, context):
    context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING)
    context.bot.send_message(
        chat_id=userId, text="Use these commands:\n1. /login username password ---to login to your google account\n2. /meet https://meet.google.com/code ---to join your link\n3. /ping ---get an ss of what's going on\n4. /help --- help")


def start(update, context):
    context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=userId, text="Hey! Ask for /help")


def main():

    print(userId)

    dp.add_handler(CommandHandler("login", login))
    dp.add_handler(CommandHandler("meet", meet))
    dp.add_handler(CommandHandler("ping", ping))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("start", start))

    logging.info("Bot started")

    updater.start_polling()


if __name__ == '__main__':
    main()
