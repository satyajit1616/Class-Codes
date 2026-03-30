from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    url = "https://parabank.parasoft.com"
    page.goto(url)
    page.locator("//input[@name='username']").fill("AT#23")
    page.locator("//input[@name='password']").fill("Satya@2026")
    page.locator("//input[@type='submit']").click()
    # page.locator("//a[text()='Open New Account']").click()
    # account = page.locator("//select[@id='type']")
    # account.select_option('SAVINGS')
    # acc_no = page.locator("#fromAccountId")
    # acc_no.select_option("15675")
    # page.locator("//input[@type='button']").click()
    page.locator("//a[text()='Transfer Funds']").click()
    page.locator("#amount").fill("20")
    page.locator("#fromAccountId").select_option("15675")
    page.locator("#toAccountId").select_option("17229")
    page.locator("//input[@type='submit']").click()
    page.locator("//a[text()='Accounts Overview']").click()

    time.sleep(10)
    browser.close()