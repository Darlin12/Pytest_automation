import time

from selenium import webdriver
from selenium.webdriver import Keys

from funciones.login_to_google import login
from funciones.send_message import send_message
from selenium.webdriver.common.by import By

def test_sendEmail():
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    driver.maximize_window()
    driver.get('https://mail.google.com/mail/u/0/#inbox')

    email = 'pytestpython50@gmail.com' #Add here your email
    password = 'pytest123' #Add here your password
    #function underneath
    login(driver, email, password)

    cc = 'darlinmanuelcasado@gmail.com' #Add here the email address to which you are gonna send the email to
    subject = 'automated message by Darlin' #Add here the subject of the email
    message = 'this second one is for a video im recording'  #Add here the message of your email
    #Function underneath
    send_message(driver, cc, subject, message)




