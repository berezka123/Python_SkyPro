from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage


def test_cart_counter():
    browser = webdriver.Chrome()
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search("Python")

    result_page = ResultPage(browser)
    to_be = result_page.add_books()

    cart_page = CartPage(browser)
    cart_page.go_to_cart()
    as_is = cart_page.get_cart_counter()

    assert to_be == as_is

    browser.quit()


def test_failed_search():
    browser = webdriver.Chrome()
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search("abracadabra")

    result_page = ResultPage(browser)
    message = result_page.get_empty_result_message()
    browser.quit()

    assert message[:40] == "Все, что мы нашли в Лабиринте по запросу"
