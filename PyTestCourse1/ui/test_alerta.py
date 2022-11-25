import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


def test_alerta_browser():
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    driver.get('https://testautomationpractice.blogspot.com/')

    driver.find_element(By.XPATH, '//*[text()="Click Me"]').click()

    alert = Alert(driver)

    alert.dismiss()

    assert driver.find_element(By.ID, 'demo').text== "You pressed Cancel!"

    time.sleep(5)

