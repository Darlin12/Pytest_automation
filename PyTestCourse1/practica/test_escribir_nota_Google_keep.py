import time

from selenium import webdriver
from funciones.añadir_nota import añadir_nota

from funciones.login_to_google import login

def test_escribir_nota_Google_Keep():
    driver = webdriver.Chrome('C:\chromedriver.exe')
    driver.maximize_window()
    driver.get('https://keep.google.com/')

    time.sleep(5)
    email = 'pytestpython50@gmail.com'  # Add here your email
    password = 'pytest123'  # Add here your password
    # function underneath
    login(driver, email, password)

    time.sleep(5)

    titulo = 'Primera nota'
    nota = 'Esta es mi primera nota'
    #Function underneath
    añadir_nota(driver, titulo, nota)


