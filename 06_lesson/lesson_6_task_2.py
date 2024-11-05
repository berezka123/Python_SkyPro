from selenium import webdriver
from selenium.webdriver.common.by import By


# Используем Google Chrome.
# Переименовать на кнопку.
driver = webdriver.Chrome()

# Переходим на страницу:
driver.get("http://uitestingplayground.com/textinput")

# Находим поле ввода и пишем в нём текст SkyPro:
driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

# Нажимаем на синюю кнопку:
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

# Получаем текст кнопки и выводим в консоль:
button_name = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(f"Текст кнопки: {button_name}")

driver.quit()
