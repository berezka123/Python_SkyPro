from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


class DataTypesSubmitted:
    """
    Класс содержит методы для проверки подсветки полей.
    """

    def __init__(self, browser: webdriver):
        self._driver = browser

    @allure.step("Проверка подсветки поля красным цветом.")
    def check_red(self) -> None:
        """
        Проверка подсветки поля красным цветом.
        """
        red = "rgba(248, 215, 218, 1)"
        assert self._driver.find_element(By.CSS_SELECTOR, "#zip-code").\
            value_of_css_property("background-color") == red

    @allure.step("Проверка подсветки полей зелёным цветом.")
    def check_green(self) -> None:
        """
        Проверка подсветки полей зелёным цветом.
        """
        green = "rgba(209, 231, 221, 1)"
        assert self._driver.find_element(By.CSS_SELECTOR, "#first-name").\
            value_of_css_property("background-color") == green
        assert self._driver.find_element(By.CSS_SELECTOR, "#last-name").\
            value_of_css_property("background-color") == green
        assert self._driver.find_element(By.CSS_SELECTOR, "#address").\
            value_of_css_property("background-color") == green
        assert self._driver.find_element(By.CSS_SELECTOR, "#e-mail").\
            value_of_css_property("background-color") == green
        assert self._driver.find_element(By.CSS_SELECTOR, "#phone").\
            value_of_css_property("background-color") == green
        assert self._driver.find_element(By.CSS_SELECTOR, "#city").\
            value_of_css_property("background-color") == green
        assert self._driver.find_element(By.CSS_SELECTOR, "#country").\
            value_of_css_property("background-color") == green
        assert self._driver.find_element(By.CSS_SELECTOR, "#job-position").\
            value_of_css_property("background-color") == green
        assert self._driver.find_element(By.CSS_SELECTOR, "#company").\
            value_of_css_property("background-color") == green
