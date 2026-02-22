from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)

input_box = driver.find_element(By.ID,"name")
input_box.send_keys("Satyajit")
time.sleep(3)
alert_btn = driver.find_element(By.ID,"alertbtn").click()
wait1 = WebDriverWait(driver,5)
alert1 = wait1.until(EC.alert_is_present())
alert1.accept()
time.sleep(3)
driver.find_element(By.ID,"name").send_keys("Satyajit")
confirm_alert = driver.find_element(By.ID,"confirmbtn")
confirm_alert.click()
wait2 = WebDriverWait(driver,5)
c_alert = wait2.until(EC.alert_is_present())
c_alert.accept()
time.sleep(3)

checkboxes = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()
time.sleep(3)

driver.find_element(By.XPATH,"//option[text()='Option1']").click()
time.sleep(3)
driver.find_element(By.ID,"autocomplete").send_keys("us")
time.sleep(4)
suggested_country = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/div")

for i in suggested_country:
    if "Austria" == i.text:
        i.click()
time.sleep(3)
r_btn = driver.find_element(By.XPATH,"//input[@value='radio1']")
r_btn.click()


time.sleep(3)




driver.quit()