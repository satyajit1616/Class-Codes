from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# name = driver.switch_to.alert
name = driver.find_element(By.ID, 'name')
name.send_keys("Satya")

driver.find_element(By.CSS_SELECTOR,"input[id = confirmbtn]").click()
wait = WebDriverWait(driver, 5)
alert1 = wait.until(EC.alert_is_present())
print(alert1.text)
alert1.accept()


time.sleep(5)
driver.quit()
