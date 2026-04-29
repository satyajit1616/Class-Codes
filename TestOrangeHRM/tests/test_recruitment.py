from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login_and_click_recruitment(setup):
    driver = setup

    login = LoginPage(driver)
    dashboard = DashboardPage(driver)


    login.login("Admin","admin123")

    dashboard.click_recruitment()

    assert "recruitment" in driver.current_url.lower()

