from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def buscar_en_barra_youtube(driver, titulo):
    barraDeBusqueda = driver.find_element(By.NAME, 'search_query')
    barraDeBusqueda.send_keys(titulo)
    barraDeBusqueda.send_keys(Keys.ENTER)
