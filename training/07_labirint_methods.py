from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

cookie = {
    "name": "cookie_policy",
    "value": "1"
}


def open_labirint():
    # Перейти на сайт «Лабиринта».
    driver.get("http://labirint.ru/")
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.add_cookie(cookie)


def search(term):
    # Найти все книги по слову Python.
    driver.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    driver.find_element(By.CSS_SELECTOR,
                        ".b-header-b-search-e-srch-icon").click()


def add_books():
    # Добавить все товары с первой страницы в корзину.
    
    to_cart_buttons = driver.find_elements(By.CSS_SELECTOR, ".btn-tocart")

    counter = 0
    for to_cart_button in to_cart_buttons:
        to_cart_button.click()
        counter += 1

    return counter


def go_to_cart():
    # Перейти в «Корзину».
    driver.get("https://www.labirint.ru/cart/")


def get_cart_counter():
    # Получить количество товаров в счетчике «Корзины».
    cart_count = driver.find_element(By.CSS_SELECTOR, ".j-cart-count").text
    return int(cart_count)


def close_driver():
    driver.quit()


def test_cart_counter():
    open_labirint()
    search("Python")
    books = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    #close_driver()

    assert books == cart_counter


def test_failed_search():
    open_labirint()
    search("abracadabra")
    message = driver.find_element(By.CSS_SELECTOR, ".index-top-title").text
    close_driver()

    assert message[:40] == "Все, что мы нашли в Лабиринте по запросу"
