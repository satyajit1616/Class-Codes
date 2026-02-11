
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(2)

upload_input= driver.find_element(By.ID,"file-upload")
upload_input.send_keys(r"C:\Users\Srs61\Desktop\t6.txt")
upload_submit = driver.find_element(By.ID,"file-submit")
upload_submit.click()
time.sleep(3)
driver.quit()