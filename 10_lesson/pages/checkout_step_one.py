from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


class CheckoutStepOne:
    """
    Класс содержит методы для заполнения формы.
    """

    def __init__(self, browser: webdriver):
        self._driver = browser

    @allure.step("Заполнение формы своими данными.")
    def filling_form(self, first_name: str, last_name: str,
                     zip_code: str) -> None:
        """
        Заполнение формы.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").\
            send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").\
            send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").\
            send_keys(zip_code)

    @allure.step("Нажатие 'Continue'.")
    def click_continue(self) -> None:
        """
        Нажатие кнопки "Continue".
        """
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()
