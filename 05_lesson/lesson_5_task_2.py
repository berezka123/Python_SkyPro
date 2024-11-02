from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# Для Google Chrome.
# Клик по кнопке без ID.
driver = webdriver.Chrome()

# Открываем страницу:
driver.get("http://uitestingplayground.com/dynamicid")
sleep(3)

# Ищем синюю кнопку и кликаем на неё:
driver.find_element(By.CLASS_NAME, "btn-primary").click()
sleep(5)
driver.quit()
