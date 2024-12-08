from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


class Inventory:
    """
    Класс содержит методы для добавления товаров в корзину и перехода в
    корзину.
    """

    def __init__(self, browser: webdriver):
        self._driver = browser

    @allure.step("Добавление товаров в корзину.")
    def add_to_cart(self) -> None:
        """
        Добавление товаров в корзину.
        """
        self._driver.find_element(By.CSS_SELECTOR,
                                  "#add-to-cart-sauce-labs-backpack").\
            click()
        self._driver.find_element(By.CSS_SELECTOR,
                                  "#add-to-cart-sauce-labs-bolt-t-shirt").\
            click()
        self._driver.find_element(By.CSS_SELECTOR,
                                  "#add-to-cart-sauce-labs-onesie").\
            click()

    @allure.step("Переход в корзину.")
    def go_to_cart(self) -> None:
        """
        Переход в корзину.
        """
        self._driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").\
            click()
