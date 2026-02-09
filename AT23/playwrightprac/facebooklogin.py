from playwright.sync_api import sync_playwright
import time

with sync_playwright() as abhi:
    browser = abhi.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.facebook.com/login/")
    page.locator("#email").fill("Satya@123")
    page.locator("#pass").fill("satya123")
    page.locator("#loginbutton").click()


    # print(btn.text_content())

    time.sleep(3)
    browser.close()
