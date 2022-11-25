from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def login(driver, user, password):
    userInput = driver.find_element(By.NAME, 'uid')
    userInput.send_keys(user)

    passwordInput = driver.find_element(By.NAME, 'password')
    passwordInput.send_keys(password)

    btn_login = driver.find_element(By.NAME, 'btnLogin').click()


