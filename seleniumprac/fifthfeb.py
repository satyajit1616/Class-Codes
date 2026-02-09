from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)

driver.find_element(By.ID,"openwindow").click()
time.sleep(2)
parent_window = driver.current_window_handle
print('parent_window:',parent_window)
all_window = driver.window_handles
print(all_window)


for win in all_window:
    if win!= parent_window:
        driver.switch_to.window(win)
        break
print('child window titles:',driver.title)

driver.find_element(By.LINK_TEXT,"Courses").click()
time.sleep(3)
driver.close()

driver.quit()

