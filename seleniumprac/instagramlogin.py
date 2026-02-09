from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.instagram.com/accounts/login/")
username=driver.find_element(By.XPATH, "//input[@name='email']")
username.send_keys("9955737680")
password=driver.find_element(By.XPATH, "//input[@name='pass']")
password.send_keys("Satya@123")
btn=driver.find_element(By.XPATH, "//span[text()='Log in']")
btn.click()
time.sleep(5)
driver.quit()