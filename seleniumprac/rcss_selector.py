from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#By Id
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("by Satya")
#By Class
# driver.find_element(By.CSS_SELECTOR, ".inputs").send_keys('By Class')
#By Tag+Id
# driver.find_element(By.CSS_SELECTOR, "input#autocomplete").send_keys("By tag+id")
#By Tag+Class
# driver.find_element(By.CSS_SELECTOR, "input.inputs").send_keys("By tag+Class")
#By Attribute
check_box=driver.find_elements(By.CSS_SELECTOR, "input[id*='checkBoxOption']")
check_box[0].click()
#By Starts with
# driver.find_element(By.CSS_SELECTOR, "input[id^='checkBox']").click()
#By Ends With
# driver.find_element(By.CSS_SELECTOR, "input[id$='Option2']").click()
#By Link Text
# driver.find_element(By.LINK_TEXT, "Open Tab").click()
# print('Link Clicked')
#By Partial Link Text
driver.find_element(By.PARTIAL_LINK_TEXT, "Open").click()
print('Link Click')
time.sleep(3)
driver.quit()