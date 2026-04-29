from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    admin_menu = (By.XPATH,"//span[text()='Admin']")
    pim_menu = (By.XPATH,"//span[text()='PIM']")
    leave_menu = (By.XPATH,"//span[text()='Leave']")
    time_menu = (By.XPATH,"//span[text()='Time']")
    recruitment_menu = (By.XPATH, "//span[text()='Recruitment']")
    myinfo_menu = (By.XPATH, "//span[text()='My Info']")
    performance_menu = (By.XPATH, "//span[text()='Performance']")
    dashboard_menu = (By.XPATH, "//span[text()='Dashboard']")
    directory_menu = (By.XPATH, "//span[text()='Directory']")
    maintenance_menu = (By.XPATH, "//span[text()='Maintenance']")
    claim_menu = (By.XPATH, "//span[text()='Claim']")
    buzz_menu = (By.XPATH, "//span[text()='Buzz']")



    def click_admin_login(self):
        self.wait.until(EC.element_to_be_clickable(self.admin_menu)).click()
    def click_pim(self):
        self.wait.until(EC.element_to_be_clickable(self.pim_menu)).click()
    def click_leave(self):
        self.wait.until(EC.element_to_be_clickable(self.leave_menu)).click()
    def click_time(self):
        self.wait.until(EC.element_to_be_clickable(self.time_menu)).click()
    def click_recruitment(self):
        self.wait.until(EC.element_to_be_clickable(self.recruitment_menu)).click()
    def click_myinfo(self):
        self.wait.until(EC.element_to_be_clickable(self.myinfo_menu)).click()
    def click_performance(self):
        self.wait.until(EC.element_to_be_clickable(self.performance_menu)).click()
    def click_dashboard(self):
        self.wait.until(EC.element_to_be_clickable(self.dashboard_menu)).click()
    def click_directory(self):
        self.wait.until(EC.element_to_be_clickable(self.directory_menu)).click()
    def click_maintenance(self):
        self.wait.until(EC.element_to_be_clickable(self.maintenance_menu)).click()
    def click_claim(self):
        self.wait.until(EC.element_to_be_clickable(self.claim_menu)).click()
    def click_buzz(self):
        self.wait.until(EC.element_to_be_clickable(self.buzz_menu)).click()



