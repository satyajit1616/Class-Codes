from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get(r"https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

dropdown_box = driver.find_element(By.ID,"autocomplete")
dropdown_box.send_keys("us")


time.sleep(3)
all_elements = driver.find_elements(By.XPATH,"//ul[@id='ui-id-1']/li/div")
print(all_elements)
for i in all_elements:
    if 'Austria' == i.text:
        print(i.text)
        i.click()


time.sleep(3)

driver.quit()