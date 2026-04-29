from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login_and_click_myinfo(setup):
    driver = setup

    login = LoginPage(driver)
    dashboard = DashboardPage(driver)


    login.login("Admin","admin123")

    dashboard.click_myinfo()

    assert "viewpersonaldetails" in driver.current_url.lower()

