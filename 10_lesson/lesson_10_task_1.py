from selenium import webdriver
from pages.data_types import DataTypes
from pages.data_types_submitted import DataTypesSubmitted
import allure


@allure.title("Автотест на заполнение формы")
@allure.description("Заполнение некоторых полей значениями и проверка \
                     окрашивания заполненных и незаполненных полей.")
@allure.feature("Форма")
@allure.severity(allure.severity_level.TRIVIAL)
def test_filling_form():
    # Значения для заполнения:
    first_name = "Иван"
    last_name = "Петров"
    address = "Ленина, 55-3"
    email = "test@skypro.com"
    phone_number = "+7985899998787"
    zip_code = ""  # оставить пустым.
    city = "Москва"
    country = "Россия"
    job_position = "QA"
    company = "SkyPro"

    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    browser = webdriver.Chrome()
    main_page = DataTypes(browser, url)
    main_page.filling_form(first_name, last_name, address, email,
                           phone_number, zip_code, city, country,
                           job_position, company)
    main_page.pressing_submit()

    result_page = DataTypesSubmitted(browser)
    result_page.check_red()
    result_page.check_green()
    browser.quit()
