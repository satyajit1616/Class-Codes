from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
home= driver.find_element(By.XPATH,"//button[text()='Home']")
home.click()
time.sleep(4)

# window = driver.current_window_handle
# print(window)

driver.find_element(By.XPATH,"//a[text()='Sign Up']").click()
time.sleep(5)

driver.find_element(By.ID,"name").send_keys("Satya")
time.sleep(4)


window = driver.window_handles
print(window)

driver.switch_to.window(window[1])
time.sleep(5)


driver.close()



driver.quit()

