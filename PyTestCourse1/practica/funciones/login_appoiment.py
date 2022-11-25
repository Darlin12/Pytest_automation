from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login(driver, user, password):
    usernameInput = driver.find_element(By.ID, 'txt-username')
    usernameInput.send_keys(user)

    passwordInput = driver.find_element(By.ID, 'txt-password')
    passwordInput.send_keys(password)

    passwordInput.send_keys(Keys.ENTER)