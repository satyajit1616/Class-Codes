from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    #for a particular checkbox
    # checkbox = page.locator("#checkBoxOption1")
    checkboxes = page.locator("input[type='checkbox']")
    count = checkboxes.count()


    for i in range(count):
        checkboxes.nth(i).check()


    time.sleep(2)
    browser.close()
