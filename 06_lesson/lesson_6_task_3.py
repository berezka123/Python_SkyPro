from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Используем Google Chrome.
# Дождаться картинки.
driver = webdriver.Chrome()
url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
waiter = WebDriverWait(driver, 30)

# Переходим на страницу:
driver.get(url)

# Дожидаемся загрузки всех картинок:
waiter.until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#landscape"))
)

# Получаем значение атрибута src у 3-й картинки:
third_picture = driver.find_element(By.CSS_SELECTOR,
                                    "#award").get_attribute("src")

# Выводим значение в консоль:
print(f"Значение атрибута src у 3-й картинки: {third_picture}")

driver.quit()
