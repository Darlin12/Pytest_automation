import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_navegacion_browser():
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    driver.get('https://www.nytimes.com/')

    driver.find_element(By.LINK_TEXT, 'Science').click()

    driver.back()

    driver.forward()

    driver.refresh()

    time.sleep(6)

