from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()

driver.get("https://ya.ru/")
sleep(3)
geo = driver.find_element(By.CSS_SELECTOR, ".informers3__geo")
location = geo.text
print(location)

sleep(10)
driver.quit()
