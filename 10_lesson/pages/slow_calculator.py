from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


class SlowCalculator:
    """
    Класс содержит методы для работы с "Медленным калькулятором".
    """

    def __init__(self, browser: webdriver, url: str):
        self._driver = browser
        self._driver.get(url)
        self._driver.maximize_window()

    @allure.step("Установка времени задержки {timeout} секунд.")
    def set_timeout(self, timeout: int) -> None:
        """
        Очистка поля ввода и ввод значения задержки отображения результата.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").\
            send_keys(str(timeout))

    @allure.step("Нажатие кнопок.")
    def pressing_buttons(self) -> None:
        """
        Поиск кнопок калькулятора и их нажатие.
        """
        self._driver.find_element(By.XPATH,
                                  '//*[@id="calculator"]/div[2]/span[1]').\
            click()
        self._driver.find_element(By.XPATH,
                                  '//*[@id="calculator"]/div[2]/span[4]').\
            click()
        self._driver.find_element(By.XPATH,
                                  '//*[@id="calculator"]/div[2]/span[2]').\
            click()
        self._driver.find_element(By.XPATH,
                                  '//*[@id="calculator"]/div[2]/span[15]').\
            click()
