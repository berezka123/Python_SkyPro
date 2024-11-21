from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self._driver = driver


    def go_to_cart(self):
        self._driver.get("http://labirint.ru/cart/")


    def get_cart_counter(self):
        cart_count = self._driver.find_element(By.CSS_SELECTOR, ".j-cart-count").text
        return int(cart_count)
