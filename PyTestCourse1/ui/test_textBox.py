import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_textbox_interaction():
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    driver.get('https://testautomationpractice.blogspot.com/')

    frame_element = driver.find_element(By.ID, "frame-one1434677811")
    driver.switch_to.frame(frame_element)
    time.sleep(2)
    textbox = driver.find_element(By.NAME, "RESULT_TextField-1")
    textbox.send_keys("Hola")
    time.sleep(2)
    textbox.clear()
    time.sleep(2)
    textbox.send_keys("Hola de nuevo")
    driver.save_screenshot('./imagen.png')
    time.sleep(2)
    valor_actual = textbox.get_attribute("value")
    time.sleep(2)
    print(valor_actual)

