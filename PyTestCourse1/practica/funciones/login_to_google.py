import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def login(driver,email, password):
    emailInput = driver.find_element(By.NAME, 'identifier')
    emailInput.send_keys(email)
    emailInput.send_keys(Keys.ENTER)

    time.sleep(7)

    passInput = driver.find_element(By.NAME, 'Passwd')
    passInput.send_keys(password)
    passInput.send_keys(Keys.ENTER)

    time.sleep(10)