from selenium.webdriver.common.by import By


class DataTypesSubmitted:

    def __init__(self, browser):
        self._driver = browser

    def check_red(self):
        red = "rgba(248, 215, 218, 1)"
        assert self._driver.find_element(By.CSS_SELECTOR, "#zip-code").\
            value_of_css_property("background-color") == red

    def check_green(self):
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
