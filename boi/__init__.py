import logging

from telegram.ext import Updater
import os
from dotenv import load_dotenv

from selenium import webdriver
from telegram.utils.request import USER_AGENT


# Logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

load_dotenv()

TOKEN = '1841656712:AAFItWZQyqHy6Cbnk9m0ZwypzX3MtLEifwQ'
updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-infobars")
options.add_argument(
    "user-agent='User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'")
options.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_camera": 2, "profile.default_content_setting_values.media_stream_mic": 2,
                                "profile.default_content_setting_values.geolocation": 2, "profile.default_content_setting_values.notifications": 2})

browser = webdriver.Chrome(
    executable_path=r"chromedriver.exe", options=options)
