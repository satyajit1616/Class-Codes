from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get(r"file:///C:/Users/Srs61/PycharmProjects/PythonProject/AT23/playwrightprac/webpage.html")

driver.maximize_window()
#File Upload
file_path = r"C:\Users\Srs61\PycharmProjects\PythonProject\AT23\playwrightprac\webpage.html"

file_upload = driver.find_element(By.CSS_SELECTOR,"input[type='file']")
file_upload.send_keys(file_path)



time.sleep(5)
driver.quit()