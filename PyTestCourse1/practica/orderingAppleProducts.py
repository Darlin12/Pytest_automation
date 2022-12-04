import time

from selenium import webdriver
from funciones import apple_function_class


def test_oderingAppleProducts():
    driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.apple.com/")

    time.sleep(5)

    #Objeto de clase
    producto = apple_function_class.Apple;


    producto.añaddirAirpods3ToCart(driver)

    ####################

    producto.añadirIphoneSetoCart(driver)

    ####################

    producto.añadirIphone14ProToCart(driver)

    ####################

    producto.removerItem(driver)

    ####################

    producto.checkOutApplePurchase(driver)

    time.sleep(10)



















