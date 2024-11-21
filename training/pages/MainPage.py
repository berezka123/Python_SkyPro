from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        # Открыть браузер и перейти на главную страницу.
        self._driver = driver
        self._driver.get("http://labirint.ru/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()


    def set_cookie_policy(self):
        # Убрать плашку «Принять cookie».
        cookie = {
            "name": "cookie_policy",
            "value": "1"
        }
        self._driver.add_cookie(cookie)


    def search(self, term):
        # Найти книги по слову <term>.
        self._driver.find_element(By.CSS_SELECTOR,
                                  "#search-field").send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR,
                        ".b-header-b-search-e-srch-icon").click()
