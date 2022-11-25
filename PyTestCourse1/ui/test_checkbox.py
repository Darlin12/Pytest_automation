import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import Mark

def test_checkbox_interaction():
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    driver.get('https://testautomationpractice.blogspot.com/')

    frame_element = driver.find_element(By.ID, "frame-one1434677811")
    driver.switch_to.frame(frame_element)

    checkbox = driver.find_element(By.NAME, 'RESULT_CheckBox-8')
    driver.execute_script("arguments[0].scrollIntoView();", checkbox)
    time.sleep(3)
    driver.execute_script("arguments[0].click();", checkbox)
    time.sleep(2)

    print("Tipo de elemento", checkbox.get_attribute('type'))
