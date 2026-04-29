import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def setup():
    #pre condition or setup
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    yield driver

    #post condition  or teardown
    driver.quit()