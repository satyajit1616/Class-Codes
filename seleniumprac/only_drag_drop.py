from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/Srs61/PycharmProjects/PythonProject/seleniumprac/class_auto_prac.html")
time.sleep(2)
driver.execute_script('window.scrollBy(0,1000);')
time.sleep(2)
source = driver.find_element(By.ID,"drag")
target = driver.find_element(By.ID,"drop")
act3 = ActionChains(driver)
act3.drag_and_drop(source,target).perform()
time.sleep(10)
print(source,target)
time.sleep(3)
driver.quit()