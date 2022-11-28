import time

from selenium import webdriver
from funciones.buscar_barra_de_busqueda_openCart import buscar_en_barra
from selenium.webdriver.common.by import By

def test_buying_imac():
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    driver.maximize_window()
    driver.get('http://opencart.abstracta.us/index.php?route=common/home')

    time.sleep(5)

    item = 'imac'
    buscar_en_barra(driver, item )

    time.sleep(5)

    result = driver.find_element(By.XPATH, "//a[normalize-space()='iMac']")
    result.click()

    time.sleep(5)

    itemImage = driver.find_element(By.XPATH, "//ul[@class='thumbnails']//li[1]//a[1]")
    itemImage.click()

    time.sleep(3)

    nextImage = driver.find_element(By.XPATH, "//button[@title='Next (Right arrow key)']")
    nextImage.click()

    time.sleep(5)

    nextImage.click()
    closeButton = driver.find_element(By.XPATH, "//button[@title='Close (Esc)']")
    closeButton.click()

    time.sleep(4)

    action = webdriver.ActionChains(driver)
    navBarOption =  driver.find_element(By.XPATH, "//a[normalize-space()='Laptops & Notebooks']")
    action.move_to_element(navBarOption).perform()

    time.sleep(5)

    windowsOption = driver.find_element(By.XPATH, "//a[normalize-space()='Windows (0)']")
    windowsOption.click()

    time.sleep(5)