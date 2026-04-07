from playwright.sync_api import sync_playwright
import time
url = "https://framework-generator.lovable.app"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.fill("#login-email","rr@gmail.com")
    page.fill("#login-password","s12345")
    page.locator("//button[@type='submit']").click()
    page.locator("//span[text()='Appointments']").click()
    page.locator("(//button[@type='button'])[1]").click()


    time.sleep(5)
    browser.close()
