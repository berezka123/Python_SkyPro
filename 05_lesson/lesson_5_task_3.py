from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# Для Google Chrome.
# Клик по кнопке с CSS-классом.
driver = webdriver.Chrome()

# Открываем страницу:
driver.get("http://uitestingplayground.com/classattr")
sleep(3)

# Ищем синюю кнопку и кликаем на неё:
driver.find_element(By.CLASS_NAME, "btn-primary").click()
sleep(3)
# Нажимаем ОК во всплывающем оповещении:
wait = WebDriverWait(driver, timeout=2)
alert = wait.until(lambda d: d.switch_to.alert)
alert.accept()

sleep(5)
driver.quit()
