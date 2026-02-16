import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.fill("#name","Satya")

    page.once("dialog",lambda dialog:(
        print("ALERT CONFIRM TEXT:-",dialog.message),
        dialog.accept()
    ))

    page.click("#confirmbtn")
    time.sleep(2)
    browser.close()