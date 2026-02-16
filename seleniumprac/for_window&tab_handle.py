from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/Srs61/PycharmProjects/PythonProject/seleniumprac/class_auto_prac.html")

parent_window = driver.current_window_handle
driver.find_element(By.XPATH,"//button[text()='Open New Tab']").click()
time.sleep(4)
all_windows = driver.window_handles
for window in all_windows:
    if window != parent_window:
        driver.switch_to.window(window)
        break
driver.switch_to.window(parent_window)
time.sleep(4)
parent_w1 = driver.current_window_handle
driver.find_element(By.XPATH,"//button[text()='Open New Window']").click()
time.sleep(4)
a_windows = driver.window_handles
for window in a_windows:
    if window != parent_w1:
        driver.switch_to.window(window)
        break
driver.switch_to.window(parent_w1)
time.sleep(5)
driver.quit()