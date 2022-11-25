import time

from selenium import webdriver
from funciones.login_to_gmail import login

def test_sendEmail():
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    driver.maximize_window()
    driver.get('https://mail.google.com/mail/u/0/#inbox')

    email = 'pytestpython50@gmail.com'
    password = 'pytest123'

    login(driver,email, password)
