from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com")
email_name=driver.find_element(By.ID, 'email')
email_name.send_keys('8144536522')
pass_name=driver.find_element(By.ID, 'pass')
pass_name.send_keys('Prasad@123')
btn=driver.find_element(By.NAME, 'login')
btn.click()

time.sleep(10)
driver.quit()
