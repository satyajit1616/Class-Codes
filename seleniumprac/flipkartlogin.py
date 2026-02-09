from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://www.flipkart.com/account/login?ret=/")
email=driver.find_element(By.CLASS_NAME, 'c3Bd2c.yXUQVt')
email.send_keys('7205385555')
btn=driver.find_element(By.CLASS_NAME, 'dSM5Ub.Kv3ekh.KcXDCU')
btn.click()

time.sleep(10)
driver.quit()







