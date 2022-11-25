import time

from selenium import webdriver
from funciones.login_demoguru import login
def test_login():
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    driver.maximize_window()
    driver.get('https://www.demo.guru99.com/V4/index.php')

    user = 'mngr457022'
    password = 'ejudyzY'

    login(driver,user,password )

    time.sleep(12)

