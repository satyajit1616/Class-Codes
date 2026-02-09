from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)

driver.execute_script('window.scrollBy(0,1000);')
time.sleep(2)
mouse_hover = driver.find_element(By.ID,"mousehover")
actions = ActionChains(driver)
actions.move_to_element(mouse_hover).perform()
time.sleep(2)
top = driver.find_element(By.LINK_TEXT,"Top")
top.click()
time.sleep(3)
print(top.is_enabled())
driver.quit()