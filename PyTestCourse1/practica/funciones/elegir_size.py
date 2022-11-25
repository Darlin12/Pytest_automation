from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
def elegir_size(driver, size):
    seleccionar_dropDown = Select(driver.find_element(By.XPATH, '//*[@id="native_dropdown_selected_size_name"]'))
    seleccionar_dropDown.select_by_visible_text(size)
