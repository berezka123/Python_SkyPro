from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.slow_calculator import SlowCalculator
import allure


@allure.title("Автотест на калькулятор")
@allure.description("Ввод значения задержки, нажатие кнопок и проверка \
                     отображения результата через установленное время \
                     задержки.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.MINOR)
def test_slow_calculator():
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    timeout = 45

    browser = webdriver.Chrome()
    waiter = WebDriverWait(browser, timeout)
    main_page = SlowCalculator(browser, url)
    main_page.set_timeout(timeout)
    main_page.pressing_buttons()

    waiter.until(
        EC.text_to_be_present_in_element((By.XPATH,
                                          '//*[@id="calculator"]/div[1]/div'),
                                         "15")
    )

    assert browser.find_element(By.XPATH, '//*[@id="calculator"]/div[1]/div').\
        text == "15"

    browser.quit()
