from selenium.webdriver.common.by import By

def add_to_cart(driver):
    addToCart = driver.find_element(By.ID, 'add-to-cart-button').click()
