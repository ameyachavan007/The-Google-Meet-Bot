import re
import time
import os
from telegram import ChatAction
from telegram.ext import run_async
from boi import updater, browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import logging


JOIN_AFTER_PEOPLE = 1


userId = ""


def num_in_string(inputString):
    return re.search('\s[0-9]+\s', inputString)


def join_meet(context, code):
    wait = WebDriverWait(browser, 10)
    browser.get("https://meet.google.com/"+code)

    time.sleep(3)
    browser.refresh()

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div/div[3]/div/div[2]/div[3]/div/span/span'))).click()

    time.sleep(1)

    browser.save_screenshot("ss.png")
    context.bot.send_chat_action(
        chat_id=userId, action=ChatAction.UPLOAD_PHOTO)
    pic = context.bot.send_photo(chat_id=userId, photo=open(
        'ss.png', 'rb'), timeout=120).message_id
    os.remove('ss.png')

    context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=userId, text="Joined the meet!")

    join_field = browser.find_element_by_xpath(
        "/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span")

    try:

        joined = browser.find_elements_by_xpath('//div[@class = "Yi3Cfd"]')

        while not (num_in_string(joined[0].text)):
            print(joined[0].text)
            time.sleep(2)
            joined = browser.find_elements_by_xpath('//div[@class = "Yi3Cfd"]')
        people_before = re.findall(
            '\s+[0-9]+\s+', joined[0].text)[0].rstrip().lstrip()

        while (int(people_before) < JOIN_AFTER_PEOPLE):
            time.sleep(2)
            joined = browser.find_elements_by_xpath('//div[@class = "Yi3Cfd"]')
            peopleNum = re.findall(
                '\s[0-9]+\s', joined[0].text)[0].rstrip().lstrip()
            print("Not joining cause only " +
                  people_before + " have joined yet")

        context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING)
        context.bot.send_message(
            chat_id=userId, text="I joined class because these many people were in: " + people_before)

        join_field.click()
        time.sleep(1)
        browser.save_screenshot("ss.png")
        context.bot.send_chat_action(
            chat_id=userId, action=ChatAction.UPLOAD_PHOTO)
        pic = context.bot.send_photo(chat_id=userId, photo=open(
            'ss.png', 'rb'), timeout=120).message_id
        os.remove('ss.png')

    except:
        context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING)
        context.bot.send_message(
            chat_id=userId, text="No one in the meet..sending ss")
        join_field.click()
        time.sleep(10)
        people_in_the_meet = browser.find_elements_by_xpath(
            "/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[2]/div/div/div[2]/div/div")
        people_in_meet = re.findall(
            '[0-9]+', people_in_the_meet[0].text)[0].rstrip().lstrip()
        total_students = int(people_in_meet)

        context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING)
        context.bot.send_message(
            chat_id=userId, text="I have joined the meet with these many people" + total_students)

        time.sleep(1)
        browser.save_screenshot("ss.png")
        context.bot.send_chat_action(
            chat_id=userId, action=ChatAction.UPLOAD_PHOTO)
        pic = context.bot.send_photo(chat_id=userId, photo=open(
            'ss.png', 'rb'), timeout=120).message_id
        os.remove('ss.png')


@run_async
def meet(update, context):
    logging.info("DOING")

    context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING)
    code = context.args[0]
    join_meet(context, code)
