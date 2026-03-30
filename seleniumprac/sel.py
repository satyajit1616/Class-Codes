from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get("https://git-scm.com/")
# print(driver.title)
time.sleep(10)
driver.quit()
