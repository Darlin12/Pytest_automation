from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def buscar_en_barra(driver, item):
    barraDeBusqueda = driver.find_element(By.ID, 'twotabsearchtextbox')
    barraDeBusqueda.send_keys(item)
    barraDeBusqueda.send_keys(Keys.ENTER)