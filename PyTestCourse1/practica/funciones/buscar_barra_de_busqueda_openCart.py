from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def buscar_en_barra(driver, item):
    search = driver.find_element(By.NAME, 'search')
    search.send_keys(item)
    search.send_keys(Keys.ENTER)