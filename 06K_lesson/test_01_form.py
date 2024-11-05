from selenium import webdriver
from selenium.webdriver.common.by import By


# Значения для заполнения:
first_name = "Иван"
last_name = "Петров"
address = "Ленина, 55-3"
email = "test@skypro.com"
phone_number = "+7985899998787"
zip_code = ""  # оставить пустым.
city = "Москва"
country = "Россия"
job_position = "QA"
company = "SkyPro"

# Используем Google Chrome.
# Форма.
driver = webdriver.Chrome()
url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

# Переходим на страницу:
driver.get(url)

# Заполняем форму значениями:
driver.find_element(By.CSS_SELECTOR,
                    'input[name="first-name"]').send_keys(first_name)
driver.find_element(By.CSS_SELECTOR,
                    'input[name="last-name"]').send_keys(last_name)
driver.find_element(By.CSS_SELECTOR,
                    'input[name="address"]').send_keys(address)
driver.find_element(By.CSS_SELECTOR,
                    'input[name="e-mail"]').send_keys(email)
driver.find_element(By.CSS_SELECTOR,
                    'input[name="phone"]').send_keys(phone_number)
driver.find_element(By.CSS_SELECTOR,
                    'input[name="city"]').send_keys(city)
driver.find_element(By.CSS_SELECTOR,
                    'input[name="country"]').send_keys(country)
driver.find_element(By.CSS_SELECTOR,
                    'input[name="job-position"]').send_keys(job_position)
driver.find_element(By.CSS_SELECTOR,
                    'input[name="company"]').send_keys(company)

# Нажимаем кнопку Submit:
driver.find_element(By.CSS_SELECTOR, ".btn").click()

# Проверяем, что поле Zip code подсвечено красным:
red = "rgba(248, 215, 218, 1)"
assert driver.find_element(By.CSS_SELECTOR, "#zip-code").\
    value_of_css_property("background-color") == red

# Проверяем, что остальные поля подсвечены зелёным:
green = "rgba(209, 231, 221, 1)"
assert driver.find_element(By.CSS_SELECTOR, "#first-name").\
    value_of_css_property("background-color") == green
assert driver.find_element(By.CSS_SELECTOR, "#last-name").\
    value_of_css_property("background-color") == green
assert driver.find_element(By.CSS_SELECTOR, "#address").\
    value_of_css_property("background-color") == green
assert driver.find_element(By.CSS_SELECTOR, "#e-mail").\
    value_of_css_property("background-color") == green
assert driver.find_element(By.CSS_SELECTOR, "#phone").\
    value_of_css_property("background-color") == green
assert driver.find_element(By.CSS_SELECTOR, "#city").\
    value_of_css_property("background-color") == green
assert driver.find_element(By.CSS_SELECTOR, "#country").\
    value_of_css_property("background-color") == green
assert driver.find_element(By.CSS_SELECTOR, "#job-position").\
    value_of_css_property("background-color") == green
assert driver.find_element(By.CSS_SELECTOR, "#company").\
    value_of_css_property("background-color") == green

driver.quit()
