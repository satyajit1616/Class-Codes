from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.drivers.chrome import ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)