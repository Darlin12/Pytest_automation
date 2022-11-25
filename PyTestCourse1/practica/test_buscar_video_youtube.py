import time

from selenium import webdriver
from selenium.webdriver import Keys

from funciones.buscar_barra_de_busqueda_youtube import buscar_en_barra_youtube
from selenium.webdriver.common.by import By




def test_make_appointement():
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    driver.maximize_window()
    driver.get('https://www.youtube.com/')

    time.sleep(3)

    titulo = 'ijustine'
    buscar_en_barra_youtube(driver,titulo)

    time.sleep(8)













