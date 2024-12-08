from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


class DataTypes:
    """
    Класс содержит методы для заполнения и отправки формы.
    """

    def __init__(self, browser: webdriver, url: str):
        self._driver = browser
        self._driver.get(url)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Заполнение формы значениями {first_name}, {last_name}, \
                 {address}, {email}, {phone_number}, {zip_code}, {city}, \
                 {country}, {job_position}, {company}.")
    def filling_form(self, first_name: str, last_name: str, address: str,
                     email: str, phone_number: str, zip_code: str, city: str,
                     country: str, job_position: str, company: str) -> None:
        """
        Заполнение формы значениями.
        """
        self._driver.find_element(By.CSS_SELECTOR,
                                  'input[name="first-name"]').\
            send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR,
                                  'input[name="last-name"]').\
            send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR,
                                  'input[name="address"]').\
            send_keys(address)
        self._driver.find_element(By.CSS_SELECTOR,
                                  'input[name="e-mail"]').\
            send_keys(email)
        self._driver.find_element(By.CSS_SELECTOR,
                                  'input[name="phone"]').\
            send_keys(phone_number)
        self._driver.find_element(By.CSS_SELECTOR,
                                  'input[name="zip-code"]').\
            send_keys(zip_code)
        self._driver.find_element(By.CSS_SELECTOR,
                                  'input[name="city"]').\
            send_keys(city)
        self._driver.find_element(By.CSS_SELECTOR,
                                  'input[name="country"]').\
            send_keys(country)
        self._driver.find_element(By.CSS_SELECTOR,
                                  'input[name="job-position"]').\
            send_keys(job_position)
        self._driver.find_element(By.CSS_SELECTOR,
                                  'input[name="company"]').\
            send_keys(company)

    @allure.step("Нажатие 'Submit'.")
    def pressing_submit(self) -> None:
        """
        Нажатие кнопки "Submit".
        """
        self._driver.find_element(By.CSS_SELECTOR, ".btn").click()
