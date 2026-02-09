from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/text-box")
time.sleep(3)
name = driver.find_element(By.ID,"userName")
name.send_keys("Automation")
name.send_keys(Keys.CONTROL+"a")
name.send_keys(Keys.CONTROL+"c")
email = driver.find_element(By.ID,"userEmail")
email.send_keys(Keys.CONTROL+"v")
time.sleep(3)
driver.quit()