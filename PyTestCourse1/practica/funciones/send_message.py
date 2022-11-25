import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def send_message(driver, cc, subject, message):
    btn_redactar = driver.find_element(By.XPATH, '//*[contains(text(), "Redactar")]')
    btn_redactar.click()
    time.sleep(15)

    ccInput = driver.find_element(By.XPATH, "//input[@role='combobox']")
    ccInput.send_keys(cc)
    time.sleep(3)
    ccInput.send_keys(Keys.ENTER)

    subjectInput = driver.find_element(By.XPATH, "//input[@placeholder='Asunto']")
    subjectInput.send_keys(subject)
    time.sleep(3)
    subjectInput.send_keys(Keys.ENTER)

    messageInput = driver.find_element(By.XPATH, "//div[@aria-label='Cuerpo del mensaje']")
    messageInput.send_keys(message)
    time.sleep(3)

    btn_sent = driver.find_element(By.XPATH, "//div[@aria-label='Enviar ‪(Ctrl-Enter)‬']")
    btn_sent.click()

    time.sleep(3)

    msgAssertion = driver.find_element(By.XPATH, "//span[@class='bAq']").text
    assert msgAssertion == 'Mensaje enviado'

    #print('Este fue el mensaje:', msgAssertion)

    time.sleep(10)

