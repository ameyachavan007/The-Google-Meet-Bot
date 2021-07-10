import logging
import os
from telegram.ext import CommandHandler, Job, run_async
from telegram import ChatAction
from boi import updater, dp, browser
from boi.login import login
from boi.meet import meet

userId = -587495317


def main():

    dp.add_handler(CommandHandler("login", login))
    dp.add_handler(CommandHandler("meet", meet))

    logging.info("Bot started")

    updater.start_polling()


if __name__ == '__main__':
    main()
