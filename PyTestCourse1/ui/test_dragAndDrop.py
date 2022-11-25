import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pytest import Mark

def test_checkbox_interaction():
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    driver.get('https://testautomationpractice.blogspot.com/')

    source = driver.find_element(By.XPATH, '//*[@class = "ui-widget-header" and text() = "Mr John"]')
    target = driver.find_element(By.ID, 'trash')

    action = ActionChains(driver)

    action.drag_and_drop(source, target).perform()

    time.sleep(5)

    source = driver.find_element(By.XPATH, '//*[@class = "ui-widget-header" and text() = "Mary"]')
    action.drag_and_drop(source, target).perform()

    time.sleep(5)

