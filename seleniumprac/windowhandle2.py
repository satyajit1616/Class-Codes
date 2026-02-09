from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

home = driver.find_element(By.XPATH, "//button[text()='Home']")
home.click()
time.sleep(3)


parent_window = driver.current_window_handle


driver.find_element(By.XPATH, "//a[text()='Sign Up']").click()
time.sleep(3)
all_windows = driver.window_handles
for window in all_windows:
    if window != parent_window:
        driver.switch_to.window(window)
        break


driver.find_element(By.ID, "name").send_keys("Satya")
time.sleep(4)

driver.quit()
