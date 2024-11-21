from selenium import webdriver
from selenium.webdriver.common.by import By


# Значения для заполнения:
first_name = "John"
last_name = "Smith"
zip_code = "33701-4313"

# Используем Google Chrome.
# Покупка.
driver = webdriver.Chrome()
url = "https://www.saucedemo.com/"

# Переходим на страницу:
driver.get(url)

# Авторизуемся как пользователь standard_user:
driver.find_element(By.CSS_SELECTOR, 'input[id="user-name"]').\
    send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, 'input[id="password"]').\
    send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, 'input[id="login-button"]').click()

# Добавляем в корзину товары:
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").\
    click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").\
    click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").\
    click()

# Переходим в корзину:
driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

# Нажимаем Checkout:
driver.find_element(By.CSS_SELECTOR, "#checkout").click()

# Заполняем форму своими данными:
driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(zip_code)


# Нажимаем кнопку Continue:
driver.find_element(By.CSS_SELECTOR, "#continue").click()

# Читаем со страницы итоговую стоимость (Total):
total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text

# Закрываем браузер:
driver.quit()

# Проверяем, что итоговая сумма равна $58.29:
assert total[total.find("$"):] == "$58.29"
