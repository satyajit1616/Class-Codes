from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

home = driver.find_element(By.ID,"opentab")
home.click()
time.sleep(3)

parent_window = driver.current_window_handle

all_windows = driver.window_handles
for window in all_windows:
    if window != parent_window:
        driver.switch_to.window(window)
        break

link = driver.find_element(By.LINK_TEXT,"Access all our Courses")
act = ActionChains(driver)
act.move_to_element(link).perform()
time.sleep(3)
driver.save_screenshot(r"C:\Users\Srs61\PycharmProjects\PythonProject\Screenshot/all_course.png")
time.sleep(3)
driver.quit()

