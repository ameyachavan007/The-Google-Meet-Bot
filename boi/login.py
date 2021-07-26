import logging
from boi import dp, browser
from telegram.ext import run_async
from telegram import ChatAction
import os

from dotenv import load_dotenv
import time

load_dotenv()
userId = os.getenv("USERID")


@run_async
def login(update, context):
    context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING)

    username = context.args[0]
    password = context.args[1]

    browser.get("https://stackoverflow.com/users/login")
    time.sleep(2)
    print("ran till here........")
    signinw_field = browser.find_element_by_xpath(
        "/html/body/div[3]/div[2]/div/div[2]/button[1]")
    signinw_field.click()
    print("clicked........")
    time.sleep(2)
    email_field = browser.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
    email_field.send_keys(username)
    time.sleep(2)
    next_field = browser.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
    next_field.click()
    time.sleep(4)
    pass_field = browser.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    pass_field.send_keys(password)
    next1_field = browser.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
    next1_field.click()
    time.sleep(2)

    browser.get('https://apps.google.com/meet/')

    # browser.save_screenshot("ss.png")
    # context.bot.send_chat_action(
    #     chat_id=userId, action=ChatAction.UPLOAD_PHOTO)
    # pic = context.bot.send_photo(chat_id=userId, photo=open(
    #     'ss.png', 'rb'), timeout=120).message_id
    # os.remove('ss.png')
    context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=userId, text="Logged In!")
