import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_element_by_Xpath():
    driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    driver.get('https://testautomationpractice.blogspot.com/')

    frame_element = driver.find_element(By.ID, "frame-one1434677811")
    driver.switch_to.frame(frame_element)

    web_element = driver.find_element(By.XPATH, '//*[@id="RESULT_TextField-1"]')
    web_element.send_keys("Darlin")

    time.sleep(10)
