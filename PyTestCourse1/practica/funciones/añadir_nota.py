import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def añadir_nota(driver, titulo, nota):
    añadir_nota = driver.find_element(By.XPATH, "//div[@aria-label='Añade una nota…']")
    añadir_nota.click()

    tituloInput = driver.find_element(By.XPATH, "//div[@aria-label='Título']")
    tituloInput.send_keys(titulo)
    tituloInput.send_keys(Keys.TAB)

    añadir_nota.send_keys(nota)
    añadir_nota.send_keys(Keys.ESCAPE)

    time.sleep(5)