from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

from seleniumprac.mousehover import actions

driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
# time.sleep(3)
# btn = driver.find_element(By.CSS_SELECTOR,".context-menu-one")
#
# act = ActionChains(driver)
# act.context_click(btn).perform()
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR,"ul.context-menu-list li.context-menu-icon-paste").click()
# time.sleep(2)
#
# ale = driver.switch_to.alert
# ale.accept()
# time.sleep(2)
# driver.quit()
driver.get("https://demoqa.com/buttons")
d_button = driver.find_element(By.ID,"doubleClickBtn")
act = ActionChains(driver)
actions.double_click(d_button).perform()
time.sleep(2)
driver.quit()




