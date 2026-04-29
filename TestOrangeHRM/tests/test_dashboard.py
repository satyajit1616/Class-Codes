from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login_and_click_dashboard(setup):
    driver = setup

    login = LoginPage(driver)
    dashboard = DashboardPage(driver)


    login.login("Admin","admin123")

    dashboard.click_dashboard()

    assert "dashboard" in driver.current_url.lower()

