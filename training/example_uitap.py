from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/visibility")

is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
print(is_displayed)

driver.find_element(By.CSS_SELECTOR, "#hideButton").click()

is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
print(is_displayed)

sleep(5)
driver.quit()
"""

"""
driver = webdriver.Chrome()
driver.implicitly_wait(20)

driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

content = driver.find_element(By.CSS_SELECTOR, "#content")
text = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(text)

sleep(3)
driver.quit()
"""

driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 40)

driver.get("http://uitestingplayground.com/progressbar")

driver.find_element(By.CSS_SELECTOR, "#startButton").click()

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#progressBar"), "75%")
)

driver.find_element(By.CSS_SELECTOR, "#stopButton").click()

print(driver.find_element(By.CSS_SELECTOR, "#result").text)

sleep(3)
driver.quit()
