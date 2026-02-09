from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")
time.sleep(2)
driver.switch_to.frame(driver.find_element(By.CLASS_NAME,"demo-frame"))
source = driver.find_element(By.ID,"draggable")
target = driver.find_element(By.ID,"droppable")
act = ActionChains(driver)
act.drag_and_drop(source, target).perform()
time.sleep(2)
driver.switch_to.default_content()
driver.close()