import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def send_message(driver, cc, subject, message):
    btn_redactar = driver.find_element(By.XPATH, '//*[contains(text(), "Redactar")]')
    btn_redactar.click()
    time.sleep(15)

    ccInput = driver.find_element(By.ID, ':cr')
    ccInput.send_keys(cc)
    time.sleep(3)
    ccInput.send_keys(Keys.ENTER)

    subjectInput = driver.find_element(By.ID, ':8u')
    subjectInput.send_keys(subject)
    time.sleep(3)
    subjectInput.send_keys(Keys.ENTER)

    messageInput = driver.find_element(By.ID, ':a1')
    messageInput.send_keys(message)
    time.sleep(3)

    btn_sent = driver.find_element(By.ID, ':8k')
    btn_sent.click()
    time.sleep(10)

