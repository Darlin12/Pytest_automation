import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import Mark

def test_calendar():
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    driver.get("https://testautomationpractice.blogspot.com/")

    driver.find_element(By.ID, 'datepicker').click()

    time.sleep(4)

    driver.find_element(By.XPATH, '//*[@class = "ui-state-default" and text()="23"]').click()
    time.sleep(4)

    driver.find_element(By.ID, 'datepicker').click()
    driver.find_element(By.XPATH, '//*[@class = "ui-state-default" and text()="25"]').click()

    time.sleep(4)
