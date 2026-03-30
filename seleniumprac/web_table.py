from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,400)")
text = driver.find_element(By.XPATH,"//table[@id='product']//td[text()='Appium (Selenium) - Mobile Automation Testing from Scratch']")
text.is_displayed()
print(text.text)
time.sleep(4)
driver.quit()