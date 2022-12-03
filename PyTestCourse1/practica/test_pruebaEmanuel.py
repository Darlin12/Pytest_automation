import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_buscar_en_google():
    driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    driver.maximize_window()
    driver.get('https://www.google.com/')
    time.sleep(5)

    textBox = driver.find_element(By.XPATH, "q")
    textBox.send_keys("lidom")

    textBox.send_keys(Keys.ENTER)

    time.sleep(5)