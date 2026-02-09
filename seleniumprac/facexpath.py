from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/login/")
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('9556888989')
driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys('Satya@123')
btn=driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
btn.click()
time.sleep(10)
driver.quit()