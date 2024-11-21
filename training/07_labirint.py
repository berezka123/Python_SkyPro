from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


cookie = {
    "name": "cookie_policy",
    "value": "1"
}


def test_cart_counter():
    driver = webdriver.Chrome()
    driver.get("http://labirint.ru/")
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.add_cookie(cookie)

    driver.find_element(By.CSS_SELECTOR, "#search-field").send_keys("Python")
    driver.find_element(By.CSS_SELECTOR,
                        ".b-header-b-search-e-srch-icon").click()

    to_cart_buttons = driver.find_elements(By.CSS_SELECTOR, ".btn-tocart")

    counter = 0
    for to_cart_button in to_cart_buttons:
        to_cart_button.click()
        counter += 1

    driver.get("https://www.labirint.ru/cart/")
    cart_count = driver.find_element(By.CSS_SELECTOR, ".j-cart-count").text

    assert counter == int(cart_count)

    sleep(10)
    driver.quit()
