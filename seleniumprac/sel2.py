from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.expandtesting.com/login")
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Satya1616")
time.sleep(10)
driver.find_element(By.CLASS_NAME, 'form-control').clear()


driver.quit()