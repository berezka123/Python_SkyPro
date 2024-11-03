from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# Для Google Chrome.
# Клик по кнопке.
driver = webdriver.Chrome()

# Открываем страницу:
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Ищем кнопку Add Element и пять раз кликаем на неё:
add_button = driver.find_element(By.CLASS_NAME, "example")
sleep(3)
for i in range(5):
    add_button.find_element(By.TAG_NAME, "button").click()
    sleep(1)

# Собираем со страницы список кнопок Delete:
delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
sleep(5)
driver.quit()

# Выводим на экран размер списка кнопок Delete:
print(f"Размер списка кнопок Delete: {len(delete_buttons)}")
