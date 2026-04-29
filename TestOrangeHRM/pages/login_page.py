from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    username = (By.NAME,"username")
    password = (By.NAME,"password")
    login_button = (By.XPATH,"//button[@type='submit']")

    def login(self,user,pwd):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()