import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import Mark

def test_window():
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.set_window_size(1024, 768)
    time.sleep(5)
    driver.maximize_window()

    #driver.minimize_window()

    driver.find_element(By.XPATH, '//*[@class = "feed-link" and text()= "Posts (Atom)"]').click()

    driver.switch_to.new_window("tab")

    driver.switch_to.new_window("window")

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    time.sleep(5)