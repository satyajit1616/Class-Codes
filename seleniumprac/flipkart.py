from re import search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.flipkart.com/')
search_box=driver.find_element(By.NAME, "q")
search_box.send_keys('Laptop')
search_box.send_keys(Keys.RETURN)

time.sleep(5)
price=driver.find_element(By.XPATH, "(//div[contains(@class,'Nx9bqj _4b5DiR')])")
print(price)
driver.quit()
