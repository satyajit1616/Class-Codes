from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

wait = WebDriverWait(driver, 5)

text_m = wait.until(EC.visibility_of_element_located((By.ID,"name")))
text_m.send_keys('Abhi')

driver.quit()