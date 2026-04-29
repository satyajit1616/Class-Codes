from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login_and_click_directory(setup):
    driver = setup

    login = LoginPage(driver)
    dashboard = DashboardPage(driver)


    login.login("Admin","admin123")

    dashboard.click_directory()

    assert "directory" in driver.current_url.lower()

