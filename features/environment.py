from behave import *

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_scenario(context, scenario):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-gpu')

    context.browser = webdriver.Chrome(chrome_options=options)


def after_scenario(context, scenario):
    context.browser.quit()
