from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH, "//input[@id='name' and @name='enter-name']").send_keys("Satyajit")
driver.find_element(By.XPATH, "//input[contains(@id,'checkBoxOption1')]").click()
driver.find_element(By.XPATH, "")
print('Check Box Clicked')
time.sleep(5)
driver.quit()