from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.flipkart.com/")
time.sleep(3)
driver.execute_script('window.scrollBy(0,2000);')
time.sleep(3)

mouse_h = driver.find_element(By.XPATH,"(//div[@class='css-175oi2r r-1awozwy'])[1]")
time.sleep(3)
actions = ActionChains(driver)
actions.move_to_element(mouse_h).perform()
time.sleep(2)
mouse_h.click()
time.sleep(3)
driver.quit()

