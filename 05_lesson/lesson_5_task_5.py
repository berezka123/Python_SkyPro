from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# Для Mozilla Firefox.
# Поле ввода.
driver = webdriver.Firefox()

# Открываем страницу:
driver.get("http://the-internet.herokuapp.com/inputs")

# Вводим в поле текст 1000.
driver.find_element(By.TAG_NAME, "input").send_keys("1000")
sleep(3)

# Очищаем это поле (метод clear).
driver.find_element(By.TAG_NAME, "input").clear()
sleep(3)

# Вводим в это же поле текст 999.
driver.find_element(By.TAG_NAME, "input").send_keys("999")

sleep(5)
driver.quit()
