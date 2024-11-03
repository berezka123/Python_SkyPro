from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()

cookie = {
    "name": "cookie_policy",
    "value": "1"
}

driver.get("http://labirint.ru/")
sleep(3)
driver.add_cookie(cookie)
sleep(3)
driver.refresh()

sleep(10)
driver.quit()
