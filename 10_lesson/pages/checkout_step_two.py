from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


class CheckoutStepTwo:
    """
    Класс содержит методы для чтения со страницы итоговой стоимости.
    """

    def __init__(self, browser: webdriver):
        self._driver = browser

    @allure.step("Чтение итоговой суммы.")
    def read_total(self) -> str:
        """
        Чтение итоговой стоимости.
        """
        total = self._driver.find_element(By.CSS_SELECTOR,
                                          ".summary_total_label").text

        return total
