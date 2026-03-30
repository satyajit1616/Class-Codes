from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/buttons")
d_button = driver.find_element(By.ID,"doubleClickBtn")
act = ActionChains(driver)
act.double_click(d_button).perform()
time.sleep(2)
driver.quit()