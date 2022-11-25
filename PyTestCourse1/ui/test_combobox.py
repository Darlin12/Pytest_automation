import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pytest import Mark

def test_checkbox_interaction():
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    driver.get('https://testautomationpractice.blogspot.com/')

    select_file = Select(driver.find_element(By.NAME, 'files'))
    select_file.select_by_value('3')
    time.sleep(10)