from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://affiliate.flipkart.com/login")
    email= page.locator("#inputEmail").fill("satya@gmail.com")
    password = page.locator("#inputPassword").fill("satya123")
    btn= page.locator("#submitLogin").click()


    time.sleep(10)
    browser.close()