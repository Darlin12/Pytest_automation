import time
from funciones.buscar_barra_de_busqueda_amazon import buscar_en_barra
from funciones.elegir_size import elegir_size
from funciones.add_to_cart import add_to_cart
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_compra_en_amazon():
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    driver.maximize_window()
    driver.get('https://www.amazon.com/')

    item1 = 'Puma'
    buscar_en_barra(driver, item1)

    time.sleep(2)

    driver.execute_script("window.scrollTo(0,2250)")

    time.sleep(4)

    shoe = driver.find_element(By.XPATH,  '//*[contains(text() , "PUMA Axelion sin cordones para hombre")]').click()

    time.sleep(5)

    size = '8'
    elegir_size(driver, size)

    time.sleep(8)

    add_to_cart(driver)

    time.sleep(5)

    item2 = 'blow dryer'

    buscar_en_barra(driver, item2)

    gafa = driver.find_element(By.XPATH, '//*[contains(text() , "Revlon Secador de cabello ligero y rápido | Impresionantes soplados de 1875 W fácil y cómodamente")]').click()

    add_to_cart(driver)

    time.sleep(5)









