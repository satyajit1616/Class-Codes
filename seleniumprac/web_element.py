

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)

name_input=driver.find_element(By.ID,"name")
name_input.send_keys("Selenium automation")

print("Textbox attribute:",name_input.get_attribute("value"))

name_input.clear()
name_input.send_keys('Automation')

print("Textbox displayed:",name_input.is_displayed())
print("Textbox enabled:", name_input.is_enabled())

checkbox=driver.find_element(By.ID,"checkBoxOption1")
checkbox.click()
print("Checkbox selected:",checkbox.is_selected())

button_text= driver.find_element(By.ID,"openwindow").text
print('Button text:',button_text)
time.sleep(3)
driver.quit()