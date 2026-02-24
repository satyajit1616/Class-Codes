from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
email=driver.find_element(By.NAME, 'email')
email.send_keys('satyajit16@gmail.com')
btn=driver.find_element(By.CLASS_NAME, 'a-button-input')
btn.click()
ap_password=driver.find_element(By.ID, 'ap_password')
ap_password.send_keys('Prasad@123')
btn=driver.find_element(By.ID, 'signInSubmit')
btn.click()
time.sleep(10)
driver.quit()