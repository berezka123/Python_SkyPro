from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


timeout = 45
# Используем Google Chrome.
# Калькулятор.
driver = webdriver.Chrome()
url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
waiter = WebDriverWait(driver, timeout)

# Переходим на страницу:
driver.get(url)

# В поле ввода по локатору #delay вводим значение 45.
driver.find_element(By.CSS_SELECTOR, "#delay").clear()
driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(str(timeout))

# Нажимаем на кнопки:
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

waiter.until(
    EC.text_to_be_present_in_element((By.XPATH,
                                      '//*[@id="calculator"]/div[1]/div'),
                                     "15")
)

assert driver.find_element(By.XPATH, '//*[@id="calculator"]/div[1]/div').\
    text == "15"

driver.quit()
