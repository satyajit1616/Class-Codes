from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    radio_btns = page.locator("input[type='radio']")
    count = radio_btns.count()

    for i in range(count):
        radio_btns.nth(i).check()
    # time.sleep(5)
    # radio_btn.click()
    time.sleep(3)
    browser.close()
