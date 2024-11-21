from selenium.webdriver.common.by import By


class ResultPage:

    def __init__(self, driver):
        self._driver = driver


    def add_books(self):
        to_cart_buttons = self._driver.find_elements(By.CSS_SELECTOR, ".btn-tocart")


        counter = 0
        for to_cart_button in to_cart_buttons:
            to_cart_button.click()
            counter += 1

        return counter


    def get_empty_result_message(self):
        message = self._driver.find_element(By.CSS_SELECTOR, ".index-top-title").text
        return message