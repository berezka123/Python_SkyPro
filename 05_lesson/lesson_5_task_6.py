from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# Для Mozilla Firefox.
# Форма авторизации.
driver = webdriver.Firefox()

# Открываем страницу:
driver.get("http://the-internet.herokuapp.com/login")

# Вводим в поле username значение tomsmith.
driver.find_element(By.NAME, "username").send_keys("tomsmith")
sleep(3)

# Вводим в поле password значение SuperSecretPassword!.
driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")
sleep(3)

# Нажимаем кнопку Login.
driver.find_element(By.CLASS_NAME, "radius").click()

sleep(5)
driver.quit()
