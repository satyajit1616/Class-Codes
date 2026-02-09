from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script('window.scrollBy(0,1300);')
time.sleep(3)

driver.switch_to.frame('courses-iframe')
heading_text = driver.find_element(By.XPATH,'//h2').text
print(heading_text)
time.sleep(3)
#
btn = driver.find_element(By.XPATH,"//a[text()='All Access plan']")
btn.click()
print(btn.is_enabled())
time.sleep(3)
#
driver.switch_to.default_content()
driver.find_element(By.ID,"name").send_keys("default_frame")
time.sleep(2)
driver.close()