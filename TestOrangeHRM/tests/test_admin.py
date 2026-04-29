from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login_and_click_admin(setup):
    driver = setup

    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    #login credetials
    login.login("Admin","admin123")

    #click admin
    dashboard.click_admin_login()

    #validation admin click or not
    assert "admin" in driver.current_url.lower()
