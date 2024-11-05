from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Используем Google Chrome.
# Нажать на кнопку.
driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 30)

# Переходим на страницу:
driver.get("http://uitestingplayground.com/ajax")

# Находим синюю кнопку и нажимаем на неё:
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# Ждём, пока появится зелёная плашка с текстом:
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.bg-success"),
                                     "Data loaded with AJAX get request.")
)

# Получаем текст из зелёной плашки:
appeared_text = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text

# Выводим текст в консоль:
print(f"Текст из плашки: {appeared_text}")

driver.quit()
