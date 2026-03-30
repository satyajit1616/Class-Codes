from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/Srs61/PycharmProjects/PythonProject/seleniumprac/class_auto_prac.html")
time.sleep(2)

parent_w1 = driver.current_window_handle
driver.find_element(By.XPATH,"//button[text()='Open New Window']").click()
time.sleep(4)
t_window = driver.window_handles
for window in t_window:
    if window != parent_w1:
        driver.switch_to.window(window)
        break
driver.switch_to.window(window)
time.sleep(4)
driver.find_element(By.ID,"winInput").send_keys("Satyajit")
time.sleep(5)
driver.find_element(By.XPATH,"//button[text()='Click Me']").click()
time.sleep(5)
wait= WebDriverWait(driver,5)
w_alert = wait.until(EC.alert_is_present())
w_alert.accept()
a_windows = driver.window_handles
for window1 in a_windows:
    if window1 != parent_w1:
        driver.switch_to.window(window1)
        break
driver.switch_to.window(parent_w1)

time.sleep(3)
driver.quit()