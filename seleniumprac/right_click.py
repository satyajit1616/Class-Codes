from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
time.sleep(2)

button = driver.find_element(By.CSS_SELECTOR,'.context-menu-one')

action = ActionChains(driver)
action.context_click(button).perform()

driver.find_element(By.CSS_SELECTOR, "ul.context-menu-list li.context-menu-icon-copy").click()
alert = driver.switch_to.alert
alert.accept()
time.sleep(3)
driver.quit()