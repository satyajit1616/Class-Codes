from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/Srs61/PycharmProjects/PythonProject/seleniumprac/practice.html")

f_name = driver.find_element(By.ID, "fname")
f_name.send_keys("Satyajit")
l_name = driver.find_element(By.ID, "lname")
l_name.send_keys("Swain")
Email = driver.find_element(By.XPATH, "//input[@id='email']")
Email.send_keys("satya123@gmail.com")
gender = driver.find_element(By.XPATH, "//input[@name='gender'][1]")
gender.click()
print(gender.is_selected())
mob = driver.find_element(By.CSS_SELECTOR, "input[id='mobile']")
mob.send_keys("8956238520")
date = driver.find_element(By.CSS_SELECTOR, "input[type='date']")
date.send_keys("04-05-2001")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()
# drop = Select(dropdown_element)
# alert = driver.switch_to.alert
# alert.accept()
dp_down = driver.find_element(By.XPATH, "//option[text()='Russia']")
dp_down.click()
print(dp_down.is_displayed())


# country_list = driver.find_element(By.XPATH, "//datalist[@id='countryList']/option")
# time.sleep(2)
# for i in country_list:
#     print(i.get_attribute("value"))



time.sleep(3)
driver.quit()