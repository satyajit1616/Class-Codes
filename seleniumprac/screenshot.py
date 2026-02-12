from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)
driver.find_element(By.ID,"opentab").click()
#driver.get_screenshot_as_file("file/path")
driver.save_screenshot(r"C:\Users\Srs61\PycharmProjects\PythonProject\Screenshot/open.png")
driver.quit()