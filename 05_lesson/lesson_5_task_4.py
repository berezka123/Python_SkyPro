from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# Для Mozilla Firefox.
# Модальное окно.
driver = webdriver.Firefox()

# Открываем страницу:
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Нажимаем на кнопку Сlose в модальном окне.
wait = WebDriverWait(driver, timeout=2)
driver.find_element(By.CLASS_NAME, "modal-footer").click()

sleep(5)
driver.quit()
